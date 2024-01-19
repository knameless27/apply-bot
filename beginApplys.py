# begin_apply.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from apply import Apply
import pyautogui
import keyboard
import time

class BeginApply:
    def __init__(self):
        self.apply = Apply()

    def makeApplications(self, env):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://www.linkedin.com/")

        time.sleep(3)

        email_input = driver.find_element("name", "session_key")
        pwd_input = driver.find_element("name", "session_password")
        submit_btn = driver.find_element(
            By.CLASS_NAME, "sign-in-form__submit-btn--full-width"
        )

        email_input.send_keys(env["EMAIL"])
        pwd_input.send_keys(env["PASSWORD"])

        time.sleep(2)

        submit_btn.click()

        time.sleep(2)

        try:
            driver.find_element(By.CLASS_NAME, "nav__button__muted--signin")
            pyautogui.alert("Check all the verify section and then click Ok!")
        except NoSuchElementException:
            print("Verify page not found! :D")

        driver.get("https://www.linkedin.com/jobs")

        time.sleep(3)

        app_input = driver.find_element(
            By.CLASS_NAME, "jobs-search-box__keyboard-text-input"
        )

        app_input.send_keys(env["POSITIONS"][0])
        time.sleep(2)
        keyboard.press("enter")
        time.sleep(5)

        pyautogui.moveTo(593, 352, 1)

        pyautogui.click()

        self.apply.start(driver)

        pyautogui.alert("it's over!")
