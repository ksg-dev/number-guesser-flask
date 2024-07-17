inputs = eval(input())
# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        output = function(*args)
        print(f"It returned: {output}")
    return wrapper


# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])