import unittest


from MRTD import decode, encode, mismatch

class TestMRTD(unittest.TestCase):
    
    
    def testMRTD1(self): 
        record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
        self.assertEqual(decode(record),{'line1': {'issuing_country': 'CIV', 'last_name': 'LYNN', 'given_name': 'NEVEAH BRAM'}, 'line2': {'passport_number': 'W620126G5', 'country_code': 'CIV', 'birth_date': '591010', 'sex': 
'F', 'expiration_date': '970730', 'personal_number': 'AJ010215I'}},"Test 1")

    def testMRTD2(self): 
        record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
        self.assertEqual(mismatch(record),"Check digits have matched","Test 2")

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









if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

