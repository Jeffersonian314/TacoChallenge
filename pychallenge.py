class Taco ():
    def __init__(self, meat, topping):
        self.meat = meat
        self.topping = topping

    def ordering(self):
        print("WELCOME TO THE TACO STORE, BRO!")

myTaco = Taco("carne", "salsa")

myTaco.ordering()

bro = input("What kind of meat would you like in your taco?")
print("Nice choice! Your taco now has" +" "+bro+" " + "as the meat!")
print("\n")
name= input("Now, what kind of topping would you like on your"+" "+bro+" "+"taco?")
print("(づ｡◕‿‿◕｡)づ")
print("Your taco is now a(n)"+" "+bro+" "+"taco topped with delicious"+" "+name+"!")
print("(づ｡◕‿‿◕｡)づ")
print("Enjoy!")
print("(づ｡◕‿‿◕｡)づ")
