# Q1. Write a program that takes as input.Using conditional statements,calculate the final tax rate based on these rules
# :Q1salaryfinaltaxrate•
# Ifsalary<30,000→5%•
# Ifsalaryis30,000–70,000→15%•
# Ifsalary>70,000→25%

# salary=int(input("Enter salary:"))
# if salary<30000:
#     print("final tax rate is 5%")
# elif salary>30000 or salary<70000:
#     print("final tax rate is 15%")

# elif salary>70000:
#     print("final taxt rate is 25%")

# else:
#     print("please enter correct amount")


# Q2 write a funntion that takes two integers and prints all even numbers between them (inclusive):

# def print_even_number(a,b):
#     for num in range(a,b+1):
#         if(num%2==0):
#             print(num)

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# print_even_number(a,b)

#Q3. write a funtion that prints the digits of a number,n
#for eg:n=321, there are 3 digits in it 3,2,1 and we need to print them.

# def digit_num(n):
#     n=str(n)
#     for i in n:
#         print(i)
# n=int(input("enter number:"))
# digit_num(n)

#Q4. write a function to return the count the number of digits in a number n.

# def count_num(n):
#     count = 0
#     for digit in str(n):   # convert number to string
#         count += 1         # increase count
#     return count

# n = int(input("Enter number: "))
# print(count_num(n))

#Q5 write a function to return sum of digit

def sum_of_digits(n):
    total = 0
    for digit in str(n):      # loop through each digit
        total += int(digit)   # convert digit back to int and add
    return total

n=int(input("enter number:"))
print(sum_of_digits(n))