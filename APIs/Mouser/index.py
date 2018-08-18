
import requests
import xml.etree.ElementTree as ET


MOUSER_API_KEY = "4085d175-210d-45a0-aaf1-a2cd1a11a2c8"

def run(mpnArr):
    makeRequest(mpnArr[0])
    return

def makeRequest(mpn):
    headers = {
        'Host': 'api.mouser.com',
        'Content-Type': 'application/soap+xml; charset=utf-8',
    }
    response = requests.post("http://api.mouser.com/service/searchapi.asmx", data=buildBody(mpn), headers=headers)
    print(response)
    #root = ET.fromstring(xml)
    return


def buildBody(mpn):
    return (
        '<?xml version="1.0" encoding="utf-8"?>' +
        '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">' +
            '<soap12:Header>' +
                getPartnerInfo() +
            '</soap12:Header>' +
            '<soap12:Body>' +
                getSearchByPartNumber(mpn) +
            '</soap12:Body>' +
        '</soap12:Envelope>'
    )

def getPartnerInfo():
    return (
        '<MouserHeader xmlns="http://api.mouser.com/service">' +
            '<AccountInfo>' +
                '<PartnerID>' + MOUSER_API_KEY + '</PartnerID>' +
            '</AccountInfo>' +
        '</MouserHeader>'
    )

def getSearchByPartNumber(mpn):
    return (
        '<SearchByPartNumber xmlns="http://api.mouser.com/service">' +
            '<mouserPartNumber>' + mpn + '</mouserPartNumber>' +
            '<partSearchOptions>1</partSearchOptions>' +
        '</SearchByPartNumber>'
    )

def getSearchByKeyword(searchKeyword):
    return (
        '<SearchByKeyword xmlns="http://api.mouser.com/service">' +
            '<keyword>searchKeyword</keyword>' +
            '<records>50</records>' +
            '<startingRecord>1</startingRecord>' +
            '<searchOptions>1</searchOptions>' +
        '</SearchByKeyword>'
    )



#def GetPartsForMouserPartNumberAndCountry(mpn):
#    return (
#        '<?xml version="1.0" encoding="utf-8"?>' +
#        '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">' +
#            '<soap12:Body>' +
#                '<GetPartsForMouserPartNumberAndCountry xmlns="http://api.mouser.com/service">' +
#                    '<internalKey>' + MOUSER_API_KEY + '</internalKey>' +
#                    '<mouserPartNumbers>' + mpn + '</mouserPartNumbers>' +
#                    #'<delimiter></delimiter>' +
#                    '<countryCode>NL</countryCode>' +
#                    #'<currencyCode>EUR</currencyCode>' +
#                '</GetPartsForMouserPartNumberAndCountry>' +
#            '</soap12:Body>' +
#        '</soap12:Envelope>'
#    )
