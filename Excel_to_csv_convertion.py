
import os
import glob
import csv
import pathlib

from xlsxwriter import Workbook

import win32com.client as win32

def convert_csv(filespath):
    filespath = pathlib.Path(filespath)
    for csvfile in glob.glob(os.path.join(filespath, '*.csv')):
        print("converting csv file: "+str(csvfile))
        workbook = Workbook(csvfile[:-4] + '.xlsx', {'constant_memory': True})
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
        os.remove(csvfile)

    return True


def convert_xls(filespath):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    filespath = pathlib.Path(filespath)
    for xlsfile in glob.glob(os.path.join(filespath, '*.xls')):
        print("converting xls file: "+str(xlsfile))
        wb = excel.Workbooks.Open(xlsfile)
        wb.SaveAs(xlsfile+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
        wb.Close()                               #FileFormat = 56 is for .xls extension
        excel.Application.Quit()
        os.remove(xlsfile)
    
    return True