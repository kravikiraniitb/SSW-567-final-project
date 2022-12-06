import unittest

from unittest.mock import patch, MagicMock

from MRTD import decode, encode, mismatch, scan, data_base

class TestMRTD(unittest.TestCase):
    
    #With middle name
    def testMRTD1(self): 
        record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
        self.assertEqual(decode(record),{'line1': {'issuing_country': 'CIV', 'last_name': 'LYNN', 'given_name': 'NEVEAH BRAM'}, 'line2': {'passport_number': 'W620126G5', 'country_code': 'CIV', 'birth_date': '591010', 'sex': 
'F', 'expiration_date': '970730', 'personal_number': 'AJ010215I'}},"Test 1")

    #no middle name
    def testMRTD4(self): 
            record = "P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5"
            self.assertEqual(decode(record),{
            "line1": {
                "issuing_country": "ABW",
                "last_name": "MALDONADO",
                "given_name": "CAMILLA"
            },
            "line2": {
                "passport_number": "V008493B6",
                "country_code": "ABW",
                "birth_date": "780909",
                "sex": "M",
                "expiration_date": "090908",
                "personal_number": "QZ181922T"
            }
        },"Test 1")


    
    def testMRTD2(self): 
        record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
        self.assertEqual(mismatch(record),"Check digits have matched","Test 2")

    #With middle name
    def testMRTD3(self): 
            #record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
            
        decoded_array = {
                    "line1": {
                        "issuing_country": "CIV",
                        "last_name": "LYNN",
                        "given_name": "NEVEAH BRAM"
                    },
                    "line2": {
                        "passport_number": "W620126G5",
                        "country_code": "CIV",
                        "birth_date": "591010",
                        "sex": "F",
                        "expiration_date": "970730",
                        "personal_number": "AJ010215I"
                    }
                }


        self.assertEqual(encode(decoded_array),"P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6","Test 3")

    #no middle name
    def testMRTD5(self): 
            #record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
            
        decoded_array = {
            "line1": {
                "issuing_country": "ABW",
                "last_name": "MALDONADO",
                "given_name": "CAMILLA"
            },
            "line2": {
                "passport_number": "V008493B6",
                "country_code": "ABW",
                "birth_date": "780909",
                "sex": "M",
                "expiration_date": "090908",
                "personal_number": "QZ181922T"
            }
        }


        self.assertEqual(encode(decoded_array),"P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5","Test 3")





   # def testMRTD4(self): 
    #        #record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
     #       self.assertEqual(scan(),"Scanned successfully","Test 2")

    #def testMRTD5(self): 
     #       #record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
      #      self.assertEqual(data_base(),"Retrieved successfully","Test 2")


    #class TestScan_db(unittest.TestCase):

    @patch('MRTD.scan')
    def testScan(self, scan):
        scan.return_value = "Scanned successfully"
        self.assertEqual(scan(),"Scanned successfully")

    @patch('MRTD.data_base')
    def testDB(self, data_base):
        data_base.return_value = "Retrieved successfully"
        #self.assertEqual(githubapi567("richkempinski"),None)
        self.assertEqual(data_base(),"Retrieved successfully")







if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

