import pandas as pd
from process import Excel, Graph, IData_inject
from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Factory method
class IDataFactory(ABC):
    @abstractmethod
    def create_data_injector(self, path):
        pass
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass
class ExcelDataFactory(IDataFactory):
    def create_data_injector(self, path):
        return Excel(path)


class GraphDataFactory(IDataFactory):
    def create_data_injector(self, path):
        return Graph(path)

class TotalSalesByRegion(DataProcessor):
    def process(self, data):
        df = pd.DataFrame(data)
        return df.groupby('region')['total sales'].sum()

class AverageOperatingMargin(DataProcessor):
    def process(self, data):
        df = pd.DataFrame(data)
        return df['operating margin'].mean()


class BestSellingProduct(DataProcessor):
    def process(self, data):
        df = pd.DataFrame(data)
        return df.groupby('product')['unit sold'].sum().idxmax()


class TotalSalesPerMonth(DataProcessor):
    def process(self, data):
        df = pd.DataFrame(data)
        df['invoice date'] = pd.to_datetime(df['invoice date'])
        df['month'] = df['invoice date'].dt.to_period('M')
        return df.groupby('month')['total sales'].sum()


class SalesMethodEachMonth(DataProcessor):
    def process(self, data):
        df = pd.DataFrame(data)
        df['invoice date'] = pd.to_datetime(df['invoice date'])
        df['month'] = df['invoice date'].dt.to_period('M')
        return df.groupby(['month', 'sales method'])['total sales'].sum().unstack()


class PreprocessingDecorator(DataProcessor):
    def __init__(self, processor):
        self._processor = processor

    def process(self, data):
        preprocessed_data = self._preprocess(data)
        return self._processor.process(preprocessed_data)

    def _preprocess(self, data):
        df = pd.DataFrame(data)
        df.fillna(0, inplace=True)
        return df.to_dict(orient='records')


if __name__ == "__main__":
    file_path = r'C:\Users\97150\OneDrive\Desktop\APDP\Data1.xlsx'

    excel_factory = ExcelDataFactory()
    excel_injector = excel_factory.create_data_injector(file_path)
    data = excel_injector.data_inject()

    strategies = [
        TotalSalesByRegion(),
        AverageOperatingMargin(),
        BestSellingProduct(),
        TotalSalesPerMonth(),
        SalesMethodEachMonth()
    ]

    for strategy in strategies:
        decorated_strategy = PreprocessingDecorator(strategy)
        result = decorated_strategy.process(data)
        print(result)
