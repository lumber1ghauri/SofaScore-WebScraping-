from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
options.add_argument("--no-sandbox")  # Stability in some environments
options.add_argument("--disable-dev-shm-usage")  # Avoid memory issues

# Use ChromeDriverManager to auto-download and manage chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL for ping pong matches
URL = "https://www.sofascore.com/it/ping-pong"
driver.get(URL)

# Wait for dynamic content to load
time.sleep(10)  # Increased to ensure JavaScript-loaded content appears

# Get page source
html = driver.page_source

# Save to HTML file
with open("sofascore_pingpong.html", "w", encoding="utf-8") as file:
    file.write(html)
print("HTML data saved to sofascore_pingpong.html")

# Close browser
driver.quit()