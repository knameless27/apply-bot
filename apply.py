from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import keyboard
import json
import time
import os

env_path = "./env.json"
ex_path = "./env.example.json"

env = {}


def applyFunct(driver):
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
        applyFunct(driver)

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
        # jpac-modal-header

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

def makeApplications():
    global env_path
    global ex_path
    global env

    if os.path.exists(env_path):
        with open(env_path, "r") as file:
            env = json.load(file)
    else:
        with open(ex_path, "r") as file_example:
            ex_content = json.load(file_example)
            with open(env_path, "w") as env_file:
                json.dump(ex_content, env_file)

        with open(env_path, "r") as env_file:
            env = json.load(env_file)

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.linkedin.com/")

    time.sleep(3)

    emailInput = driver.find_element("name", "session_key")
    pwdInput = driver.find_element("name", "session_password")
    submitBtn = driver.find_element(
        By.CLASS_NAME, "sign-in-form__submit-btn--full-width"
    )

    emailInput.send_keys(env["EMAIL"])
    pwdInput.send_keys(env["PASSWORD"])

    time.sleep(2)

    submitBtn.click()

    time.sleep(2)

    try:
        driver.find_element(By.CLASS_NAME, "nav__button__muted--signin")
        pyautogui.alert("Check all the verify section and then click Ok!")
    except NoSuchElementException:
        print("Verify page not found! :D")

    driver.get("https://www.linkedin.com/jobs")

    time.sleep(3)

    appInput = driver.find_element(
        By.CLASS_NAME, "jobs-search-box__keyboard-text-input"
    )

    appInput.send_keys(env["POSITION"])
    time.sleep(2)
    keyboard.press("enter")
    time.sleep(5)

    pyautogui.moveTo(593, 352, 1)

    pyautogui.click()

    applyFunct(driver)

    time.sleep(100)


makeApplications()
