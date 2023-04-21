from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link1 = 'https://suninjuly.github.io/selects2.html'
link2 = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link1)
number1 = browser.find_element(By.CSS_SELECTOR, 'span#num1').text
number2 = browser.find_element(By.CSS_SELECTOR, 'span#num2').text
print(number2)
res = int(number1) + int(number2)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(res)) # ищем элемент с текстом "Python"

browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-default"]').click()

sleep(15)