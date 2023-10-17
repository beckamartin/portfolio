def format_duration(seconds):
    from datetime import timedelta
    
    if seconds == 0:
        return "now"
    
    dt = timedelta(seconds=seconds)
    years, days = divmod(dt.days, 365)
    days, seconds = divmod(days * 86400 + dt.seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if years == 1:
        years = str(years) + " year"
    else:
         years = str(years) + " years"

    if days == 1:
        days = str(days) + " day"
    else:
        days = str(days) + " days"

    if hours == 1:
        hours = str(hours) + " hour"
    else:
        hours = str(hours) + " hours"

    if minutes == 1:
         minutes = str(minutes) + " minute"
    else:
        minutes = str(minutes) + " minutes"

    if seconds == 1:
        seconds = str(seconds) + " second"
    else:
        seconds = str(seconds) + " seconds"
        
    array = list()
    answer = str()

    for x in (years, days, hours, minutes, seconds):
        if x[0] == "0":
            pass
        else:
            array.append(x)

    if len(array) == 1:
        answer = array[0]

    elif len(array) == 2:
        answer = array[0] + " and " + array[1]

    else:
        for time in array[0:-2]:
            answer = answer + time + ", "
        answer = answer + array[-2] + " and " + array[-1]

    return answer