class main():
    def __init__(self):
        self.hexBinary = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    def NibbleToHex(self):
        BinaryNibble = self.binaryInput()
        for i in range(len(BinaryNibble)):
            tmp = list(BinaryNibble[i][::-1])
            for y in range(len(BinaryNibble[i])):
                tmp[y] = str(int(tmp[y])*(2**y))
            BinaryNibble[i] = "".join(tmp)
            BinaryNibble[i] = self.addBinary(BinaryNibble[i])
        print("Hex Digits: {Hex}".format(Hex="".join(BinaryNibble)))            

    def binaryInput(self):
        binary = str(input("Enter Binary: "))
        if not len(binary)%4 == 0:
            binary = "0"*((((len(binary)//4)+1)*4)-len(binary))+binary
        binary = [binary[i:i+4] for i in range(0, len(binary), 4)]
        return binary

    def addBinary(self, binary):
        tmp = sum(map(int, binary))
        if tmp >= 10:
            return self.hexBinary[tmp]
        return str(tmp)
        
main().NibbleToHex()
