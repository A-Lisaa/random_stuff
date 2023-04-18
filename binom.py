from math import factorial


def main():
    sign = True # True = +, False = -
    power = 2

    for position in range(power+1):
        coefficient = factorial(power) // (factorial(position)*factorial(power - position))
        if coefficient > 1:
            print(coefficient, end="*")

        if position < power:
            print("a", end="")
            if power - position > 1:
                print(f"^{power - position}", end="")
        if position > 0:
            print("*", end="")
            print("b", end="")
            if power - position > 1:
                print(f"^{power - position}", end="")

        if power != position:
            print(" + " if sign or coefficient % 2 != 0 else " - ", end = "")


if __name__ == "__main__":
    main()
