from random import randint


def scores():
    for i in range(1, 11):
        random_num = randint(60, 101)
        if 60 <= random_num < 70:
            print "Score: " + str(random_num) + "; Your grade is D"
        elif 70 <= random_num < 80:
            print "Score: " + str(random_num) + "; Your grade is C"
        elif 80 <= random_num < 90:
            print "Score: " + str(random_num) + "; Your grade is B"
        elif 90 <= random_num <= 100:
            print "Score: " + str(random_num) + "; Your grade is A"
scores()
