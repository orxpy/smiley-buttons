from microbit import*

def on_button_pressed_a():
    spiral = {}
    spiral[0] = images(0, 0, 0, 0, 0)
    display.show(spiral[0])



input.on_button_pressed(Button.A, on_button_pressed_a)