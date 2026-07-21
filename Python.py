#Section - A, Part-1, question-1
# Input from the user
print("Sectin-A  question-1")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
height_cm = float(input("Enter your height in cm: "))
print("Name:", name)
print("Age:", age)
print("Height:", height_cm)
# convert cm to feet
height_feet = height_cm * 0.0328084
print("Height in feet:",round(height_feet, 2),"feet")
# user is adult or not
adult = age>=18
if adult:
    print("Adult? : Yes")
else:    
    print("Adult? : NO")
print("\n") #for printing in new line and give some space 

#part-1 , question-2
print("Sectin-A  question-2")

a = 47
b = 5
print("Value of a =", a)
print("Value of b =", b)
# Arithmetic Operator
print("Arithmetic Operators")
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus", a%b)
print("Power:", a**b)
# comparison Operator
print(" Comparison Operators")
print("a == b:", a==b)
print("a != b:", a!=b)
print("a > b:", a>b)
print("a < b:", a<b)
print("a >= b:", a>=b)
print("a <= b:", a<=b)
# Logical Operator
print("Logical Operators")
print("Is a greater than 40 and less than 100?")
print(a > 40 and a < 100 )
# Membership Operators
numbers =[10,47,90]
print("47 in list:", 47 in numbers)
print("50 in list:", 50 in numbers)
# Identity Operators
print("Identity Operators")
x = None#
y = None
print("x is y :", x is y)
print("\n")

# part-1 question-3
print("Sectin-A  question-3")

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Input")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")  
print("\n")

#Section-B question-4
# Print a pattern using nested for loop
print("Sectin-B question-4")

for i in range(1,7):
    for j in range(i):
        print("*", end="")
    print()
# print a table 
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1,11):
    print(num, "x", i, "=", num*i)
print("\n")

# question-5 String Operation
print("Sectin-B  question-5")

sentence = input("Enter a sentence:")
print("Uppercase:", sentence.upper())
print("lowercase:", sentence.lower())
# count vowels
count=0
for ch in sentence.lower():
    if ch in "aeiou":
        count += 1
print("Number of Vowels :", count)        
# Reverse the sentence
print("Reverse:", sentence[::-1])
# Replaces the space with underscores
print("Replace Space :", sentence.replace(" ", "_"))
# python is present or not
if "python" in sentence.lower():
    print("The word 'python' is present.")
else: 
    print("The word 'python' is Not present.")    
print("\n")

# question-6 while loop 
print("Sectin-B  question-6")

total = 0
count = 0
while True:
    number = int(input("Enter a number(0 to stop): "))
    if number == 0:
        break
    total += number
    count += 1
if count > 0:
    average= total/count
else:
    average = 0
print("Result")
print("Total =", total)
print("Count =", count)
print("Average =", average)
print("\n")

# Section-C Question-7
print("Sectin-C question-7")

numbers = [15,3,9,27,6,42,18,3,9,55]
print("original list:", numbers)
# ascending order
ascending = sorted(numbers)
print("Ascending order:", ascending)
# descending order
descending = sorted(numbers,reverse=True)
print("Descending order:", descending)
# removing duplicate values
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List without Duplicates:", unique)        
# second largest number
unique.sort(reverse=True)
print("Second largest number:", unique[1])
# # list comprehension for even numbers
even_numbers =[num for num in numbers if num %2 ==0]
print("Even Numbers:", even_numbers)
print("\n")

 # question-8 Set Operations
print("Sectin-C question-8")

classA ={"Alice","Bob","Carol","David"}
classB ={"Carol","David","Eve","Frank"}
#print union
print("Union:")
print(classA | classB)
#print intersection
print("Intersection:")
print(classA & classB)
#print difference
print("Difference (Only Class A):")
print(classA - classB)
# symmetric difference
print("Symmetric Difference:")
print(classA ^ classB)
print("\n")

# question-9 Tuple Usage
print("Sectin-C question-9")

movies = (("3 idiots", "Dhammal", "Housefull", "Welcome", "KGF"))
print("Movies Name:", movies)
#print first and last movie using indexing
print("First Movie:", movies[0])
print("last Movie:", movies[-1])
# reverse the tuple 
print("Reverse Tuple:", movies[::-1])
#convert tuple to list
movie_list = list(movies)
print("Movie list:",  movie_list)
# add new movie
movie_list.append("Bahubali")
print("After adding new movie:",movie_list)
# convert back to tuple
movies = tuple(movie_list)
print("Movie Tuple:", movies)
print("Updated Tuple:", movies)
print("\n")

# Question-10 Dictionary
print("Sectin-C question-10")

student = {"name": "Aliya", "roll.no":"2146","marks":{"Maths":86,"English":90,"Science":85,"Computer": 94}}
print("Student Data:", student)
#print keys and values
print("Keys:", student.keys())
print("Values:", student.values())
# calculate average marks
marks= student["marks"]
average = sum(marks.values())/len(marks)
print("Average Marks:", average)
# add new subject
marks.update({"Hindi": 88, "Physics":84})
print("After adding new subject:")
print(marks)
#delete one subject
marks.pop("English")
print("After Removing English:")
print(marks)
print("\n")

# question-11 Dictionary Comprehension
print("Sectin-C question-11")

words = ["Apple","Banana","Cherry","Date","Watermelon"]
print("Fruits Words:", words)
# word length
word_length = {word:len(word) for word in words}
print("Dictionary:")
print(word_length)
# filter the words with length greater than 5
filtered = {word: length for word, length in word_length.items() if length>5}
print("Filtered Dictionary:", filtered)
print("\n")

# Section- D, Functions, Question-12
# function to check prime number
print("Sectin-D  question-12")

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
# Factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
# Reverse a string
def reverse_string(s):
    return s[::-1]
# calling the function
num = int(input("Enter a number: "))
print("Is Prime:", is_prime(num))
print("Factorial:",factorial(num))
text=input("Enter a string:")
print("Reversed String:", reverse_string(text))       
print("\n")

# question-13 *args and **kwargs
# *args
print("Sectin-D  question-13")

def total_marks(*subjects):
    total=sum(subjects)
    average=total/len(subjects)
    print("Total marks:",total)
    print("Average marks:", average)
# function call
total_marks(85,90,95,80,78,88)
# **kwargs
def student_profile(**details):
    print("Student Details")
    for key, value in details.items():
        print(key,".",value)
    # function call
student_profile(Name="Riya",Age=22,City="Delhi",Course="B.Tech CSE")        
print("\n")

# question-14 lambda, map(), filter(), enumerate()
print("Sectin-D question-14")

marks=[45,82,67,91,55,73,88,39,95,60]
print("Marks:", marks)
# using the filter 
above60 = list(filter(lambda x:x>60,marks))
print("Marks Above 60:",above60)

#using the map()
bonus= list(map(lambda x:min(x+5,100),marks))
print("Bonus Marks:",bonus)

# sort the list in descending order
sorted_marks = sorted(marks, key=lambda x:x, reverse=True)
print("Descending Order:",sorted_marks)

#using enumerate
print("Ranking")
for rank,score in enumerate(sorted_marks,start=1):
    print(rank,":",score)
print("\n")

# Question-15, zip()function
print("Sectin-D  question-15")

students = ["Alice","Bob","Carol","David"]
scores = [88,72,95,61]
#pair and print the pairs
pairs = list(zip(students,scores))
print("Student and Score")
for student, score in pairs:
    print(student,"-", score)

# Highest score
highest = max(pairs, key=lambda x:x[1])
print("Highest Score:")
print(highest[0],"-", highest[1])

#usig list comprehension
result=[f"{student} scored {score}" for student, score in zip(students, scores)]
print(("Result List"))
for i in result:
    print(i)
print("\n")

# Section-E, question-16, Module usage
print("Sectin-E  question-16")

import os
import sys
import datetime
import math
# Os Module
# print current directory
print("Current Directory:")
print(os.getcwd())
# all files / folders in current directory
print("Files and Folders:")
print(os.listdir())
# file exists or not
print("Does notes.txt exists?")
print(os.path.exists("notes.txt"))

# sys module
# check python version
print("Python Version:")
print(sys.version)
# print platform
print("Platform:")
print(sys.platform)
# memory size of 1000 numbers
numbers = list(range(1000))
print("Memory Size:")
print(sys.getsizeof(numbers))

# Datetime module
#print current date and time
today = datetime.datetime.now()
print("Current Date and Time:")
print(today.strftime("%d-%b-%Y %H:%M:%S"))
# calculate the days for new year
new_year = datetime.datetime(today.year +1,1,1,)
days_left = (new_year - today).days
print("Days left Until New Year:", days_left)

# Math module
# print pi upto 5 decimal places
print("pi:", round(math.pi,5))
# find sqrt, ceiling, floor 
print("Square Root:", math.sqrt(78.6))
print("Ceiling:", math.ceil(78.6))
print("floor:", math.floor(78.6))
# calculate factorial of 10
print("Factorial of 10:", math.factorial(10))
print("\n")

# Section - F, Question-17 file Handling
# create and write to a file
print("Sectin-F question-17")

file = open("diary.txt","w")
file.write("India is a big Country.")
file.write("I live in India.")
file.write("Delhi is the Capital Of India.")
file.close()
# Read the file
file = open("diary.txt","r")
print("File Contents:")
print(file.read())
file.close()
# append new lines
file = open("diary.txt","a")
file.write("India is the land of festivals.")
file.write("I Love my Country.")
file.close()
# read the file
file = open("diary.txt","r")
print("Updated File:")
print(file.read())
file.close()
print("\n")

# question - 18, Exception handling
# ask the user for two numbers and divide them
print("Sectin-F  question-18")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer numbers.")

else:
    print("Result =",result)
finally:
    print("Calculate attempt finished.\n")

#open a file for reading
try:
    file = open("missing.txt","r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: The file is 'missing.txt' was not found.\n")

#Access the index 10
my_list = [10,20,30,40,50]
try:
    print(my_list[10])
except IndexError:
    print("Error: List index is out of range.\n")
print("\n")

#Section- G, Question - 19 OOP - Library System
# Base class
print("Sectin-G question-19")

class Book:
    def __init__(self,title,author,year,price):
        self.title = title
        self.author = author
        self.year = year
        self.__price = price #private

    def get_price(self):
        return self.__price
    
    def info(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Year: {self.year}")
        print(f"Price : {self.__price}")
#print using the f-strings
    def __str__(self):
        return f"{self.title} by {self.author}"    
    
# Child Class
# created a child class which has an attribute of file size
class EBook(Book):
    def __init__(self,title,author,year,price,file_size):
        super().__init__(title,author,year,price)
        self.file_size = file_size

    def info(self):
        super().info()
        print(f"File Size :{self.file_size} MB") 
        print()    
    
# Child Class
# created a child class which count the name of pages
class PrintedBook(Book):
    def __init__(self,title,author,year,price,pages):
        super().__init__(title,author,year,price)
        self.pages = pages

    def info(self):
        super().info()
        print(f"Pages :{self.pages}") 
        print()       

# Library Class
class Library:
    def __init__(self):
        self.books = []
# add the book in library
    def add_book(self,book):
        self.books.append(book)
# show all the books
    def show_all_books(self):
        for book in self.books:
            book.info()
# book find by their author name
    def find_by_author(self, author_name):
        print("Books by", author_name)
        for book in self.books:
            if book.author == author_name:
                print(book)
# print the total sum of all the values
    def total_value(self):
        total = 0
        for book in self.books:
            total += book.get_price()
        return total

# Objects
book1 = EBook("Python Basics","Saurabh",2024,500,20)
book2 = PrintedBook("AI Book","Rakesh Gupta", 2023,700,300) 
# Polymorphism
books = [book1, book2]
print("Polymorphism")
for b in books:
    b.info()
# Library
library = Library()
library.add_book(book1)
library.add_book(book2)

print("All Books")
library.show_all_books()
library.find_by_author("Saurabh")
#returns the sum of all the values
print("Total Value =", library.total_value())
print("\n")

# Bonus Mini Project 
# Build a command line contact book
print("Project: Contact Book Mini Project")
class ContactBook:

    def __init__(self):
        self.contacts ={}
# Add Contact
    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")    
        city = input("Enter City: ")

        self.contacts[name] ={"phone":phone,"email":email,"city":city}
        print("Contact Added Successfully")
# view contacts
    def view_contacts(self):
        if not self.contacts:
            print("No Contacts Found") 
            return
        for name, info in self.contacts.items():
            print("-------------")
            print("Name:",name)
            print("Phone:",info["phone"])
            print("Email:",info["email"])
            print("City:",info["city"])
        print()
# Search Contacts
    def search_contact(self):
        name = input("Enter Name to search: ") 

        if name in self.contacts:
           print(self.contacts[name])
        else:
            print("Contact not found")       
# Delete Contacts
    def delete_contact(self):
        name = input("Enter Name To Delete:  ")

        if name in self.contacts:
           del self.contacts[name]
           print("Contact Deleted")
        else:
           print("Contact Not Found")    
# Save to File
    def save_file(self):
        try:
            file = open("Contacts.txt","w")
            for name,info in self.contacts.items():
                file.write( f"{name},{info['phone']},{info['email']},{info['city']}")
            file.close()
            print("Contacts Saved Successfully")

        except Exception:
          print("Error Saving File")
#load from file
    def load_file(self):
        try:
            file = open("Contacts.txt","r")
            for line in line:
                name,phone,email,city = line.strip().split(",")
                self.contacts[name] ={"phone":phone,"email":email,"city":city}
            file.close()
            print("Contacts Loaded Successfully.\n")

        except FileNotFoundError:
           print("Contacts.txt not found")    
# lambda function
    def lambda_demo(self):
        upper = lambda x:x.upper()
        print("Contact Names: ")
        for name in self.contacts:
            print(upper(name))
# List Comprehension
    def list_demo(self):
        names = [name for name in self.contacts]
        print("Names List:", names)            

book = ContactBook()
while True:
    print("======Contact Book======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Delete Contacts")
    print("5. Save Contacts")
    print("6. Load Contacts")
    print("7. Lambda Demo")
    print("8. List Comprehension Demo")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book.add_contact()

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        book.search_contact()
        
    elif choice == "4":
        book.delete_contact()
        
    elif choice == "5":
        book.save_file()
        
    elif choice == "6":
        book.load_file()
        
    elif choice == "7":
        book.lambda_demo()
        
    elif choice == "8":
        book.list_demo()
        
    elif choice == "9":
       print("Thank you!")
       break

    else:
      print("Invalid Choice")
