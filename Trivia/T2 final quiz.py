#Term 2 final
#Sabastian Taton
# Jan. 2 2019
#Questions read from  plain text file
import sys

def open_file(file_name,mode):
    """ Opens the file"""
    try:
        trivia = open(file_name,mode)
    except IOError as e:
        print("Unable to open file",file_name,"Ending program.",e)
        input("Press enter to exit the program.")
        sys.exit()
    else:
        return trivia

def next_line(trivia):
    """Return line from file, formatted correctly"""
    line = trivia.readline()
    line = line.replace("/","\n")
    return line

file_name = "test_questions.txt"
trivia = open_file(file_name,"r")
line = next_line(trivia)
print(line)
