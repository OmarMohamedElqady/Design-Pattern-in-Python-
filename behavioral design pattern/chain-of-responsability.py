"""
The Chain of Responsibility design pattern is a "behavioral design pattern" that allows an object to pass 
a request along a chain of handlers. Each handler in the chain decides either to process the request or 
to pass it along the chain to the next handler
"""

"""
The Chain of Responsibility Design Pattern comprises the following key components:

Handler: This is an interface or abstract class that declares a method for handling requests
         and a reference to the next handler in the chain.

Concrete Handler: The concrete class that implements the Handler interface. It decides whether to process
                     a request or pass it to the next handler.

Client: The class that initiates the request and sends it to the first handler in the chain.
"""

"""

 Example:
 Let's say we have an application that processes customer support tickets. The tickets can be classified into 
different categories such as technical issues, billing inquiries, or general questions. We can use the Chain 
of Responsibility pattern to create a chain of handlers, where each handler specializes in handling a specific 
type of ticket.
 The chain may look like this:
 TechnicalSupportHandler -> BillingSupportHandler -> GeneralSupportHandler


"""


class Handler:
    def __init__(self, successor = None) :
        self._successor = successor

    def HandleRequest(self, request):
        if self._successor :
            return self._successor.HandleRequest(request)
        return None

class ConcreteHandler1(Handler):
    def HandleRequest(self, request):
        if request == "A":
            print("HandleRequest A from ConcreteHandler1")

        else :
            super().HandleRequest(request)    

class ConcreteHandler2(Handler):
    def HandleRequest(self, request):
        if request == "B":
            print("HandleRequest B from ConcreteHandler2")

        else :
            super().HandleRequest(request)    

class ConcreteHandler3(Handler):
    def HandleRequest(self, request):
        if request == "C":
            print("HandleRequest C from ConcreteHandler3")

        else :
            super().HandleRequest(request)    

class main():
    Handler1 = ConcreteHandler1()
    Handler2 = ConcreteHandler2()
    Handler3 = ConcreteHandler3()

    requests = ["A", "B", "C"]

    for req in requests:
        Handler3.HandleRequest(req)

if __name__ =="__main__":
    main()




