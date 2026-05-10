1. Swapping Two Numbers (No Third Variable)
Question: Swap the values of two variables without using a temporary third variable.

Python
# Answer
a = 10
b = 20
a = a + b  # a becomes 30
b = a - b  # b becomes 10 (30-20)
a = a - b  # a becomes 20 (30-10)
print(f"a: {a}, b: {b}")


2. Even or Odd (No Modulo Operator)
Question: Check if a number is even or odd without using the % operator.

Python
# Answer
num = 7
if (num // 2) * 2 == num:
    print("Even")
else:
    print("Odd")
