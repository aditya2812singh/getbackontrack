import openpyxl
#Create new workbook

wb = openpyxl.Workbook() 
#Get SHEET name

Sheet_name = wb.sheetnames
#Save created workbook at same path where .py file exist

wb.save(filename='Test1.xlsx')