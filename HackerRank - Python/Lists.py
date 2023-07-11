queryList = []
N = int(input())
for i in range(N):
    queryList.append(input())

resultList =[]
for command in queryList:
    if command.__contains__('insert'):
        operation, value1, value2 = command.split(' ')
        resultList.insert(int (value1), int (value2))
    elif command.__contains__('print'):
        print(resultList)
    elif command.__contains__('remove'):
        operation, value1 = command.split(' ')
        resultList.remove(int (value1))
    elif command.__contains__('append'):
        operation, value1 = command.split(' ')
        resultList.append(int (value1))
    elif command.__contains__('sort'):
        resultList.sort()
    elif command.__contains__('pop'):
        resultList.pop()
    elif command.__contains__('reverse'):
        resultList.reverse()
    else:
        print('Bad operation.')