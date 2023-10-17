# Outdated

def main():

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

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")

            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                month = months.index(month) + 1

            if int(month) > 12 or int(day) > 31:
                continue

        except:
            continue

        else:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break

if __name__ == "__main__":
    main()