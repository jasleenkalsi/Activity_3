from payee.payee import Payee

class BillingAccount:
    """
    A class to represent a user's balances for various utility bills.

    Attributes:
        __balances (dict): A dictionary storing the balances for each payee (utility type) such as electricity, internet, and telephone.
        
    """
    def __init__(self):
        """
        Initializes all balances to 0.
        """
        self.__balances = {
            Payee.ELECTRICITY: 0.0,
            Payee.INTERNET: 0.0,
            Payee.TELEPHONE: 0.0
        }

    def add_balance(self, payee: Payee, amount: float):
        """
        Adds funds to the balance of a particular utility.
        
        Args:
            payee (Payee): The payee to which the funds will be applied.
            amount (float): The amount to apply to the balance.
        
        Raises: 
            ValueError: When the amount is non-numeric or negative.
            KeyError: If the payee is invalid.
        """
        if isinstance(amount, (int, float)):
            if payee in self.__balances:
                self.__balances[payee] += amount
        else:
            raise ValueError("Amount must be numeric.")

    def deduct_balance(self, payee: Payee, amount: float):
        """
        Deducts funds from the balance of a particular utility.
        
        Args:
            payee (Payee): The payee to which the funds will be deducted.
            amount (float): The amount to deduct from the balance.
        
        Raises: 
            ValueError: When the amount is non-numeric, negative, or greater than the balance.
            KeyError: If the payee is invalid.
        """
        if isinstance(amount, (int, float)):
            if payee in self.__balances:
                self.__balances[payee] -= amount
        else:
            raise ValueError("Amount must be numeric.")
        
        self.__balances[payee] -= amount

    def get_balance(self, payee: Payee) -> float:
        """
        Returns the balance of the specified utility.
        
        Args:
            payee (Payee): The payee for which the balance is requested.
        
        Returns:
            float: The balance of the specified utility.
        
        Raises:
            KeyError: If the payee is invalid.
        """
        if payee in self.__balances:
            return self.__balances.get(payee, 0.0)

    def __str__(self):
        """
        Returns a string representation of the BillingAccount object.
        
        Returns:
            string: A representation of the BillingAccount object.
        """
        return (f"Electricity Balance: ${self.__balances[Payee.ELECTRICITY]:,.2f}\n"
                f"Internet Balance: ${self.__balances[Payee.INTERNET]:,.2f}\n"
                f"Telephone Balance: ${self.__balances[Payee.TELEPHONE]:,.2f}")
    
