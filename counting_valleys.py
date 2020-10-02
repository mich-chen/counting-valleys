def countingValleys(steps, path):

    valleys = 0
    # valley_down = False
    # valley_up = False
    sealevel = 0

    for i in range(steps):
        if path[i] == 'D':
            # if sealevel == 0:
            #     valley_down = True
            sealevel -= 1

        if path[i] == 'U':
            sealevel += 1
            # if sealevel == 0:
            #     valley_up = True

        # if reached sealevel from an UP then exiting a valley
        if sealevel == 0 and path[i] == 'U':
            valleys += 1

        # alternative brute force solution:
        # if valley_down == True and valley_up == True:
        #     valleys += 1
        #     valley_down = valley_up = False

    return valleys


if __name__ == '__main__':

    print(countingValleys(8, "UDDDUDUU"))
    print(countingValleys(12, "DDUUDDUDUUUD"))
    