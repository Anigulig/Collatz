'''This piece of code executes the Collatz conjecture algorithm on numbers.'''

#import pyximport; pyximport.install()
import time
def collatz(limit):
    num = 1
    while num < int(limit) + 1:
        print(num)
        number = num
        loop = 2
        terms = 0
        while loop != 1:
            if (number % 2 == 0):
                number = int(number/2)
                print(number)
            elif (number % 2 != 0):
                number = int((number * 3) + 1)
                print(number)
            elif (number == 1):
                print("1")
            loop = number
            terms += 1
            
        else:
            print("THE END!")
            print("The total stopping time is " + str(terms))
            if (num == 1):
                stopTime = terms
            else:
                if (terms > stopTime):
                    stopTime = terms
                    longestTerm = num
                else:
                    stopTime = stopTime
        num += 1
    else:
          print("End of your request!")   
          print("The maximum total stopping time is " + str(stopTime) + " for the number " + str(longestTerm))

def stopTimes():
    num = 1
    limit = input("Enter the number upto which for all numbers, the Collatz algorithm is to be applied.")
    while num < int(limit) + 1:
        #print(num)
        number = num
        loop = 2
        terms = 0
        while loop != 1:
            if (number % 2 == 0):
                number = int(number/2)
                '''print(number)'''
            elif (number % 2 != 0):
                number = int((number * 3) + 1)
                '''print(number)'''
            elif (number == 1):
                '''print("1")'''
            loop = number
            terms += 1
                
        else:
            #print("THE END!")
            #print("Number: " + str(num) + ", Stopping time: " + str(terms))
            #print(terms)
            if (num == 1):
                stopTime = terms
            else:
                if (terms > stopTime):
                    stopTime = terms
                    longestTerm = num
                else:
                    stopTime = stopTime
        num += 1
    else:
        print("End of your request!")   
        print("The maximum total stopping time is " + str(stopTime) + " for the number " + str(longestTerm))  
        check = input("Enter 1 to perform the Collatz algorithm on this number.")
        if (check == "1"):
            singleCollatz(longestTerm)
        else:  
            return 0

def singleCollatz(num):
    loop = 2
    terms = 0
    while loop != 1:
        if (num % 2 == 0):
            num = int(num/2)
            print(num)
        elif (num % 2 != 0):
            num = int((num * 3) + 1)
            print(num)
        elif (num == 1):
            print("1")
        loop = num
        terms += 1
    else:
        print("THE END!")
        print("The total stopping time is " + str(terms))


print("Enter 1 to perform Collatz algorithm for all natural numbers upto this number.")
print("Enter 2 to only calculate stopping times for the Collatz conjecture")
choice = input("Enter 3 to perform the Collatz algorithm on only one number: ")

if (choice == "1"):
    limit = input("Enter the number upto which you want to perform the algorithm: ")
    collatz(limit)
elif (choice == "2"):
    stopTimes()
elif (choice == "3"):
    num = input("Enter the required number: ")
    singleCollatz(int(num))
else:
    print("ERROR!")
