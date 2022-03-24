import json
import xlwt
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

        jsonObj = Text2JSON(ll)
        with open('test2.json', 'w') as f:
            json.dump(jsonObj, f, indent=4)
    pass

main()