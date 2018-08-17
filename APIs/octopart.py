

## read from octopart

from pyoctopart.octopart import Octopart
import time

OCTOPART_API_KEY = "7af92444"

def run(mpnArr):
    # prepare data for pyoctopart library
    octopartApi = Octopart(apikey=OCTOPART_API_KEY)
    i:int = 0
    for mpn in mpnArr:
        output = octopartApi.parts_match([{
            "mpn": mpn,
            "reference":  "line" + i.__str__(),
        }])
        print(output)
        i = i + 1
        if  (( i % 25) == 24):
            time.sleep(60)

            # prepare data for pyoctopart library
    #query = []
    #i: int = 0
    #for mpn in mpnArr:
    #    query += [{
    #        "mpn": mpn,
    #        "reference": "line" + i.__str__(),
    #    }]
    #    i = i + 1
    #octopartApi = Octopart(apikey=OCTOPART_API_KEY)
    ## test(octopartApi.parts_search(TEST_MPN))
    #output = octopartApi.parts_match(queries=query)
    #print(output)