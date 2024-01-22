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
            try:
                scrollable_element = driver.find_element(
                    By.CLASS_NAME, "jobs-search-results-list"
                )
                scroll_height = driver.execute_script(
                    "return arguments[0].scrollHeight;", scrollable_element
                )

                # Obtener la posición actual del desplazamiento vertical
                scroll_position = driver.execute_script(
                    "return arguments[0].scrollTop + arguments[0].clientHeight;",
                    scrollable_element,
                )
            except NoSuchElementException:
                scroll_height = 0
                scroll_position = 0

            if scroll_height != scroll_position:
                pyautogui.scroll(-120)
                pyautogui.click()
                time.sleep(5)
            else:
                current_page = driver.find_element(
                    By.CLASS_NAME,
                    "active",
                )
                next_page_button = current_page.find_element(
                    By.XPATH,
                    "./following-sibling::li[@class='artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view']",
                )
                next_page_button.click()

            self.start(driver)  # Use 'self.start' to call the instance method

        def exitingModal():
            time.sleep(5)
            pyautogui.moveTo(543, 362, 1)
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
