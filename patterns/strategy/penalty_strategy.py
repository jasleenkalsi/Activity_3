from payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PenaltyStrategy(PaymentStrategy):
    """
    Strategy for applying a penalty for insufficient payment.

    This class applies a penalty fee if the payment made is insufficient
    to cover the balance of the specified utility in a BillingAccount.
    If the balance is positive after the payment, a penalty fee is added to
    the balance.
    """

    def process_payment(self, account: BillingAccount, payee: Payee , amount: float) -> str:
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            account.add_balance(payee, 10.00)  
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:.2f}."
