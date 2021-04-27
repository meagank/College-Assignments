######################################################################################################################
# Name: Meagan Kropp
# Date: December 15, 2019
# Description: Use a seed to get a list of numbers, sort them using different sorting methods, and get the number of swaps and comparisons each method took.
######################################################################################################################
from random import randint, seed
# creates the list using the seed provided by the user
def getList():
        seed(theseed)
        mylist = []
        for i in range(1, 10):
            mylist.append(randint(1, 100))
        return mylist

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(list):
        n = list
        swaps = 0
        comparisons = 0
        for i in range(1, len(n)):
                for j in range(1, len(n) - i+ 1):
                        comparisons += 1
                        if (n[j] < n[j - 1]):
                                temp = n[j]
                                n[j] = n[j - 1]
                                n[j - 1] = temp
                                swaps += 1
        print "After bubble sort: {}".format(n)
        return comparisons,swaps

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optBubble(list):
        n = list
        swaps = 0
        comparisons = 0
        for i in range(1, len(n)):
                swapped = False
                for j in range(1, len(n) - i+ 1):
                        comparisons += 1
                        if (n[j] < n[j - 1]):
                                temp = n[j]
                                n[j] = n[j - 1]
                                n[j - 1] = temp
                                swaps += 1
                                swapped = True
                if swapped == False:
                        break
        print "After bubble sort: {}".format(n)
        return comparisons,swaps


# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(list):
        n = list
        comparisons = 0
        swaps = 0
        for i in range(0, len(n) - 1):
                       minPosition = i
                       for j in range(i + 1, len(n)):
                               comparisons += 1
                               if (n[j] < n[minPosition]):
                                       minPosition = j
                       temp = n[i]
                       n[i] = n[minPosition]
                       n[minPosition] = temp
                       swaps += 1
        print "After selection sort: {}".format(n)
        return comparisons, swaps
        
# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(list):
        n = list
        i = 1
        comparisons = 0
        swaps = 0
        while (i < len(n)):
                comparisons += 1
                if (n[i - 1] > n[i]):
                        temp = n[i]
                        j = i - 1
                        comparisons += 1
                        while (j >= 0 and n[j] > temp):
                                n[j + 1] = n[j]
                                j -= 1
                                swaps += 1
                                comparisons += 1
                        n[j + 1] = temp
                i += 1
        print "After insertion sort: {}".format(n)
        return comparisons, swaps


# the main part of the program
theseed = input("What do you want to use as the seed? ")
list = getList()
theList = getList()
origList = getList()
orgList = getList()

#insert your main code below.

print "The list: {}" .format(list)
comps, swaps = bubbleSort(list)
print "{} comparisons; {} swaps" .format(comps, swaps)
print
print "The list: {}" .format(theList)
comps, swaps = optBubble(orgList)
print "{} comparisons; {} swaps" .format(comps, swaps)
print
print "The list: {}" .format(theList)
comps, swaps = selectionSort(list)
print "{} comparisons; {} swaps" .format(comps, swaps)
print
print "The list: {}" .format(theList)
comps, swaps = insertionSort(origList)
print "{} comparisons; {} swaps" .format(comps, swaps)


