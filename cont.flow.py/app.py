#num: int = 10

#if num < 0:
   #print("The number is positive.")
#else:
    #print("now this code will execute.")

#num: int = 1

#if num > 0: # Program execution step# 1 if condition = False
   # print("The number is positive.")
#elif num < 0: # Program execution step# 2 if condition = False
    #print("The number is negative.")
#else: # Program execution step# 3 python will execute the else block
    #print("The number is zero.")

#def check_status(code):
       # match code:
            #case 200:
            # print("OK")
            #case 400:
            # print("Bad Request")
             #case 404:
             #print("Not Found")
            #case _:
             #print("Unknown Status")

#check_status(200)  # Output: OK
#check_status(404)  # Output: Not Found
#check_status(500)  # Output: Unknown Status

 #x ="-"
 #print(x*12)

 #x: range = range(12)
 #for num in x:
       # print(num)

       # Iterate over a list
#fruits: list = ["apple", "banana", "cherry"]
#for fruit in fruits:
    #print(fruit)

# Note: Membership Operators in Python in, not in# Iterate over a list
 #fruits: list = ["apple", "banana", "cherry"]
 #for fruit in fruits:
    #print(fruit)

# Note: Membership Operators in Python in, not in

# Iterate over a string
#word: str = "Python"
#for letter in word:
    #print(letter)

    #numbers = [1, 2, 3, 4, 5]

#for num in numbers:
   # print(num)
#else:
   # print("Loop completed successfully!")

#numbers = [1, 2, 3, 4, 5]

#for num in numbers:
    #print(num)
    #if num == 3:
       # print("Breaking the loop!")
        #break
#else:
    #print("Loop completed successfully!")  # This will NOT run

#numbers = [1, 2, 3, 4, 5]

#for num in numbers:
    #if num == 4:
       # continue
    #print(num)
#else:
    #print("Loop completed successfully!")  # This will not run

    # Print numbers from 1 to 5
#count: int = 1
#while count <= 10:
   # print(count)
    #count += 1
