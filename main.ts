let total = 0
let LABOUR = 0.75
let RENT = 1
let PRICE_PER_INCH_DIAMETER = 0.5
let HST = 1.13
let diameter = game.askForNumber("Enter the diameter of the pizza you would like (inch): ")
let sub_total = 100 * (PRICE_PER_INCH_DIAMETER * diameter + LABOUR + RENT)
total = sub_total * HST
total = Math.round(total)
total = total / 100
game.splash("The cost for a " + convertToText(diameter) + " inch pizza is $" + convertToText(total))
