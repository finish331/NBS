# coding=UTF-8
import pandas
from bs4 import BeautifulSoup as BS
import requests
from data_processing import Clear

def Crawler(url):
    table = pandas.read_html(url)[0]
    new_table = table.fillna(value = 0)
    return new_table

def del_empty_col(table):
    table['Rk'].astype('str')
    temp = table[table.Rk != 'Rk']
    del_col = [19, 24]
    temp2 = temp.drop(table.columns[del_col], axis=1)
    new_table = temp2.reset_index(drop=True)
    # print(new_table.loc[0:30, :'Player'])
    return new_table

if __name__ == '__main__':
    # for year in range(2017, 2020):
    #     url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_leaders.html'

    table = del_empty_col(Crawler('https://www.basketball-reference.com/leagues/NBA_2019_advanced.html'))
    # print(type(table))
    # list = table.values.tolist()
    # print(type(list))
    Clear(table)
