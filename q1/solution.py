
class Inventory:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def check_item(self, size):
        for i in range(len(ls)):
            if (ls[i].size == size):
                return i

    def sale(self):
        n = int(input("How many clothes to sale: "))
        total = 0
        for j in range(n):
            size = input("Enter size : ")
            quantity = int(input("Enter quantity: "))
            i = obj.check_item(size)
            if i and ls[i].quantity >= quantity:
                ls[i].quantity -= quantity
                print('Yes')
            else:
                print("No")

    def main(self):
        print("\n1.Make a sale\n2.Exit")
        option = int(input("Enter option here: "))
        while True:
            if option == 1:
                obj.sale()
            elif option == 2:
                break
            else:
                print("Enter a valid input!")

ls1 = list(range(2,1000))
for i in ls1:
    ls1[i]= ls1[i]+"L"

ls2 = list(range(1000,2))
for i in ls2:
    ls2[i]= ls2[i]+"S"

ls = ls1 + "S" + "M" + "L" + ls2

obj = Inventory('', 0, 0, 0, '')
obj.main()