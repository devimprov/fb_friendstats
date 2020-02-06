import operator
import json

#Read Friends
with open("friends.json","r") as file:
    friends = json.loads(file.read())

friendlist = []

for friend in friends["friends"]:
    friendlist.append(friend['name'])

firstnames = []

for friend in friendlist:
    first = friend.split(" ")[0]
    firstnames.append(first)

namecount = {}

for name in firstnames:
    try:
        namecount[name]
    except:
        namecount[name] = 0

    namecount[name] = namecount[name] + 1

sorted_namedata = sorted(namecount.items(), key = operator.itemgetter(1), reverse=True)

for name in sorted_namedata:
    name, number = name
    print(f"{name} - {number}")
