def hello():
  name = str("hello world")
  print  (str(name))

  return  
  
hello()
# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           # Python3 Program to
# find sum of square
# of first n natural
# numbers


# Return the sum of
# square of first n
# natural numbers

def squaresum(n):

    # Iterate i from 1
    # and n finding
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)

    return sm


# Driven Program
n = 4
print(squaresum(n))

# This code is contributed by Nikita Tiwari.*/
