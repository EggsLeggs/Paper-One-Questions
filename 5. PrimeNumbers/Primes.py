class PrimeCheck():
    def main(self):
        number = self.numberInput()
        if number <= 1:
            print("Not greater than 1")
        else:
            prime = True
            for i in range(2,number):
                if i != number:
                    if number%i == 0:
                        prime = False
            if prime:
                print("Is prime")
            else:
                print("Is not prime")
        if self.repeatInput():
            self.main()
    
    def numberInput(self):
        NumberToFind = input("\nEnter a number to check: ")
        try:
          NumberToFind = int(NumberToFind)
        except ValueError:
          print("\nOnly whole numbers are allowed\n")
          return self.numberInput()
        return NumberToFind

    def repeatInput(self):
        repeatInp = str(input("\nWould you like to enter another number [Y/N]: ")).upper()
        if repeatInp == "Y":
            return True
        elif repeatInp == "N":
            return False
        else:
          print("\nOnly Y and N are allowed")
          return self.repeatInput()
        return repeat

PrimeCheck().main()
