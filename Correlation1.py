import plotly.express as px 
import csv
import numpy as np 

def get_data_source(data_path):
            marks_in_percentage = []
            days_present = []
            with open('Student Marks vs Days Present.csv') as f:
                    csv_reader = csv.DictReader(f)
                    for row in csv_reader:
                                    marks_in_percentage.append(float(row['Days Present']))
                                    days_present.append(float(row['Marks In Percentage']))
            return{'x': marks_in_percentage,'y': days_present}

def findCorrelation(data_source):
            correlation = np.corrcoef(data_source['x'],data_source['y'])
            print('Correlation between student marks and days present are ',correlation[0,1])

def setup():
        data_path = './Student Marks vs Days Present.csv'
        data_source = get_data_source(data_path)
        findCorrelation(data_source)
setup()
                                    