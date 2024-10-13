""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

def strategy():
    print("STRATEGY PATTERN OUTPUT")

    # Given: Creates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 200.0)
    account.add_balance(Payee.INTERNET, 100.0)
    account.add_balance(Payee.TELEPHONE, 150.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Create a Payment object with a PenaltyStrategy payment strategy.


    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.

    


    # 3. Create a Payment object with a PartialPaymentStrategy payment strategy.
    

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.
    

    # 5. Using the Payment object created in step 3, make another payment for the 
    # TELEPHONE bill with an amount that pays off the remainder of the balance - print 
    # the result of the pay_bill method.
   

    # 6. Print the BillingAccount object to show the updated balances for each of the payees.
    

def observer():
    print("OBSERVER PATTERN OUTPUT")
    # 1. Create a Restaurant object.
   

    #2. Create two Chef objects with names of your choice.
    
    
    #3. Create two Waiter objects with names of your choice.
    

    #4. Print each of the Chef and Waiter objects.
    

    #5. Attach one chef (of your choice) as a restaurant observer.
    

    #6. Attach one waiter (of your choice) as a restaurant observer.
    

    #7. Add the following events:
    #   New dish added to the menu: Grilled Cheese Sandwich.
    #   Special promotion on desserts.
    #   We are out of tomatoes!
    # When the program executes, note who receives notification of the events
    # and who does not receive notification.




if __name__ == "__main__":
    strategy()
    print("************************************")
    observer()