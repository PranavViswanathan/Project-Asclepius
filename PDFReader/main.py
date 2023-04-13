
from tabula.io import read_pdf
import re
try:
    file = "sampleInsurance23.pdf"
    tables = read_pdf(file, pages = 1)
    try:
        df = tables[0]
        dictDf = df.to_dict('split')
        entries = dictDf['data']
        finalDict = dict()
        for entryPair in entries:
            finalDict[entryPair[0]] = entryPair[1]
        for key in finalDict.keys():
            print(key, "  :  ", finalDict[key])
    except:
        print("No Tables Found")
except:
    print("Invalid File")