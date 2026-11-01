class Payment_methods:
    def process_payment(self, amount):
        print("Payment is being processed...")
class CreditCardPayment(Payment_methods):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}...")


class PayPalPayment(Payment_methods):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}...")
        

payment = [Payment_methods() ,CreditCardPayment(), PayPalPayment()]
for payment in payment:
    payment.process_payment(100)  