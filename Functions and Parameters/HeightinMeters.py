INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

def convert_height_to_meters(feet, inches):
    inches_total = (feet * 12) + inches
    CM_total = (inches_total) * 2.54 
    meters = (CM_total) * 0.01
    print(str(feet) + " feet, " + str(inches) + " inches " + "= " + str(meters) + " meters")
    
convert_height_to_meters(6, 4)
convert_height_to_meters(5, 8)
convert_height_to_meters(5, 2)