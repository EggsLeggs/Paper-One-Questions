class GameClass():
    def __init__(self):
        self.GuessArray = []
        self.NumberOfGuesses = len(self.GuessArray)
    
    def mainLoop(self):
        NumberToGuess = input("P1 - Choose a whole number between 1 and 10: ")
        try:
            NumberToGuess = int(NumberToGuess)
        except ValueError:
            print("\nOnly whole numbers are allowed\n")
            self.mainLoop()
            return
        if (NumberToGuess <= 0) or (NumberToGuess > 10):
            print("\nSorry, only numbers between 1 and 10\n")
            self.mainLoop()
            return
        while (self.NumberOfGuesses < 5) and (NumberToGuess not in self.GuessArray):
            Guess = self.getPlayer2Answer()
            self.GuessArray.append(Guess)
            self.NumberOfGuesses = len(self.GuessArray)
        if NumberToGuess in self.GuessArray:
            print("Player Two wins")
        else:
            print("Player One wins")

    def getPlayer2Answer(self):
        Guess = input("P2 - Guess a whole number between 1 and 10: ")
        try:
            Guess = int(Guess)
        except ValueError:
            print("\nOnly whole numbers are allowed\n")
            Guess = self.getPlayer2Answer()
        if (Guess <= 0) or (Guess > 10):
            print("\nSorry, only numbers between 1 and 10\n")
            Guess = self.getPlayer2Answer()
        else:
          return Guess 


GameClass().mainLoop()
