# stupid-mark
Смешной телеграм бот на python для групп! Отправляет рандомайзером сообщения из базы данных messages.db . 


Бот в телеграм @stupidmarkrobot 

Хотите сделать похожего? Хорошо! Иструкция по установке!

Нужен linux

1. установка базы данных 
Debian based OS:

в консоль вводим:

sudo apt install sqlite3

Pacman based os(arch linux based os):

в консоль:

sudo pacman -S sqlite3

2. Если не стоит python 3, то ставим
debian:
sudo apt install python3
pacman:
sudo pacman -S python3

3.  Почти все готово! Ставим библиотеки для пайтон!
all OS:
pip install -r requirements.txt

4. Запускаем бота!
заходим в main.py и меняем слово токен на ваш токен бота полученный в botfather
сохраняем
вводим в консоль(в папке с ботом):
python3 main.py
