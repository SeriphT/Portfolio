#write it
#writes to a text file
#Sabastian Taton 12/18

def main():
    text_file = open("write_it.txt", "w")
    text_file.write("Line 1")
    text_file.write("Line 2")
    text_file.write("Line 3")
    text_file.close()

    print("Writing to a file with writelines()")
    text_file = open("write_it.txt", "w")
    lines = ["score1\n","score2\n","score3\n","score4\n","score5\n" ]
    text_file.writelines(lines)
    text_file.close()

    
main()
