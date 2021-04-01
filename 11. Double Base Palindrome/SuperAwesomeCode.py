class palindromeGame():
  def __init__(self):
    self.NumberToLoop = self.setupNumberLoop()

  def setupNumberLoop(self):
    NumberToLoop = input("Choose the amount numbers to show palindromes for: ")
    try:
      NumberToLoop = int(NumberToLoop)
    except ValueError:
      print("\nOnly whole numbers are allowed\n")
      return self.setupNumberLoop()
    if NumberToLoop <= 0:
      print("\nSorry, only numbers greater than 0\n")
      return self.setupNumberLoop()
    return NumberToLoop
  
  def showPalindromes(self):
    print("Denary\t\tBinary")
    for i in range(self.NumberToLoop):
      if checks().checkPalindrome(int("{0:b}".format(i))) and checks().checkPalindrome(i):
        print("{Denary}\t\t\t{Binary}".format(Denary=i,Binary="{0:b}".format(i)))
  
class palindromeGame20():
  def showPalindromes(self):
    count,i = 0,0
    print("\nFirst 20 Palindromes:")
    print("Denary\t\t\tBinary")
    while count < 20:
      if checks().checkPalindrome(int("{0:b}".format(i))) and checks().checkPalindrome(i):
        print("{Denary}\t\t\t{Binary}".format(Denary=i,Binary="{0:b}".format(i)))
        count += 1
      i += 1

class checks():
  def checkPalindrome(self, value):
    tmp = [0,0]
    tmp[1] = value
    while value > 0:
      tmp[0] = tmp[0]*10+value%10
      value = value//10
    if tmp[1] == tmp[0]:
      return True
    else:
      return False

# palindromeGame().showPalindromes()  # Run if you want to set the number of repeats
palindromeGame20().showPalindromes()
