#!/usr/bin/python
import re

with open('dnslog.txt') as dnslog:
    log = dnslog.readlines()
    dnslog.close()

time = []  # time in H:m:S
date = []
raw_time = []  # time in us
new_requests = [0]  # line number
new_sites = []  # line number of original request
site_name = []  # name of original request (string)
duplicates = []  # line number of other request

for current_line in range((len(log) // 2)+1):  # Creates an array of dns request times
    x = log[current_line].find("AAAA")
    if (x != -1):
        del log[current_line]

for current_line in range(len(log)):
    line_time = re.search(r'[0-9]+:[0-9]+:[0-9]+:[0-9]+',log[current_line])  # Searches line by line for the appropriate time format
    time.append(line_time.group())  # Puts time in an array
    times_list = time[current_line].split(":")  # Splits hours/minutes/seconds/us into a list
    raw_time.append(int(times_list[0]) * 3600000000 + int(times_list[1]) * 60000000 + int(times_list[2]) * 1000000 + int(float(times_list[3])))  # Finds a raw time in micro seconds
    line_date = re.search(r'[0-9]+-[0-9]+-[0-9]+', log[current_line])
    date.append(line_date.group())

for current_line in range(len(log) - 1):  # Compares time difference between each line and records line of new sites
    next_line = current_line + 1
    time_difference = raw_time[next_line] - raw_time[current_line]
    if time_difference > 10000000: #at least 10 seconds, finds each new request
        new_requests.append(current_line)

# go line by line, adds line if it isn't in new_requests and reset when matches new_requests
for element in range(len(log) - 1):
    if element not in new_requests:
        duplicates.append(log[element + 1])
duplicates.append(log[len(log) - 1])

individual_requests = len(new_requests)
new_url = []
url_names = []
for loops in range(individual_requests):
    new_url.append([])
    url_names.append([])

url_count = 0
for element in range(len(log)):
    if element not in new_requests:
        new_url[url_count - 1].append(element)
    else:
        url_count = url_count + 1

for element in range(len(new_url)):
    for line in range(len(new_url[element])):
        temp = new_url[element][line]

        x = log[temp]
        url_string = str(x)
        string = url_string.split(" ")
        name = string[13]
        if name not in url_names[element]:
            url_names[element].append(string[13])

for element in range(len(new_requests)):  # Uses lines from time difference to find corresponding dnslog lines
    new_sites.append(log[new_requests[element] + 1])
    # print new_sites[element]
    site = str(new_sites[element]).split(" ")
    site_name.append(site[13])

with open('report.txt', 'w+') as dns_results:
    for element in range(len(url_names)):
        unique_count = 0
        first_line = url_names[element]
        dns_results.write("\nNew request: " + str(
            site_name[element] + " Accessed: " + str(date[element]) + str(time[element]) + "\n"))
        for line in range(len(url_names[element])):
            result = url_names[element][line]
            dns_results.write(str(line + 1) + "-" + " " + result + "\n")
            unique_count = unique_count + 1
        dns_results.write("There were " + str(unique_count) + " unique DNS requests\n")
