def on_button_pressed_a():
    global Intensity
    Intensity += 50
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Intensity
    Intensity += -50
input.on_button_pressed(Button.B, on_button_pressed_b)

Intensity = 255
# Adding the code forever to constantly loop.

def on_forever():
    led.set_brightness(Intensity)
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                # . # . #
                . # . # .
    """)
    # Adding a pause for 500ms
    basic.pause(500)
    basic.clear_screen()
    basic.show_leds("""
        # . # . #
                . # . # .
                # . # . #
                . # . # .
                # . # . #
    """)
    basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever)
