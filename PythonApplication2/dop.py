import random
import collections 
TeamNum = input('how many teams will be playing?')
TeamNum = int(TeamNum)
while TeamNum > 0:
    

    print(TeamNum)
    TeamName = input('Enter the team name: ')
    TeamNum = TeamNum - 1
    DraftNumbers = list(range(1,TeamNum))
    random.shuffle(DraftNumbers)
    print(TeamName,'',DraftNumbers[0])
    DraftNumbers.remove(DraftNumbers[0])
    Trash =[]
    Trash.insert(DraftNumbers[0],DraftNumbers[0])
    print(Trash)
    
 

