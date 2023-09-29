# Question 1
# """Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.""""

def hello_name(user_name):
    print("hello " + user_name + "!")

hello_name("Robert")


# Question 2
# """Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing"""
    
def first_odds():

       oddnum = range(1,100)
       for o in oddnum:
              if o%2!=0:
                print (o)


# Question 3
# """write a Python function, max_num_in_list to return the max number of a given list"""

def max_num_in_list(a_list):

    a_list = max(5,10, 15,20, 25, 30)
    print(a_list)


# Question 4
# """Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# # unless it is also divisible by 400. The return should be boolean Type (true/false)."""

def is_leap_year(a_year):

    if (a_year % 4) == 0: 
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
a_year = int(input("Enter year to check: "))   
if (is_leap_year(a_year)):
       print("Leap Year")
else:
       print("Not Leap Year") 


# Question 5
# """
# Write a function to check to see if all numbers in list are consecutive numbers. For example,
# [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# """

def is_consecutive(a_list):
    a_list = sorted(a_list)
    if a_list:
       print(a_list)
       print(list(range(a_list[0], a_list[-1]  + 1)))
       return a_list == list(range(a_list[0], a_list[-1] + 1))
    else:
       return True  
print(is_consecutive([0, 1, 2, 3, 4]))

    
    
  

            
            
   
    
   







    







    
    
    


