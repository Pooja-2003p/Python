# ---Part 1: List Basics---

fruits = ["Apple", "Banana", "Orange", "Grapes", "Cherry", "Pineapple"]

fruits[2] = "Mango"

print("First 3 fruits:", fruits[:3])
print("Last 2 fruits:", fruits[-2:])
print("Reversed list:", fruits[::-1])


# Part 2: ---List Comprehension----

numbers = [2, 5, 8, 11, 14, 17, 20, 25]

squares = [i * i for i in numbers]
print("Squares:", squares)

even = [i for i in numbers if i % 2 == 0]
print("Even:", even)


# Part 3: ----If-Else List Comprehension---

temperature = [35, 12, 40, 8, 22, 45, 18]

weather = ["Hot" if i > 30 else "Cool" for i in temperature]
print("Weather:", weather)


# Part 4: ---String Manipulation-----

names = ["taniya", "suman", "pooja", "anu", "rani"]

capitalized_names = [i.title() for i in names]
print("Capitalized Names:", capitalized_names)

filtered_names = [i for i in names if len(i) >= 5]
print("Names with 5+ chars:", filtered_names)


# Part 5: -----List Methods------
list1 = []

list1.append(10)
list1.append(20)
list1.append(30)

list1.insert(1, 15)

list1.remove(20)

pop =list1.pop()
print("Pop Element:", pop)

unordered = [8, 3, 1, 5, 4]

unordered.sort()

print("My List:", list1)
print("Sorted List:", unordered)


# Part 6: ---Advanced List Comprehension----

words = ["information", "backend", "administration", "hellokitty", "learning"]

word_lengths = [len(i) for i in words]
print("Word Lengths:", word_lengths)

prices = [100, 250, 45, 300, 80]

discounted_prices = [i * 0.9 if i > 150 else i for i in prices]
print("Discounted Prices:", discounted_prices)
