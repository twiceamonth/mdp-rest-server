# mdp fastapi server

## Перед запуском
На компьютере должен быть установлен Docker и Git. Их можно найти на оффициальных сайтах:

https://www.docker.com/products/docker-desktop/

https://git-scm.com/downloads

И для всех последующих манипуляций Docker должен быть запущен.

## Запуск проекта
Сначала нужно скопировать репозиторий к себе. Для этого надо перейти в необходимый каталог открыть и открыть там консоль.
Это можно сделать нажав на поле пути в проводнике и написав cmd нажать Enter. Или нажав правую кнопку миши и далее "Открыть в терминале".
Далее в консоли необходимо выполнить следущую команду:

```commandline
git clone https://github.com/twiceamonth/mdp-rest-server.git
```

Также проект можно скачать с репозитория zip архивом. И после того как был скачать zip архив его необходимо разархивировать в нужную деррикторию. 

Далее нужно зайти в папку скачанного проекта и открыть там консоль. 
Чтобы собрать контейнер необходимо прописать команду ниже и дождаться полной сборки контейнера:

```commandline
 docker-compose up --build
```

После того как контейнер собрался приложение доступно по локальному адресу. Все API запросы необходимо отправлять на этот адрес.

```commandline
http://localhost:8000/
```

Документация доступна по адресу:

```commandline
http://localhost:8000/docs
```

Если стрктура базы данных не создалась, в папке с проектом есть файл ```mdp-clear.sql```, это образ базы данных с пустыми таблицами. Чтобы загрузить бекам в контейнер необходимо выполнить в терминале следующую команду:

```commandline
type mdp-clear.sql | docker exec -i mdp-db psql -U postgres -d postgres
```