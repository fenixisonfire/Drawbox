import box


#Error handling to ensure input is of int type
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print ("Please enter a valid integer number.")


#
def main():
    w = get_int('Rectangle width: ')
    h = get_int('Rectangle height: ')
    box.drawbox(w, h)


main()
