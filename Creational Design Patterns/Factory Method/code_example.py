from abc import ABC, abstractmethod

# ---------- Product Interface ----------
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self,amount):
        pass


# ---------- Concreate Products ----------
class CashPaymentProcessor(PaymentProcessor):

    def pay(self, amount):
        print(f"Payment of {amount} done using Cash")

class CreditCardPaymentProcessor(PaymentProcessor):

    def pay(self, amount):
        print(f"Payment of {amount} done using Credit Card")


# ---------- Creator (Abstract)----------
class PaymentGateway(ABC):

    @abstractmethod
    def createProcessor(self) -> PaymentProcessor:
        pass

    def makePayment(self,amount):
        processor: PaymentProcessor= self.createProcessor()
        processor.pay(amount)
    

# ---------- Concreate Creators(Abstract)----------
class CashPaymentGateway(PaymentGateway):

    def createProcessor(self) -> PaymentProcessor:
        return CashPaymentProcessor()

class CreditCardPaymentGateway(PaymentGateway):

    def createProcessor(self) -> PaymentProcessor:
        return CreditCardPaymentProcessor()



if __name__ == "__main__":

    gateway:PaymentGateway= CashPaymentGateway()
    gateway.makePayment(100)

    gateway= CreditCardPaymentGateway()
    gateway.makePayment(500)