import numpy as np
import pandas as pd
import os, sys
import time
import datetime

def pprinter_log(dir_name):
    log = open('log.txt', 'w')
    head = "Файл скопированный;Файл изначальный;Вес, Кб;Вес, Мб;Статус;Дата;Время;Удалено"
    log.write(head + '\n')
    for dirs, folder, files in os.walk(dir_name):
        for i in files:
            f = os.path.join(dirs, i)
            t = str(datetime.datetime.strptime(time.ctime(os.path.getmtime(f)), "%a %b %d %H:%M:%S %Y")).split(" ")
            s = os.path.getsize(f)
            b = f'{f};{"C" + f[1:]};{s};{round(s/1024/1024,2)};Обработано;{t[0]};{t[1]};2020-12-16'
            print(b)
            log.write(b + '\n')
    log.close()

# data = pd.read_csv('log.txt', sep=';', encoding='cp1251')
# data.to_csv('log_csv.csv', encoding='cp1251', index=False, decimal=',', sep=';')

if __name__ == "__main__":
        # pprinter_log(os.getcwd())
        pprinter_log(os.getcwd()+'\\21_12_2020_logPdf')

