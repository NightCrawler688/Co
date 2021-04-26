import plotly.express as px 
import csv
import numpy as np 

def get_data_source(data_path):
            ice_cream_sales = []
            cold_drink_sales = []
            with open(data_path) as csv_files:
                        csv_reader = csv.DictReader(csv_files)
                        for row in csv_reader:
                                    ice_cream_sales.append(float(row['Temperature']))
                                    cold_drink_sales.append(float(row['Ice-cream Sales( ₹ )']))
            return{'x': ice_cream_sales,'y': cold_drink_sales}

def findCorrelation(data_source):
            correlation = np.corrcoef(data_source['x'],data_source['y'])
            print('Correlation between cold drinks and ice cream sales ',correlation[0,1])

def setup():
        data_path = "./TICCD.csv"
        data_source = get_data_source(data_path)
        findCorrelation(data_source)
setup()