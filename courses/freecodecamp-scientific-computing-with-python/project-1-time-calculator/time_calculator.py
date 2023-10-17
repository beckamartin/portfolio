def main():
    print(add_time("3:00 PM", "24:10", "Monday"))


def add_time(start, duration, day = None):
    time, ampm = start.split(" ")

    start_hour = int(time.split(":")[0])
    start_minute = int(time.split(":")[1])

    add_hour = int(duration.split(":")[0])
    add_minute = int(duration.split(":")[1])

    if ampm == "PM":
        start_hour += 12

    total_minutes = start_minute + add_minute
    carry_hour = total_minutes // 60
    total_minutes = total_minutes % 60

    total_hours = start_hour + add_hour + carry_hour
    carry_day = total_hours // 24
    total_hours = total_hours % 24

    if total_hours == 0:
        total_hours = 12
        ampm = "AM"
    elif total_hours < 12:
        ampm = "AM"
    elif total_hours == 12:
        ampm = "PM"
    else:
        ampm = "PM"
        total_hours = total_hours % 12

    new_time = f"{total_hours}:{total_minutes:02} {ampm}"

    if day:
        day = day.title()
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = week.index(day)
        end_index = (start_index + carry_day) % 7
        new_time = f"{new_time}, {week[end_index]}"

    if carry_day == 1:
        new_time += f" (next day)"
    elif carry_day > 1:
        new_time += f" ({carry_day} days later)"

    return new_time


if __name__ == "__main__":
    main()