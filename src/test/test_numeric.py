# To be filled by students
# Set up relative paths
import os, sys, unittest
import pandas as pd
import numpy as np

if os.path.abspath('.') not in sys.path:
    sys.path.append(os.path.abspath('.'))

from src.numeric import NumericColumn

class TestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.df = pd.DataFrame({'Date': ["19/06/2019", "13/06/2019", "07/06/2019", "28/05/2019", "22/05/2019", "10/05/2019", "13/04/2019", "11/04/2019", "11/04/2019", "09/04/2019", "06/04/2019", "30/03/2019", "18/03/2019", "16/03/2019", "15/03/2019", "09/03/2019", "21/02/2019", "20/02/2019", "05/02/2019", "25/01/2019", "21/12/2018", "19/12/2018", "19/12/2018", "15/12/2018", "15/12/2018", "11/12/2018", "05/12/2018", "30/11/2018", "28/11/2018", "20/11/2018", "17/11/2018", "16/11/2018", "03/11/2018", "30/10/2018", "20/10/2018", "19/10/2018", "10/10/2018", "06/10/2018", "28/09/2018", "26/09/2018", "24/09/2018", "22/09/2018", "22/09/2018", "17/09/2018", "13/09/2018", "09/09/2018", "08/09/2018", "07/09/2018", "05/09/2018", "01/09/2018", "29/08/2018", "24/08/2018", "22/08/2018", "21/08/2018", "17/08/2018", "27/06/2018", "23/06/2018", "21/06/2018", "16/06/2018", "08/06/2018", "07/06/2018", "26/05/2018", "26/05/2018", "26/05/2018", "26/05/2018", "22/05/2018", "16/05/2018", "12/05/2018", "12/05/2018", "06/05/2018", "05/05/2018", "28/04/2018", "27/04/2018", "20/04/2018", "17/04/2018", "14/04/2018", "12/04/2018", "10/04/2018", "09/04/2018", "08/04/2018", "06/04/2018", "06/04/2018", "29/03/2018", "24/03/2018", "22/03/2018", "22/03/2018", "17/03/2018", "17/03/2018", "17/03/2018", "16/03/2018", "13/03/2018", "10/03/2018", "08/03/2018", "07/03/2018", "07/03/2018", "02/03/2018", "26/02/2018", "24/02/2018", "24/02/2018", "21/02/2018", "21/02/2018", "17/02/2018", "07/02/2018", "07/02/2018", "30/01/2018", "05/01/2018", "15/12/2017", "11/12/2017", "10/12/2017", "09/12/2017", "08/12/2017", "07/12/2017", "07/12/2017", "06/12/2017", "06/12/2017", "02/12/2017", "01/12/2017", "24/11/2017", "22/11/2017", "22/11/2017", "21/11/2017", "17/11/2017", "10/11/2017", "10/11/2017", "09/11/2017", "04/11/2017", "03/11/2017", "03/11/2017", "02/11/2017", "27/10/2017", "26/10/2017", "23/10/2017", "19/10/2017", "17/10/2017", "14/10/2017", "13/10/2017", "13/10/2017", "11/10/2017", "10/10/2017", "06/10/2017", "04/10/2017", "30/09/2017", "26/09/2017", "15/09/2017", "14/09/2017", "13/09/2017", "13/09/2017", "13/09/2017", "13/09/2017", "12/09/2017", "02/09/2017", "01/09/2017", "23/08/2017", "23/08/2017", "22/08/2017", "21/08/2017", "21/08/2017", "19/08/2017", "16/08/2017", "16/08/2017", "11/08/2017", "10/08/2017", "05/08/2017", "04/08/2017", "02/08/2017", "01/08/2017", "29/07/2017", "29/07/2017", "26/07/2017", "21/07/2017", "05/07/2017", "01/07/2017", "30/06/2017", "24/06/2017", "24/06/2017", "24/06/2017", "23/06/2017", "21/06/2017", "21/06/2017", "20/06/2017", "17/06/2017", "16/06/2017", "15/06/2017", "03/06/2017", "03/06/2017", "02/06/2017", "27/05/2017", "26/05/2017", "24/05/2017", "24/05/2017", "17/05/2017", "17/05/2017", "13/05/2017", "11/05/2017", "06/05/2017", "03/05/2017", "03/05/2017", "26/04/2017", "21/04/2017", "18/04/2017", "13/04/2017", "11/04/2017", "08/04/2017", "08/04/2017", "08/04/2017", "07/04/2017", "07/04/2017", "04/04/2017", "01/04/2017", "31/03/2017", "29/03/2017", "29/03/2017", "29/03/2017", "27/03/2017", "25/03/2017", "21/03/2017", "20/03/2017", "18/03/2017", "18/03/2017", "15/03/2017", "15/03/2017", "14/03/2017", "11/03/2017", "11/03/2017", "11/03/2017", "11/03/2017", "04/03/2017", "04/03/2017", "03/03/2017", "01/03/2017", "01/03/2017", "01/03/2017", "28/02/2017", "13/02/2017", "10/02/2017", "08/02/2017", "08/02/2017", "02/02/2017", "28/01/2017", "25/01/2017", "23/01/2017", "31/12/2016", "17/12/2016", "17/12/2016", "17/12/2016", "17/12/2016", "10/12/2016", "08/12/2016", "08/12/2016", "26/11/2016", "18/11/2016", "17/11/2016", "16/11/2016", "11/11/2016", "11/11/2016", "07/11/2016", "07/11/2016", "29/10/2016", "26/10/2016", "26/10/2016", "21/10/2016", "19/10/2016", "19/10/2016", "18/10/2016", "13/10/2016", "13/10/2016", "13/10/2016", "12/10/2016", "12/10/2016", "12/10/2016", "10/10/2016", "07/10/2016", "01/10/2016", "27/09/2016", "26/09/2016", "26/09/2016", "21/09/2016", "21/09/2016", "14/09/2016", "14/09/2016", "13/09/2016", "10/09/2016", "10/09/2016", "05/09/2016", "03/09/2016", "28/08/2016", "27/08/2016", "27/08/2016", "26/08/2016", "17/08/2016", "13/08/2016", "12/08/2016", "16/07/2016", "12/07/2016", "05/07/2016", "02/07/2016", "21/06/2016", "21/06/2016", "20/06/2016", "09/06/2016"],
                        'Id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300],
                        'suburb': ["Avalon Beach", np.nan, "", "Avalon Beach", "Whale Beach", "Bilgola Plateau", np.nan, "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Whale Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Clareville", "Bilgola Plateau", "Avalon Beach", "Whale Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Whale Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Clareville", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Beach", "Bilgola Plateau", "Bilgola Beach", "Avalon Beach", "Whale Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Bilgola Plateau", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", "Avalon Beach", ""],
                        'postalCode': ["2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", "2107", ""],
                        'bed': [4, 4, 3, np.nan, 5, 4, 3, 5, -1, -2, 0, 6, 4, 4, 4, 5, 4, 3, 3, 4, 0, 4, 4, 3, 3, 3, 5, 4, 3, 3, 4, 5, 6, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 4, 4, 4, 6, 3, 3, 4, 3, 5, 3, 3, 5, 4, 4, 5, 5, 6, 5, 3, 5, 6, 5, 3, 3, 4, 4, 4, 4, 4, 5, 3, 4, 5, 3, 3, 3, 4, 4, 4, 4, 3, 5, 3, 3, 4, 3, 4, 5, 3, 3, 4, 3, 4, 4, 4, 3, 4, 2, 4, 4, 3, 4, 4, 4, 5, 4, 4, 2, 4, 3, 5, 3, 3, 4, 3, 6, 3, 4, 3, 4, 4, 4, 2, 5, 3, 4, 4, 4, 5, 4, 5, 3, 3, 4, 5, 3, 3, 4, 6, 7, 3, 3, 3, 3, 3, 4, 4, 4, 2, 4, 5, 2, 6, 4, 4, 4, 4, 3, 3, 4, 4, 5, 6, 4, 3, 5, 5, 5, 5, 2, 4, 3, 4, 3, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 4, 3, 4, 3, 4, 4, 4, 3, 4, 3, 3, 5, 4, 4, 5, 3, 4, 5, 4, 5, 2, 5, 4, 5, 3, 4, 4, 3, 4, 2, 2, 4, 4, 6, 3, 3, 4, 3, 4, 3, 4, 4, 4, 5, 4, 4, 4, 5, 5, 2, 5, 3, 2, 4, 3, 4, 5, 3, 5, 5, 3, 3, 4, 4, 5, 3, 4, 2, 4, 4, 5, 3, 3, 3, 4, 3, 3, 3, 3, 4, 4, 4, 3, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 2, 4, 4, 3, 4, 3, 4, 5, 3, 3, 4, 4, 5, 3, 3, 2],
                        'propType': ["HOUSE", " ", "1232", "53", " ", "", "house", "house", " ", "house", "", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "duplex/semi-detached", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "duplex/semi-detached", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "townhouse", "townhouse", "townhouse", "house", "house", "townhouse", "house", "house", "townhouse", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", "house", ""]})

    def tearDown(self):
        print('tearDown\n')

    def test_unique(self):
        print('test_unique')
        numeric_stats = NumericColumn('bed', self.df)

        unique_values = numeric_stats.get_unique()
        expected_unique_values = 10

        self.assertEqual(unique_values, expected_unique_values)


    def test_missing(self):
        print('test_missing')
        numeric_stats = NumericColumn('bed', self.df)
        
        missing_values = numeric_stats.get_missing()
        expected_missing_values = 1

        self.assertEqual(missing_values, expected_missing_values)
    
    def test_zeros(self):
        print('test_zeros')
        numeric_stats = NumericColumn('bed', self.df)

        zero_values = numeric_stats.get_zeros()
        expected_zero_values = 2

        self.assertEqual(zero_values, expected_zero_values)

    def test_negatives(self):
        print('test_negatives')
        numeric_stats = NumericColumn('bed', self.df)

        negative_values = numeric_stats.get_negatives()
        expected_negative_values = 2

        self.assertEqual(negative_values, expected_negative_values)

        
    def test_mean(self):
        print('test_mean')
        numeric_stats = NumericColumn('bed', self.df)

        average = numeric_stats.get_mean() 
        expected_average = 3.762541806020067

        self.assertEqual(average, expected_average)


    def test_std(self):
        print('test_std')
        numeric_stats = NumericColumn('bed', self.df)

        std = numeric_stats.get_std()
        expected_std = 1.0429380096814662

        self.assertEqual(std, expected_std)
        
    def test_min(self):
        print('test_min')
        numeric_stats = NumericColumn('bed', self.df)

        min = numeric_stats.get_min()
        expected_min = -2

        self.assertEqual(min, expected_min)
        

    def test_max(self):
        print('test_max')
        numeric_stats = NumericColumn('bed', self.df)

        max = numeric_stats.get_max()
        expected_max = 7

        self.assertEqual(max, expected_max)

    def test_median(self):
        print('test_median')
        numeric_stats = NumericColumn('bed', self.df)

        median = numeric_stats.get_median()
        expected_median = 4

        self.assertEqual(median, expected_median)
    
    # def test_histogram(self):
    #     print('test_histogram')

    def test_freq(self):
        numeric_stats = NumericColumn('propType', self.df)

        frequency_table = numeric_stats.get_frequent()

        # check if the result generate by get_frequent match expected result
        self.assertEqual(279, frequency_table.occurrence[frequency_table.value == 'house'].values[0])
        self.assertEqual(0.93, round(frequency_table.percentage[frequency_table.value == 'house'].values[0], 2))

    def test_table(self):
        numeric_stats = NumericColumn('bed', self.df)
        table = numeric_stats.construct_table()

        # check if the shape of the table generate by construct_table match is as expected
        self.assertEqual(9, table.shape[0])
        self.assertEqual(1, table.shape[1])

        self.assertEqual(table.value[table.index == 'number of unique values'].values[0], '10.0')
        self.assertEqual(table.value[table.index == 'number of missing values'].values[0], '1.0')
        self.assertEqual(table.value[table.index == 'number of rows with zero values'].values[0], '2.0')
        self.assertEqual(table.value[table.index == 'number of rows with negative values'].values[0], '2.0')
        self.assertEqual(table.value[table.index == 'Average'].values[0], '3.762541806020067')
        self.assertEqual(table.value[table.index == 'Standard Deviation'].values[0], '1.0429380096814662')
        self.assertEqual(table.value[table.index == 'Minimum'].values[0], '-2.0')
        self.assertEqual(table.value[table.index == 'Maximum'].values[0], '7.0')
        self.assertEqual(table.value[table.index == 'Median'].values[0], '4.0')

if __name__ == '__main__':
    unittest.main()