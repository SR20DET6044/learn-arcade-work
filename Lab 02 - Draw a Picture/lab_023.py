import arcade

arcade.open_window(600, 600, "Tic Tac Toe")

arcade.set_background_color((91, 128, 88))

arcade.start_render()

#vertical

arcade.draw_rectangle_filled(200, 300, 20, 600, (224, 224, 209))

arcade.draw_rectangle_filled(400, 300, 20, 600, (224, 224, 209))

#horizontal

arcade.draw_rectangle_filled(300, 200, 600, 20, (224, 224, 209))

arcade.draw_rectangle_filled(300, 400, 600, 20, (224, 224, 209))

#x



#o




arcade.finish_render()

arcade.run()