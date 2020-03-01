#!/usr/bin/python
import os

fullLog = []
requestTypeList = []

addressList = []
printList = []
addressDict = {}
resultsList = []

folder = os.getcwd()

for file in os.listdir(folder):  # Reads all logs files in the current directory into a giant list and removes empty lines
    if file.endswith(".log"):  # finds only log files
        with open(file, 'r') as log:  # opens files as read only
            Log_file = log.readlines()
            for line in Log_file:
                if line == "\n":  # skips blanks lines
                    Log_file.remove(line)
                else:  # stores anything else in the full log of all logs in the folder
                    fullLog.append(line)

timeList = []
ipList = []
arpRequestList = []

for line in fullLog:
    infoSplit = line.split(" ")  # splits information, will contain different information if IP or ARP
    if infoSplit[1] == "IP":  # splits requests into IP or ARP
        ipList.append(infoSplit[2])
    elif infoSplit[1] == "ARP" or "ARP,":
        if infoSplit[2] == "Request":  # only keeping requests, replies have a different format so we aren't using those
            arpRequestList.append(infoSplit[4])
            timeList.append(infoSplit[0])

for line in ipList:
    addr = line.split(".")  # can't just go by lines because the logs have extensions, only 0 - 3 contain the IP
    scanAddr = addr[0] + "." + addr[1] + "." + addr[2] + "." + addr[3]  # Builds IP address without junk on the end
    if scanAddr in addressDict:  # counts how many times each address' shows up
        addressDict[scanAddr] = addressDict[scanAddr] + 1
    else:
        addressDict[scanAddr] = 1

addressDict = dict((ad, count) for ad, count in addressDict.items() if count > 50)  # removes anything with less than 50

timeListPrev = 0
arpRequest = 0

for address in range(len(arpRequestList) - 1):
    for arpRequestList[address] in addressDict:
        timeListCurrent = timeList[address]
        timeListCurrent = timeListCurrent.split(":")
        timeListNow = 24 * float(timeListCurrent[0]) + 60 * float(timeListCurrent[1]) + 60 * float(timeListCurrent[2])
        timeDifference = timeListNow - timeListPrev
        timeListPrev = timeListNow
        if timeDifference > 1000:  # checks that time difference is at least a half second to not write the same request twice
            #print("Scanned from " + arpRequestList[address] + " at " + timeList[address])
            resultsList.append("Scanned from " + arpRequestList[address] + " at " + timeList[address] + "\n")

with open('report.txt', 'w+') as scanResults:
    for element in range(len(resultsList)):
        scanResults.write(resultsList[element])
