# if __name__ == '__main__':
n = int(input())
arr = set(map(int, input().split()))

print(arr)
l = list(arr)
l.sort(reverse=True)
print(l[1])