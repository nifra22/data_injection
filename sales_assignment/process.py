import pandas as pd
from abc import ABC, abstractmethod

class IData(ABC):
    @abstractmethod
    def data_inject(self): pass

    @abstractmethod
    def data_preprocess(self): pass

class IData_inject(ABC):
    @abstractmethod
    def data_inject(self, path): pass

class IData_preprocess(IData):
    @abstractmethod
    def data_preprocess(self, path): pass

class Excel(IData_inject):
    def __init__(self, path):
        self.path = path

    def data_inject(self, path):
        df = pd.read_excel(path)
        data = df.to_dict(orient='records')
        return data

class Graph(IData_inject):
    def __init__(self, path):
        self.path = path

    def data_inject(self, path):
        with open(path, 'r') as file:
            data = file.read()
        return data

path = ""
excel = Excel(path)
graph = Graph(path)

file_path = r'C:\Users\97150\OneDrive\Desktop\APDP\Data1.xlsx'
excel = Excel(file_path)
Feed_data = excel.data_inject(file_path)
Feed_data_frame = pd.DataFrame(Feed_data)
print(Feed_data_frame)
