# prints odd and even numbers
def odd_even(x, y):
    for count in range(x, y):
        if count % 2 == 0:
            print "Number is " + str(count) + ". This is an even number"
        elif count % 2 != 0:
            print "Number is " + str(count) + ". This is an odd number"
odd_even(1, 2001)


# multiplies through a list
def multiply(a, x):
    for i in range(len(a)):
        a[i] *= x
    print a
multiply([1, 2, 5, 7], 3)
