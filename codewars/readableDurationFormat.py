def format_duration(seconds):
    if seconds == 0:
        return 'now'
    out = ""
    years = 0
    days = 0
    hours = 0
    minutes = 0

    while seconds >= 31536000: # add the number of years in seconds
        years += 1
        seconds -= 31536000
    if years > 0:
        out += str(years) + " year"
    if years > 1: # makes year plural if there is more than 1 year
        out += 's'
    if seconds > 0 and years > 0: # if other time will be added, add a comma and space for it
        out += ', '

    while seconds >= 86400: # same as above with days
        days += 1
        seconds -= 86400
    if days > 0:
        out += str(days) + " day"
    if days > 1:
        out += 's'
    if seconds > 0 and days > 0:
        out += ', '


    while seconds >= 3600: # same as above with hours
        hours += 1
        seconds -= 3600
    if hours > 0:
        out += str(hours) + " hour"
    if hours > 1:
        out += 's'
    if seconds > 0 and hours > 0:
        out += ', '

    while seconds >= 60: # same as above with minutes
        minutes += 1
        seconds -= 60
    if minutes > 0:
        out += str(minutes) + " minute"
    if minutes > 1:
        out += 's'
    if seconds > 0 and minutes > 0:
        out += ', '

    if seconds > 0:
        out += str(seconds) + ' second' # adds seconds since that's all that's left, don't  add anything if not
    if seconds > 1:
        out += 's'

    if ',' in out: # change the last comma to the word ' and '
        out = out[::-1].replace(',','dna ', 1)
        out = out[::-1]

    return out




# 60 seconds/minutes
# 60 * 60 = 3600 seconds/hour
# 60 * 60 * 24 = 86400 seconds/day
# 60 * 60 * 24 * 365 = 31536000 seconds/year
"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

"""