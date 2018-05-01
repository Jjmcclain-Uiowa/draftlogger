import os

for file in os.listdir("drafts"):
    file = open('drafts\\draft.txt', 'r')
    for line in file:
        print(line)