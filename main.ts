input.onButtonPressed(Button.A, function () {
    Intensity += 50
})
input.onButtonPressed(Button.B, function () {
    Intensity += -50
})
let Intensity = 255
// Adding the code forever to constantly loop.
basic.forever(function () {
    led.setBrightness(Intensity)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        `)
    // Adding a pause for 500ms
    basic.pause(500)
    basic.clearScreen()
    led.setBrightness(Intensity)
    basic.showLeds(`
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        `)
    basic.pause(500)
    basic.clearScreen()
})
