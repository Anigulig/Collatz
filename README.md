# Collatz
A python program to run the Collatz algorithm.
The Collatz conjecture is a conjecture in mathematics considered to be an extremely difficult problem to solve. It is named after Lothar Collatz, the person who introduced this idea.

The Collatz Conjecture is very simply stated and easy to understand. Take any arbitrary positive integer.
If the number is even, divide it by 2 and if the number is odd, multiply the number by 3 and add 1. Perform the same operation on the number obtained and on the numbers obtained successively. The Collatz conjecture states that all such sequences will end in the number 1. For example:

**3, 10, 5, 16, 8, 4, 2, 1** (Stepwise explanation below)

3   --> arbitrary positive integer

10  = 3 x 3 + 1

5   = 10 / 2

16  = 5 x 3 + 1

8   = 16 / 2

4   = 8 / 2

2   = 4 / 2

1   = 2 / 1

More information can be viewed at the wikipedia page https://en.wikipedia.org/wiki/Collatz_conjecture

# Program specific information:

Please note that the program is not capable of error handling currently. Therefore, it would be necessary to rerun the program if the user hits an error while running the program. Errors should be minimal (only arising when the user provides input at the beginning of the program). I am currently working on this issue and will have it solved optimistically within a few days (by 15 August 2020). 

**Thank you** to whoever uses the program. Please do tell your friends about the existence of a conjecture such as this. You may
not mention to them about this program but it would be helpful if you do. This way, more people will come to know about the existence of the Collatz conjecture and will also have at hand a quick way to try it out. This is the aim of this project of mine, that is, to **make more people aware**.
