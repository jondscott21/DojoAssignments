# part 1
def draw_stars(lil_list):
    for i in range(len(lil_list)):
        print lil_list[i]*"*"

draw_stars([4, 6, 1, 3, 5, 7, 25])


# part 2
def draw_stars(lil_list):
    for i in range(len(lil_list)):
        if type(lil_list[i]) is str:
            x = str.lower(lil_list[i])
            print x[0]*len(x)
        else:
            print lil_list[i]*"*"
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Neutron"])

# Pair programmed with: Sarah Drake, Jon Eboh, Jackie Thind.