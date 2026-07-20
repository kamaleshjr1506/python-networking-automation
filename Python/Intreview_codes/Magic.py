Magic Methods(__repr__, __str__, __add__, __len__ etc.)
Return vs Yield
generator vs iterator
Context Manager
Decerators
Get Set in encapsulation
Operator Overloading




#Context Manager
f = open("file.txt")
data = f.read()
f.close()
#👉 If error happens before close() → file stays open ❌

#✅ Solution
with open("file.txt") as f:
    data = f.read()

#👉 Automatically:
# open ✔️
# use ✔️
# close ✔️
# A context manager is an object that defines:
# __enter__()
# __exit__()

#with A() as x:

obj = A()
x = obj.__enter__()
try:
    # your code
finally:
    obj.__exit__()



#Generators vs Iterators
#👉 Generator: A function that yields values one at a time, allowing you to iterate over
def gen():
    yield 1
    yield 2
    yield 3
    yield 4
g= gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


#Encapsulation
#👉 Encapsulation: The bundling of data and methods that operate on that data within a single unit, typically a class.
class A:
    def __init__(self):
        self.__x = "kamales"
    
    @property    
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        self.__x = value
        print(self.__x)
        
a = A()
print(a.x)
a.x = 1000
print(a.x)


#Decorator 
#A decorator is a function that modifies or extends the behavior of another function without changing its original source code.
#A decorator should return a wrapper function:

def my_dec(fun):
    def wrapper():
        print("strat")
        #print("name",fun.__name__)  # special attribute to get the name of the function
        fun()
        print("end")
    return(wrapper)


@my_dec
def display():
    print("hello")
display()


#Dunder Methods (Magic Methods)
#👉 Dunder methods, also known as magic methods, are special methods in Python that have double underscores at the beginning and end of their names. They allow you to define how objects of a class behave with respect to built-in operations.
class sam:
    def __init__(self,value):
        self.value = value
    
    def __add__(self,other):
        print(self.value + other.value)
n1 = sam(1)
n2 = sam(20)
(n1+n2)