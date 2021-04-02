class ISBNcheck():
    def main(self):
        ISBN = []
        total = 0
        for i in range(13):
            ISBN.append(self.numberInput())
            if i != 12:
                if i % 2 == 0:
                    ISBN[i]*=1
                if i % 2 == 1:
                    ISBN[i]*=3
                total += ISBN[i]
        if (10 - (total % 10)) == ISBN[12]:
            print("Valid ISBN")
        else:
            print("Invalid ISBN")
    
    def numberInput(self):
        NumberToFind = input("Input: ")
        try:
          NumberToFind = int(NumberToFind)
        except ValueError:
          print("\nOnly whole numbers are allowed\n")
          return self.numberInput()
        if len(str(NumberToFind)) > 1:
          print("\nSorry, 1 digit allowed\n")
          return self.numberInput()
        return NumberToFind

ISBNcheck().main()
