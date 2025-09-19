from abc import ABC,abstractmethod
from collections import defaultdict

# ---------- Base publisher ----------
# The base publisher class includes subscription management
# code and notification methods.
class EventManager:

    def __init__(self):
        self.listners= defaultdict(list)
    
    def subscribe(self,eventType,listner):
        self.listners[eventType].append(listner)
    
    def unsubscribe(self,eventType,listner):
        self.listners[eventType].remove(listner)
    
    def notify(self,eventType,data):
        for listner in self.listners[eventType]:
            listner.update(data)

# ---------- publisher ----------
# The concrete publisher contains real business logic that's
# interesting for some subscribers.
class Editor:

    def __init__(self):
        self.eventManager= EventManager()

    def openFile(self,fileName):
        # some file open logic code here

        self.eventManager.notify("open",fileName)
    
    def saveFile(self,fileName):
        # some file save logic here

        self.eventManager.notify("save",fileName)

# ---------- Subscriber Interface ---------- 
class EventListner(ABC):

    @abstractmethod
    def update(self,data):
        pass 

# ---------- Concrete Subscribers ---------- 
class LoggingListner(EventListner):

    def __init__(self,msg):
        self.msg= msg

    def update(self, fileName):
        # some logic for logging msg string to file
        self.msg= f"LOGGED: {self.msg} {fileName}"
        print(self.msg)

class EmailListner(EventListner):

    def __init__(self,email,msg):
        self.msg= msg
        self.email= email

    def update(self, fileName):
        # some logic for Sending msg string as Mail
        self.msg= f"MAILED: TO {self.email} {self.msg} {fileName} "
        print(self.msg)


if __name__=="__main__":

    editor= Editor()
    logger= LoggingListner("Someone has opened the file: ")
    editor.eventManager.subscribe("open",logger)
    emailAlerts= EmailListner("john@gmail.com","Someone has changed the file: ")
    editor.eventManager.subscribe("save",emailAlerts)

    editor.openFile("file.txt")
    editor.saveFile("some_file.txt")