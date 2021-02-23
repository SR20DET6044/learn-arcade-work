import arcade

arcade.open_window(600,600,"Draw snowman")


arcade.start_render()

# set background color

arcade.set_background_color(arcade.csscolor.ALICE_BLUE)


# draw snowman body

arcade.draw_circle_filled(300, 120, 120, arcade.csscolor.ANTIQUE_WHITE)

arcade.draw_circle_filled(300,280,80,arcade.csscolor.ANTIQUE_WHITE)

# draw snowman eyes

arcade.draw_circle_filled(270,285,10,arcade.csscolor.BLACK)

arcade.draw_circle_filled(330,285,10,arcade.csscolor.BLACK)

#draw snowman nose

arcade.draw_triangle_filled(270, 250, 300, 280, 300, 265, arcade.csscolor.DARK_SALMON)

#draw snowman button

arcade.draw_circle_filled(300, 130, 8, arcade.csscolor.DARK_OLIVE_GREEN)

arcade.draw_circle_filled(300, 165, 8, arcade.csscolor.DARK_OLIVE_GREEN)

#draw snowman hat

arcade.draw_triangle_filled(260, 350, 340, 350, 300, 440, arcade.csscolor.SIENNA)

arcade.finish_render()


arcade.run()
