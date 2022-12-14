import unittest
import time

#from unittest.mock import patch, MagicMock

from Part3PerfTesting import encode_measure, decode_measure, mismatch_measure

class TestMRTD(unittest.TestCase):
    def testPerf1(self): 
        t1 = time.time()
        self.assertEqual(mismatch_measure(),None)
        t2 = time.time()
        diff = (t2-t1)*1000
        print("The processing time taken with unit tests: "+str(diff))

# only one test case above as we only had to change the function name above to get the result for each criteria (Encode, decode, mismatch)



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

