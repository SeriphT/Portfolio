#read it program
#working with reading from a file
#Sabastian Taton
#12/18

def main():
    print("Opening file...")
    
    text_file = open("asdfg.txt", "r")
    text_file.close()

    print("Reading characters from the file")
    text_file = open("asdfg.txt", "r")
    print(text_file.read(1))
    print(text_file.read(5))
    text_file.close()

    text_file = open("asdfg.txt", "r")
    print(text_file.read(5))
    text_file.close()

    text_file = open("asdfg.txt", "r")
    whole_file = text_file.read()
    print(whole_file)
    text_file.close()

    print("Reading from a line")
    text_file = open("asdfg.txt", "r")
    print(text_file.readline(1))
    print(text_file.readline(5))
    text_file.close()

    print("Reading one line at a time")
    text_file = open("asdfg.txt", "r")
    print(text_file.readline())
    print(text_file.readline())
    print(text_file.readline())
    text_file.close()

    print("Reading to a list")
    text_file = open("asdfg.txt", "r")
    lines = text_file.readlines()
    print(lines)
    print(len(lines))
    for i in lines:
        print(i)
    text_file.close()

    print("Looping through a file")
    text_file = open("asdfg.txt", "r")
    count = 0
    for line in text_file:
        count+=1
        print(line)
    text_file.close()
    print(count)
    
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
##    text_file = open("asdfg.txt", "r")
    
main()


