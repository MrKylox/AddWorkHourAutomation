import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from userAccount import log_in
import os

class workTime():
    
    def __init__(self):
        account = log_in()
        self.username = account.get_user()
        self.password = account.get_pass()
        self.brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.chrome_driver_path = "C:/chromedriver/chromedriver-win64/chromedriver.exe"
        self.options = Options()
        self.options.binary_location = self.brave_path
        self.driver = None

    def _getBravePath(self):
        return self.brave_path
    
    def _getChromePath(self):
        return self.chrome_driver_path

    def _initialize_webdriver(self):
        self.driver = webdriver.Chrome(service=Service(self.chrome_driver_path), options=self.options)

    def addWorkHours(self):
        print("Testing")
        if not os.path.isfile(self._getBravePath()):
            raise FileNotFoundError(f"Brave browser executable not found at {self._getBravePath()}")

        if not os.path.isfile(self._getChromePath()):
            raise FileNotFoundError(f"ChromeDriver executable not found at {self._getChromePath()}")

        try:
            print("Initializing WebDriver with Brave browser...")
            self._initialize_webdriver()
            print("WebDriver initialized.")
            
            print("Opening E-services...")
            self.driver.get("https://web.mnsu.edu/eservices/")
            print("E-services opened.")
            
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "starid"))
            )
            password_field = self.driver.find_element(By.ID, "pinnbr")

            username_field.send_keys(self.username)
            password_field.send_keys(self.password)

            submit_btn = self.driver.find_element(By.XPATH, '//input[@type="submit" and @value="Log in"]')
            submit_btn.click()
            print("Pressed the Submit Button")

            accept_tuition_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "accept_tuition"))
            )
            accept_tuition_checkbox.click()
            print("Clicked accept_tuition checkbox.")

            understand_drop_checkbox = self.driver.find_element(By.ID, "understand_drop")
            understand_drop_checkbox.click()
            print("Clicked understand_drop checkbox.")

            submit_button = self.driver.find_element(By.NAME, "emquery")
            submit_button.click()
            print("Clicked the 'Continue' submit button.")

            student_employment_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Student Employment')]"))
            )
            student_employment_link.click()
            print("Clicked the 'Student Employment' link.")

            enter_time_worked_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@title='Enter Time Worked.']"))
            )
            enter_time_worked_link.click()
            print("Clicked the 'Enter Time Worked' link.")

            with open('InputData.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    date = row['date']
                    start_time = row['startTime']
                    end_time = row['endTime']

                    add_hour = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "addTime"))
                    )
                    add_hour.click()

                    select_date = Select(self.driver.find_element(By.ID, 'date'))
                    select_date.select_by_value(date)

                    select_start_time = Select(self.driver.find_element(By.ID, 'startTime'))
                    select_start_time.select_by_value(start_time)

                    select_end_time = Select(self.driver.find_element(By.ID, 'endTime'))
                    select_end_time.select_by_value(end_time)

                    add_time = self.driver.find_element(By.ID, "timeSaveOrAddId")
                    add_time.click()
                    
                    self.driver.implicitly_wait(10)

            logout = self.driver.find_element(By.LINK_TEXT, "Logout")
            logout.click()
            input("Press Enter to quit...")  # Pause script execution
            print("End of script.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()

