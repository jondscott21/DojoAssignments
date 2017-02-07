#find and replace
test_string = "If monkeys like bananas, then I must be a monkey!"
print test_string.find("monkey")
print test_string.rfind("monkey")
print test_string.replace("monkey", "alligator")

#min and max values in the list
x = [3, 76, 49, 32, 743, 90, 5, 7]
print min(x)
print max(x)

#sort and slice
list1 = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
list1.sort()
print list1

list2 = list1[:2]
list1 = list1[2:]
print list2
print list1

list3 = list1
list3.insert(0, list2)
print list3
