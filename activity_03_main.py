""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
from billing_account import BillingAccount
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy
from patterns.strategy.penalty_strategy import PenaltyStrategy
from payment.payment import Payment
from payee.payee import Payee

def strategy():
    """
    Tests the implementation of the Strategy pattern.
    """
    # Create a BillingAccount instance
    billing_account = BillingAccount()

    # Create payment strategies
    partial_payment_strategy = PartialPaymentStrategy()
    penalty_strategy = PenaltyStrategy()

    # Create Payment instances with strategies
    payment_with_partial = Payment(partial_payment_strategy)
    payment_with_penalty = Payment(penalty_strategy)

    # Test partial payment strategy
    try:
        print(payment_with_partial.pay_bill(billing_account, 50.00, Payee.ELECTRICITY))
    except ValueError as e:
        print(f"Error: {e}")

    # Test penalty payment strategy
    try:
        print(payment_with_penalty.pay_bill(billing_account, 30.00, Payee.INTERNET))
    except ValueError as e:
        print(f"Error: {e}")

    # Test with an invalid strategy
    try:
        invalid_payment = Payment("invalid_strategy")
    except ValueError as e:
        print(f"Error: {e}")

def observer():
    # Implementation of the observer pattern testing goes here
    pass

if __name__ == "__main__":
    strategy()
    observer()
