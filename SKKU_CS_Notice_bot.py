from selenium import webdriver
import os
import telegram

bot = telegram.Bot(token="606156755:AAEnv8PSpcozLlOs-O5tVh6k3RDCtn3eq8M")
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('--disable-setuid-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
# driver = webdriver.Chrome(executable_path=BASE_DIR+"/chromedriver", chrome_options=options)

driver.get("http://cs.skku.edu/open/notice/list")
driver.implicitly_wait(10)
articles = driver.find_elements_by_xpath('//table[@id="boardList"]/tbody/tr[@role = "row"]')
try:
    numLatestArticle = articles[0].text.split()[0]

    with open(os.path.join(BASE_DIR, "notice.txt"), 'r') as f_read:
        numOldArticle = f_read.readline()
        f_read.close()
        if numOldArticle != numLatestArticle:
            for article in articles:
                numArticle = article.text.split()[0]
                if numArticle <= numOldArticle:
                    break

                titleList = article.text.split()
                sendingMessage = '[컴퓨터공학과 공지사항 ' + titleList[-2] + ']\n'
                for elem in titleList[2:-3]:
                    sendingMessage += elem + ' '

                sendingMessage += "\nviews : " + titleList[-1]
                sendingMessage += "\nhttp://cs.skku.edu/open/notice/view/" + str(numArticle)
                bot.sendMessage(chat_id=chat_id, text=sendingMessage)

            with open(os.path.join(BASE_DIR, "notice.txt"), 'w+') as f_write:
                f_write.write(numLatestArticle)
                f_write.close()
except Exception as e:
    print(e)

driver.get("http://cs.skku.edu/open/news/list")
driver.implicitly_wait(10)
articles = driver.find_elements_by_xpath('//table[@id="boardList"]/tbody/tr[@role = "row"]')
try:
    numLatestArticle = articles[0].text.split()[0]

    with open(os.path.join(BASE_DIR, "news.txt"), 'r') as f_read:
        numOldArticle = f_read.readline()
        f_read.close()
        if numOldArticle != numLatestArticle:
            for article in articles:
                numArticle = article.text.split()[0]
                if numArticle <= numOldArticle:
                    break

                titleList = article.text.split()
                sendingMessage = '[컴퓨터공학과 새소식 ' + titleList[-2] + ']\n'
                for elem in titleList[1:-3]:
                    sendingMessage += elem + ' '

                sendingMessage += "\nviews : " + titleList[-1]
                sendingMessage += "\nhttp://cs.skku.edu/open/news/view/" + str(numArticle)
                bot.sendMessage(chat_id=chat_id, text=sendingMessage)

            with open(os.path.join(BASE_DIR, "news.txt"), 'w+') as f_write:
                f_write.write(numLatestArticle)
                f_write.close()
except Exception as e:
    print(e)

driver.get("http://cs.skku.edu/open/seminar/list")
driver.implicitly_wait(10)
articles = driver.find_elements_by_xpath('//table[@id="boardList"]/tbody/tr[@role = "row"]')
try:
    numLatestArticle = articles[0].text.split()[0]

    with open(os.path.join(BASE_DIR, "seminar.txt"), 'r') as f_read:
        numOldArticle = f_read.readline()
        f_read.close()
        if numOldArticle != numLatestArticle:
            for article in articles:
                numArticle = article.text.split()[0]
                if numArticle <= numOldArticle:
                    break

                titleList = article.text.split()
                sendingMessage = '[컴퓨터공학과 세미나공지 ' + titleList[-2] + ']\n'
                for elem in titleList[1:-3]:
                    sendingMessage += elem + ' '

                sendingMessage += "\nviews : " + titleList[-1]
                sendingMessage += "\nhttp://cs.skku.edu/open/seminar/view/" + str(numArticle)
                bot.sendMessage(chat_id=chat_id, text=sendingMessage)

            with open(os.path.join(BASE_DIR, "seminar.txt"), 'w+') as f_write:
                f_write.write(numLatestArticle)
                f_write.close()
except Exception as e:
    print(e)

driver.get("http://cs.skku.edu/open/recruit/list")
driver.implicitly_wait(10)
articles = driver.find_elements_by_xpath('//table[@id="boardList"]/tbody/tr[@role = "row"]')
try:
    numLatestArticle = articles[0].text.split()[0]

    with open(os.path.join(BASE_DIR, "recruit.txt"), 'r') as f_read:
        numOldArticle = f_read.readline()
        f_read.close()
        if numOldArticle != numLatestArticle:
            for article in articles:
                numArticle = article.text.split()[0]
                if numArticle <= numOldArticle:
                    break

                titleList = article.text.split()
                sendingMessage = '[컴퓨터공학과 취업/인턴십정보 ' + titleList[-2] + ']\n'
                for elem in titleList[1:-3]:
                    sendingMessage += elem + ' '

                sendingMessage += "\nviews : " + titleList[-1]
                sendingMessage += "\nhttp://cs.skku.edu/open/recruit/view/" + str(numArticle)
                bot.sendMessage(chat_id=chat_id, text=sendingMessage)

            with open(os.path.join(BASE_DIR, "recruit.txt"), 'w+') as f_write:
                f_write.write(numLatestArticle)
                f_write.close()
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()

    
