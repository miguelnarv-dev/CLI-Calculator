import math
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    operators = input("Enter an operator: ")
    if operators == "+":
        print(Calculator(a,b).add())
    elif operators == "-":
        print(Calculator(a,b).subtract())
    elif operators == "*":
        print(Calculator(a,b).multiply())
    elif operators == "/":
        if b == 0:
            print("Error: Division by zero")
            return
        else:
            print(Calculator(a,b).divide())
    else:
        print("Invalid operator")
if __name__ == "__main__":
    main()