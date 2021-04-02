class persistance():
    def __init__(self):
        self.count = 0

    def main(self):
        number = self.numberInput()
        choice = self.decisionInput()
        if choice == "A":
            self.additivePersistance(number)
        if choice == "M":
            self.multiplicativePersistance(number)
        print ("Persistance: {}".format(self.count))
        
    def decisionInput(self):
        repeatInp = str(input("Additive or multiplicative persistance [A/M]: ")).upper()
        if (repeatInp == "A") or (repeatInp == "M"):
            return repeatInp
        else:
          print("\nOnly A and M are allowed")
          return self.repeatInput()
        return repeat

    def numberInput(self):
        NumberToFind = input("Input: ")
        try:
          NumberToFind = int(NumberToFind)
        except ValueError:
          print("\nOnly whole numbers are allowed\n")
          return self.numberInput()
        if NumberToFind <= 0:
          print("\nSorry, only numbers greater than 0\n")
          return self.numberInput()
        return NumberToFind

    def additivePersistance(self,number):
        digits = [int(x) for x in str(number)]
        if len(digits)!=1:
            self.additivePersistance(sum(digits))
            self.count += 1

    def multiplicativePersistance(self,number):
        digits = [int(x) for x in str(number)]
        if len(digits)!=1:
            result = 1
            for i in digits:
                 result = result * i
            self.multiplicativePersistance(result)
            self.count += 1

persistance().main()
