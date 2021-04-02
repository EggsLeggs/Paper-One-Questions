class Lucky():
    def main(self):
        Number = self.numberInput()
        Lucky, Repeated = self.check(Number)
        if Lucky == True:
            print("Output: True, all digits are different")
        elif Lucky == False:
            print("Output: False, the following digits are repeated: {repeat}".format(repeat = ", ".join(Repeated)))

    def check(self, Number):
        Lucky = True
        repeated = []
        NumArray = list(str(Number))
        for i in range(len(NumArray)):
            if (i+1)!=len(NumArray):
               for y in range((i+1),len(NumArray)):
                   if NumArray[i] == NumArray[y]:
                       repeated.append(str(NumArray[i]))
                       Lucky = False
        return Lucky, repeated

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

Lucky().main()
