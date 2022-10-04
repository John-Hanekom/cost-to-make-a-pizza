MULTIPY_OR_DIVIDE = 100
total = 0
LABOUR = 0.75
RENT = 1
PRICE_PER_INCH_DIAMETER = 0.5
HST = 1.13
diameter = game.ask_for_number("Enter the diameter of the pizza you would like (inch): ")
sub_total = PRICE_PER_INCH_DIAMETER * diameter + LABOUR + RENT
total = sub_total * HST
total = Math.round(0.01)
game.splash("The cost for a " + convert_to_text(diameter) + " inch pizza is $" + convert_to_text(total))