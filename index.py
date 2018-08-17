

import Read_Excel as RE
import APIs.index as API

def run():
    mpns = RE.getData('C:/Users/sb/Desktop/PycharmProjects/gmpn.xlsx');

    API.runAllApis(mpns)

run()
