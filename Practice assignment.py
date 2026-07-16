#part-1 list basics & slicing
travel_bag=["Passport",3,"Charger",120.05, "Sunglasses","True"]
#print the entire list
print("Travel Bag:",travel_bag)
#print the first and last element
print("First Element:",travel_bag[0])
print("Last Element:",travel_bag[5])
#print the fourth element  using negative indexing
print("Fourth Element:",travel_bag[-4])
#slice and print a sublist containing just charger and '120.05'
print("Sliced List:",travel_bag[2:4])
#reverse the list
print("Reversed list:",travel_bag[::-1])

#part-2 modification list & sorting
scores=[85,92,78,92,89,76]
print("Scores list:",scores)
#extend the list
scores.extend([95,88,82])
print("After extend:",scores)
# append the list
scores.append([5,10])
print("After append:",scores)
#access the number
print("Number 10:",scores[-1][1])
#insert the number
scores.insert(3,90)
print("After insertion:",scores)
#pop the number
scores.pop()
print("After Popped last elemenr:",scores)
scores.pop(5)
print("After popped 5th element:",scores)
#remove the element
scores.remove(92)
print("After removing:",scores)
#count the 92 in the list
scores.count(92)
print("Count of 92:",scores)
#sort the list in descending order
scores.sort(reverse=True)
print("Descending order:",scores)
#reverse the list
scores.reverse()
print("After Reversing:",scores)

#part-3 Nested list & multi-dimensional indexing
classroom=[
["Alice",90,88],
["Bob",78,82],
["Charlie",95,91],
["Diana",85,89],
]
#access charlie's science grade
print("Charlie's Science Grade:",classroom[2][2])
# Bob's maths grade
print("Bob's Maths Grade:",classroom[1][1])
#update the Diana's maths grade
classroom[3][1]=88
print("updated Maths Grade:")
print(classroom)
#print average grade
for student in classroom:
    name=student[0]
    average=(student[1]+student[2])/2
    print(name,"Average Grade:",average)

#part-4 loops & generation
multiples_of_three=[]
# find multiple of 3
for i in range(1,31):
    if i%3==0:
        multiples_of_three.append(i)
print("Multiples of 3:")
print(multiples_of_three)
#print using indices
for i in range(len(multiples_of_three)):
    print("Element at index",i,"is",multiples_of_three)

#part-5 zip()function
products=["laptop","Smartphone","Headphones","Tablet"]
prices=[1200,800,150,450]
print("Products and Prices")
#zip function
for product,price in zip(products,prices):
    print("Product:",product, "| Price:$",price)
    #number Catalog
print("catalog")    
count = 1
for product,price in zip(products,prices):
    print(count,".",product, "($",price,")", sep="")
    count+=1
# Day 1 and Day 2 sales
day_1_sales=[10,15,8,12]
day_2_sales=[5,20,12,18]
print("Total Sales")
for day1, day2 in zip(day_1_sales,day_2_sales):
    print(day1+day2)

#challenge question
day_1_revenue=[]
for price, quantity in zip(prices,day_1_sales):
    revenue=price*quantity
    day_1_revenue.append(revenue)
print("Day 1 Revenues:",day_1_revenue)
