def drawline(first, middle, last, length):
    # add first character for the line
    line = first
    # add the middle characters
    for i in range(0, length - 2):
        line += middle
    # print out the whole line
    print(line + last)


# the main box drawing function
def drawbox(width, height):
    # draw 1st line
    drawline('┌', ' - ', '┐', width)
    # draw middle lines
    for i in range(0, height - 2):
        drawline('|', '   ', '|', width)
    # draw last line
    drawline('└', ' - ', '┘', width)

# uncomment to run manually
# drawbox(3, 4)



