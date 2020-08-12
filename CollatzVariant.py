# This piece of code executes the Collatz conjecture algorithm on numbers.
# Copyright (C) 2020  Zander Kraig

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import graph

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
    stoptimes_array = []
    num = 1
    limit = input("Enter the number upto which for all numbers, the Collatz algorithm is to be applied.")
    while num < int(limit) + 1:
        number = num
        loop = 2
        terms = 0
        while loop != 1:
            if (number % 2 == 0):
                number = int(number/2)
            elif (number % 2 != 0):
                number = int((number * 3) + 1)
            loop = number
            terms += 1
                
        else:
            print("Number: " + str(num) + ", Stopping time: " + str(terms))
            stoptimes_array.append(terms)
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
        choice = input("Do you want to see a graph that displays this information? (y/n) ")
        if choice == 'y':
            graph.displaystoptimesGraph(stoptimes_array)
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

input("Press any key to close")
