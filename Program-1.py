class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b   # normal division

cal = Calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", cal.add(a, b))
print("Subtraction:", cal.sub(a, b))
print("Multiplication:", cal.mul(a, b))
print("Division:", cal.div(a, b))
