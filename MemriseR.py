from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound


opt = webdriver.ChromeOptions()
opt.add_argument("headless")
driver = webdriver.Chrome(chrome_options = opt)




def question():
    return driver.find_element_by_css_selector("div.question-row.clearfix").get_attribute("textContent")[31:-14]

def mots():
    return [x.get_attribute("textContent") for x in driver.find_elements_by_css_selector("span.val")]

def sens():
    q = question()
    return int((q in Dict[1]))



def reponse():
    s = sens()
    if question() in Dict[s]:
        i = Dict[s].index(question())
        rep = Dict[int(not s)][i]
        print(rep)
        return rep
    return False




driver.get('https://www.memrise.com/login/')
driver.find_elements_by_xpath('//*[@id="login"]/div[4]/input')[0].send_keys(input('Email : '))
driver.find_elements_by_xpath('//*[@id="login"]/div[5]/input')[0].send_keys(input('MDP : '))
driver.find_elements_by_xpath('//*[@id="login"]/input[3]')[0].click()
driver.get('https://www.memrise.com/course/1082981/lmw-chaptal-english/garden/speed_review/')


winsound.Beep(500,100)

try:
    
    while 1:
        
    
    
        test = True  
        Dict = ([],[])
        dict = open("dict.txt","r+")
        for rd in dict.readlines():
                i = rd.index("¤")
                Dict[0].append(rd[:i])
                Dict[1].append(rd[i+1:-1])
        
        
        
        while driver.find_elements_by_css_selector('div.overlay-content') == []:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.question-row.clearfix")))
            s = sens()
            rep = reponse()
            if type(rep) == str:
                num = mots().index(rep)
                driver.find_elements_by_css_selector("span.val")[num].click()
                driver.implicitly_wait(1)
            else:
                q = question()
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'li.shiny-box.choice.clearfix.correct')))
                rep = driver.find_elements_by_css_selector('li.shiny-box.choice.clearfix.correct')[0].get_attribute("textContent")[36:-30]
                Dict[s].append(q)
                Dict[int(not sens)].append(rep)
                print("apprend :"+q)
                driver.implicitly_wait(2)
                if s == 0: dict.write(q+"¤"+rep+"\n")
                elif s == 1: dict.write(rep+"¤"+q+"\n")
                
        dict.close()
        # winsound.Beep(2500,200)
        
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button.continue-btn.js-continue-btn")))
        driver.find_elements_by_css_selector("button.continue-btn.js-continue-btn")[0].click()
    
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.next_btn.btn.btn-primary.btn-large")))
        driver.find_elements_by_css_selector("div.next_btn.btn.btn-primary.btn-large")[0].click()
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.mode-selector-button.enabled")))
        driver.find_elements_by_css_selector("div.mode-selector-button.enabled")[0].click()
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.mode-icon.speed_review.enabled")))
        driver.find_elements_by_css_selector("div.mode-icon.speed_review.enabled")[0].click()
        
except:
    winsound.Beep(4000,100)
    driver.save_screenshot('screenshot.png')
    driver.quit()