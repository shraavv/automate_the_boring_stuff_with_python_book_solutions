def printTable(x):
    colWidths = [0] * len(x)

    for i in range(len(x)):
        for j in range(len(x[i])):
            length=len(x[i][j])
            colWidths[j-1] = max(colWidths[j-1],length)

    for i in range(len(x[0])):
        for j in range(len(x)):
            print(x[j][i].rjust(colWidths[j]+1), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
