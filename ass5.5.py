def func(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s"  % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
    
func('carrot','oranges','eggs','bread','yogurt','potatoes','paratha')