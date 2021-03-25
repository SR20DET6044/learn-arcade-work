import arcade

def

arcade.open_window(600, 600, "Car")

arcade.set_background_color((arcade.csscolor.CORNFLOWER_BLUE))

arcade.start_render()

#rectangle body

arcade.draw_rectangle_filled(300, 325, 120, 20, (201, 40, 67))

arcade.draw_rectangle_filled(300, 330, 240, 20, (201, 40, 67))

arcade.draw_rectangle_filled(180, 325, 20, 20, (201, 40, 67))

arcade.draw_rectangle_filled(420, 325, 20, 20, (201, 40, 67))

arcade.draw_rectangle_filled(300, 340, 260, 25, (201, 40, 67))

#polygon top body

arcade.draw_polygon_filled(((220, 320),
                            (380, 320),
                            (350, 390),
                            (250, 390),
                            ),
                           (201, 40, 67))

#windows

arcade.draw_polygon_filled(((280, 360),
                            (355, 360),
                            (345, 380),
                            (280, 380),
                            ),
                           arcade.csscolor.LIGHT_SKY_BLUE)

arcade.draw_polygon_filled(((245, 360),
                            (270, 360),
                            (270, 380),
                            (255, 380),
                            ),
                           arcade.csscolor.LIGHT_SKY_BLUE)

#arc over wheels

arcade.draw_arc_filled(385, 315, 70, 25, (201, 40, 67), 0, 180)

arcade.draw_arc_filled(215, 315, 70, 25, (201, 40, 67), 0, 180)

arcade.draw_circle_filled(215, 295, 28, arcade.csscolor.CORNFLOWER_BLUE)

arcade.draw_circle_filled(385, 295, 28, arcade.csscolor.CORNFLOWER_BLUE)

#circle wheels

arcade.draw_circle_filled(385, 300, 20, arcade.csscolor.DARK_SLATE_GREY)

arcade.draw_circle_filled(215, 300, 20, arcade.csscolor.DARK_SLATE_GREY)

arcade.draw_circle_filled(385, 300, 15, arcade.csscolor.GREY)

arcade.draw_circle_filled(215, 300, 15, arcade.csscolor.GREY)

#headlight

arcade.draw_arc_filled(430, 330, 10, 20, arcade.csscolor.WHITE_SMOKE, 90, 270)

#taillight

arcade.draw_arc_filled(170, 330, 10, 20, arcade.csscolor.GOLDENROD, 270, 450)

#door handle

arcade.draw_line(285, 345, 300, 345, arcade.color.BLACK, 2)


arcade.finish_render()

arcade.run()