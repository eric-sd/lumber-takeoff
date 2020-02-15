#!/usr/bin/python3

import math
import configparser

config = configparser.ConfigParser()
config.read('lumber.ini')
walls = config.sections()


def convertToInches(feet):
    inches = int(feet) * 12
    return inches

def figureOutStuds(wallWidth, studSpacing):
    numberOfStuds = convertToInches(wallWidth) / int(studSpacing)
    numberOfStuds = numberOfStuds + 2 # add two more studs for the connections
    return math.ceil(numberOfStuds)

totalStuds = 0

for wall in walls:
    print(wall + " Width = " + config[wall]['width'])
    print(wall + " Width Inches = " + str(convertToInches(config[wall]['width'])))
    print(wall + " Stud Spacing Inches = " + str(config[wall]['studSpacing']))
    print(wall + " Studs Required = " + str(figureOutStuds(config[wall]['width'], config[wall]['studSpacing'])))
    totalStuds = totalStuds + figureOutStuds(config[wall]['width'], config[wall]['studSpacing'])
    print("")

print("Totals Studs Required = " + str(totalStuds))
