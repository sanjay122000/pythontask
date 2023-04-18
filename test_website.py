import unittest
import requests

class TestWebsite(unittest.TestCase):
    def test_website_loads(self):
        url = "https://atg.world"
        response = requests.get(url)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        if status_code == 200:
            print(f"INFO: Successfully loaded {url}")
        else:
            print(f"ERROR: Failed to load {url}")

if __name__ == '__main__':
    unittest.main()


