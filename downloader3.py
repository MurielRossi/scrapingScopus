from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

options = webdriver.ChromeOptions()
options.add_extension('./scopus-ext.crx')

browser = webdriver.Chrome("./chromedriver", options=options)


browser.get(
    "https://www.scopus.com/search/form.uri?display=basic#basic"
)


def execute():

    open_scopus()
    login()
    go_to_page("https://www.scopus.com/search/form.uri?zone=TopNavBar&origin=searchbasic&display=basic#basic")

    csv = pd.read_csv("acceptedInstance3.csv")
    colonna = csv["TITLE"]

    for x in colonna:
        print(x)
        search(x)
        try:
            download()
        except TimeoutException as ex:
            print("failed")
        go_to_page("https://www.scopus.com/search/form.uri?display=basic#basic")
        time.sleep(5)

        reset_query = browser.find_element(By.CLASS_NAME, "reset-button")
        reset_query.click()



def open_scopus():
    browser.get(
        "https://www.scopus.com/search/form.uri?display=basic#basic"
    )

    time.sleep(5)
    print(browser.title)


def login():
    email_field = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID, "bdd-email")))
    email_field.send_keys("my-email")
    continue_button = browser.find_element(By.ID, "bdd-elsPrimaryBtn")
    continue_button.click()
    pass_field = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.ID, "bdd-password")))
    pass_field.send_keys("my-password")
    login_button = browser.find_element(By.ID, "bdd-elsPrimaryBtn")
    login_button.click()


def go_to_page(url):
    browser.get(url)
    time.sleep(5)


def search(x):
    casella_ricerca = browser.find_element(
        By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/micro-ui/scopus-homepage/div/div/els-tab/els-tab-panel[1]/div/form/div[1]/div/div[2]/els-input/div/label/input")
    casella_ricerca.send_keys(x)
    bottone_submit = browser.find_element(
        By.CLASS_NAME, "DocumentSearchForm-module__7qtE8")
    bottone_submit.click()


def download():
    element_download_href = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ddmDocTitle")))
    element_download_href.click()
    time.sleep(5)
    element_download = browser.find_element(
        By.ID, "ddmDownloadButton")
    element_download.click()


try:
    print("ciao")
    execute()
finally:
    time.sleep(5)
    browser.quit()
