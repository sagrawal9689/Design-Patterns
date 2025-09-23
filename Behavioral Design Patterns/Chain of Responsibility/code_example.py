from abc import ABC,abstractmethod

# ---------- Handler Interface ----------
class Logger(ABC):

    @abstractmethod
    def log(self,request):
        pass 

    @abstractmethod
    def setNext(self):
        pass 

# ---------- Base handler ----------
class BaseLogger(Logger):

    def __init__(self) -> None:
        self.next:Logger= None

    def log(self, request):
        if self.next:
            self.next.log(request)

    def setNext(self,next: Logger):
        self.next= next

# ---------- Concrete handlers ----------
class DebugLogger(BaseLogger):

    def log(self,request):

        if request.get("level") == "DEBUG":
            print(f"[DEBUG]: {request.get('message')}")
        else:
            super().log(request)

class InfoLogger(BaseLogger):

    def log(self,request):

        if request.get("level") == "INFO":
            print(f"[INFO]: {request.get('message')}")
        else:
            super().log(request)

class ErrorLogger(BaseLogger):

    def log(self,request):

        if request.get("level") == "ERROR":
            print(f"[ERROR]: {request.get('message')}")
        else:
            super().log(request)


if __name__ == "__main__":
    logger1= ErrorLogger()
    logger2= InfoLogger()
    logger3= DebugLogger()

    logger1.setNext(logger2)
    logger2.setNext(logger3)

    logger1.log({ "level": "INFO", "message": "Server started at port 5000" })
    logger1.log({ "level": "DEBUG", "message": "username is Sahil" })
    logger1.log({ "level": "ERROR", "message": "Invalid username" })