import pandas as pd 
import numpy as np

class HandleOutliers:
    
    def remove_outliers(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        higher = Q3 + 1.5*IQR
        return df[(df[column] >= lower) & (df[column] <= higher)]

