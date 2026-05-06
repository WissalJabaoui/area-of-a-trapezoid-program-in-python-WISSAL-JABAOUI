# Area of trapezoid.This program asks the user for the values of base1, base2 and the height. 
# it then calculates and displays the area.
# done by Wissal Jabaoui 
game.splash("Let's calculate the area of a trapezoid!")
base1 = game.ask_for_number("what is the length of base1 in (cm)? ")
base2 = game.ask_for_number("what is the length of base2 in (cm)? ")
height = game.ask_for_number("what is the height in (cm)? ")
area = (base1 + base2) / 2 * height
game.splash("the area of a trapzoid is:" + str(area))