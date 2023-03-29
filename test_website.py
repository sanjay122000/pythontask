import unittest
import requests
class TestWebsite(unittest.TestCase):
def test_website_loads(self):
    response = requests.get("https://atg.world")
    self.assertEqual(response.status_code, 200)
def test_website_loads(self):
    try:
        response = requests.get("https://atg.world")
        self.assertEqual(response.status_code, 200)
    except Exception as e:
        print("Error:", e)
        self.fail("Website did not load properly")
if __name__ == '__main__':
    unittest.main()

