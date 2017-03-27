# written by Bahar Zarin, 2016
import numpy as np
import pandas as pd
from bokeh.io import gridplot
from bokeh.charts import Histogram, output_file,show
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='Data Analyzer')
    parser.add_argument('--input_path', dest='input_path', help='The path to the csv file containing data',
                        default='Test.csv' , type=str)
    parser.add_argument('--save_path', dest='save_path',
                        help='Path to save the outputs',
                        default='./', type=str)
    parser.add_argument('--columns', dest='col_names',
                        help='Name of data columns',
                        default=['TripId', 'DeviceId','ProviderId','Mode',\
                                 'StartDate','StartWDay','EndDate','EndWDay','StartLocLat',\
                                 'StartLocLon','EndLocLat','EndLocLon','IsStartHome','IsEndHome',\
                                 'GeospatialType','ProviderType','ProviderDrivingProfile',\
                                 'VehicleWeightClass','FirstZoneName','LastZoneName',\
                                 'MultipleZones','MultipleCorridors'], type=list)
    parser.add_argument('--cols_to_analyze', dest='cols_to_analyze',
                        help='Name of data columns to be analyzed',
                        default=['Mode','IsStartHome','IsEndHome','VehicleWeightClass'], type=list)
    args = parser.parse_args()
    return args

def plot_hists(dataframe,cols,save_path=None):
    hist_plots = []
    for colname in cols:
        newfig = Histogram(dataframe[colname], title='Histogram of {}'.format(colname), tools="save",
                background_fill_color="#E8DDCB")
        hist_plots.append([newfig])
    final_fig = gridplot(hist_plots)
    show(final_fig)
    if save_path:
        output_file(save_path,'Histograms')

if __name__ == '__main__':
    args = arg_parse()
    readdata=pd.read_csv(args.input_path)
    col_names = args.col_names
    cols_to_analyze = args.cols_to_analyze
    A=np.array(readdata)
    bf=pd.DataFrame(readdata)
    df=pd.DataFrame(readdata.values, columns=col_names)
    for col in cols_to_analyze:
        freq=df[col].value_counts()
        print('*************************************')
        print('The frequency for column {} is:'.format(col))
        print(freq)
        print('*************************************')

