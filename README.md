# Тема 1. Введение в Python
Отчет по Теме #1 выполнил:
- Чешегоров Алексей Александрович
- АИС-21-1

| Задание | Лаб_раб | 
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Задание 1
### Установка

### Результат.
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.1.jpg)
## Выводы
Git установлен

## Задание 2
### Настройка
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.2.jpg)
## Выводы
Можно настроить личные данные, редактор, а так же просматривать список настроек с помощью команды git config --list

## Задание 3
### Создание нового репозитория
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.3.jpg)
## Выводы
Для связи между локальным репозиторием и удалённым нужно инициализирвоать репозиторий локально.
  
## Задание 4
### Подготовка файлов
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.4.jpg)
## Выводы
Есть команды для добавления одног офайла и проверки статуса файлов.

## Задание 5
### Фиксация изменений
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.5.jpg)
## Выводы
Для фиксации изменений используем команду git commit
Для просмотра коммитов используем команду git log

## Задание 6
### Подключение к удаленному репозиторию
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.6(1).jpg)
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.6(2).jpg)
## Выводы
Подключение к удалённому репозиторию происходит с помощью команды git remote add origin URL
С помощью git push добавляем изменения в удалённый репозиторий
С помощью git pull извлекаем изменения
незафиксированные изменения можно сохранять с помощью git stash

## Задание 7
### Ветвление
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.7(1).jpg)
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.7(2).jpg)
## Выводы
Ветвление используется для организации работы по разным направлениям(веткам)
git branch название_ветки - cоздание ветки
git checkout / git switch - переключение между ветками
git merge - слияние веток


## Задание 8
### Особенности применения «Фетч»
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.8.jpg)
## Выводы
git fetch извлекает изменения из удалённого репозитория, но не объединяет их с локальной веткой
git fetch [Удалённый репозиторий]

## Задание 9
### Удаление файлов, веток, локальных и удалённых репозиториев
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.9(1).jpg)
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.9(2).jpg)
## Выводы
git rm [название файла] - удалить файл
git rm --cached [название файла] - удалить файл из индекса
git branch -D - принудительное удаление локальной ветки
git push origin --delete [название ветки] - удаление кдалённый ветки

## Задание 10
### Отслеживание изменений в коммитах
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.10.jpg)
## Выводы
git log / git diff - команды для отслеживания изменений в коммитах

## Задание 11
### Возвращение файла к предыдущему (определенному) состоянию
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.11.jpg)
## Выводы
git checkout [хэш коммита] -- [путь к файлу] - возвращение файла к предыдущему состоянию (на момент указанного комита)
-m - флаг, позволяющий оставить описание коммиту во время ег осоздания
  
## Задание 12
### Возвращение к предыдущему коммиту
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.12(1).jpg)
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.12(2).jpg)
## Выводы
git reset --soft - сброс до предыдущего коммита (с сохранением изменений в рабочей директории)
git reset --hard - сброс до предыдущего коммита (с потерей изменений)
git reset --hard [хэш коммита] - сброс до конкретного коммита
  
## Задание 13
### Исправление коммита
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.13(1).jpg)
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.13(2).jpg)
## Выводы
После выполнение команды git commit --amend откроется текстовый редактор для редакции сообщения или добавления файлов. После внесения изменений коммит будет исправлен
  
## Задание 14
### Разрешение конфликтов при слиянии
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.14.jpg)
В данном случае нет конфликтов, потмоу что происходит слияние между одной и той же веткой.
## Выводы
Разрешение конфликтов при слиянии включает в себя изменение кода, чтобы устранить конфликты, и продолжение слияния после их разрешения
  
## Задание 15
### Настройка .gitignore
![Меню](https://github.com/illusprite/SoftwareEngineering/blob/Topic_1/pic/2.15.jpg)
## Выводы
Файл .gitignore - важная составляющая каждого репозитория
Преимущества использования:
#### Исключение ненужных файлов
#### Сокращение размера репозитория
#### Соблюдение принципов безопасности
#### Сохранение чистоты репозитория
