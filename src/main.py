import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default = "notebook"

import plotly.express as px
import os


if __name__ == "__main__":

    # get root
    root = os.path.join(os.getcwd(), os.pardir)
    root = os.path.abspath(root)

    df = pd.read_csv(os.path.join(root, 'dataset/train.csv'))
    
    print('----data train----')
    print(df.head())
    print('\n')

    # fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
    #                     color='petal_length', symbol='species')


