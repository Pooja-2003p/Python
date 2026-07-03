# ---Question1----
def multiply_numbers(num1, num2=10):
    return num1 * num2

print("Multiply (5, 4):", multiply_numbers(5, 4))
print("Multiply (7):", multiply_numbers(7))

#---Question2-----
def sum_all(*args):
    return sum(args)


print("Sum all (1,2,3):", sum_all(1, 2, 3))
print("Sum all (10,20,30,40):", sum_all(10, 20, 30, 40))

# ---Question3----
def top_student(**kwargs):
    highest = max(kwargs, key=kwargs.get)
    return highest


print("Top Student:", top_student(alice=85, bob=92, charlie=78))

# ---lambda function-----
uppercase=lambda text: text.upper()


print("Uppercase String:",uppercase("hello world"))
# ---map,filter,emuerate---
# --Question1----
mixed_list = [1, "hello", 3.14, "world", 42]


strings = list(filter(lambda x: type(x) == str, mixed_list))


print("Filtered Strings:", strings)


#----Question2----
celsius_temps = [0, 20, 37, 100]


fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_temps))


print("Fahrenheit Temps:", fahrenheit)

#----Question3----
words = ["apple", "bat", "cat", "elephant"]


word_dict = {}


for index, word in enumerate(words, start=1):
    if len(word) > 4:
        word_dict[index] = word


print("Enumerated Words:", word_dict)
# ---combine filter&map----

numbers = list(range(1, 21))


result = list(
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print("Squared Even Numbers:", result)
