import json
import xlwt
import xlrd
from json2text import JSON2Text, Text2JSON

def main():
    with open('test.json', 'r') as f:
        jsonObj = json.load(f)
        ll = JSON2Text(jsonObj)
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('Sheet1')
        worksheet.write(0, 0, 'key')
        worksheet.write(0, 1, 'text')

        for i, (key, text) in enumerate(ll):
            worksheet.write(i + 1, 0, key)
            worksheet.write(i + 1, 1, text)
        workbook.save('test.xls')
        
        print(ll)
        pass

        
    with open('test2.json', 'w') as f:
        workbook = xlrd.open_workbook('test.xls')
        worksheet = workbook.sheet_by_name('Sheet1')
        ll = []
        for i in range(1, worksheet.nrows):
            ll.append((worksheet.cell_value(i, 0), worksheet.cell_value(i, 1)))
        jsonObj = Text2JSON(ll)
        json.dump(jsonObj, f, indent=4)
    pass

main()