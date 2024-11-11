import math

class BasicCalculator:
    def __init__(self, num1):
        self.num1 = num1 
    
    def get_value(self):
        return self.num1

    def add(self, num):
        return self.num1 + num

    def sub(self, num):
        return self.num1 - num

    def mul(self, num):
        return self.num1 * num

    def div(self, num):
        if num != 0:
            return self.num1 / num
        else:
            return "Cannot divide by zero"

    # Operator Overloading for Basic Calculator
    def __add__(self, other):
        return BasicCalculator(self.num1 + other.num1)

    def __mul__(self, other):
        return BasicCalculator(self.num1 * other.num1)

    def __truediv__(self, other):
        if other.num1 != 0:
            return BasicCalculator(self.num1 / other.num1)
        else:
            return "Cannot divide by zero"

class ScientificCalculator(BasicCalculator):
    def __init__(self, num1):
        super().__init__(num1)

    def power(self, exponent):
        return self.num1 ** exponent

    def sqrt(self):
        return self.num1 ** 0.5

    def sine(self, x, y):
        return y / math.sqrt(x**2 + y**2)

    def cosine(self, x, y):
        return x / math.sqrt(x**2 + y**2)

    def tangent(self, x, y):
        return x / y

    # Overriding methods to handle complex numbers
    def add_complex(self, complex1, complex2):
        result = complex1 + complex2
        print("Complex Addition:", result)
        return result

    def sub_complex(self, complex1, complex2):
        result = complex1 - complex2
        print("Complex Subtraction:", result)
        return result

    def mul_complex(self, complex1, complex2):
        result = complex1 * complex2
        print("Complex Multiplication:", result)
        return result

# Function to perform calculations
def perform_calculation(calculator, operation, x, y=None):
    if operation == 'add':
        return calculator.add(y)
    elif operation == 'sub':
        return calculator.sub(y)
    elif operation == 'mul':
        return calculator.mul(y)
    elif operation == 'div':
        return calculator.div(y)
    elif operation == 'power' and isinstance(calculator, ScientificCalculator):
        return calculator.power(y)  
    elif operation == 'sqrt' and isinstance(calculator, ScientificCalculator):
        return calculator.sqrt()  
    elif operation == 'sine' and isinstance(calculator, ScientificCalculator):
        return calculator.sine(x, y)  
    elif operation == 'cosine' and isinstance(calculator, ScientificCalculator):
        return calculator.cosine(x, y) 
    elif operation == 'tangent' and isinstance(calculator, ScientificCalculator):
        return calculator.tangent(x, y)  
    elif operation == 'add_complex' and isinstance(calculator, ScientificCalculator):
        return calculator.add_complex(x, y)  
    elif operation == 'sub_complex' and isinstance(calculator, ScientificCalculator):
        return calculator.sub_complex(x, y) 
    elif operation == 'mul_complex' and isinstance(calculator, ScientificCalculator):
        return calculator.mul_complex(x, y)  
    else:
        return "Invalid operation"
##################################################################################
                #####OutPut#####

print("Question 1 output")
calc = BasicCalculator(10)
print(calc.add(10))  # Output: 20
print(calc.mul(5))   # Output: 50
print(calc.div(2))   # Output: 5
print(calc.get_value())  # Output: 10


print("\nQuestion 2 output")
sci_calc = ScientificCalculator(4)
print(sci_calc.sqrt())  # Output: 2.0
print(sci_calc.power(3))  # Output: 64.0
print(sci_calc.sine(0, 1))  # Output: 1.0
print(sci_calc.cosine(0, 1))  # Output: 0.0
print(sci_calc.tangent(1, 1))  # Output: 1.0

# Complex number operations
print("\nQuestion 3 output")
print("Complex Addition:", sci_calc.add_complex(2+3j, 3+4j))  # Output: (5+7j)
print("Complex Subtraction:", sci_calc.sub_complex(2+3j, 1+4j))  # Output: (1-1j)
print("Complex Multiplication:", sci_calc.mul_complex(2+3j, 1+1j))  # Output: (-1+5j)


print("\nQuestion 4 output")
basic_calc = BasicCalculator(10)
sci_calc = ScientificCalculator(4)
# Perform basic arithmetic using BasicCalculator
print(perform_calculation(basic_calc, "add", 10, 5))  # Output: 15
print(perform_calculation(basic_calc, "mul", 10, 5))  # Output: 50
# Perform scientific calculations using ScientificCalculator
print(perform_calculation(sci_calc, "power", 2, 3))  # Output: 64
print(perform_calculation(sci_calc, "sine", 1, 1))  # Output: 0.7071


print("\nQuestion 5 output")
calc1 = BasicCalculator(10)
calc2 = BasicCalculator(20)
# Basic Calculator Operations
print(calc1.add(5))  # Output: 15
print(calc1.sub(3))  # Output: 7
print(calc1.mul(2))  # Output: 20
print(calc1.div(4))  # Output: 2.5
# Operator Overloading with Calculator instances
calc3 = calc1 + calc2
calc4 = calc1 * calc2
calc5 = calc2 / calc1
print(calc3.get_value())  # Output: 30
print(calc4.get_value())  # Output: 200
print(calc5.get_value())  # Output: 2.0