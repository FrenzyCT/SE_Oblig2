'''Et år er et skuddår:

Når det er delelig med 4, men ikke 100
Når det er delelig med 400
(For eksempel var år 2000 et skuddår)
Et år er ikke et skuddår

er ikke et skuddår:
Når det ikke er delelig med 4
Når det er delelig med 100, men ikke 400.
(For eksempel var ikke 1700, 1800 og 1900 skuddår, ei heller blir 2100 et)'''


def calculate_if_leap_year(leapyear):
    if leapyear % 4 == 0 and leapyear % 100 != 0:
        return True
    elif leapyear % 400 == 0:
        return True
    return False



if __name__ == "__main__":
    print("hva year do you whant to check for leapyear?: ")
    year = int(input())

    isLeapyear = calculate_if_leap_year(year)
    print(f"Is {year} a leapyear?: {isLeapyear}")
