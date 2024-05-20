import pandas as pd
import csv
import matplotlib.pyplot as plt
from time import sleep

#reading the csv file:
data = pd.read_csv('companies.csv')

#Calculate the ROI for each campaign using formula:

data['ROI'] =(( data['Revenue'] - data['Spent']) / data['Spent'])*100

# Calculate the average ROI for all campaigns:
with open('companies.csv','r') as csvfile :
    lines = csvfile.readlines()
num_lines = len(lines)
average_of_ROI = (data['ROI'].sum() / num_lines )
print(f"Average of ROI is : {average_of_ROI}")

#Identify the campaign with the highest ROI:
print(f"Highest ROI is : {max(data['ROI'])} ")

#Draw a ROI distribution chart
sleep(3)

plt.hist(data['ROI'], bins=20, edgecolor='black')
plt.title('ROI Distribution')
plt.xlabel('ROI (%)')
plt.ylabel('Frequency')
plt.show()

#----------------------------end----------------------
sleep(3)
print("parham code")
sleep(3)
exit()

