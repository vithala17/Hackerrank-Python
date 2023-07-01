classScores = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        classScores.append([name,score])

classScores.sort()
sortedScores = set()

for i in classScores:
        sortedScores.add(i[1])

scoresList = list(sortedScores)
scoresList.sort()
# print(scoresList)

for i in classScores:
        if i[1] == scoresList[1]:
                print(i[0])
