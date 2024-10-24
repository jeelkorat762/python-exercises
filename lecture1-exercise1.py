#1
name = input("Enter your name: ")

print(f"Welcome, {name}!")

# 2
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

gross_pay = hours * rate

print(f"Gross pay: {gross_pay}")

# 3

width = 17
height = 12.0

a = width // 2
print(a)

b = width / 2.0
print(b)

c = height / 3
print(c)

#4

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.3f}")