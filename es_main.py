import re
import time
from selenium import webdriver
chrome_driver = 'G:/seleninum project/chromedriver.exe'
driver =  webdriver.Chrome(chrome_driver)
 
driver.get('https://www.google.com/search?q=software+developer+veritas+pune+contact+email+%22gmail%22+site:linkedin.com&oq=software+developer+veritas+pune+contact+email+%22gmail%22+site:linkedin.com&aqs=chrome..69i57.64719j0j7&sourceid=chrome&ie=UTF-8')
time.sleep(50)
#change page setting to 100 pages
#software developer veritas pune contact email "gmail" site:linkedin.com   (I searched)
page_source = driver.page_source

EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

list_of_emails = []

for re_match in re.finditer(EMAIL_REGEX, page_source):
    list_of_emails.append(re_match.group())

for i, email in enumerate(list_of_emails):
    print(f'{i+1}:{email}')    
