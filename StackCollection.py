import Stack as st
class StackCollection ():     
    def __init__(self):
        self.__data=st.Stack()
        
        
    def add(self,e):
            Hey=st.Stack()              
            if self.__data.isEmpty():
                self.__data.push(e)
            else:
                while not self.__data.isEmpty() and self.__data.top()<e:
                    Hey.push(self.__data.pop())
                    
                self.__data.push(e)
                while not Hey.isEmpty():
                    self.__data.push(Hey.pop())                

            
    def remove(self,e):
            Hey=st.Stack()              
            if self.__data.isEmpty():
                return None
            else:
                while not self.__data.isEmpty() and self.__data.top()!=e:
                    Hey.push(self.__data.pop())
                if self.__data.isEmpty():
                    temp=None                      
                else:
                    temp=self.__data.pop()
                while not Hey.isEmpty():
                    self.__data.push(Hey.pop())    
                return temp  


    def find(self,e): 
            Hey=st.Stack()              
            if self.__data.isEmpty():
                return None
            else:
                while not self.__data.isEmpty() and self.__data.top()!=e:
                    Hey.push(self.__data.pop())
                if self.__data.isEmpty():
                    temp=None                      
                else:
                    temp=self.__data.top()==e
                while not Hey.isEmpty():
                    self.__data.push(Hey.pop())    
                return temp                   

#Si la pila originial queda vacio retorna none si no queda vacia lo encontro 

    def printStack(self):
            Hey=st.Stack()              
            if self.__data.isEmpty():
                return None
            else:
                while not self.__data.isEmpty():
                    Hey.push(self.__data.pop())
                    print(Hey.top(),end=" ")
                print(" ")

                while not Hey.isEmpty():
                    self.__data.push(Hey.pop())         
                    
                    