import pandas as pd

file = r'C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\Summer Coding Stuff\Aptitude\post-school-qualification-field-of-study-2018-census.csv'

df = pd.read_csv(file)

print(df.head(10))