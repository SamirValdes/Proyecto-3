import Queue as qc
class QueueCollection():
    def __init__(self):
        self.__data=qc.Queue()
        
        
    def add(self,e):
            Hey=qc.Queue()
            if self.__data.isEmpty():
                self.__data.enqueue(e)
            else:
                while not self.__data.isEmpty() and self.__data.first()<e:
                    Hey.enqueue(self.__data.dequeue())
                    
                self.__data.enqueue(e)
                while not Hey.isEmpty():
                    self.__data.enqueue(Hey.dequeue()) 
               
    def remove(self,e):                                                                                    
            Hey=qc.Queue()
            if self.__data.isEmpty():
                return None
            else:                    
                while not self.__data.isEmpty() and self.__data.first()!=e:
                    Hey.enqueue(self.__data.dequeue())
                if self.__data.isEmpty():
                    temp=None
                else:
                    temp=self.__data.dequeue()
                while not Hey.isEmpty():
                    self.__data.enqueue(Hey.dequeue())
                return temp
            
            
    def find(self,e):
            Hey=qc.Queue()
            if self.__data.isEmpty():
                return None
            else:                    
                while not self.__data.isEmpty() and self.__data.first()!=e:
                    Hey.enqueue(self.__data.dequeue())
                if self.__data.isEmpty():
                    temp=None
                else:
                    temp=self.__data.first()==e
                while not Hey.isEmpty():
                    self.__data.enqueue(Hey.dequeue())
                return temp        
                        
    def printQueue(self):
        
            Hey=qc.Queue()              
            if self.__data.isEmpty():
                return None
            else:
                while not self.__data.isEmpty():
                    Hey.enqueue(self.__data.dequeue())
                    print(Hey.first(),end=" ")
                print(" ")

                while not Hey.isEmpty():
                    self.__data.enqueue((Hey.dequeue()))                   
            
            