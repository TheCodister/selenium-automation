import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# File containing only test data
csv_file = 'datafile001.csv'

# Load test data
test_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print("Level 1: Data-Driven Automation")

for i, data in enumerate(test_data, start=1):
    test_case_id = f"TC-001-{i:03}"
    try:
        # Start WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://school.moodledemo.net/login/index.php")
        time.sleep(2)

        # Login (credentials from CSV)
        driver.find_element(By.ID, "username").send_keys(data['username'])
        driver.find_element(By.ID, "password").send_keys(data['password'])
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        # Click Dashboard
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(2)

        # Perform a hardcoded action (e.g., click a dropdown and select an option)
        driver.find_element(By.CSS_SELECTOR, '.dropdown > .btn-outline-secondary').click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "All").click()
        time.sleep(1)

        # Verify result (hardcoded selector)
        result_text = driver.find_element(By.LINK_TEXT, "Attempt quiz now").text
        expected_result = data['expected_result']

        if result_text == expected_result:
            print(f"{test_case_id}: Passed")
        else:
            print(f"{test_case_id}: Failed - Expected: {expected_result}, Found: {result_text}")

    except Exception as e:
        print(f"{test_case_id}: Failed - Error: {e}")

    finally:
        driver.close()

print("All test cases completed.")
