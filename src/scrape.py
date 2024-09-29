import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup, Tag

def scrape_website(website):
    print('Launching Chrome...')
    
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        print('Website scraped successfully!')
        html = driver.page_source
        # time.sleep(10)
        return html
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return body_content
    return body_content.get_text()

def clean_body_content(body_content):
    print('Type of body_content:', type(body_content))
    print('Length of body_content:', len(str(body_content)))
    if not isinstance(body_content, Tag):
        return ""  

    soup = BeautifulSoup(str(body_content), 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    
    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)]