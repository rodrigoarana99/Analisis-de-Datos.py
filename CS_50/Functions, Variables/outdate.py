months= [
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


def is_valid_date(date_str):
    parts = date_str.split("/")
    if len(parts) == 3:
        year, month, day = map(int, parts)
        return 1 <= month <= 12 and 1 <= day <= 31
    else:
        # Splitting the input by space or slash to check for other formats
        parts = date_str.split()
        if len(parts) == 3:
            month, day, year = parts
            return month in months and day.isdigit() and year.isdigit()
        elif len(parts) == 1:
            # If there is only one part, then it could be in the format: year/month/day
            parts = date_str.split("/")
            if len(parts) == 3:
                year, month, day = map(int, parts)
                return 1 <= month <= 12 and 1 <= day <= 31
    return False

def convert_to_yyyy_mm_dd(date_str):
    parts = date_str.split("/")
    if len(parts) == 3:
        year, month, day = map(int, parts)
        return f"{year:04d}-{month:02d}-{day:02d}"
    else:
        parts = date_str.split()
        if len(parts) == 3:
            month, day, year = parts
            month_index = months.index(month) + 1
            return f"{year:04d}-{month_index:02d}-{int(day):02d}"
        elif len(parts) == 1:
            parts = date_str.split("/")
            year, month, day = map(int, parts)
            return f"{year:04d}-{month:02d}-{day:02d}"

def main():
    while True:
        date_input = input("Enter a date (in month-day-year, year/month/day, or Month day, year format): ")
        if is_valid_date(date_input):
            formatted_date = convert_to_yyyy_mm_dd(date_input)
            print("Formatted date (YYYY-MM-DD):", formatted_date)
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
