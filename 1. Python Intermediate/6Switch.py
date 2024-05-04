# the switches are pretty much the same as `if`, `elif`, `and` and `or` statements. which is newly introduced to python 3.5 

direction = input("which direction? ").lower()

match direction:   # this means that what ever someone inputs in the directions, if it is one of the cases below, match it: 
    case "north":   # if someone has input "north", then print "go Up".
        print("go upwards")
    case "south":   # if someone has input "south", then print "go down".
        print("go downwards")
    case "east":   # if someone has input "east", then print "go right".
        print("go right")
    case "west":   # if someone has input "west", then print "go left".
        print("go left")

    case _:         # the `_:` means that if none of the cases above are entered, then print this text:
        print("not a valid direction!! make sure you have entered the right input!")

