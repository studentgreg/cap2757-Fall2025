# Week #3 - Data Processing

import pandas as pd

personal_info = {
    "name":["greg","alice","leo","rebeca","david"],
    "age":[23,35,45,25,30],
    "height_cm":[184,175,160,180,170],
    "weight_kg":[85,65,70,90,60]
}
print(personal_info,type(personal_info))

df = pd.DataFrame(personal_info)
print(df)

print(df.columns) # printing the names of the columns
print(df.shape) # number of rows and number of columns
print(df["name"]) # accessing one specific column
print(df["age"])
print(df[["height_cm","weight_kg"]]) # accessing multiple columns
print(df["age"].min()) # minimum value
print(df["age"].max()) # maximum value
print(df["age"].mean()) # average value
print(df["age"].median()) # median value
print(df["age"].std()) # standard deviation value

print(df.describe())

condition = df["age"]>30
print(df[condition])

# Add two more columns, one for height in inches and one for weight in lbs

df["height_in"]=df["height_cm"]*0.393701
df["weight_lbs"]=df["weight_kg"]*2.20462
print(df)

# Create a new column named BMI that calculates the body mass index
df["bmi"]=df["weight_kg"]/((df["height_cm"]/100)**2)
print(df)