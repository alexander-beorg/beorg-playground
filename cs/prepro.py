import os
import pandas as pd

def preprint(dir_name):
    log = open('log_preprint.txt', 'w')
    p = 0
    for dirs, folder, files in os.walk(dir_name):
        for i in files:
            if str(i)[-4:] == ".csv":
                f = os.path.join(dirs, i)
                print(f)
                p += 1
                log.write(f + '\n')
    print(f'Total .csv files: {p}')
    log.write(f'Total .csv files: {p}')
    log.close()

def prepro(dir_name):
    # dir_name = os.getcwd()
    log, log_err = open('log_prepro.txt', 'w'), open('log_prepro_err.txt', 'w')
    log_p, log_e = 0, 0
    for dirs, folder, files in os.walk(dir_name):
        for i in files:
            if str(i)[-4:] == ".csv":
                # f = f"{str(dirs) + '/' + str(i)}"
                f = os.path.join(dirs, i)
                try:
                    data = pd.read_csv(f, encoding="cp1251", sep=';')
                    data['Каналы'] = 3
                    data['Бит'] = 24
                    data['dpi X'] = 300
                    data['dpi Y'] = 300
                    data.to_csv(f, encoding="cp1251", sep=';', index=False)
                    log_p += 1
                    log.write(f + '\n')
                    print(f'OK {log_p}  {f}')
                except Exception as e:
                    log_e += 1
                    log_err.write(f'{f} # {e}' + '\n')
                    print(f'ERROR {log_e}  {f}')
                    continue
    print(f'Total OK .csv files: {log_p}')
    print(f'Total ERROR .csv files: {log_e}')
    log.write(f'Total OK .csv files: {log_p}')
    log_err.write(f'Total ERROR .csv files: {log_e}')
    log.close()
    log_err.close()

if __name__ == "__main__":
    # preprint(os.getcwd())
    preprint("D:\\Code\\Projects\\16_12_2020_preparce\\test")
    # prepro(os.getcwd())
    # prepro("D:\\Code\\Projects\\16_12_2020_preparce\\test")

