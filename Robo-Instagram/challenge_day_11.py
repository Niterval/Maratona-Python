from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask, render_template, request
from random import choice
import time
from automation import scraping_ig




app = Flask('Sorteio Instagram')

@app.route("/")
def index():
    return render_template('index.html') 

######## Dentro dessa função result está pegando 2 valores #########
@app.route("/result")
def result():
	input_url_post = request.args.get('url')
	winners = request.args.get('winners')

	# scraping_ig(input_url_post)

	driver = webdriver.Chrome()
	driver.get('https://www.instagram.com/')
	time.sleep(2)

	######## Selecionando elementos de Login ################
	input_user = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('gameconta012@gmail.com')
	input_pssword = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('0102Instagram')
	time.sleep(3)

	############# Pressionadno ENTER para logar ###########
	driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
	time.sleep(4)
	############# Clicando para não salvar infromações de login nem ativar notificaçõies ###########
	driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
	time.sleep(6)
	driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

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

	    #### Vencedor #####
	    winners = (list_user_comment)

	    winner_list = []

	    if winners == '1':
	    	randon1 = choice(winners)
	    	winner_list.append(randon1)

	    elif winners == '2':
	    	randon1 = choice(winners)
	    	randon2 = choice(winners)
	    	winner_list.append(randon1)
	    	winner_list.append(randon2)

	    else:
	    	randon1 = choice(winners)
	    	randon2 = choice(winners)
	    	randon3 = choice(winners)
	    	winner_list.append(randon1)
	    	winner_list.append(randon2)
	    	winner_list.append(randon3)

	### Nº total de comentarios únicos #### 
	total_comments = len(list_user_comment)

	return render_template('result.html', total_comments = total_comments, winner_list = winner_list) 



app.run()