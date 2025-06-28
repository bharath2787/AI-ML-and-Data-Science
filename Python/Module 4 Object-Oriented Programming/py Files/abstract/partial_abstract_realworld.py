



'''
Real-World Example: Payment System with Partial Abstraction
Let’s consider a payment gateway system where:

The base class Payment defines a general process_payment() method (which can be common for all types of payments).
However, the detailed implementation of how the payment is processed (i.e., using credit cards, PayPal, etc.) is left to the subclasses.



Why Partial Abstraction?
Code Reusability: The base class can handle common operations for all types of payments, avoiding code duplication.
Flexibility: The subclasses are free to implement their own verification and execution logic specific to the payment method they handle.



Real-World Analogy:
Think of a restaurant system where the base class Order defines the steps for 
processing an order (e.g., take_order(), process_payment()). However, each 
type of order (dine-in, takeout, delivery) would have its own way of handling 
specifics like delivery charges, special instructions, etc.

This allows the system to keep a standard structure but provides customizability for different types of orders.


'''


from abc import ABC, abstractmethod

# Abstract base class (partial abstraction)
class Payment(ABC):
    
    # A concrete method - shared functionality
    def process_payment(self, amount):
        print(f"Processing payment of {amount}...")
        self._verify_payment()  # Specific method for payment verification (abstract)
        self._execute_payment()  # Specific method for executing the payment (abstract)
        print(f"Payment of {amount} completed successfully.")

    @abstractmethod
    def _verify_payment(self):
        """Method to verify payment details, must be implemented in subclasses"""
        pass

    @abstractmethod
    def _execute_payment(self):
        """Method to execute payment, must be implemented in subclasses"""
        pass


# Subclass for Credit Card payment
class CreditCardPayment(Payment):
    def _verify_payment(self):
        print("Verifying Credit Card details...")

    def _execute_payment(self):
        print("Charging Credit Card for payment.")


# Subclass for PayPal payment
class PayPalPayment(Payment):
    def _verify_payment(self):
        print("Verifying PayPal account details...")

    def _execute_payment(self):
        print("Charging PayPal account for payment.")


# Subclass for Cryptocurrency payment
class CryptoPayment(Payment):
    def _verify_payment(self):
        print("Verifying Cryptocurrency wallet details...")

    def _execute_payment(self):
        print("Charging Cryptocurrency wallet for payment.")


# Testing the classes
def test_payment(payment_method: Payment, amount: float):
    payment_method.process_payment(amount)


# Creating instances of different payment methods
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
crypto_payment = CryptoPayment()

# Processing payments
test_payment(credit_card_payment, 100)
test_payment(paypal_payment, 200)
test_payment(crypto_payment, 300)
