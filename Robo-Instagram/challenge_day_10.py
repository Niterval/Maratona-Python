from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import choice
import time


print('Sorteio Instagram\n')
print('Insira a URL postagem:')
input_url_post = input('>>>  ')
print('Aguarde...\n\n#################')



driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

time.sleep(2)

######### Selecionando elementos de Login ################
input_user = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('xxxxxxxx')
input_pssword = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('xxxxxxxx')
time.sleep(3)

############# Pressionadno ENTER para logar ###########
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
time.sleep(4)
############# Clicando para não salvar infromações de login nem ativar notificaçõies ###########
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(6)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

######## Link post #############
driver.get(input_url_post)
time.sleep(3)

btn_more_commentes = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
time.sleep(3)
comments = driver.find_elements(By.CLASS_NAME, 'C4VMK')

list_user_comment = []

try:
    while btn_more_commentes.is_displayed():
        btn_more_commentes.click()
        time.sleep(7)
        btn_more_commentes = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
    
except:
    # print('Ops! Tente novamente mais tarde...')
    pass

comments = driver.find_elements(By.CLASS_NAME, 'C4VMK')
for comment in comments:
    user_name = comment.find_element(By.CLASS_NAME, 'sqdOP').text
    if user_name in list_user_comment:
        continue
    else:
        list_user_comment.append(user_name)

print(f'{len(list_user_comment)} usuário (únicos) participando do sorteio')
print(f'O sorteador foi: {choice(list_user_comment)}')


# driver.quit()
