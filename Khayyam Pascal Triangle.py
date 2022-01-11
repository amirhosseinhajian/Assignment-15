n = int(input("Please enter n: "))
if n > 0:
    triangle = [[1]]
    for i in range(1, n):
        buffer = []
        buffer.append(1)
        for j in range(2, len(triangle)+1):
            buffer.append(triangle[i - 1][j - 2] + triangle[i - 1][j - 1])
        buffer.append(1)
        triangle.append(buffer)

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=" ")
        print()