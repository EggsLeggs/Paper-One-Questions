class doubleFactorial():
    def main(self):
        calculation = []
        total = 1
        number = self.numberInput()
        for i in range(1,number+1):
            if number % 2 == 0:
                if i % 2 == 0:
                    calculation.append(str(i))
                    total *= i
            else:
                if i % 2 == 1:
                    calculation.append(str(i))
                    total *= i
        print("Output: {inputs}!! = {maths} = {result}".format(inputs=number, maths="*".join(calculation[::-1]), result=total))

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

doubleFactorial().main()
