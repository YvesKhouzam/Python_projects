import openpyxl
import os

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook["Sheet1"]
print(type(sheet))
