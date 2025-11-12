def add(a, b):
    """Додавання двох чисел"""
    return a + b

def subtract(a, b):
    """Віднімання двох чисел"""
    return a - b

def multiply(a, b):
    """Множення двох чисел"""
    return a * b

def divide(a, b):
    """Ділення двох чисел"""
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

def power(a, b):
    """Піднесення числа a до степеня b"""
    return a ** b

def modulo(a, b):
    """Остача від ділення"""
    if b != 0:
        return a % b
    else:
        return "Помилка: ділення на нуль!"

print("=== Простий калькулятор ===")
print("Операції: +, -, *, /, **, %")
print("Для виходу введіть 'exit'")

while True:
    operation = input("\nВведіть операцію (+, -, *, /, **, %) або 'exit': ")

    if operation.lower() == 'exit':
        print("Good bye!")
        break

    if operation not in ['+', '-', '*', '/', '**', '%']:
        print("Невірна операція!")
        continue

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '**':
            result = power(num1, num2)
        elif operation == '%':
            result = modulo(num1, num2)

        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введіть коректні числа!")
