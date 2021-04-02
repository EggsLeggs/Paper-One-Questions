class Jumbled():
    def main(self):
        number = self.numberInput()
        jumbled = self.check(number)
        if jumbled:
            print("Output: False")
        if not jumbled:
            print("Output: True, all neighbouring digits differ by a maximum of 1")

    def check(self, number):
        jumbled = False
        numArray = [int(x) for x in str(number)]
        for i in range(len(numArray)-1):
            if not(((numArray[i] + 1) == numArray[i+1]) or ((numArray[i] - 1) == numArray[i+1])):
                jumbled = True
        return jumbled

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

Jumbled().main()
