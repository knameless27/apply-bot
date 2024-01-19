from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import time

class Apply:
    def start(self, driver):  # Add 'self' as the first parameter
        applyButton = None

        def checkingErrors():
            try:
                driver.find_element(By.CLASS_NAME, "artdeco-inline-feedback--error")
                pyautogui.alert("Check all the questions and then click Ok!")
            except NoSuchElementException:
                print("Can't found errors in form...")

        def nextOffer():
            pyautogui.scroll(-120)
            pyautogui.click()
            time.sleep(5)
            self.start(driver)  # Use 'self.start' to call the instance method

        def exitingModal():
            time.sleep(5)
            pyautogui.moveTo(543, 352, 1)
            pyautogui.click()
            time.sleep(5)
            nextOffer()

        def jumpingModal():
            checkingErrors()
            try:
                driver.find_element(By.CLASS_NAME, "jpac-modal-header")
                exitingModal()
            except NoSuchElementException:
                print("Application finished")

            try:
                time.sleep(3)
                driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click()
                time.sleep(2)
                jumpingModal()
            except NoSuchElementException:
                print("exiting modal")
                exitingModal()
            exitingModal()

        try:
            applyButton = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        except NoSuchElementException:
            nextOffer()

        try:
            driver.find_element(By.CLASS_NAME, "artdeco-button__icon--in-bug")
            applyButton.click()
            time.sleep(2)
            jumpingModal()
        except NoSuchElementException:
            nextOffer()
