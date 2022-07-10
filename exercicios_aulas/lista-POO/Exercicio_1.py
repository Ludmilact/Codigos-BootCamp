#Function to calculate Roman values
class ConvertIntToRoman:
    
    def __init__(self, number: int ):
        self.number = number
        self.ans = ""
        self.intToRoman()

    def intToRoman(self):

        #Storing roman values of digits from 0-9
        #when placed at different places

        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # Converting to roman

        thousand = m [self.number // 1000]
        hundereds = c [(self.number % 1000) // 100]
        tens = x [(self.number % 100) // 10]
        ones = i[self.number % 10]

        self.ans = (thousand + hundereds + tens + ones)

# Driver code
if __name__ == "__main__":
    numer = int(input("Digite um número: "))
    resultado1 = ConvertIntToRoman(numer)
    print(resultado1.ans)