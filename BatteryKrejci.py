#Jack Krejci
#Code for a battery monitor in an electric car determining the overall range
    #that it can travel in miles taking temperature, speed, traffic, and
    #climate control from the vehicle into consideration

#Use print function to create a proper title for the program
print("*" * 70)
print("*%s*" % "BATTERY LIFE ESTIMATOR".center(68))
print("*%s*" % "(version 1.0)".center(68))
print("*" * 70)
print()

#Create variables for temp, traffic, speed, climate control, beginning/ending overall range
range_current = float(input("Enter the current battery range in KWH: "))
temp = float(input("Enter current temperature: "))
traffic = input("How is traffic: (G)ood, (M)oderate, or (S)top-and-go? ")

#Automatically put traffic into uppercase incase user enters lowercase
#Initializes the variable for speed reduction incase traffic isn't good
traffic = traffic.upper().strip()
speed_red = 0
#Asks user for average speed only if the traffic is good
    #otherwise the question will be skipped
if traffic == "G":
    speed = float(input("What will be your average speed? "))
    if speed > 80:
        speed_red = 0.2
    elif speed > 60:
        speed_red = .1
    else:
        speed_red = 0
clim_con = input("Will the climate control be (O)ff, (L)ow, (M)edium, or (H)igh? ")

#Automatically puts letters in uppercase for climate control
    #incase user entered lowercase 
clim_con = clim_con.upper().strip()
print()

#Use if statement to determine if the temperature will reduce mileage and by how much
if temp > 100:
    temp_red = 0.4
elif temp > 85:
    temp_red = 0.1
elif temp < 0:
    temp_red = 0.4
elif temp < 20:
    temp_red = 0.3
elif temp < 40:
    temp_red = 0.2
else:
    temp_red = 0
    
#Use if statement to determine any traffic reduced mileage
if traffic == "S":
    traff_red = 0.25
elif traffic == "M":
    traff_red = 0.10
else:
    traff_red = 0
    
#Use if statement to determine any climate control reduced mileage
if clim_con == "O":
    clim_red = 0
elif clim_con == "L":
    clim_red = .05
elif clim_con == "M":
    clim_red = 0.1
elif clim_con == "H":
    clim_red = 0.2
    
#Totals the speed reduction percentage and calulates the overall range
total_red = speed_red + temp_red + traff_red + clim_red
over_range = (1-total_red) * range_current

#Creates strings in order to properly format the results
starter = "Starting Range (miles)"
temper = "% Temperature reduction"
trafficer = "% Traffic reduction"
speeder = "% Speed reduction"
climater = "% Climate control reduction"
totaler = "Total % reduction"
overaler = "Overall range (miles)"

#Takes the reduction decimals and converts them to whole numbers still having 2 decimal points
    #for better formatting 
temp_red *= 100
traff_red *= 100
speed_red *= 100
clim_red *= 100
total_red *= 100

#Formats the results with proper alignment 
print("Here is your battery range report:")
print("%-30s%10.2f" % (starter,range_current))
print("%-30s%10.2f" % (temper,temp_red))
print("%-30s%10.2f" % (trafficer, traff_red))
print("%-30s%10.2f" % (speeder,speed_red))
print("%-30s%10.2f" % (climater,clim_red))
print("%-30s%10.2f" % (totaler,total_red))
print("%-30s%10.2f" % (overaler,over_range))
print()
print("*" * 70)

    
    




