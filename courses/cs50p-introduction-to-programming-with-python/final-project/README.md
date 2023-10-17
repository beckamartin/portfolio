# Random Pokemon Battle Teams
#### Video Demo:  <https://youtu.be/TkEr3x2QTcI>
#### Description:
    
As the name suggests, the program output is a team with random pokemon monsters. The input from user is how many monsters we  want and which types should be used. Then the program chooses randomly from a CSV file and finishes with second CSV file output.

The program does not use any non-standard libraries, only sys, csv, re and random. It consists of one main and three more functions. The main runs loops for checking the user's input, reading and writing the csv file.

At first we need to start the program from console with argv. Usually as python project.py pokemon.csv after.csv.

Then we choose the size of a team and then select the types one by one. In reality there is 18 types of pokemons, but in the program we use only five - normal, rock, fire, water and grass.

Then there are the functions. The first one called check_argv checks if the program has three argvs and two of them must end with .CSV. Second function select_type() uses re.search to look for the specific type of user input. Third function random_pokemon() picks the random pokemon from csv file by used type.

In the end there are two types of output. One is printed team in console and the second is the CSV file.