class politeNumbers():
    def __init__(self):
        self.number = self.numberInput()
        self.politenessArray = []
        self.numsArray = self.generateArray(self.number)

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

    def generateArray(self, number):
        lessThanNums = []
        for i in range(number):
            if i != 0:
                lessThanNums.append(i)
        return lessThanNums
    
    def main(self):
        for i in range(len(self.numsArray)):
            self.add([],i)
        print("Output: {}".format(len(self.politenessArray)))
        print("Explanation:")
        for i in range(len(self.politenessArray)):
            tmp = ""
            for y in self.politenessArray[i]:
                tmp = tmp + str(y) + " + "
            tmp = tmp[:len(tmp)-2]
            print(("{Number} = "+tmp).format(Number=self.number))
        print("Hence answer is {Number}".format(Number=len(self.politenessArray)))

    def add(self, array, index):
        if index < len(self.numsArray)-1:
            if sum(array) < self.number:
                array.append(self.numsArray[index])
                sum(array)+self.add(array,index+1)
                return 1
            elif sum(array) == self.number:
                self.politenessArray.append(array)
                return(sum(array))
            else:
                return 1
        else:
            return 1
        
politeNumbers().main()
