__author__ = 'echoecho'

def whileloop(loop_top, inc):
    i = 0
    numbers = []

    while i < loop_top:
        print "At the top i is %d" % i
        numbers.append(i)

        i += inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

def forloop(loop_top, inc):
    numbers = []

    for i in range(0, loop_top, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    print "The numbers: "

    for num in numbers:
        print num

whileloop(10, 2)
forloop(10, 2)