# take the input
n = int(input("Enter the number : "))
# define the function
def factorial(n):
    if n<0 :
        return "factorial can't define for negative number"

    elif n==0 or n==1 :
        return 1

    else:
        return (n * factorial(n-1))
# print the answer
print(f"The Factorial of {n} is : {factorial(n)}")