# CS50 P-Shirt


from sys import argv
from sys import exit
from os.path import exists
from os.path import splitext
from PIL import Image
from PIL import ImageOps


def main():
    check_file(argv)

    modify_image(argv)


def modify_image(argv):
    photo = Image.open(argv[1])

    shirt = Image.open("shirt.png")

    shirt_size = shirt.size

    photo = ImageOps.fit(photo, shirt_size)

    photo.paste(shirt, shirt)

    photo.save(argv[2])


def check_file(argv):
    extensions = (".jpg", ".png", ".jpeg")

    name1, extension1 = splitext(argv[1])
    name2, extension2 = splitext(argv[2])

    if len(argv) <= 2:
        exit("Too few command-line arguments")
    
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    
    elif len(argv) == 3:
        if argv[1].endswith(extensions) == False or argv[2].endswith(extensions) == False:
            exit("Invalid output")
             
        elif extension1 != extension2:
            exit("Input and output have different extensions")

        elif exists(argv[1]) == False:
            exit("Input does not exist")


if __name__ == "__main__":
    main()