# Created by: David Wang
# Created on: 1-Dec-2017
# Created for: ICS3U
# Daily Assignment - Unit6-02
# This program displays an enumerated type

from enum import Enum

# an enumerated type of planets
Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

print('Sunday(1), Monday(2), Tuesday(3), Wednesday(4), Thursday(5), Friday(6), Saturday(7)')

day_of_the_week_selected = raw_input('Enter your favorite day of the week: ')

counter = 0
position = None

for a_day in Days:
    if str(a_day) == day_of_the_week_selected:
        print(day_of_the_week_selected)
        position = counter + 1
    counter = counter + 1
print("Day")
print(position)
print("is your favourite day of the week")

