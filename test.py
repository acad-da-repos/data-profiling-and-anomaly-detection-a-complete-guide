
import unittest
import pandas as pd
import numpy as np
from assignment import profile_data, detect_anomalies

class TestDataProfilingAndAnomalyDetection(unittest.TestCase):
    def test_profile_data(self):
        data = {'A': [1, 2, 3, 1, np.nan], 'B': ['X', 'Y', 'X', 'Z', 'Y']}
        df = pd.DataFrame(data)
        profile = profile_data(df)

        self.assertIsInstance(profile, dict)
        self.assertEqual(profile['A']['unique_values'], 3)
        self.assertEqual(profile['A']['missing_values'], 1)
        self.assertEqual(profile['B']['unique_values'], 3)
        self.assertEqual(profile['B']['missing_values'], 0)

    def test_detect_anomalies(self):
        data = {'Value': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]}
        df = pd.DataFrame(data)
        anomalies = detect_anomalies(df, 'Value')

        self.assertIsInstance(anomalies, pd.Series)
        self.assertTrue(anomalies.iloc[10]) # 100 should be an anomaly
        self.assertFalse(anomalies.iloc[0]) # 0 should not be an anomaly

if __name__ == '__main__':
    unittest.main()
