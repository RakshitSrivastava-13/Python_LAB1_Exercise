# Write a Python program to convert the given list to a list of dictionaries.
# ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
# "800000", "FFFF00"]

# Expected Output: {’colorName’: ’Black’, ’colorCode’: ’000000’}, {’color-
# Name’: ’Red’, ’colorCode’: ’FF0000’}, ’colorName’: ’Maroon’, ’colorCode’:

# ’800000’}, {’colorName’: ’Yellow’, ’colorCode’: ’FFFF00’}


# Given lists
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["000000", "FF0000", "800000", "FFFF00"]


color_list = []
for i in range(len(color_names)):
    color_dict = {"colorName": color_names[i], "colorCode": color_codes[i]}
    color_list.append(color_dict)

# Print the result
for color in color_list:
    print(color)

