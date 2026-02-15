#AssignmentProblems

#Q1. Write a program that asks the user for their name and age,then print sasentence like  "Hello Shradha, you are 21 years old!"

name=input("enter you name:")
age=input("your age:")
print(f"Hello {name}, you are {age} years old!")

# .Q2 Take two numbers as input from the user and print their sum,difference,product,and quotient

number1=int(input("Enter number1:"))
number2=int(input("Enter number2:"))
sum=number1+number2
difference=number1-number2
product=number1*number2
quotient=number1/number2
print(f"Sum:{sum}")
print(f"Difference:{difference}")   
print(f"Product:{product}")
print(f"Quotient:{quotient}")

# Q4. Ask the user to enter two integers and one float. Convert them all to floats and print their average
int1=int(input("Enter first integer:"))
int2=int(input("Enter second integer:"))
int3=float(input("Enter a float:"))
average=(float(int1)+float(int2)+int3)/3
print(f"Average:{average}")

# Q4. The user enters a string containinga number(e.g.,).Convert it to"45"•an integer •a float• a string again 
# Print allthree values with their types.

user_input=input("Enter a number in string format:")

int_value=int(user_input)

float_value=float(user_input)

str_value=str(user_input)

print(f"integer value:{int_value}, type:{type(int_value)}")
print(f"float value:{float_value}, type:{type(float_value)}")
print(f"string value:{str_value}, type:{type(str_value)}")


#Q.5
x =10+3*2**2
print(x)

#Q6 write a program to swap two numbers entered by the user
 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=b,a
print(f"After swapping: a={a}, b={b}")

#  Q7 Ask the user for a temperature in Celsius(string input).Convert it to float ,then calculate and print temperature in Fahrenheit

# Ask the user for temperature in Celsius (string input)
temp = input("Enter temperature in Celsius: ")

# # Convert to float
temp_celsius = float(temp)

# Convert Celsius to Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32

# Print the result
print(f"Temperature in Fahrenheit: {temp_fahrenheit}")


#Q8 take the radius as user input and print the area

radius=float(input("enter radius:"))
PI=3.14
area=PI*radius*radius
print(f"area is:{area}")

#Q.10 Ask the user for Principal (P), Rate (R), Time (T)
# ✅ Convert all inputs to float
# ✅ Compute Simple Interest
# ✅ Print the result

p=float(input("Enter principal:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))

interest=(p*r*t)/100

print(f"result is:{interest}")

#take a decimal number as input (like 45.78) and print:

# integer part → 45

# fractional part → .78

number=input("enter decimal number")

integer_part,fractional_part=number.split(".")

print("Integer part:", integer_part)
print("Fractional part: ." + fractional_part)