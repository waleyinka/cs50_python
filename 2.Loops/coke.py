# Task: https://cs50.harvard.edu/python/psets/2/coke/

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

if __name__ == "__main__":
     main()