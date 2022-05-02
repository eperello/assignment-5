# CMPS 2200 Assignment 5
## Answers

**Name:** Ethan Perello


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
Select the coin with the highest power of 2 value that is still less than N and choose as many of those coins as you can that when added up are still less than N. Then subtract the value of those coins from N to create a new N and repeat the process with the new N until you have coins that add up to the original value of N. This algorithm is optimal because it follows the greedy hcoice and optimal substructure properties.






- **1b.**
Work and Span are O(n)



- **2a.**
The greedy algorithm does not produce the fewest number of coins because it does not take into account the values of smaller coins. If you have 15 dollars and coins are in denominations of 11,10,5,1 the greedy algorithm would have one 11 and four 1s, but the fewest number of coins would be one 10 and one 5. This algorithm also does not work because it cannot guarentee that there is exact change.

- **2b.**
Compute how many coins are needed to equal 1 through N dollars. Assign those number of coin values to each dollar value. Then find the minimum number of coins needed to add up to N dollars by adding up those smaller values. The work and span would be O(nN) where small n is the number of different coins and big N is the value of dollars we are trying to achieve.
















