# Задание 1  Создание своего docker image с http сервером nginx. Замена страницы приветсвия Nginx на свою

- Создаем контейнер на основе nginx  - "sudo docker run -d -p 8001:80 --name=homework_nginx nginx"
- входим в файловую систему контейнера "sudo docker exec -it homework_nginx bash"
- меняем данные файла приветствия  "echo '<h1>Hello from my NGINX !!!!!!!</h1>' > usr/share/nginx/html/index.html"
- проверяем внесение изменеий в терминале "cat usr/share/nginx/html/index.html"
- задоим в браузер "http://127.0.0.1:8001/"


# Задание 2  Создание контейнера для REST API сервера проекта из курса по Django

- Скачиваем репозиторий;
- создаем образ -   "sudo docker build . --tag=image_homework_2"
- проверяем наличие данного образа  -   "sudo docker images" 
- собираем контейнер на основе созданного образа -  "sudo docker container run -d -p 8000:8000 --name=cont_hw2 image_homework_2"
- проверяем запущен ли контейнер  -  "sudo docker ps"
- делаем запрос через файл requests.http   
- проверяем работу приложения в браузере