from selenium import webdriver

path_to_chromedriver = "D:\Archivos Lavila\Downloads\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#aca escogemos la pagina que queremos hacer usar scraping
url = 'https://mail.google.com/mail/u/0/#inbox'
browser.get(url)