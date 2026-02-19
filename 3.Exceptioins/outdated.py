# Task: https://cs50.harvard.edu/python/psets/3/outdated/


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ").strip()

while True:
    try:
        #for dates formated as: mm/dd/yyyy
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        #for dates formated as: month_name day, year
        elif "," in date:
            month_name, day, year = date.replace(",", "").split()
            if month_name in months:
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

    except ValueError:
        pass