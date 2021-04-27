###########################################################################################
# Name: Meagan Kropp
# Date: December 6, 2019
# Description: Create a program that counts the number of zeros between 1 and a user defined end point.
###########################################################################################

from time import time

#function that finds number of zeros in a number
def findZeros(n):
    zeros = 0
    while (n > 0):
        if (n % 10 == 0):
            zeros += 1
        n /= 10
    return zeros


#MAIN PROGRAM

n = 0
maximum = input("What number do you want to count zeros to? ")
count = 0

#get start time
begTime = time()

while (n < maximum):
    n += 1
    count = count + findZeros(n)

#get end time
endTime = time()
print "The number of zeros written from 1 to {} is {}." .format(maximum, count)
print "This took {} seconds." .format(endTime - begTime)

    

