
#question number 1

# def is_palindrome(s):
#     if(s[::-1]==s):
#         print("true")
#     else:
#         print("false")
# s = input("enter string->")
# is_palindrome(s)        


#question number 2

# def calculator(num1, num2, operation):
#     if operation == 'add':
#         return num1 + num2
#     elif operation == 'subtract':
#         return num1 - num2
#     elif operation == 'multiply':
#         return num1 * num2
#     elif operation == 'divide':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operation"  

# num1 = int(input("enter first number->"))
# num2 = int(input("enter second number->"))   
# operation = input("enter operation->")
# print(calculator(num1,num2,operation))



#queston 3

# def wordcounter(s):
#     count = {}
#     for char in s:
#         if char in count:
#             count[char]+=1
#         else:
#             count[char]=1
#     return count
# s = input("enter string->")
# wordcounter(s)
# str=wordcounter(s)
# print(str)



#question 4

# def print_pattern(n):
#     for i in range(0,n+1):
#        print('*' * i)   
# n=int(input("enter number->"))
# print_pattern(n)            



#question 5

# def multiplication(n):
#     for i in range(1,11):
#         print(n*i)
# n=int(input("enter number->"))
# multiplication(n)         
        