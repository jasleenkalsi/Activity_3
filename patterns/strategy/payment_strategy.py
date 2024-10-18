from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """
    Abstract base class for payment strategies.
    """

    @abstractmethod
    def process_payment(self, account, amount: float, payee):
        """
        Process the payment for a specific payee.

        Args:
            billing_account (BillingAccount): The billing account to deduct the payment from.
            amount (float): The amount to be paid.
            payee: The payee for which the payment is being made.
        
        Returns:
            str: A confirmation message indicating the payment result.
        """
        pass
