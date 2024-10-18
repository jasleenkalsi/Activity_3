from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount

class Payment:
    """
    A class to handle payments using a specific payment strategy.
    """
    
    def __init__(self, strategy: PaymentStrategy):
        """
        Initializes the Payment class with a specific payment strategy.
        
        Args:
            strategy (PaymentStrategy): The payment strategy to use for payments.
        
        Raises:
            ValueError: If the provided strategy is not a PaymentStrategy.
        """
        if isinstance(strategy, PaymentStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Invalid Strategy")
        
    def pay_bill(self, billing_account: BillingAccount, amount: float, payee):
        """
        Processes the bill payment using the assigned strategy.

        Args:
            billing_account (BillingAccount): The billing account to deduct from.
            amount (float): The amount to be paid.
            payee: The payee to which the payment is made.
        
        Returns:
            str: The result of the payment processing.
        """
        return self.strategy.process_payment(billing_account, amount, payee)
