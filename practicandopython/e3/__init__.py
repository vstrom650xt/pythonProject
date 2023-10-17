import datetime

if __name__ == '__main__':
    today = datetime.date.today()
    year = today.year
    try:
        year2 = input("put a year")
        year2 = int(year2)

        if year2 > year:
            remaining_years = year2 - year
            print("Remaining years:", remaining_years)
        else:
            yearss =year - year2
            print("The entered year is not in the future.")

    except ValueError:
        print('input error')



