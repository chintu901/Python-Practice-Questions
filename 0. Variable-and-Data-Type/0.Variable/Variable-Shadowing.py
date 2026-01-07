# Question: A variable score = 50 exists globally. A function updates score locally to 100. Print both values.

score = 50

def update():
    score = 100
    print(score)

print(score)