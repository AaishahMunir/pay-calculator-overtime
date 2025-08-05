#Rewrite your pay computaion to give the emploee 1.5 times the hourly rate for hours worked above 40 hours.
string_hours = input ("Enter hours: ")
string_rate = input ("Enter rate: ")
float_hours = float(string_hours)
float_rate = float(string_rate)
# print("fh , fr")
if float_hours > 40.0:
    print ("Overtime")
    regular = float_rate * 40.0
    print("Regular Pay: ", regular)
    overtime_hours = float_hours - 40.0
    overtime_pay = overtime_hours * (float_rate * 1.5)
    print("Overtime Pay: ", overtime_pay)
    expected_pay = regular + overtime_pay
    print("Total Pay: ", expected_pay)
else:
    print ("Regular")
    regular_pay = float_hours * float_rate
    print("Total Pay: ", regular_pay)
print("Done")
# This code calculates the pay based on hours worked and rate, applying overtime rules if applicable.