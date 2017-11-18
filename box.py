

#
def drawline(first, middle, last, length):
    line = first
    for i in range(0, length - 2):
        line += middle
    print(line + last)


#
def drawbox(width, height):
    drawline('┌', ' - ', '┐', width)
    for i in range(0, height - 2):
        drawline('|', '   ', '|', width)
    drawline('└', ' - ', '┘', width)

# Testing:
# drawbox(4, 4)

#'┌ ─ ┐\n|   |\n└ ─ ┘\n'
#'┌ - ┐\n│   │\n└ - ┘\n'



