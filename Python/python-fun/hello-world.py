x = "Hello Python!"
print x
y = 42
print y
# define a function that says hello to the name provided
# this starts a new block
# name = "jon"
def say_hello(name):
  #these lines are indented therefore part of the function
    if "jon":
        print 'Hello, ' + name + ' from inside the function'
    else:
        print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
say_hello(name"")