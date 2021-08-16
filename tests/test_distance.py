import unittest
from mlproject.distance import haversine

class TestDistanceMethods(unittest.TestCase):

    def test_type_return(self):
        lat1, lon1 = 48.865070, 2.380009
        #Insert your coordinates from google maps here
        lat2, lon2 = 52.52926912695634, 13.339730682682458
        hav_value = haversine(lon1, lat1, lon2, lat2)
        self.assertTrue(isinstance(hav_value, (int,float)),
        'Return value is not an int/float')

    def test_result_return(self):
        lat1, lon1 = 48.865070, 2.380009
        #Insert your coordinates from google maps here
        lat2, lon2 = 52.52926912695634, 13.339730682682458
        return self.assertEqual(round(haversine(lon1, lat1, lon2, lat2),2), 871.59)