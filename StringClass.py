# Write a class that stores a string and all its status details such as number of
# uppercase characters, lowercase characters, vowels , consonants , spaces.

class String:
   def __init__(self):
      self.str = ""
      self.vowels = 0
      self.consonants = 0
      self.upperCase = 0
      self.lowerCase = 0
      self.spaces = 0
     
   def read(self):
      self.str = input("Enter the String")

   def display(self):
      string = self.str
      Vowels = "aeiouAEIOU"
      Consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
      
      for i in range(0,len(string)):
          for j in range(0,len(Vowels)):
             if(string[i] == Vowels[j]):
                self.vowels += 1
          for j in range(0,len(Consonants)):
             if(string[i] == Consonants[j]):
                self.consonants += 1
          if(string[i] >='A' and string[i] <='Z'):
             self.upperCase += 1
          if(string[i] >='a' and string[i] <='z'):
             self.lowerCase += 1
          if(string[i] == " "):
             self.spaces += 1
      
      print("No.of.Vowels : ",self.vowels)
      print("No.of Consonants : ",self.consonants)
      print("No.of UpperCase Characters :" ,self.upperCase)
      print("No.of LowerCase Characters : ",self.lowerCase)
      print("No.of Spaces : ",self.spaces)

Str = String()
Str.read()
Str.display()