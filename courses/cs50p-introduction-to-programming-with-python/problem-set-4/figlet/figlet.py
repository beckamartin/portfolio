# Frank, Ian and Glen’s Letters

def main():
    import sys
    from pyfiglet import Figlet
    from random import choice

    figlet = Figlet()

    if len(sys.argv) == 1:
        font = choice(figlet.getFonts())

        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit(1)
    else:
        sys.exit(1)

    text = input("Input: ")

    print("Output: \n", figlet.renderText(text))

if __name__ == "__main__":
    main()