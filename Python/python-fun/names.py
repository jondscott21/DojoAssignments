# part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for i in range(len(students)):
    print students[i]["first_name"], students[i]["last_name"]


#part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for i in range(len(users)/2):
    for j in range(len(users["Students"])):
        print str(j) + " " + users["Students"][j]["first_name"] + " " + users["Students"][j]["last_name"]\
              + " " + str(len(users["Students"][j]["first_name"]) + len(users["Students"][j]["last_name"]))
for i in range(len(users)):
    for j in range(len(users["Instructors"])):
        print str(j) + " " + users["Instructors"][j]["first_name"] + " " + users["Instructors"][j]["last_name"]\
              + " " + str(len(users["Instructors"][j]["first_name"]) + len(users["Instructors"][j]["last_name"]))

# pair programmed with Jon Eboh and Jackie Thind
