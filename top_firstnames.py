#! /usr/bin/env python3

import operator
import json
import sys 

if len(sys.argv) > 1:
    friendsfile = sys.argv[1]
else:
    friendsfile = "friends.json"


#Read friends.json file as json
with open(friendsfile,"r") as file:
    friends = json.loads(file.read())

#Extract list of friends names from file
friendlist = []

for friend in friends["friends"]:
    friendlist.append(friend['name'])

#Extract first names from friends list
firstnames = []

for friend in friendlist:
    first = friend.split(" ")[0]
    firstnames.append(first)

#Get how many of each name there are, store value in dict
namecount = {}

for name in firstnames:
    try:
        namecount[name]
    except:
        namecount[name] = 0

    namecount[name] = namecount[name] + 1

#Sort the data so the largest amount of names is on top. This outputs as list of tuples with name and number

sorted_namedata = sorted(namecount.items(), key = operator.itemgetter(1), reverse=True)

#Loop through the list of tuples and print tha name and how many instances of the name there were
for name in sorted_namedata:
    name, number = name
    print(f"{name} - {number}")

