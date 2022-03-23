number = int(input("x,please enter  number: "))

while number >= 0:
    coin_1 = int(input("x: enter your coin: "))


    def square(coin_1):
        return coin_1 ** 0.5


    number -= square(coin_1)
    print(number)
    if square(coin_1) <= number:
        number -= square(coin_1)
        print(number)
    if number == 0:
        print("x is the winner!")
        quit()

    coin_2 = int(input("y: enter your coin: "))


    def square_2(coin_two):
        return coin_two ** 0.5


    number -= square_2(coin_2)
    if number == 0:
        print("y is the winner!")
        quit()
    print(number)
