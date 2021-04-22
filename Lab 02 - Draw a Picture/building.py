import arcade

arcade.open_window(600, 600, "Building")

arcade.set_background_color((0, 0, 156))

arcade.start_render()

#road

arcade.draw_rectangle_filled(300, 40, 600, 80, (55, 59, 64))

arcade.draw_rectangle_filled(300, 90, 600, 20, (116, 121, 130))


arcade.draw_rectangle_filled(300, 40, 40, 10, (214, 170, 11))

arcade.draw_rectangle_filled(150, 40, 40, 10, (214, 170, 11))

arcade.draw_rectangle_filled(450, 40, 40, 10, (214, 170, 11))

arcade.draw_rectangle_filled(0, 40, 40, 10, (214, 170, 11))

arcade.draw_rectangle_filled(600, 40, 40, 10, (214, 170, 11))


#car

def draw_car_1():

    arcade.draw_rectangle_filled(340, 60, 70, 15, (189, 31, 31))

    arcade.draw_rectangle_filled(340, 70, 40, 17, (156, 191, 247))

    arcade.draw_rectangle_filled(340, 60, 70, 15, (189, 31, 31))

    arcade.draw_circle_filled(320, 55, 8, arcade.csscolor.DARK_GREY)

    arcade.draw_circle_filled(360, 55, 8, arcade.csscolor.DARK_GREY)

draw_car_1()

def draw_car_2():

    arcade.draw_rectangle_filled(140, 24, 40, 17, (156, 191, 247))

    arcade.draw_rectangle_filled(140, 14, 70, 15, (51, 204, 97))

    arcade.draw_rectangle_filled(140, 14, 70, 15, (51, 204, 97))

    arcade.draw_circle_filled(120, 9, 8, arcade.csscolor.DARK_GREY)

    arcade.draw_circle_filled(160, 9, 8, arcade.csscolor.DARK_GREY)

draw_car_2()

arcade.finish_render()

arcade.run()