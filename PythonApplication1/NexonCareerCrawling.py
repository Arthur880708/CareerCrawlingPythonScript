import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class NexonCareerCrawling:
    def StartCrawling(self):
        # Initialize the Selenium webdriver
        driver = webdriver.Chrome()

        # The base URL of the job listing page on Nexon careers website
        base_url = "https://career.nexon.com/user/recruit/member/postList"

        # The parameters for filtering the job listings by job category "Design"
        params = {
            "joinCorp": "NX",           # NX - Nexon 본사
            "jobGroupCd": "5",          # 5 - 게임개발
            "reSubj": ""                # 검색어가 있을경우 여기 입력
        }

        # Navigate to the base URL with the job category parameters
        driver.get(base_url + "?" + "&".join([f"{k}={v}" for k, v in params.items()]))

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.content, "html.parser")
        last_page_link = soup.find("a", {"class": "last"})
        if last_page_link:
            num_pages = int(last_page_link["href"].split("(")[-1].split(")")[0])
        else:
            num_pages = int(soup.find("span", {"class": "num"}).text.strip().split("\n")[-1])

        driver.implicitly_wait(10)

        # Loop through all pages and extract the dt elements
        for page in range(1, num_pages + 1):
            # Parse the HTML content of the response using BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # Find all the wrapPostGroup divs
            wrap_post_groups = soup.find_all("div", {"class": "wrapPostGroup"})

            # Loop through each wrapPostGroup div and extract the dt elements
            for wrap_post_group in wrap_post_groups:
                dt_elements = wrap_post_group.find_all("dt")
                for dt_element in dt_elements:
                    text = dt_element.text.strip()
                    print(text)

            print("-" * 50)

            try:

                # Wait for the "next page" button to appear
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "page.next"))
                )

                driver.execute_script("arguments[0].click();", next_button)
                driver.implicitly_wait(10)
            except NoSuchElementException:
                # Stop the loop if the "next page" button is not found
                break

        # Quit the Selenium webdriver
        driver.quit()