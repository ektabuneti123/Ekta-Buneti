#Name - Ekta Buneti
#Roll no - F077
#write a program to create variables outside the class and apply logic.
coat1 = 890
coat2 = 1590

class price:
    def shopping(self, price):
        if price >= 1000:
            return "Too costly"
        else:
            return "Available in good price range"

pri = price()

res1 = pri.shopping(coat1)
res2 = pri.shopping(coat2)

print("Price Range of Coat 1 : ", coat1, "is", res1)
print("Price Range of Coat 2 : ", coat2, "is", res2)











