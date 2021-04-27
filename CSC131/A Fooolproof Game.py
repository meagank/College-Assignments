###########################################################################################
# Name: Meagan Kropp
# Date: February 4, 2020
# Description: Randomizes two numbers to determine a winner in a coin toss and  add that win to the total for that game.
###########################################################################################
from random import randint

def randomNum():
    value = randint(0,1)
    return value

def percent(group, total):
    percent = round((float(group) / total) * 100)
    return percent

games = input("How many games? ")
tosses = input("How many coin tosses per game? ")

aWins = 0
bWins = 0
profWins = 0

for g in range(games):
    # group varaibles
    groupA = 0
    groupB = 0
    prof = 0
    
    for t in range(tosses):
        n1 = randomNum()        # generates either a 1(heads) or 0(tails)
        n2 = randomNum()

        if ((n1 == 1) and (n2 == 1)):     # if both are heads(1) add 1 win to group a
            groupA += 1

        elif ((n1 == 0) and (n2 == 0)):  # if both are tails(0) add 1 win to group b
            groupB += 1
        else:                       # if one is heads(1) and one is tails(0) add 1 win to prof
            prof +=1
    
    print "Game {}:".format(g)
    print " Group A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%)".format(groupA, percent(groupA, tosses), \
                                                                         groupB, percent(groupB, tosses), \
                                                                         prof, percent(prof, tosses))
  

    number = randomNum() # generates a random number incase two groups win the same number of tosses

    if ((groupA > groupB) and (groupA > prof)):       # adds a win to group A if it won the most tosses in a game
        aWins += 1
        
    elif ((groupB > groupA) and (groupB > prof)):     # adds a win to group B if it won the most tosses in a game
        bWins += 1
        
    elif ((prof > groupA) and (prof > groupB)):       # adds a win to prof if it won the most tosses in a game
        profWins += 1
        
    elif((groupA == groupB) and (groupA > prof)):     # adds a win to either group A or group B if they both had the same number of tosses( and the most tosses)
        if (number == 1):
            aWins += 1
        else:
            bWins += 1
            
    elif((groupA == prof) and (groupA > groupB)):     # adds a win to either group A or prof if they both had the same number of tosses( and the most tosses)
        if (number == 1):
            aWins += 1
        else:
            profWins += 1
            
    elif((groupB == prof) and (groupB > groupA)):     # adds a win to either group B or prof if they both had the same number of tosses( and the most tosses)
        if (number == 1):
            bWins += 1
        else:
            prof += 1
            
    elif((groupA == groupB) and (groupA == prof)):    # if there is a three way tie, randomize a number that determines a winner for the game
        number = randint(0,2)
        if (number == 1):
            aWins += 1
        elif (number == 0):
            bWins += 1
        else:
            prof += 1
            
        
        
                                                                             
print "Wins: Group A={} ({}%); Group B={} ({}%); Prof={} ({}%)".format(aWins, percent(aWins, games), \
                                                                       bWins, percent(bWins, games), \
                                                                       profWins, percent(profWins, games))
