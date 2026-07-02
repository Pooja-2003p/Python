#Part-1 welcome and string manipulation
a = "Welcome To Python Cafe"
print(a)

full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))

print((full_name.strip()))
print((full_name.title()))

first_name = full_name.split()[0]
print("Hello,", first_name +"!")

# the menu and operators
menu = ("Burger, Pizza, pasta, Coffee")
print("Menu:", menu)

item = input("what would you like to order?")

if item in menu:
    quantity = int(input("How many would you like?"))
    
    price = 150
    total_cost = price * quantity
    print("Awesome!Calculating your bill..")

#Discounts and logics
discount = 0

if age < 18 or quantity > 5:
    discount = total_cost * 0.10
    print("10% Discount applied!")

elif age > 60:
    discount = total_cost * 0.20
    print("20% Discount applied!")

else:
    print("No Discount applied!")
    final_bill = total_cost - discount

# the receipt and nested logic
if final_bill > 500:
    if first_name.startswith("A") or first_name.startswith("S"):
        print("VIP Customer")

    print()
    for i in range(5):
        for j in range(25):
            print("*", end="")
        print()

print("         RECEIPT")
print("Name     :", full_name)
print("Item     :", item)
print("Qunatity :", quantity)
print("final Bill :", final_bill)

for i in range(5):
    for j in range(25):
        print("*", end="")
    print()
