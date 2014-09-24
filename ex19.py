def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or we can use variable from our script:"
cheesenum = 10
crackernum = 50

cheese_and_crackers(cheesenum, crackernum)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20 , 5 + 6)

print "And we can combine the two, variable and math:"
cheese_and_crackers(cheesenum + 100, crackernum + 1000)
  
