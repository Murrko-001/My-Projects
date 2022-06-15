import time
from typing import NamedTuple, Optional, Dict, Tuple, List, Any
import requests
from bs4 import BeautifulSoup
import re
import json
import os

BASE_URL = "https://python.iamroot.eu/"


class FullScrap(NamedTuple):
    linux_only_availability: List[str]
    most_visited_webpage: Tuple[int, str]
    changes: List[Tuple[int, str]]
    params: List[Tuple[int, str]]

    def as_dict(self) -> Dict[str, Any]:
        return {
            'linux_only_availability': self.linux_only_availability,
            'most_visited_webpage': self.most_visited_webpage,
            'changes': self.changes,
            'params': self.params
        }


class WebPage:
    def __init__(self, url: str, soup, count: int, links: List[str]):
        self.url = url
        self.count = count
        self.soup = soup
        self.links = links

    def link_remove(self, item):
        if item in self.links:
            self.links.pop(self.links.index(item))

    def plus_count(self) -> None:
        self.count += 1

    def link_extract(self) -> None:
        url_in_parts = self.url.split("/")[3:-1]

        soup_links = self.soup.find_all("a", href=True)

        list_of_links = []
        for i in soup_links:
            list_of_links.append(i['href'])

        for pure_link in list_of_links:
            if "https:/" not in pure_link and "http:/" not in pure_link and "www." not in pure_link:
                if "html" == pure_link[-4:] or "/" == pure_link[-1]:

                    if "../" not in pure_link:
                        if len(url_in_parts) > 0:
                            pure_link = BASE_URL + "/".join(url_in_parts) + "/" + pure_link
                        else:
                            pure_link = BASE_URL + pure_link

                    else:
                        pure_link = BASE_URL + pure_link[3:]

                    if "#" in pure_link:
                        pure_link = pure_link[:pure_link.find("#")]

                    if pure_link != self.url and pure_link not in self.links:
                        self.links.append(pure_link)


class WebPages:
    def __init__(self, sites: List[WebPage]):
        self.sites = sites

    def add_new_site(self, new_site: WebPage):
        self.sites.append(new_site)

    def page_index(self, item):
        for i in self.sites:
            if item == i.url:
                return self.sites.index(i)


def check_if_visited(url, instance: WebPages):
    for i in instance.sites:
        if i.url == url:
            i.plus_count()
            i.link_remove(url)
            return True
    return False


def download_webpage(url: str, instance: WebPages) -> requests.Response:

    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")

    instance.add_new_site(WebPage(url, soup, 1, []))
    curr_page = instance.sites[instance.page_index(url)]
    curr_page.link_extract()

    for site in curr_page.links:
        if check_if_visited(site, instance):
            pass
        else:
            time.sleep(0.5)
            print("got: ", url)
            download_webpage(site, instance)
    print('out ', url)
    return response


def get_linux_only_availability(instance: WebPages) -> List[str]:
    list_of_functions = []
    for i in instance.sites:
        if "https://python.iamroot.eu/library" in i.url:
            dts = i.soup.find_all("dt", id=True)

            for dt in dts:
                for j in dt.next_sibling.next_sibling.find_all("p"):
                    if "Linux" in str(j):
                        if dt['id'] not in list_of_functions:
                            list_of_functions.append(dt['id'])

    return list_of_functions

def get_most_visited_webpage(instance: WebPages) -> Tuple[int, str]:
    new_max = 0
    new_url = ""
    for i in instance.sites:
        if i.count > new_max:
            new_max = i.count
            new_url = i.url
    return new_max, new_url


def get_changes(instance: WebPages) -> List[Tuple[int, str]]:
    dict_of_functions = {}
    list_of_functions = []

    for i in instance.sites:
        if f"https://python.iamroot.eu/library" in i.url:
            result = i.soup.find_all("span", class_="versionmodified added")

            for j in result:
                version = j.string[15: 18]

                if version in dict_of_functions:
                    dict_of_functions[version] += 1
                else:
                    dict_of_functions[version] = 1

    sort_dict = sorted(dict_of_functions.items(), key=lambda x: x[1], reverse=True)
    for i in sort_dict:
        pos_2 = i[0]
        pos_1 = int(i[1])
        list_of_functions.append((pos_1, pos_2))
    return list_of_functions


def get_most_params(instance: WebPages) -> List[Tuple[int, str]]:
    list_of_functions = []
    for i in instance.sites:
        if "https://python.iamroot.eu/library" in i.url:

            result = i.soup.find_all("dt", id=True)

            for dts in result:
                ems = dts.find_all("em")
                fun = dts['id']
                if len(ems) >= 10:
                    list_of_functions.append((len(ems), fun))

    return sorted(list_of_functions, reverse=True)


def scrap_all(instance: WebPages) -> FullScrap:
    scrap = FullScrap(
        linux_only_availability=get_linux_only_availability(instance),
        most_visited_webpage=get_most_visited_webpage(instance),
        changes=get_changes(instance),
        params=get_most_params(instance),
    )
    return scrap


def main() -> None:
    obj = WebPages([])

    time_start = time.time()
    download_webpage(BASE_URL, obj)
    print(json.dumps(scrap_all(obj).as_dict()))
    print('took', int(time.time() - time_start), 's')


if __name__ == '__main__':
    main()
