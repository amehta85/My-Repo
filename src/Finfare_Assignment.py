import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Test Data
test_data = {"NFLX", "MSFT", "TSLA", "GOOGL", "AMZN", "AAPL"}

def main():
    # Initialize the Chrome browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # 1. Opens webpage www.google.com/finance on a chrome browser
        driver.get("https://www.google.com/finance")

        # 2. Verifies the page is loaded by asserting the page title
        assert "Google Finance" in driver.title, f"Expected 'Google Finance' in title but got {driver.title}"

        # 3. Retrieves the stock symbols listed
        time.sleep(5)  # Wait for the page to load completely
        stock_elements = driver.find_elements(By.XPATH, "//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div[5]/div/c-wiz/section/div[2]/div[2]")
        assert(len(stock_elements) == 1)
        stock_elements = stock_elements[0].text.split("\n")
        suggested_stocks=set()
        for i, t in enumerate(stock_elements):
            print(i, t)
            if i % 5 == 0 and t != "INDEX":
                suggested_stocks.add(t)
        print(suggested_stocks)
        assert(len(suggested_stocks) > 0)

        # 4. Compare the stock symbols retrieved from (3) with given test data
        print("Retrieved Symbols:", suggested_stocks)
        
        # 5. Symbols in retrieved data but not in test data
        missing_from_test_data = suggested_stocks - test_data
        print("Stock symbols in retrieved data but not in test data:", missing_from_test_data)

        # 6. Symbols in test data but not in retrieved data
        missing_from_retrieved = test_data - suggested_stocks
        print("Stock symbols in test data but not in retrieved data:", missing_from_retrieved)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()