'''
Consider a payment system where we enforce a structure for payment methods.

Explanation:

Payment is an abstract class.
pay() is an abstract method that each payment method must implement.
CreditCardPayment and PayPalPayment implement pay() differently.

'''


from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# Creating instances
credit_card = CreditCardPayment()
credit_card.pay(100)  # Output: Paid 100 using Credit Card

paypal = PayPalPayment()
paypal.pay(200)  # Output: Paid 200 using PayPal
