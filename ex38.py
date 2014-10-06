ten_things = "Apple, Oranges, Crows, Telephone, Light, Sugar"

stuff = ten_things.split(', ')

print "printing stuff"
print stuff

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print "printing more_stuff: ", more_stuff

more_stuff.sort()
print "printing sorted more_stuff: ", more_stuff

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now" % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join()
print '#'.join(stuff[3:5])
