# Вывод на консоль N топа вакансий по запросу

"Программа" была написана для получения вакансий с сайтов HeadHunter и SuperJob 

"Версия" 0.1

## Требования

Для корректной работы Вам необходимо получить API-ключ от SuperJob 
(инструкция [тут](https://api.superjob.ru/register)).
После получения ключа необходимо передать его в переменную окружения (или 
положить в `.env`-файл в корне проекта) в таком виде:

```shell
SJ_API_KEY=Ваш API-ключ
```

## Установка

- Рекомендуется использовать виртуальное окружение для запуска проекта.
- Для корректной работы Вам необходим Python версии 3.11 и выше.
- Нужно установить все необходимые модули:

```shell
poetry install
```

## Запуск

```shell
python main.py
```

***
Код написан в образовательных целях на курсах для backend-разработчиков Python [sky.pro](https://sky.pro/).
