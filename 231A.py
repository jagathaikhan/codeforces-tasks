counter = 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        counter += 1
print(counter)