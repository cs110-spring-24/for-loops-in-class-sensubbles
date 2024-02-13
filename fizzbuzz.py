### 4: FizzBuzz

#In the `fizzbuzz.py` file, we will write some code to simulate the Fizz Buzz problem.

#Instruction

#1. Print out all the numbers between 1 and 30
#2. If the number is a multiple of 3, instead of printing the number, print out “Fizz”
#3. If the number is a multiple of 5, instead of printing the number, print out “Buzz”
#4. If the number is a multiple of 15, instead of printing the number, print out “FizzBuzz”

fizz = 0
buzz = 0
fizzbuzz = 0

for count in range(1, 30, 1):
   if count % 15 == 0:
        print("Fizzbuzz")
        fizzbuzz += 1
   elif count % 3 == 0:
        print("Fizz")
        fizz+= 1
   elif count % 5 == 0:
        print("Buzz")
        buzz += 1
print(f"We got {fizz} fizzes, {buzz} buzzes, and {fizzbuzz} fizzbuzzes")
    