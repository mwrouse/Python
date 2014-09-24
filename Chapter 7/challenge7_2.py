"""
    Program: challenge7_2.py
    Author: Michael Rouse
    Date: 10/30/13
    Description: Imporve the trivia challenge program so that it maintains a high scores list
                 in a file. The program should record the player's name and score if the player
                 makes the list. Store the high scores using a plain text file.
"""
import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    point_value = next_line(the_file)

    return category, question, answers, correct, point_value

def get_explanation(file):
    """ Gets explanation for answer """
    explanation = next_line(file)

    return explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def loadHighScores():
    """ Load high scores from .dat file """
    file = "high_scores.dat"
    
    try:
        highScoreFile = open(file, "rb")

    except:
        highScoreFile = open(file, "wb")
        # Create 10 blank highscores
        blankScores = ["Blank", "0", "1", "Blank", "0", "2", "Blank", "0", "3", "Blank", "0", "4", "Blank", "0", "5", "Blank", "0", "6", "Blank", "0", "7", "Blank", "0", "8",
                       "Blank", "0", "9", "Blank", "0", "10"]

        # Dump blank high scroes into .dat file
        pickle.dump(blankScores, highScoreFile)
        
        highScoreFile.close()
        highScoreFile = open(file, "rb")
    
    # Load scores from .dat file
    scores = pickle.load(highScoreFile)

    return scores

def saveHighScores(scores):
    """ Writes highscores to .dat file """
    file = "high_scores.dat"

    highScoreFile = open(file, "wb")

    # Dump scores into .dat file
    pickle.dump(scores, highScoreFile)

    highScoreFile.close()

    return True

def getUserInfo(score, rank, highScores, positions):
    """ Gets user info for highscore """
    print("Congratulations you have a highscore!")

    # Get name of user
    username = input("What is your name? ")
    
    # Get user's score
    score = str(score)

    # Trim scores for new score list
    beforeUser = highScores[0: positions[rank][0]]
    afterUser = highScores[positions[rank][0]:30]

    # Create new highscores list    
    highScores = beforeUser + [username, score, str(rank)] + afterUser

    # Trim highscores list down to 10 ranks
    del(highScores[30:len(highScores) + 1])

    # increase the rank amount of users below the user
    rankCount = 1
    if rank < 10:
        for i in range(rank, 10):
            oldRank = highScores[positions[rank + rankCount][2]]
            newRank = int(oldRank) + 1
            highScores[positions[rank + rankCount][2]] = str(newRank)
            rankCount += 1

    # Write high scores to .dat file
    saveHighScores(highScores)

    # Display high scores
    display_scores(highScores, positions)
    
def display_scores(highScores, positions):
    """ Displays a list of high scores """
    print("Here is the new list of highscores:")
    print("Rank       Name                     Score\n")      
    for i in range(1, 11):
        namePos = positions[i][0]
        scorePos = positions[i][1]
        rankPos = positions[i][2]

        name = str(highScores[namePos])
        score = str(highScores[scorePos])
        rank = str(highScores[rankPos])

        display = rank + "          " + name + "\t\t" + score
        
        print(display)
    
def main():
    """ Main program """
    positions = {1: [0, 1, 2], 2: [3, 4, 5], 3: [6, 7, 8], 4: [9, 10, 11], 5: [12, 13, 14], 6: [15, 16, 17], 7: [18, 19, 20], 8: [21, 22, 23], 9: [25, 25, 26], 10: [27, 28, 29]}
    
    highScores = loadHighScores()
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)   
    score = 0

    # get first block
    category, question, answers, correct, point_value = next_block(trivia_file)
    explanation = get_explanation(trivia_file)
    
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(point_value)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        
        # get next block
        category, question, answers, correct, point_value = next_block(trivia_file)
        explanation = get_explanation(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    rank = 11
    
    # Detect if user has a high score
    for i in range(1, 10):

        position = positions[i][1]

        highscore = int(highScores[position])
        
        if score >= highscore:
            if i < rank:
                rank = i

    if rank <= 10:
        getUserInfo(score, rank, highScores, positions)
      
 
main()  
input("\n\nPress the enter key to exit.")
