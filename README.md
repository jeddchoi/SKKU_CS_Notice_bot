# SKKU_CS_Notice_bot
SKKU Computer Science Board Scrapper using Telegram Bot. @SKKU_CS_Notice_bot

# How to use
1. 먼저 관련된 dependency를 세팅한다.

sudo apt-get remove google-chrome-stable
rm ~/selenium-server-standalone-*.jar
rm ~/chromedriver_linux64.zip
sudo rm /usr/local/bin/chromedriver
sudo rm /usr/local/bin/selenium-server-standalone.jar

sudo apt-get update
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

wget -N http://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

wget -N http://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.1.jar -P ~/
sudo mv -f ~/selenium-server-standalone-3.9.1.jar /usr/local/bin/selenium-server-standalone.jar
sudo chown root:root /usr/local/bin/selenium-server-standalone.jar
sudo chmod 0755 /usr/local/bin/selenium-server-standalone.jar

sudo apt-get install python3
sudo apt-get install python3-pip
sudo python3 -m pip install -U selenium bs4 python-telegram-bot requests

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

cat /var/log/syslog | grep CRON
cat /var/mail/luv_gwangyoung 

2. 크롬 드라이버가 /usr/local/bin/ 아래 폴더에 잘 저장되어 있는지 확인한다.
3. crontab -e하면 열리는 vim 창에서 아래와 같이 저장한다.
0 * * * * /usr/bin/python3 /home/luv_gwangyoung/SKKU_CS_Notice_bot.py



