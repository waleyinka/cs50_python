# COKE MACHINE

# Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user
# has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

def main():
     amount_due = 50

     while amount_due > 0:
          print(f"Amount Due: {amount_due}")

          coin = get_coin()

          if coin == 0:
               print("Invalid amount! Please insert 5, 10 or 25\r\nInsert coin (5, 10, 25):")
               continue
          amount_due -= coin

          if amount_due > 0:
               print(f"Amount due: {amount_due}")

     print(f"Change Owed: {abs(amount_due)}")

def get_coin():
     amount_inserted = int(input("Insert coin (5, 10, 25):"))
     if amount_inserted in [5, 10, 25]:
          return amount_inserted
     else:
          return 0

main()