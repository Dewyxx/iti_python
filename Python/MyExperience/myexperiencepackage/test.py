from myexperiencepackage.simplefile import readfile, writefile
import pandas as pd


# Write to a text file
writefile('example.txt', 'a test program!')

# Read from the text file
content_text = readfile('example.txt', option="text")
print(content_text)  

df = pd.DataFrame({
    'Name': ['Nadosh', 'Dewy'],
    'Age': [21, 22]
})

# Write DataFrame to an Excel file
writefile('sample.xlsx', df, option="excel")

# Read from the Excel file
content_excel = readfile('sample.xlsx', option="excel")
print(content_excel)
