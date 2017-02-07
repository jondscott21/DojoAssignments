import random


def coin_toss(num):
    print "Starting the program..."
    attempt = 0
    head_count = 0
    tail_count = 0
    while num > 0:
        num -= 1
        attempt += 1
        a_float = random.random()
        heads_or_tails = round(a_float)
        if heads_or_tails % 2 == 0:
            head_count += 1
            print "Attempt #" + str(attempt) +": Throwing a coin... It's a head! ... Got " + str(
                head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
        elif heads_or_tails % 2 != 0:
            tail_count += 1
            print "Attempt #" + str(attempt) + ": Throwing a coin... It's a head! ... Got " + str(
                head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"

coin_toss(5000)
