def gridPrint(grid):
    offset = 4
    for y in range(10):
        line = []
        for x in range(10):
            if (x-offset, y-offset) in grid.keys():
                if grid[(x-offset, y-offset)] == True:
                    line.append("#")
                else:
                    line.append(".")
            else:
                line.append(".")
        print(" ".join(line))
