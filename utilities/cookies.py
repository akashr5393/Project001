import pickle
import os

class CookieManager:
    def __init__(self, driver, path="cookies.pkl"):
        self.driver = driver
        self.path = path

    def save_cookies(self):
        with open(self.path, "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)

    def load_cookies(self, url):
        self.driver.get(url)  # Required before adding cookies
        if os.path.exists(self.path):
            with open(self.path, "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
