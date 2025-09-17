from abc import ABC,abstractmethod

# ---------- ProductA Interface ----------
class Button(ABC):

    @abstractmethod
    def render(self):
        pass

# ---------- ProductB Interface ----------
class Checkbox(ABC):

    @abstractmethod
    def render(self):
        pass


# ---------- Concrete ProductA1 ----------
class WinButton(Button):

    def render(self):
        print("Rendering Windows button")

# ---------- Concrete ProductA2 ----------
class MacButton(Button):

    def render(self):
        print("Rendering Mac button")

# ---------- Concrete ProductB1 ----------
class WinCheckbox(Checkbox):

    def render(self):
        print("Rendering Windows checkbox")
# ---------- Concrete ProductB2 ----------
class MacCheckbox(Checkbox):

    def render(self):
        print("Rendering Mac checkbox")

# ---------- Abstract Factory Interface ----------
class GUIFactory(ABC):

    @abstractmethod
    def createButton(self)-> Button:
        pass

    @abstractmethod
    def createCheckbox(self)-> Checkbox:
        pass

# ---------- Concrete Factory ----------
class Winfactory(GUIFactory):

    def createButton(self) -> Button:
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        return WinCheckbox()

# ---------- Concrete Factory ----------
class Macfactory(GUIFactory):

    def createButton(self) -> Button:
        return MacButton()
    
    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()


def getOs():
    return "MAC"

if __name__== "__main__":
    
    os= getOs()
    factory: GUIFactory
    if os=="WIN":
        factory:GUIFactory= Winfactory()
    elif os=="MAC":
        factory:GUIFactory= Macfactory()

    button= factory.createButton()
    checkbox= factory.createCheckbox()
    button.render()
    checkbox.render()



