def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()


my_list=[22,25,23,24]  #itertors 
my_iter=iter(my_list)
print(next(my_iter))

def my_decorator(function):
    def wrapper(*args,**kwargs):
        print("Before funtion calling")
        result=function(*args,**kwargs)
        print("After funtion calling")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b
print("Sum",add(3,6))

''' output 
Before function call
Hello!
After function call
22
Before funtion calling
After funtion calling
Sum 9 '''