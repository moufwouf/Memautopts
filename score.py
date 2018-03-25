from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument("--window-size=1000,600")
driver = webdriver.Chrome(chrome_options = opt)

driver.get('https://www.memrise.com/login/')
driver.find_elements_by_xpath('//*[@id="login"]/div[4]/input')[0].send_keys(input('Email : '))
driver.find_elements_by_xpath('//*[@id="login"]/div[5]/input')[0].send_keys(input('MPD : '))
driver.find_elements_by_xpath('//*[@id="login"]/input[3]')[0].click()
driver.get('https://www.memrise.com/course/1082981/lmw-chaptal-english/leaderboard/')
# if len(driver.find_elements_by_css_selector('button.close')) >0 : #decommenter si offre promo
#     driver.find_elements_by_css_selector('button.close')[0].click()
#     driver.refresh()


p = [0,0,0]
a,t1 = 0,0

while 1:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'li.leaderboard-row.current span.row-points')))
    p[0] = driver.find_elements_by_css_selector('li.leaderboard-row.current span.row-points')[0].get_attribute("textContent")
    
    driver.find_elements_by_xpath('//*[@id="content"]/div/div/div/div[2]/ul/li[2]')[0].click()
    time.sleep(0.8)
    p[1] = driver.find_elements_by_css_selector('li.leaderboard-row.current span.row-points')[0].get_attribute("textContent")
    
    driver.find_elements_by_xpath('//*[@id="content"]/div/div/div/div[2]/ul/li[3]')[0].click()
    time.sleep(0.8)
    p[2] = driver.find_elements_by_css_selector('li.leaderboard-row.current span.row-points')[0].get_attribute("textContent")
    t2 = time.time()
    
    nbt = p[2].split(',')
    b = int(nbt[0]+nbt[1]+nbt[2])
    
    
    print(p)
    v = (b-a)/(t2-t1)
    print(str(int(v*3600))+' pts/h')
    a = b
    t1 = time.time()
    time.sleep(5)
    driver.refresh()



