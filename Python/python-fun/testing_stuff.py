# def say_hi():
#   return "Hi"
# greeting = say_hi() #the returned value from say_hi function gets assigned to the 'greeting' variable
# print greeting # this will output 'Hi'


# def add(a, b):
#   x = a + b
#   return x
# sum1 = add(4,6)
# print sum1
# sum2 = add(1,4)
# print sum2
# sum3 = sum1 + sum2
# print sum3

# def multiply(arr,num):
#     for x in range(len(arr)):
#         arr[x] *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b


# dog = ("Canis Familiaris", "dog", "carnivore", 12)
# for data in dog:
#      print data


# weekend = {"Sun": "Sunday", "Mon": "Monday"} #literal notation
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print weekend["Sun"]
# print capitals["svk"]
# #to print all keys
# for data in capitals:
#      print data
# #another way to print all keys
# for key in capitals.iterkeys():
#      print key
# #to print the values
# for val in capitals.itervalues():
#      print val
# #to print all keys and values
# for key,data in capitals.iteritems():
#      print key, " = ", data


context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"