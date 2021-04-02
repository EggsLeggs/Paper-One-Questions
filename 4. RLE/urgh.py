class RLE():
    def main(self):
        string = str(input("Original text: "))
        RLEarray = self.check(string)
        print("Compressed text: {encoded}".format(encoded = " ".join(RLEarray)))

    def check(self, string):
        array = []
        count = 1
        Letter = string[0]
        stringArray = list(string)
        for i in range(len(stringArray)):
            if (i+1)!=len(stringArray):
                if stringArray[i] == stringArray[i+1]:
                    count += 1
                else:
                    array.append(Letter)
                    array.append(str(count))
                    Letter = stringArray[i+1]
                    count = 1
            else:
                array.append(Letter)
                array.append(str(count))
        return array

RLE().main()
