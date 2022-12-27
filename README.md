# count_clicks
Это программа для сокращениядлинных ссылок и счета кликов по этой ссылке.
### Для запуска программы требуется:
 * скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * операционная система linux, windows 7 или выше.
 * установить все нужные библиотеки Python командой:
```
pip install -r requirements.txt
```
### Как запустить программу:
* запустить программу с помощью команды:
```
python main.py https://docs.python.org/3.6/howto/argparse.html - длинная ссылка
python main.py https://bit.ly/3BbJKFh - короткая ссылка
```
* Если вы ввели длинную ссылку, то в терминале выведется новая короткая ссылка:
~~~
Битлинк https://bit.ly/3BbJKFh
~~~
* Если вы введёте сразу короткую ссылку, то терминал вывидет количество сделанных кликов по этой ссылке:
~~~
Сделано кликов 0
~~~
### Цель проекта:
* Код написан в образовательных целях 

