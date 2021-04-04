triangle = []
depth = int(input())
for i in range(depth):

    if i == 0:

        new_line = [1]
        triangle.append(new_line)

    elif i == 1:
        new_line = [1, 1]
        triangle.append(new_line)

    else:
        new_line = [c for c in range(i + 1)]
        for k in range(1, i):
            new_line[0] = 1
            new_line[i] = 1

            new_line[k] = triangle[i - 1][k] + triangle[i - 1][k - 1]
        triangle.append(new_line)

countr = 0

for z in triangle:
    countr += 1
    space = '  ' * (depth - countr)
    print(space, end='')
    for b in z:
        print(b, '  ', end='')
    print('')
