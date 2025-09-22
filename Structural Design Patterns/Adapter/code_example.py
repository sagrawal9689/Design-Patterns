from abc import ABC,abstractmethod

# ---------- Client Interface ----------
class Shape(ABC):

    @abstractmethod
    def draw(self,x,y,widht,height):
        pass

# ---------- Adaptee Service ----------
class LegacyRectangle:

    def draw(self,x1,y1,x2,y2) -> None:
        print(f"Drawing rectangle using x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")

# ---------- Adapter ----------
class DrawRectangleAdapter(Shape):

    def __init__(self,adaptee:LegacyRectangle):
        self.adaptee= adaptee
    
    def draw(self, x, y, widht, height):
        x1,y1= x,y 
        x2,y2= x+widht,y+height
        self.adaptee.draw(x1,y1,x2,y2)


if __name__=="__main__":

    rectangleService= LegacyRectangle()
    drawRectAdapter= DrawRectangleAdapter(rectangleService)

    drawRectAdapter.draw(1,1,2,2) 