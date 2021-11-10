from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

service = Service('C:/Users/maria/Desktop/chromedriver.exe')
website = 'https://www.starz.com/ar/es/'
path = service

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(website)

time.sleep(2)

explore_button = driver.find_element(By.XPATH, '//a[@href="/ar/es/search"]')
explore_button.click()
time.sleep(2)
series_movies_button = driver.find_element(By.XPATH, '//a[@href="/ar/es/view-all/all/0"]')
series_movies_button.click()
time.sleep(2)
filters_button = driver.find_element(By.XPATH, '//span[@class="pl-1 title text-uppercase"]')
filters_button.click()
time.sleep(2)
movies_button = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/starz-filter-drawer/section/div[2]/div/div[2]/button[2]')
movies_button.click()
time.sleep(2)
apply_button = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/starz-filter-drawer/section/div[2]/div/div[1]/div/div/button[2]')
apply_button.click()

time.sleep(2)
i = 1
j = 1
movies_series = []

movies = driver.find_elements(By.CLASS_NAME, 'grid-item')
for movie in movies:
    time.sleep(1)
    more_info = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/div/div/div/section[1]/virtual-scroller/div[2]/div['+str(j)+']/div['+str(i)+']/div/starz-content-item/article/div[1]/a[2]/span')
    time.sleep(1)
    more_info.click()
    i += 1
    if i == 7:
        i = 1
        j += 1
    time.sleep(2)
    title = driver.find_element(By.XPATH, '//*[@id="moviesDetailsH1"]').text
    movies_series.append(title)
    year = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[4]').text
    movies_series.append(year)
    duration = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/section/ul/li[2]').text
    movies_series.append(duration)
    synopsis = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-movie-details/div/div/section/div[1]/div[2]/div[1]/p').text
    movies_series.append(synopsis)
    driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    if j == 24:
        driver.execute_script("window.scrollTo(0, 4500)")
        time.sleep(1)

time.sleep(1)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(1)
series_button = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/starz-filter-drawer/section/div[2]/div/div[2]/button[3]')
series_button.click()
time.sleep(2)
apply_button = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/starz-filter-drawer/section/div[2]/div/div[1]/div/div/button[2]')
apply_button.click()

i = 1
j = 1
series = driver.find_elements(By.CLASS_NAME, 'grid-item')

for serie in series:
    time.sleep(1)
    more_info = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-view-all/div/div/div/div/section[1]/virtual-scroller/div[2]/div['+str(j)+']/div['+str(i)+']/div/starz-content-item/article/div[1]/a[2]/span')
    time.sleep(1)
    more_info.click()
    i += 1
    if i == 7:
        i = 1
        j += 1
    time.sleep(3)
    title = driver.find_element(By.XPATH, '//*[@id="seriesDetailsH1"]').text
    movies_series.append(title)
    year = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[4]').text
    movies_series.append(year)
    episodes = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/ul/li[2]').text
    movies_series.append(episodes)
    synopsis = driver.find_element(By.XPATH, '//*[@id="subview-container"]/starz-series-details/div[1]/section/div[1]/div[2]/div[2]/p').text
    movies_series.append(synopsis)
    driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    if i == 5 and j == 12:
        break

driver.quit()

df = pd.DataFrame({'movies & series': movies_series})
print(df)
df.to_csv('movies_series.csv', index=False)