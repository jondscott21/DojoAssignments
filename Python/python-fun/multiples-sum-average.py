# multiples part 1: prints 1-1000
for count in range(1, 1001):
    print count

# multiples part 2: prints multiples of 5 from 5-1,000,000
for count1 in range(5, 1000001, 5):
    print count1

# sum list
a = [1, 2, 5, 10, 255, 3]
sum_a = 0
for i in a:
    sum_a += i
print sum_a

# average list
a = [1, 2, 5, 10, 255, 3]
sum_avg = 0
for i in a:
    sum_avg += i
print sum_avg / len(a)

