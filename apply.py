from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import keyboard
import time
import os

env_path = "./.env"
ex_path = "./.env.example"

env = {}


def makeApplications():
    global env_path
    global ex_path
    global env

    def getVariables(content):
        for line_number, line in enumerate(content, start=1):
            stripped_line = line.strip()
            if "=" in stripped_line:
                name, value = stripped_line.split("=", 1)
                env[name] = value
            else:
                print(
                    f"Error en la línea {line_number}: '{line.strip()}' no contiene un '=' o tiene un formato incorrecto."
                )
        return env

    if os.path.exists(env_path):
        with open(env_path, "r") as file:
            content = file.readlines()
            getVariables(content)
    else:
        with open(ex_path, "r") as file_example:
            ex_content = file_example.read()
            with open(env_path, "w") as env_file:
                env_file.write(ex_content)

        with open(env_path, "r") as env_file:
            content = env_file.readlines()
            getVariables(content)

    driver = webdriver.Chrome()

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

    time.sleep(5)

    driver.get("https://www.linkedin.com/jobs")

    time.sleep(3)

    appInput = driver.find_element(
        By.CLASS_NAME, "jobs-search-box__keyboard-text-input"
    )

    appInput.send_keys(env["POSITION"])
    time.sleep(2)
    keyboard.press("enter")
    time.sleep(5)

    jobList = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")

    actions = ActionChains(driver)
    
    scrollOrigin = ScrollOrigin.from_element(jobList, 0, -50)

    actions.scroll_from_origin(scrollOrigin, 0, 10000).perform()

    jobs = jobList.find_elements(By.XPATH, "*")

    ezApply = driver.find_element(By.CLASS_NAME, "job-card-list__icon")
    print(ezApply)
    # for job in jobs:
    #     if ezApply:
    #         print(job)

    time.sleep(100)


makeApplications()
