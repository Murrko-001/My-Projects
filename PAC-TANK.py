import tkinter
import time


class Tanks:
    def __init__(self, position, speed, x, y, color):
        self.position = position
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color

        self.body = canvas.create_rectangle(self.x - 25, self.y - 25, self.x + 25, self.y + 25, width=2,
                                            outline=self.color)
        self.wheel_L = canvas.create_rectangle(self.x - 30, self.y - 30, self.x - 25, self.y + 30, width=2,
                                               outline=self.color)
        self.wheel_R = canvas.create_rectangle(self.x + 30, self.y - 30, self.x + 25, self.y + 30, width=2,
                                               outline=self.color)
        self.canon = canvas.create_rectangle(self.x - 2.5, self.y - 50, self.x + 2.5, self.y, width=2,
                                             outline=self.color, fill=background)

    def steer_horizontal(self, direction):
        x1, y1, x2, y2 = canvas.coords(self.body)
        x_center = x1 + 25
        y_center = y1 + 25
        canvas.coords(self.body, x_center - 25, y_center - 25, x_center + 25, y_center + 25)
        canvas.coords(self.wheel_L, x_center + 30, y_center + 30, x_center - 30, y_center + 25)
        canvas.coords(self.wheel_R, x_center - 30, y_center - 30, x_center + 30, y_center - 25)
        canvas.coords(self.canon, x_center, y_center - 2.5, x_center + 50 * direction, y_center + 2.5)
        canvas.update()
        canvas.after(10)

    def left(self, _):
        self.steer_horizontal(-1)
        self.position = "left"

    def right(self, _):
        self.steer_horizontal(1)
        self.position = "right"

    def steer_vertical(self, direction):
        x1, y1, x2, y2 = canvas.coords(self.body)
        x_center = x1 + 25
        y_center = y1 + 25
        canvas.coords(self.body, x_center - 25, y_center - 25, x_center + 25, y_center + 25)
        canvas.coords(self.wheel_L, x_center - 30, y_center - 30, x_center - 25, y_center + 30)
        canvas.coords(self.wheel_R, x_center + 30, y_center - 30, x_center + 25, y_center + 30)
        canvas.coords(self.canon, x_center - 2.5, y_center, x_center + 2.5, y_center + 50 * direction)
        canvas.update()
        canvas.after(10)

    def down(self, _):
        self.steer_vertical(1)
        self.position = "down"

    def up(self, _):
        self.steer_vertical(-1)
        self.position = "up"

    def reset_position(self, direction, x_center, y_center):
        canvas.coords(self.body, x_center - 25, y_center - 25, x_center + 25, y_center + 25)
        canvas.coords(self.wheel_L, x_center - 30, y_center - 30, x_center - 25, y_center + 30)
        canvas.coords(self.wheel_R, x_center + 30, y_center - 30, x_center + 25, y_center + 30)
        canvas.coords(self.canon, x_center - 2.5, y_center, x_center + 2.5, y_center + 50 * direction)
        canvas.update()
        canvas.after(10)
        self.position = "up"

    def tank_collision(self, second_tank):
        x1_b, y1_b, x2_b, y2_b = canvas.coords(self.body)
        x1_c, y1_c, x2_c, y2_c = canvas.coords(self.canon)
        x1_l, y1_l, x2_l, y2_l = canvas.coords(self.wheel_L)
        x1_r, y1_r, x2_r, y2_r = canvas.coords(self.wheel_R)

        x1_b_2, y1_b_2, x2_b_2, y2_b_2 = canvas.coords(second_tank.body)
        x1_c_2, y1_c_2, x2_c_2, y2_c_2 = canvas.coords(second_tank.canon)
        x1_l_2, y1_l_2, x2_l_2, y2_l_2 = canvas.coords(second_tank.wheel_L)
        x1_r_2, y1_r_2, x2_r_2, y2_r_2 = canvas.coords(second_tank.wheel_R)

        if self.position == "up":
            if second_tank.position == "up":
                # canon on body
                # canon on left wheel
                # canon na right wheel
                # right wheel na left wheel
                # right wheel na body
                # left wheel na right wheel
                # left wheel na body
                if x2_c >= x1_b_2 and x1_c <= x2_b_2 and y1_b_2 <= y1_c <= y2_b_2 or \
                        x2_c >= x1_l_2 and x1_c <= x2_l_2 and y1_l_2 <= y1_c <= y2_l_2 or \
                        x1_c <= x2_r_2 and x2_c >= x1_r_2 and y1_r_2 <= y1_c <= y2_r_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y1_r <= y2_l_2 or \
                        x2_r >= x1_b_2 and x1_r <= x2_b_2 and y1_l_2 <= y1_b <= y2_l_2 or \
                        x2_l >= x1_r_2 and x1_l <= x2_r_2 and y1_r_2 <= y1_l <= y2_r_2 or \
                        x2_l >= x1_b_2 and x1_l <= x2_b_2 and y1_r_2 <= y1_b <= y2_r_2:
                    return False
            elif second_tank.position == "right":
                # canon na wheel
                # left wheel na wheel
                # right wheel na wheel
                # wheel na canon
                if x2_c >= x1_l_2 and x1_c <= x2_l_2 and y1_l_2 <= y1_c <= y2_l_2 or \
                        x2_l >= x1_l_2 and x1_l <= x2_l_2 and y1_l_2 <= y1_l <= y2_l_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y1_r <= y2_l_2 or \
                        x1_l <= x2_c_2 and x2_l >= x1_c_2 and y1_c_2 <= y1_l <= y2_c_2:
                    return False
            elif second_tank.position == "left":
                if x2_c >= x1_l_2 and x1_c <= x2_l_2 and y1_l_2 <= y1_c <= y2_l_2 or \
                        x2_l >= x1_l_2 and x1_l <= x2_l_2 and y1_l_2 <= y1_l <= y2_l_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y1_r <= y2_l_2 or \
                        x1_r <= x2_c_2 and x2_r >= x1_c_2 and y1_c_2 <= y1_r <= y2_c_2:
                    return False
            elif second_tank.position == "down":
                # left wheel na right (from my pov)
                # left wheel na body
                # right wheel left (from my pov)
                # right wheel na canon
                # canon na canon
                # right wheel na canon
                # left wheel na canon
                # canon na body
                if x1_l <= x2_r_2 and x2_l >= x1_r_2 and y1_r_2 <= y1_l <= y2_r_2 or \
                        x1_l <= x2_b_2 and x2_l >= x1_b_2 and y1_b_2 <= y1_l <= y2_b_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y1_r <= y2_l_2 or \
                        x2_r >= x1_b_2 and x1_r <= x2_b_2 and y1_b_2 <= y1_r <= y2_b_2 or \
                        x2_c >= x1_c_2 and x1_c <= x2_c_2 and y1_c_2 <= y1_c <= y2_c_2 or \
                        x2_r >= x1_c_2 and x1_r <= x2_c_2 and y1_c_2 <= y1_r <= y2_c_2 or \
                        x1_l <= x2_c_2 and x2_l >= x1_c_2 and y1_c_2 <= y1_l <= y2_c_2 or \
                        x1_b <= x2_c_2 and x2_b >= x1_c_2 and y1_c_2 <= y1_b <= y2_c_2:
                    return False

        if self.position == "right":
            if second_tank.position == "up":
                if y1_c <= y2_l_2 and y2_c >= y1_l_2 and x2_l_2 >= x2_c >= x1_l_2 or \
                        y1_l <= y2_l_2 and y2_l >= y1_l_2 and x2_l_2 >= x2_l >= x1_l_2 or \
                        y1_r <= y2_l_2 and y2_r >= y1_l_2 and x2_l_2 >= x2_r >= x1_l_2 or \
                        y2_l >= y1_c_2 and y1_l <= y2_c_2 and x2_c_2 >= x2_l >= x1_c_2:
                    return False
            elif second_tank.position == "right":
                # canon na body
                # canon na left wheel
                # canon na right wheel
                # wheel_l na wheel_p
                # wheel_l na body
                # wheel_p na wheel_l
                # wheel_p na body
                if y1_c <= y2_b_2 and y2_c >= y1_b_2 and x2_b_2 >= x2_c >= x1_b_2 or \
                        y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x2_c >= x1_r_2 or \
                        y2_c >= y1_l_2 and y1_c <= y2_l_2 and x2_l_2 >= x2_c >= x1_l_2 or \
                        y2_l >= y1_r_2 and y1_l <= y2_r_2 and x2_r_2 >= x2_l >= x1_r_2 or \
                        y2_l >= y1_b_2 and y1_l <= y2_b_2 and x2_r_2 >= x2_b >= x1_r_2 or \
                        y2_r >= y1_l_2 and y1_r <= y2_l_2 and x2_l_2 >= x2_r >= x1_l_2 or \
                        y2_r >= y1_b_2 and y1_r <= y2_b_2 and x2_l_2 >= x2_b >= x1_l_2:
                    return False
            elif second_tank.position == "left":
                # wheel_l na wheel_p
                # wheel_l na body
                # wheel_p na wheel_l
                # wheel_p na body
                # canon na canon
                # wheel_p na canon
                # left wheel na canon
                # canon na body
                if y2_l >= y1_r_2 and y1_l <= y2_r_2 and x2_l_2 >= x2_r >= x1_l_2 or \
                        y2_l >= y1_b_2 and y1_l <= y2_b_2 and x2_b_2 >= x2_l >= x1_b_2 or \
                        y1_r <= y2_l_2 and y2_r >= y1_l_2 and x2_r_2 >= x2_r >= x1_r_2 or \
                        y1_r <= y2_b_2 and y2_r >= y1_b_2 and x2_b_2 >= x2_r >= x1_b_2 or \
                        y1_c <= y2_c_2 and y2_c >= y1_c_2 and x2_c_2 >= x2_c >= x1_c_2 or \
                        y1_c <= y2_l_2 and y2_c >= y1_l_2 and x2_l_2 >= x2_c >= x1_l_2 or \
                        y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x2_c >= x1_r_2 or \
                        y1_b <= y2_c_2 and y2_b >= y1_c_2 and x2_b_2 >= x2_c >= x1_b_2:
                    return False
            elif second_tank.position == "down":
                if y1_c <= y2_l_2 and y2_c >= y1_l_2 and x2_l_2 >= x2_c >= x1_l_2 or \
                        y1_l <= y2_l_2 and y2_l >= y1_l_2 and x2_l_2 >= x2_l >= x1_l_2 or \
                        y1_r <= y2_l_2 and y2_r >= y1_l_2 and x2_l_2 >= x2_r >= x1_l_2 or \
                        y2_r >= y1_c_2 and y1_r <= y2_c_2 and x2_c_2 >= x2_r >= x1_c_2:
                    return False

        if self.position == "left":
            if second_tank.position == "up":
                # canon na wheel
                # wheel_l na wheel_p
                # wheel_p na wheel_p
                # canon na wheel_l
                if y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x1_c >= x1_r_2 or \
                        y1_l <= y2_r_2 and y2_l >= y1_r_2 and x2_r_2 >= x1_l >= x1_r_2 or \
                        y1_r <= y2_r_2 and y2_r >= y1_r_2 and x2_r_2 >= x1_r >= x1_r_2 or \
                        y2_l >= y1_c_2 and y1_l <= y2_c_2 and x2_c_2 >= x1_l >= x1_c_2:
                    return False
            elif second_tank.position == "right":
                if y2_l >= y1_r_2 and y1_l <= y2_r_2 and x2_l_2 >= x1_r >= x1_l_2 or \
                        y2_l >= y1_b_2 and y1_l <= y2_b_2 and x2_b_2 >= x1_l >= x1_b_2 or \
                        y1_r <= y2_l_2 and y2_r >= y1_l_2 and x2_r_2 >= x1_r >= x1_r_2 or \
                        y1_r <= y2_b_2 and y2_r >= y1_b_2 and x2_b_2 >= x1_r >= x1_b_2 or \
                        y1_c <= y2_c_2 and y2_c >= y1_c_2 and x2_c_2 >= x1_c >= x1_c_2 or \
                        y1_c <= y2_l_2 and y2_c >= y1_l_2 and x2_l_2 >= x1_c >= x1_l_2 or \
                        y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x1_c >= x1_r_2 or \
                        y1_b <= y2_c_2 and y2_b >= y1_c_2 and x2_b_2 >= x1_c >= x1_b_2:
                    return False
            elif second_tank.position == "left":
                if y1_c <= y2_b_2 and y2_c >= y1_b_2 and x2_b_2 >= x1_c >= x1_b_2 or \
                        y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x1_c >= x1_r_2 or \
                        y2_c >= y1_l_2 and y1_c <= y2_l_2 and x2_l_2 >= x1_c >= x1_l_2 or \
                        y2_l >= y1_r_2 and y1_l <= y2_r_2 and x2_r_2 >= x1_l >= x1_r_2 or \
                        y2_l >= y1_b_2 and y1_l <= y2_b_2 and x2_r_2 >= x1_b >= x1_r_2 or \
                        y2_r >= y1_l_2 and y1_r <= y2_l_2 and x2_l_2 >= x1_r >= x1_l_2 or \
                        y2_r >= y1_b_2 and y1_r <= y2_b_2 and x2_l_2 >= x1_b >= x1_l_2:
                    return False
            elif second_tank.position == "down":
                if y1_c <= y2_r_2 and y2_c >= y1_r_2 and x2_r_2 >= x1_c >= x1_r_2 or \
                        y1_l <= y2_r_2 and y2_l >= y1_r_2 and x2_r_2 >= x1_l >= x1_r_2 or \
                        y1_r <= y2_r_2 and y2_r >= y1_r_2 and x2_r_2 >= x1_r >= x1_r_2 or \
                        y2_r >= y1_c_2 and y1_r <= y2_c_2 and x2_c_2 >= x1_r >= x1_c_2:
                    return False

        if self.position == "down":
            if second_tank.position == "up":
                if x1_l <= x2_r_2 and x2_l >= x1_r_2 and y1_r_2 <= y2_l <= y2_r_2 or \
                        x1_l <= x2_b_2 and x2_l >= x1_b_2 and y1_b_2 <= y2_l <= y2_b_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y2_r <= y2_l_2 or \
                        x2_r >= x1_b_2 and x1_r <= x2_b_2 and y1_b_2 <= y2_r <= y2_b_2 or \
                        x2_c >= x1_c_2 and x1_c <= x2_c_2 and y1_c_2 <= y2_c <= y2_c_2 or \
                        x2_r >= x1_c_2 and x1_r <= x2_c_2 and y1_c_2 <= y2_r <= y2_c_2 or \
                        x1_l <= x2_c_2 and x2_l >= x1_c_2 and y1_c_2 <= y2_l <= y2_c_2 or \
                        x1_b <= x2_c_2 and x2_b >= x1_c_2 and y1_c_2 <= y2_b <= y2_c_2:
                    return False
            elif second_tank.position == "right":
                if x2_c >= x1_r_2 and x1_c <= x2_r_2 and y1_r_2 <= y2_c <= y2_r_2 or \
                        x2_l >= x1_r_2 and x1_l <= x2_r_2 and y1_r_2 <= y2_l <= y2_r_2 or \
                        x2_r >= x1_r_2 and x1_r <= x2_r_2 and y1_r_2 <= y2_r <= y2_r_2 or \
                        x1_l <= x2_c_2 and x2_l >= x1_c_2 and y1_c_2 <= y2_l <= y2_c_2:
                    return False
            elif second_tank.position == "left":
                if x2_c >= x1_r_2 and x1_c <= x2_r_2 and y1_r_2 <= y2_c <= y2_r_2 or \
                        x2_l >= x1_r_2 and x1_l <= x2_r_2 and y1_r_2 <= y2_l <= y2_r_2 or \
                        x2_r >= x1_r_2 and x1_r <= x2_r_2 and y1_r_2 <= y2_r <= y2_r_2 or \
                        x2_r >= x1_c_2 and x1_r <= x2_c_2 and y1_c_2 <= y2_r <= y2_c_2:
                    return False
            elif second_tank.position == "down":
                if x2_c >= x1_b_2 and x1_c <= x2_b_2 and y1_b_2 <= y2_c <= y2_b_2 or \
                        x2_c >= x1_l_2 and x1_c <= x2_l_2 and y1_l_2 <= y2_c <= y2_l_2 or \
                        x1_c <= x2_r_2 and x2_c >= x1_r_2 and y1_r_2 <= y2_c <= y2_r_2 or \
                        x2_r >= x1_l_2 and x1_r <= x2_l_2 and y1_l_2 <= y2_r <= y2_l_2 or \
                        x2_r >= x1_b_2 and x1_r <= x2_b_2 and y1_l_2 <= y2_b <= y2_l_2 or \
                        x2_l >= x1_r_2 and x1_l <= x2_r_2 and y1_r_2 <= y2_l <= y2_r_2 or \
                        x2_l >= x1_b_2 and x1_l <= x2_b_2 and y1_r_2 <= y2_b <= y2_r_2:
                    return False

    def obstacles_check(self, obstacles_list):
        x1_v, y1_v, x2_v, y2_v = canvas.coords(self.canon)
        x1_l, y1_l, x2_l, y2_l = canvas.coords(self.wheel_L)
        x1_p, y1_p, x2_p, y2_p = canvas.coords(self.wheel_R)
        x1_t, y1_t, x2_t, y2_t = canvas.coords(self.body)
        obstacle_num = -1

        for o in obstacles_list:
            obstacle_num += 1
            if self.position == "up":
                # canon
                # wheel_L
                # wheel_R
                # body
                if x1_v <= o[2] and x2_v >= o[0] and o[1] <= y1_v <= o[3] or \
                        x1_l <= o[2] and x2_l >= o[0] and o[1] <= y1_l <= o[3] or \
                        x1_p <= o[2] and x2_p >= o[0] and o[1] <= y1_p <= o[3] or \
                        x1_t <= o[2] and x2_t >= o[0] and o[1] <= y1_t <= o[3]:
                    return obstacles[obstacle_num]

            elif self.position == 'down':
                if x1_v <= o[2] and x2_v >= o[0] and o[3] >= y2_v >= o[1] or \
                        x1_l <= o[2] and x2_l >= o[0] and o[1] <= y2_l <= o[3] or \
                        x1_p <= o[2] and x2_p >= o[0] and o[1] <= y2_p < o[3] or \
                        x1_t <= o[2] and x2_t >= o[0] and o[1] <= y2_t < o[3]:
                    return obstacles[obstacle_num]

            elif self.position == "right":
                if y2_v >= o[1] and y1_v <= o[3] and o[0] <= x2_v <= o[2] or \
                        y2_l >= o[1] and y1_l <= o[3] and o[0] <= x2_l <= o[2] or \
                        y2_p >= o[1] and y1_p <= o[3] and o[0] <= x2_p <= o[2] or \
                        y2_t >= o[1] and y1_t <= o[3] and o[0] <= x2_t <= o[2]:
                    return obstacles[obstacle_num]

            elif self.position == "left":
                if y2_v >= o[1] and y1_v <= o[3] and o[0] <= x1_v <= o[2] or \
                        y2_l >= o[1] and y1_l <= o[3] and o[0] <= x1_l <= o[2] or \
                        y2_p >= o[1] and y1_p <= o[3] and o[0] < x1_p <= o[2] or \
                        y2_t >= o[1] and y1_t <= o[3] and o[0] < x1_t <= o[2]:
                    return obstacles[obstacle_num]


class Points:
    def __init__(self):
        self.points_list = {}
        self.score = 0
        self.score_text = canvas.create_text(1180, 680, text='Score: 0', fill='white', font='fixedsys 20')

        self.lives = 3
        self.lives_text = canvas.create_text(100, 680, text='Lives: 3', fill='white', font='fixedsys 20')

    def points_generation(self, length, x_start, y_start, space_x, space_y):
        for i in range(length):
            point = canvas.create_oval(i * space_x + (x_start - 10), i * space_y + (y_start - 10),
                                       i * space_x + (x_start + 10), i * space_y + (y_start + 10), fill='yellow',
                                       outline="")
            self.points_list[point] = canvas.coords(point)

    def points_score_system(self):
        det_point = self.detect_point()

        if det_point is not None:
            canvas.delete(det_point)
            self.points_list.pop(det_point)
            self.score += 20

            canvas.delete(points.score_text)
            self.score_text = canvas.create_text(1180, 680, text=f'Score: {self.score}', fill='white',
                                                 font='fixedsys 20')

    def detect_point(self):
        x1_v, y1_v, x2_v, y2_v = canvas.coords(tank_one.canon)
        x1_l, y1_l, x2_l, y2_l = canvas.coords(tank_one.wheel_L)
        x1_p, y1_p, x2_p, y2_p = canvas.coords(tank_one.wheel_R)
        x1_t, y1_t, x2_t, y2_t = canvas.coords(tank_one.body)

        for point_name, point_coordinates in self.points_list.items():
            x1, y1, x2, y2 = point_coordinates

            if tank_one.position == "up":
                if x1_v <= x2 and x2_v >= x1 and y1 <= y1_v <= y2 or \
                        x1_l <= x2 and x2_l >= x1 and y1 <= y1_l <= y2 or \
                        x1_p <= x2 and x2_p >= x1 and y1 <= y1_p <= y2 or \
                        x1_t <= x2 and x2_t >= x1 and y1 <= y1_t <= y2:
                    return point_name
            elif tank_one.position == "down":
                if x1_v <= x2 and x2_v >= x1 and y2 >= y2_v >= y1 or \
                        x1_l <= x2 and x2_l >= x1 and y1 <= y2_l <= y2 or \
                        x1_p <= x2 and x2_p >= x1 and y1 <= y2_p < y2 or \
                        x1_t <= x2 and x2_t >= x1 and y1 <= y2_t < y2:
                    return point_name
            elif tank_one.position == "right":
                if y2_v >= y1 and y1_v <= y2 and x1 <= x2_v <= x2 or \
                        y2_l >= y1 and y1_l <= y2 and x1 <= x2_l <= x2 or \
                        y2_p >= y1 and y1_p <= y2 and x1 <= x2_p <= x2 or \
                        y2_t >= y1 and y1_t <= y2 and x1 <= x2_t <= x2:
                    return point_name
            elif tank_one.position == "left":
                if y2_v >= y1 and y1_v <= y2 and x1 <= x1_v <= x2 or \
                        y2_l >= y1 and y1_l <= y2 and x1 <= x1_l <= x2 or \
                        y2_p >= y1 and y1_p <= y2 and x1 < x1_p <= x2 or \
                        y2_t >= y1 and y1_t <= y2 and x1 < x1_t <= x2:
                    return point_name

    def lives_minus(self):
        tank_one.reset_position(-1, tank_two.x, tank_one.y)
        tank_two.reset_position(-1, tank_two.x, tank_two.y)
        self.lives -= 1
        canvas.delete(self.lives_text)
        self.lives_text = canvas.create_text(100, 680, font='fixedsys 20', fill='white', text=f'Lives: {self.lives}')


class FollowLogic:
    def __init__(self):
        self.hit = "no"
        self.coordinates_save = []
        self.position_two_save = ""
        self.dist_x_save = 0
        self.dist_y_save = 0

    def follow(self, victim_body, follower_body):
        x1_vic, y1_vic, x2_vic, y2_vic = canvas.coords(victim_body)
        x1_f, y1_f, x2_f, y2_f = canvas.coords(follower_body)
        dist_x = x1_f + 25 - x1_vic + 25  # dist_x < 0 --> right; dist_x > 0 --> left
        dist_y = y1_f + 25 - y2_vic  # y1_vic+25  # dist_y < 0 --> down; dist_y > 0 --> up

        hit_coord = self.follow_tank_avoid(tank_two)
        if hit_coord is not None:
            self.hit = "yes"
            self.coordinates_save = hit_coord
            self.position_two_save = tank_two.position
            self.dist_x_save = dist_x
            self.dist_y_save = dist_y

        if self.hit == "yes":
            if self.position_two_save == 'up' or self.position_two_save == "down":
                if self.dist_x_save <= 0:
                    if x1_f - 5 > self.coordinates_save[2]:
                        self.hit = "no"
                    else:
                        tank_two.right(None)
                        tank_two.position = "right"
                else:
                    if x2_f + 5 < self.coordinates_save[0]:
                        self.hit = "no"
                    else:
                        tank_two.left(None)
                        tank_two.position = "left"

            if self.position_two_save == 'right' or self.position_two_save == 'left':
                if self.dist_y_save <= 0:
                    if y1_f - 5 > self.coordinates_save[3]:
                        self.hit = "no"
                    else:
                        tank_two.down(None)
                        tank_two.position = "down"
                else:
                    if y2_f + 5 < self.coordinates_save[1]:
                        self.hit = "no"
                    else:
                        tank_two.up(None)
                        tank_two.position = "up"

        elif abs(dist_x) > abs(dist_y) and self.hit == "no":
            if dist_x <= 0:
                tank_two.right(None)
                tank_two.position = "right"

            elif dist_x > 0:
                tank_two.left(None)
                tank_two.position = "left"

        elif abs(dist_x) < abs(dist_y) and self.hit == "no":
            if dist_y <= 0:
                tank_two.down(None)
                tank_two.position = "down"

            elif dist_y > 0:
                tank_two.up(None)
                tank_two.position = "up"

    @staticmethod
    def follow_tank_avoid(following_tank):
        # to avoid getting stuck at corners
        x1, y1, x2, y2 = canvas.coords(following_tank.canon)
        x1_l, y1_l, x2_l, y2_l = canvas.coords(following_tank.wheel_L)
        x1_r, y1_r, x2_r, y2_r = canvas.coords(following_tank.wheel_R)
        obstacle_num = -1

        for p in obstacles:
            obstacle_num += 1
            if following_tank.position == "up":
                if x1_l <= p[2] and x2_r >= p[0] and p[1] <= y1 - 2 <= p[3]:
                    return obstacles[obstacle_num]

            elif following_tank.position == 'down':
                if x1_l <= p[2] and x2_r >= p[0] and p[3] >= y2 + 2 >= p[1]:
                    return obstacles[obstacle_num]

            elif following_tank.position == "right":
                if y2_l >= p[1] and y1_r <= p[3] and p[0] <= x2 + 2 <= p[2]:
                    return obstacles[obstacle_num]

            elif following_tank.position == "left":
                if y2_l >= p[1] and y1_r <= p[3] and p[0] <= x1 - 2 <= p[2]:
                    return obstacles[obstacle_num]


class Program:
    def __init__(self):
        self.been_pressed = False

    def movement_init(self, _):
        if not program.been_pressed:
            self.points_render()
        program.been_pressed = True
        canvas.delete(intro)

        while 0 < points.lives <= 3:
            points.score -= 1
            canvas.delete(points.score_text)
            points.score_text = canvas.create_text(1180, 680, text=f'Score: {points.score}', fill='white',
                                                   font='fixedsys 20')
            if len(points.points_list) == 0:
                break

            elif tank_two.tank_collision(tank_one) is False:
                points.lives_minus()

                if points.lives > 0:
                    for i in countdown_list:
                        countdown = canvas.create_text(width / 2, height / 2, text=i, font='fixedsys 70', fill=text_c)
                        master.update()
                        time.sleep(1)
                        canvas.delete(countdown)
            else:
                self.movement()

        if points.lives > 0:
            canvas.create_text(width / 2, height / 2, font="fixedsys 60", fill=text_c,
                               text=f"{you_won:^24}\n{'your final score is ':^22}{points.score:<}")
        else:
            canvas.create_text(width / 2, height / 2, font="fixedsys 60", fill=text_c,
                               text=f"{'GAME OVER!':^24}\n{'your final score is ':^22}{points.score:<}")

    @staticmethod
    def movement():
        points.points_score_system()
        if tank_one.position == 'up' and tank_one.obstacles_check(obstacles) is None and tank_one.tank_collision(
                tank_two) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_one.canon)
            if y1 > 0:
                canvas.move(tank_one.wheel_L, 0, -tank_one.speed)
                canvas.move(tank_one.wheel_R, 0, -tank_one.speed)
                canvas.move(tank_one.canon, 0, -tank_one.speed)
                canvas.move(tank_one.body, 0, -tank_one.speed)

        if tank_one.position == 'down' and tank_one.obstacles_check(obstacles) is None and tank_one.tank_collision(
                tank_two) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_one.canon)
            if y2 < height:
                canvas.move(tank_one.wheel_L, 0, tank_one.speed)
                canvas.move(tank_one.wheel_R, 0, tank_one.speed)
                canvas.move(tank_one.canon, 0, tank_one.speed)
                canvas.move(tank_one.body, 0, tank_one.speed)

        if tank_one.position == 'left' and tank_one.obstacles_check(obstacles) is None and tank_one.tank_collision(
                tank_two) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_one.canon)
            if x1 > 0:
                canvas.move(tank_one.wheel_L, -tank_one.speed, 0)
                canvas.move(tank_one.wheel_R, -tank_one.speed, 0)
                canvas.move(tank_one.canon, -tank_one.speed, 0)
                canvas.move(tank_one.body, -tank_one.speed, 0)

        if tank_one.position == 'right' and tank_one.obstacles_check(obstacles) is None and tank_one.tank_collision(
                tank_two) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_one.canon)
            if x2 < width:
                canvas.move(tank_one.wheel_L, tank_one.speed, 0)
                canvas.move(tank_one.wheel_R, tank_one.speed, 0)
                canvas.move(tank_one.canon, tank_one.speed, 0)
                canvas.move(tank_one.body, tank_one.speed, 0)

        # tank_two
        foll.follow(tank_one.body, tank_two.body)

        if tank_two.position == 'up' and tank_two.obstacles_check(obstacles) is None and tank_two.tank_collision(
                tank_one) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_two.canon)
            if y1 > 0:
                canvas.move(tank_two.wheel_L, 0, -tank_two.speed)
                canvas.move(tank_two.wheel_R, 0, -tank_two.speed)
                canvas.move(tank_two.canon, 0, -tank_two.speed)
                canvas.move(tank_two.body, 0, -tank_two.speed)

        if tank_two.position == 'down' and tank_two.obstacles_check(obstacles) is None and tank_two.tank_collision(
                tank_one) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_two.canon)
            if y2 < height:
                canvas.move(tank_two.wheel_L, 0, tank_two.speed)
                canvas.move(tank_two.wheel_R, 0, tank_two.speed)
                canvas.move(tank_two.canon, 0, tank_two.speed)
                canvas.move(tank_two.body, 0, tank_two.speed)

        if tank_two.position == 'left' and tank_two.obstacles_check(obstacles) is None and tank_two.tank_collision(
                tank_one) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_two.canon)
            if x1 > 0:
                canvas.move(tank_two.wheel_L, -tank_two.speed, 0)
                canvas.move(tank_two.wheel_R, -tank_two.speed, 0)
                canvas.move(tank_two.canon, -tank_two.speed, 0)
                canvas.move(tank_two.body, -tank_two.speed, 0)

        if tank_two.position == 'right' and tank_two.obstacles_check(obstacles) is None and tank_two.tank_collision(
                tank_one) is not False:
            x1, y1, x2, y2 = canvas.coords(tank_two.canon)
            if x2 < width:
                canvas.move(tank_two.wheel_L, tank_two.speed, 0)
                canvas.move(tank_two.wheel_R, tank_two.speed, 0)
                canvas.move(tank_two.canon, tank_two.speed, 0)
                canvas.move(tank_two.body, tank_two.speed, 0)

        canvas.update()
        canvas.after(10)

    @staticmethod
    def points_render():
        points.points_generation(4, 42.5, 42.5, 50, 0)
        points.points_generation(11, 42.5, 92.5, 0, 50)
        points.points_generation(4, 202.5, 92.5, 0, 50)
        points.points_generation(5, 85, 282.5, 50, 0)
        points.points_generation(5, 85, 462.5, 50, 0)
        points.points_generation(9, 85, 597.5, 50, 0)
        points.points_generation(11, 367.5, 42.5, 0, 50)
        points.points_generation(2, 262.5, 640, 0, 50)
        points.points_generation(2, 205, 505, 0, 50)
        points.points_generation(9, 537.5, 300, 0, 50)
        points.points_generation(4, 412.5, 42.5, 50, 0)

        points.points_generation(4, width - 42.5, 42.5, -50, 0)
        points.points_generation(11, width - 42.5, 92.5, 0, 50)
        points.points_generation(4, width - 202.5, 92.5, 0, 50)
        points.points_generation(5, width - 85, 282.5, -50, 0)
        points.points_generation(5, width - 85, 462.5, -50, 0)
        points.points_generation(9, width - 85, 597.5, -50, 0)
        points.points_generation(11, width - 367.5, 42.5, 0, 50)
        points.points_generation(2, width - 262.5, 640, 0, 50)
        points.points_generation(2, width - 205, 505, 0, 50)
        points.points_generation(9, width - 537.5, 300, 0, 50)
        points.points_generation(4, width - 412.5, 42.5, -50, 0)

        points.points_generation(3, 590, 675, 50, 0)
        points.points_generation(3, 590, 462.5, 50, 0)
        points.points_generation(10, 412.5, 257.5, 50, 0)
        points.points_generation(10, 412.5, 122.5, 50, 0)

    @staticmethod
    def generate_obstacles():
        obstacle_color = "blue"

        wall_up = canvas.create_rectangle(0, -80, 455, 2, outline=obstacle_color, width=3)
        wall_up_two = canvas.create_rectangle(455, -80, 825, 2, outline=obstacle_color, width=3)
        wall_up_three = canvas.create_rectangle(825, -80, width, 2, outline=obstacle_color, width=3)

        wall_down = canvas.create_rectangle(0, height, width, height + 80, outline=obstacle_color, width=3)
        wall_right = canvas.create_rectangle(width, 0, width + 80, height / 2, outline=obstacle_color, width=3)
        wall_right_two = canvas.create_rectangle(width, height / 2, width + 80, height, outline=obstacle_color, width=3)

        wall_left = canvas.create_rectangle(-80, 0, 2, height / 2, outline=obstacle_color, width=3)
        wall_left_two = canvas.create_rectangle(-80, height / 2, 2, height, outline=obstacle_color, width=3)

        wall_lives = canvas.create_rectangle(0, height - 80, 200, height, outline=obstacle_color, width=3)
        wall_score = canvas.create_rectangle(width - 200, height - 80, width, height, outline=obstacle_color, width=3)

        wall_one = canvas.create_rectangle(width / 2 - 60, height / 2 - 60, width / 2 + 60, height / 2 + 60,
                                           outline=obstacle_color, width=3)
        wall_two = canvas.create_rectangle(85, 85, 160, 240, outline=obstacle_color, width=3)
        wall_three = canvas.create_rectangle(width - 160, 85, width - 85, 240, outline=obstacle_color, width=3)
        wall_five = canvas.create_rectangle(width - 245, 0, width - 325, 240, outline=obstacle_color, width=3)
        wall_six = canvas.create_rectangle(245, 0, 325, 240, outline=obstacle_color, width=3)

        wall_seven = canvas.create_rectangle(410, 165, width - 410, 215, outline=obstacle_color, width=3)
        wall_eight = canvas.create_rectangle(590, 0, 690, 80, outline=obstacle_color, width=3)
        wall_nine = canvas.create_rectangle(width - 495, height / 2 - 60, width - 410, height / 2 + 180,
                                            outline=obstacle_color, width=3)
        wall_ten = canvas.create_rectangle(410, height / 2 - 60, 495, height / 2 + 180, outline=obstacle_color, width=3)
        wall_eleven = canvas.create_rectangle(width / 2 - 60, 505, width / 2 + 60, 625, outline=obstacle_color, width=3)

        wall_twelve = canvas.create_rectangle(85, 325, 325, 420, outline=obstacle_color, width=3)
        wall_thirteen = canvas.create_rectangle(85, 505, 162.5, 555, outline=obstacle_color, width=3)
        wall_fourteen = canvas.create_rectangle(247.5, 505, 325, 555, outline=obstacle_color, width=3)

        wall_fifteen = canvas.create_rectangle(width - 85, 325, width - 325, 420, outline=obstacle_color, width=3)
        wall_sixteen = canvas.create_rectangle(width - 85, 505, width - 162.5, 555, outline=obstacle_color, width=3)
        wall_seventeen = canvas.create_rectangle(width - 247.5, 505, width - 325, 555, outline=obstacle_color, width=3)

        wall_eighteen = canvas.create_rectangle(width - 495, height - 80, width - 325, height,
                                                outline=obstacle_color, width=3)
        wall_nineteen = canvas.create_rectangle(325, height - 80, 495, height, outline=obstacle_color, width=3)

        return [canvas.coords(wall_up), canvas.coords(wall_up_two), canvas.coords(wall_up_three),
                canvas.coords(wall_down), canvas.coords(wall_right), canvas.coords(wall_right_two),
                canvas.coords(wall_left_two), canvas.coords(wall_left), canvas.coords(wall_lives),
                canvas.coords(wall_score), canvas.coords(wall_one), canvas.coords(wall_two), canvas.coords(wall_three),
                canvas.coords(wall_five), canvas.coords(wall_six), canvas.coords(wall_seven), canvas.coords(wall_eight),
                canvas.coords(wall_nine), canvas.coords(wall_ten), canvas.coords(wall_eleven),
                canvas.coords(wall_twelve), canvas.coords(wall_thirteen), canvas.coords(wall_fourteen),
                canvas.coords(wall_fifteen), canvas.coords(wall_sixteen), canvas.coords(wall_seventeen),
                canvas.coords(wall_eighteen), canvas.coords(wall_nineteen)]


if __name__ == '__main__':
    # tkinter init
    master = tkinter.Tk()
    master.title("Pac-Tank")

    height = 720
    width = 16 / 9 * height  # 1280
    background = "black"

    canvas = tkinter.Canvas(master, width=width, height=height, bg=background)
    canvas.pack()

    # init text
    countdown_list = [3, 2, 1, "GO!"]
    you_won = "YOU'VE WON!"
    get_caught = "DON'T GET CAUGHT!"
    text_c = "yellow"

    intro = canvas.create_text(width / 2, height / 2, text=F"{'PAC-TANK':^17}\n{get_caught:^17}", fill=text_c,
                               font='fixedsys 60')

    # creating instances
    tank_one = Tanks("up", 8, width / 2, 135, "yellow")
    tank_two = Tanks("up", 7, width / 2, height - 40, "red")
    points = Points()
    program = Program()
    foll = FollowLogic()

    obstacles = program.generate_obstacles()

    # bindings
    canvas.bind_all("<Left>", tank_one.left)
    canvas.bind_all("<Right>", tank_one.right)
    canvas.bind_all("<Down>", tank_one.down)
    canvas.bind_all("<Up>", tank_one.up)

    canvas.bind_all("<Return>", program.movement_init)

    tkinter.mainloop()
