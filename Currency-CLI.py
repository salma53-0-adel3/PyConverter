import time
import os
def clear_screen() :
    os.system('cls' if os.name == 'nt' else 'clear')
def rate() :
    print("\nUSD: 1.0\nEUR: 0.89\nEGP: 52.31\nRMB: 6.70\n")
prices = {
    'USD' : 1.0,
    'EUR' : 0.89,
    'EGP' : 52.31,
    'RMB' : 6.70,   
}
def convert() :
    print("Welcome to 'Currency Coverter'  ")   
    print(r"""
     +===============================================================+
        / $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ /|
       / || [100]          THE UNITED STATES OF AMERICA   [100] || / |
      /  ||                                                     ||/  |
  +===============================================================+   |
  | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |   |
  | || +------+                                       +------+ || |   |
  | || | 100  |      THE UNITED STATES OF AMERICA     | 100  | || |   |
  | || +------+                                       +------+ || |   /
  | ||                .-----------------------.                || |  /
  | ||               /   *   S A L O M A   *   \               || | /
  | ||               \   ONE HUNDRED DOLLARS   /               || |/
  | ||                '-----------------------'                || |
  | || +------+                                       +------+ || |
  | || | 100  |        THIS NOTE IS LEGAL TENDER      | 100  | || |
  | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
  +===============================================================+                   """)
    print('_'*65)
    rate()
    currency=input("Choose a currency to convert from: ").upper()
    while True :
        try: amount=float(input("Enter the amount: "))
        except ValueError : clear_screen() ; print("This's not a number.") ; continue
        while True :
            confirm=input(f"You entered {amount} {currency}. confirm? (Y/N): ").upper()
            if confirm == "N" or confirm == "Y" :
                break
            else : clear_screen() ; print("Invalid Input")
        if confirm == "Y" : 
            break
    clear_screen()
    rate()
    currency2 = input("Choose a currency to convert to: ").upper()
    print("Analyzing your request....please wait")
    time.sleep(2)
    print(f"Checking for {currency2}'s best rates available....please wait")
    time.sleep(3)
    print(f"Getting a discount price for {currency}....please wait")
    time.sleep(4)
    if currency not in prices or currency2 not in prices :
        print("Invalid currency. Conversion canceled.\nReturning to main menu...")
        time.sleep(5)
        convert()
    else :
     clear_screen()
     print(f"Preparing the deal from {currency} to {currency2}....Please wait")
     time.sleep(3)
     curr_rate = prices[currency]
     curr_rate2 = prices[currency2]
     Calculator = (amount / curr_rate) * curr_rate2
     print(f"Exchange Rate: 1 {currency} = {curr_rate2 / curr_rate:.4f} {currency2}.")
     print(f"{amount} {currency} is equal to {Calculator:.2f} {currency2}")
     while True :
         choice = input("Do you accept this transaction? (Y/N): ").lower()
         if choice == "y" : print("\n***** Transaction Successful! *****\n") ; break
         elif choice == "n" : print("\nTransaction Canceled\n") ; break
         else : print("Invalid Input")
    while True :
     another= input("Do you want to perform another conversion? (Y/N): ").lower()
     if another == "n" : print("Thanks for using our app!") ; break
     elif another != 'y' and another != 'n' :  print("Invalid Input")
     else :
      print("Loading...")
      time.sleep(4)
      clear_screen()
      convert()
      break
convert()