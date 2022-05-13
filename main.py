from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("headless")
driver1 = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(options=chrome_options)

start_id = 9360358
counter = 0

isFound = False

INCREMENT = 45_000


def get_link(id):
    return f"https://events.webinar.ru/3865279/9049787/record-new/{id}"


# -------------------- x + 45k                                      --------------- x
try:
    while True:
        # print(f"{start_id=}")
        counter += 1
        lower_id = start_id - counter

        # print(f"{lower_id=}")
        url = get_link(lower_id)

        driver.get(url=url)
        time.sleep(2)
        if "Схемотехника электронных устройств. Тепляков А.П." in driver.title:
            print(driver.title)
            print(url)
            print()
            start_id = start_id + INCREMENT
            counter = 0
            continue

        higher_id = start_id + counter
        # print(f"{higher_id=}")
        url = get_link(higher_id)

        driver.get(url=url)
        time.sleep(2)
        if "Схемотехника электронных устройств. Тепляков А.П." in driver.title:
            print(driver.title)
            print(url)
            print()
            start_id = start_id + INCREMENT
            counter = 0
            continue

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
