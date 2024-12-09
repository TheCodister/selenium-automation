import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# File containing dropdown test data
csv_file = 'datafile002.csv'

# Load dropdown data
dropdown_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dropdown_data.append(row)

# TC-002: Test dropdown selections dynamically
print("TC-002: Test dropdown selections dynamically")
test_case_number = 1

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://school.moodledemo.net/login/index.php")
    time.sleep(2)

    # Login to the system (use valid credentials here)
    driver.find_element(By.ID, "username").send_keys("student")  # Replace with your data
    driver.find_element(By.ID, "password").send_keys("moodle2024")  # Replace with your data
    driver.find_element(By.ID, "loginbtn").click()
    time.sleep(2)

    # Navigate to the Dashboard
    driver.find_element(By.LINK_TEXT, "Dashboard").click()
    print("Dashboard clicked")
    time.sleep(2)

    for data in dropdown_data:
        try:
            # Generate dynamic test case ID
            test_case_id = f"TC-002-{test_case_number:03}"
            print(f"Running {test_case_id}")

            # First dropdown selection
            first_dropdown_option = data['first_dropdown']

            dropdown_element = driver.find_element(By.CSS_SELECTOR, '.dropdown > .btn-outline-secondary').click()
            print("Dropdown clicked")
            time.sleep(2)

            driver.find_element(By.LINK_TEXT, first_dropdown_option).click()
            print(f"{test_case_id}: First dropdown option selected: {first_dropdown_option}")
            time.sleep(2)

            # Second dropdown selection
            second_dropdown_option = data['second_dropdown']

            dropdown_element = driver.find_element(By.CSS_SELECTOR, '.btn-group > .btn').click()
            print("Second dropdown clicked")
            time.sleep(2)

            driver.find_element(By.LINK_TEXT, second_dropdown_option).click()
            print(f"{test_case_id}: Second dropdown option selected: {second_dropdown_option}")
            time.sleep(2)

            # Mark test case as passed
            print(f"{test_case_id} Passed")
            test_case_number += 1

        except Exception as e:
            print(f"{test_case_id} Failed: {e}")
            test_case_number += 1

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.close()
    print("All test cases completed.")
