
lbs = float(input("Please enter the lbs of water treated: "))
ounces = lbs * 16
gallons = int(ounces / 128)
ounces = ounces - gallons * 128
print("That’s",gallons,"gallons and",ounces,"ounces of treated waste water.")

# help(type) will output documentation for a particular Python3 data type 

