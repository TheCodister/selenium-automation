# Level 1
# TC-001

import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # Correct import of By

csv_file = 'credential.csv'

test_data = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

# TC-001-001
print("TC-001-001: Access courses on list of category page")
for data in test_data:
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://school.moodledemo.net/login/index.php")
        time.sleep(2)

        # Login as student
        driver.find_element(By.ID, "username").send_keys(data['username'])
        driver.find_element(By.ID, "password").send_keys(data['password'])
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        # Check if Dropdown menu exists (indicating successful login)
        driver.find_element(By.XPATH, '//div[contains(@class, "dropdown")]').click()

        # Check if logout button exists (indicating successful login)
        # driver.find_element_by_id("logoutbtn")

        # Find home tab in navigation bar
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        print("Dashboard clicked")
        time.sleep(2)

        # Dropdown
        dropdown_element = driver.find_element(By.CSS_SELECTOR, '.dropdown > .btn-outline-secondary').click()
        print("Dropdown clicked")
        time.sleep(2)

        # Go to courses
        driver.find_element(By.LINK_TEXT, "All").click()
        print("All clicked")
        time.sleep(2)

        dropdown_element = driver.find_element(By.CSS_SELECTOR, '.btn-group > .btn').click()
        print("Second dropdown clicked")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Sort by dates").click()
        print("Sort by dates clicked")
        time.sleep(2)

        print("TC-002-001 Passed")
    except Exception as e:
        print(f"Error: {e}")

    driver.close()

# END
