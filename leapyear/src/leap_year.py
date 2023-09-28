
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
