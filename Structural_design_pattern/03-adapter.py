"""
Adapter is a type of ٍٍStructural Design Patterns

The Adapter is used when you have an existing interface that doesn't directly map to an interface 
that the client requires. So, then you create the Adapter that has a similar functional role, but
with a new compatible interface.
"""

class ClassA():
    "A Sample Class the implements IA"

# Target Interface:
# In this context, the target interface is the interface
#  that the client expects to interact with, which is the
#  ClassA interface by the method_a function.

    def method_a(self):
        print("method A")

class ClassB():
    "A Sample Class the implements IB"
# Adaptee (Initialized):
#Adaptee in this context is ClassB, which contains the method_b() function.

 
    def method_b(self):
        print("method B")

class ClassBAdapter():
    "ClassB does not have a method_a, so we can create an adapter"
    
# adapter converter 
# The converter is the ClassBAdapter class, which is used to 
# adapt the ClassB interface to the ClassA interface. The adapter 
# provides the method_a() function that the client expects,
#  but performs this function by calling the method_b() function from ClassB.

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()
          
# Client (client):
# The client is the part of the code that uses the converter 
# to interact with the initializer. In this context, the client 
# is the final part of the code that uses the ITEMS list to interact
#  with ClassA and ClassBAdapter objects.




# Before the adapter I need to test the objects class to know which
# method to call.
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# After creating an adapter for ClassB I can reuse the same method
# signature as ClassA (preferred)
ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()

    """
    when to use :
    1 - working with a new interface (in compatible)        compatible == two things that can't interfere with each other  


    2 - classes with different implementation but do the same job 
    
    """

"""


The Adapter design pattern is a structural pattern that acts as a 
bridge between two incompatible interfaces, allowing them to 
work together. Imagine you have two friends—one speaks only 
English, and the other speaks only French. You want them to 
communicate, but there’s a language barrier. You step in as an 
adapter, translating messages between them. Your role enables 
the English speaker to convey messages to you, and you convert 
those messages into French for the other person. Similarly, the 
Adapter pattern bridges the gap between incompatible 
interfaces.

"""
 

"""
Target Interface: ClassA
Adaptee: ClassB            
Adapter: ClassBAdapter
Client: The last piece of code that uses the ITEMS list to interact with objects.

"""

