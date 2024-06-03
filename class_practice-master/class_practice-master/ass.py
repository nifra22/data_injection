import pandas as pd

class Csv:
    path = ""
    def __init__(self, path):
        self.path = path

class Graph:
    def __init__(self, path):
        pass

csv = Csv()
path = pd.read_csv(r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv')
