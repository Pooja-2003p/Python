#part-1 set de-duplication and basic operations
my_list=[10,20,20,30,40,40,50]
print("My List:",my_list)
 #print the unique numbers
unique_numbers=set(my_list)
print("Unique Numbers:",unique_numbers)
#print intersection values
even_numbers={20,30,40,60,80}
print("Intersection:",unique_numbers.intersection(even_numbers))
#print the union of both sets
print("Union:",unique_numbers.union(even_numbers))

#part-2 advance set methods
my_set = set()
#add the value
my_set.add(5)
my_set.add(10)
print("Sets:",my_set)
#update method to add muultiple values
my_set.update([15,20,25])
print("After updating the element:",my_set)
#remove the element
my_set.remove(10)
print("After removing the element:",my_set)
print("Final Set:",my_set)
#using the .issubset 
subset={5,15,20,25,30}
print("Is Subset:",my_set.issubset(subset))

#part-3 Tuple packing and unpacking 
student_info=("Alice",20,"A")
#formatted the student info
name, age, grade = student_info
print("Name:", name)
print("Age:", age)
print("Grade:", grade)
#type error
# student_info[0]="Bob"
# print(student_info[0])

#part-4 Tuple methods and indexing 
scores=(85,90,85,70,85,95)
print("Scores:",scores)
#using the count method
print("Count of 85:",scores.count(85))
#using the index method
print("Index number of 90:",scores.index(90))

#part-5 Dictionary Creation and manipulation 
employee={"Name":"Mayank", "Department":"IT", "Salary":50000}
print("Employee:",employee)
#update the salary
employee.update({"Salary":65000})
print("After updation salary:",employee)
# add a new key-value pair
employee["Role"]="Manager"
print("After adding new pair:",employee)
# delete a department
del employee["Department"]
print("After delete department:",employee)
print("Final Dictionary:",employee)

#part-6 looping through dictionaries
capitals={"France":"Paris","Japan":"Tokyo","India":"New Delhi"}
#use a for loop to print only keys
print("countries:")
for country in capitals:print(country)
# use a for loop to print only values
print("Capitals:")
for capital in capitals.values():print(capital)
# print both keys and values
print("Country and Capital:")
for country,capital in capitals.items():
     print(f"The capital of {country} is {capital}")

#part-7 Basic Dictionary comprehension
nums=[1,2,3,4,5]
print("Numbers:",nums)
#using a dictionary comprehension
square_dict={i:i**2 for i in nums}
print("Square Dict:",square_dict)

# part-8 Dictionary comprehension with conditions
marks={"Alice":85,"BOb":40,"Charlie":92,"David":55}
print("Studnets marks:",marks)
#using a dict. comprehension with conditions
passed_students={name:mark for name, mark in marks.items() if mark>=60}
print("Passes_Students:",passed_students)

#part-9 user-defined functions(basics)
#greeting message
def greet(name):
    return(f"Good Morning,{name}!")
print(greet("Alice"))

# generte a table
def generate_table(n):
    table = []
    for i in range(1,11):
        table.append(n*i)
    return table
print("Table of 7:",generate_table(7))

#part-10 Advance logic inside functions
def check_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n** 0.5)+1):
        if n % i ==0:
            return False
        
    return True
print("IS 47 Prime?",check_prime(47))  
print("IS 10 Prime?",check_prime(10))  

# remove duplicates and sort the list
numbers=[4,2,8,2,5,1,6,4]
cleaned_list=sorted(set(numbers))
print("Cleaned list:",cleaned_list)
