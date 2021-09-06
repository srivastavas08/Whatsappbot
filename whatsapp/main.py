
from webbrowser import open_new #can be used to simply controll browser
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install()) --- For automatically downloading chrome browser
from time import sleep
import pywin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
import psutil

chatbot = ChatBot(
    'Mr. Bot',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    preprocessors = ['chatterbot.preprocessors.clean_whitespace',
                     'chatterbot.preprocessors.unescape_html',
                     'chatterbot.preprocessors.convert_to_ascii'],
    logic_adapters = [
        # {
        #     'import_path': 'chatterbot.logic.BestMatch',
        #     'default_response': 'I am sorry, but I do not understand. I am still Learning',
        #     'maximum_similarity_threshold': 0.9
        # },
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri = 'sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(chatbot)
trainerr = ListTrainer(chatbot)
trainerr.train([
    "Hi, who is this?",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "What do you want?",
    "I am a whatsapp Bot",
    "what you can do for me?",
    "I can chat with you",
    "Can you help me?",
    "Please contact my creator KC for any help"

])
trainerr.train([
    "what do you want?",
    "I want to have a conversation with you",
    "Can you help me?",
    "Please contact my creator KC for any help"

])

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english"
)


def calling_chrome():
    # To invoke chrome Please run this script
    # chrome.exe --remote-debugging-port=8989 --user-data-dir=C:\Users\KUNALCHANDRA\PycharmProjects\whatsappAutomation\Chrome-Data

    os.chdir('C:\Program Files\Google\Chrome\Application') #Setting directory to chrome path
    os.popen(r'chrome.exe --remote-debugging-port=8989 --user-data-dir=C:\Users\KUNALCHANDRA\PycharmProjects\whatsappAutomation\Chrome-Data')
    os.chdir(r'C:\Users\KUNALCHANDRA\PycharmProjects\whatsappAutomation\whatsapp') #Setting directory back to project



def send_message_at_starting():

    driver.implicitly_wait(20)

    driver.find_element_by_css_selector('span[title="Standby"]').click()
    driver.implicitly_wait(20)
    message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    message.send_keys('Hello')
    message.send_keys(Keys.ENTER)

    # print('finished')

def get_message(current_user):
    sleep(2)
    list_user = [user.text for user in current_user]
    active_user = list_user[-1]
    list_user = list_user[0: len(list_user)-1]
    n = list_user.index(active_user)
    new_message = list_user[n+1]
    reply= chatbot.get_response(new_message)
    reply = str(reply)
    sleep(1)
    send_message(reply)
    print(f"Bot Replied {reply}")
    return new_message

def send_message(current_message):
    message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    message.send_keys(current_message)
    message.send_keys(Keys.ENTER)
    # print('Done')
    driver.implicitly_wait(20)
    driver.find_element_by_css_selector('span[title="Standby"]').click()

def check_new_message():
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_css_selector('span[class="_23LrM"]').click()
        driver.implicitly_wait(20)
        current_user = driver.find_elements_by_css_selector('span[class ="_ccCW FqYAR i0jNr"]')
        current_message = get_message(current_user)
        print(f"User Replied = {current_message}")
        sleep(5)
        return check_new_message()

    except:
        pass
        return check_new_message()



phone_no = '+919458707426'
parsed_message = 'HI'
calling_chrome()

chrome_object = Options()
chrome_object.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path = 'chromedriver.exe', options = chrome_object)
driver.get(url='https://web.whatsapp.com/')
send_message_at_starting()
check_new_message()





# def check_chrome():
#     for p in psutil.process_iter(attrs=['pid', 'name']):
#         if p.info['name'] == "chrome.exe":
#             print("yes", (p.info['name']))
#         return True
#     return False
#
# value = check_chrome()
# print(value)
# if value == False: