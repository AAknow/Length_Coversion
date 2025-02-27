## CST-16163 Intro to Computer Programming
## By: Aaron Knowles

## A function to convert U.S. Customary System measurements to Metric measurements
def conversion():
    result = 0
    measurement = ""
    
    prompt = input("What type of U.S. Customary System length would you like to convert to its " + \
        "\nMetric System counterpart: Miles, Yards, Feet, or Inches?\n")
    
    num = float(input("What number would you like to be converted?\n"))

    # Determines what we are converting to and calculates the result
    if prompt.lower() == "miles":
        metric = input("What would you like to convert it to: Kilometers, Meters, or Centimeters?\n")

        if metric.lower() == "kilometers":
            result = num * 1.60934
            measurement = "km"
            
        elif metric.lower() == "meters":
            result = num * 1609.34
            measurement = "meters"
            
        elif metric.lower() == "centimeters":
            result = num * 160934
            measurement = "cm"

        else:
            print("Oops, try again!")
            conversion()
        
    elif prompt.lower() == "yards":
        metric = input("What would you like to convert it to: Kilometers, Meters, or Centimeters?\n")

        if metric.lower() == "kilometers":
            result = num * 0.0009144
            measurement = "km"
            
        elif metric.lower() == "meters":
            result = num * 0.9144
            measurement = "meters"
            
        elif metric.lower() == "centimeters":
            result = num * 91.44
            measurement = "cm"

        else:
            print("Oops, try again!")
            conversion()
            
    elif prompt.lower() == "feet":
        metric = input("What would you like to convert it to: Kilometers, Meters, or Centimeters?\n")

        if metric.lower() == "kilometers":
            result = num * 0.0003048
            measurement = "km"
            
        elif metric.lower() == "meters":
            result = num * 0.3048
            measurement = "meters"
            
        elif metric.lower() == "centimeters":
            result = num * 30.48
            measurement = "cm"

        else:
            print("Oops, try again!")
            conversion()
        
    elif prompt.lower() == "inches":
        metric = input("What would you like to convert it to: Kilometers, Meters, or Centimeters?\n")

        if metric.lower() == "kilometers":
            result = num * 2.54e-5
            measurement = "km"
            
        elif metric.lower() == "meters":
            result = num * 0.0254
            measurement = "meters"
            
        elif metric.lower() == "centimeters":
            result = num * 2.54
            measurement = "cm"

        else:
            print("Oops, try again!")
            conversion()
        
    else:
        print("Oops, try again!")
        conversion()

    ## Displays the result if one was calculated
    if result != 0:
        print("Your converted number is: " + str(round(result, 2)) + " " + measurement)

    ## Asks the user if they want to restart
    restart = input("Would you like to convert another number, yes or no? ")

    if restart.lower() == "yes":
        conversion()

    else:
        print("Thanks for converting!")

## Runs the conversion function on startup
conversion()



