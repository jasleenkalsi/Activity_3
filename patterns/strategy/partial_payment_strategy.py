from payee.payee import Payee
from payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount

class PartialPaymentStrategy(PaymentStrategy):
    """
    Strategy for making a partial payment on a bill.
    
    This class is an implementation of the PaymentStrategy interface, allowing
    a partial payment to be made to a utility bill within a BillingAccount. It
    deducts the specified amount from the balance and returns a message indicating
    the payment status and the remaining balance.

    """

    def process_payment(self, account: BillingAccount, payee: Payee , amount: float ) -> str:
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
