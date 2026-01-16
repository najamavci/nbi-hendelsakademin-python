#1a There are about 470 km between Stockholm and Gothenburg.
# Write a program that calculates how long it takes to drive from Stockholm to Gothenburg.
# You need to ask the user how fast they will drive, in km/h.
# Answer in hours.

distance = 470
speed = int(input("How fast do you drive from Stockholm to Gothenburg by car? "))

time = distance / speed

print("The distance between Stockholm and Gothenburg is", distance, "km")
print("The driver drives", speed, "km/h")
print("The driver arrives in", int(round(time)),  "hours from Stockholm to Gothenburg")

#1b Modify the program so that it answers in minutes instead of hours.
time_minutes = time * 60
print("The driver arrives in", int(time_minutes),  "minutes from Stockholm to Gothenburg")


