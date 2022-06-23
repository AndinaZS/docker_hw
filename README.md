# docker_hw
   
## задание 1
dockerfile и html в папке task 1    
команда для запуска: docker run -d -p 80:80 <имя образа>

## задание 2
dockerfile и проект в папке task 2   
команда для запуска: docker run -d -e DEBUG=True -p 8080:5060 <имя образа>    


P.S.: т.к. в отсутствие файла .env образ отказался собираться, проставила в settings.py дефолтные значание DEBUG и SEKRET_KEY.   
DEBUG по умолчанию проставила в False, подменяется на True в команде выше (раз использование переменных окружения требуется по заданию :))   

*Файл для импорта в Postman: docker_netology.postman_collection.json*
