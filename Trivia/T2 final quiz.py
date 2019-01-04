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

def next_block(trivia):
    category = next_line(trivia)
    question = next_line(trivia)
    answers = []
    for i in range(4):
        ans = next_line(trivia)
        answers.append(ans)
    correct = next_line(trivia)
    if correct:
        correct = correct[0]
    explanation = next_line(trivia)
    return category, question, answers, correct, explanation

def welcome(title):
    print("\t\tWelcome to Trivia Challenge!")
    print('\t\t',title,'\t\t')

def main():
    trivia = open_file("test_questions.txt", "r")
    title = next_line(trivia)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(trivia)
    while category:
        print(category)
        x =0
        for i in range(4):
            x+=1
            print(x, answers[i])
        answer = input("Your Answer:")
        if correct == answer:
                print("Correct!")
                score += 10
        else:
                print("Incorrect!")
        print(explanation)
        print(score)
        next_block(trivia)
    print(score)
    trivia.close()
    input("Press enter to exit the program.")
    sys.exit()

main()
