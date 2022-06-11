import json

topics = []
numbers = []
total = 0

file = open("trivia.json")
questions = json.load(file)
file.close()

for q in questions:
    
    if q["category"] not in topics:
        topics.append(q["category"])
        numbers.append(0)
    
    numbers[topics.index(q["category"])] += 1
    
    total += 1

for i in range (0,len(numbers)):
    print(f"{topics[i]}: {numbers[i]}")
    
print("Total number of questions:",total)
