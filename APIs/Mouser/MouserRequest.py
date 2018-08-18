
import requests


class MouserRequest:
    _apiKey = ''

    def __init__(self, apiKey):
        self._apiKey = apiKey

    def make_request(self, mpn):
        headers = {
            'Host': 'api.mouser.com',
            'Content-Type': 'application/soap+xml; charset=utf-8',
        }
        body = self.buildBody(mpn)
        response = requests.post("http://api.mouser.com/service/searchapi.asmx", data=body, headers=headers)
        return response


    def buildBody(self, mpn):
        return (
            '<?xml version="1.0" encoding="utf-8"?>' +
            '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">' +
                '<soap12:Header>' +
                    self.getPartnerInfo() +
                '</soap12:Header>' +
                '<soap12:Body>' +
                    self.getSearchByPartNumber(mpn) +
                '</soap12:Body>' +
            '</soap12:Envelope>'
        )

    def getPartnerInfo(self):
        return (
            '<MouserHeader xmlns="http://api.mouser.com/service">' +
                '<AccountInfo>' +
                    '<PartnerID>' + self._apiKey + '</PartnerID>' +
                '</AccountInfo>' +
            '</MouserHeader>'
        )

    def getSearchByPartNumber(self, mpn):
        return (
            '<SearchByPartNumber xmlns="http://api.mouser.com/service">' +
                '<mouserPartNumber>' + mpn + '</mouserPartNumber>' +
                '<partSearchOptions>1</partSearchOptions>' +
            '</SearchByPartNumber>'
        )

#def getSearchByKeyword(searchKeyword):
#    return (
#        '<SearchByKeyword xmlns="http://api.mouser.com/service">' +
#            '<keyword>searchKeyword</keyword>' +
#            '<records>50</records>' +
#            '<startingRecord>1</startingRecord>' +
#            '<searchOptions>1</searchOptions>' +
#        '</SearchByKeyword>'
#    )



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
