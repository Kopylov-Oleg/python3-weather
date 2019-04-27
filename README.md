# python3-weather
Семестровый проект "Погода в мире" по курсу "Совместная разработка приложений на Python3" 
### Постановка задачи: 
Создание программы, позволяющей узнать погоду в крупных городах мира на данный момент и выводящую информацию об этом с помощью текста и *очень* приятной анимации. 
### Авторы: 
> [Копылов Олег 424](https://github.com/Kopylov-Oleg)

> [Васьков Александр 424](https://github.com/AVasK)
### Project roadmap:
![alt text](https://raw.githubusercontent.com/AVasK/python3-weather/master/plan.jpg)
- [x] Step 1
- [ ] Step 2 (*90%* complete)
- [ ] Step 3
- [ ] Step 4 (Work In Progress)

### Схема GUI интерфейса:
![alt text](https://pp.userapi.com/c854128/v854128419/26f3e/N55nEweiqCY.jpg)

### Используемые API:
- [x] www.apixu.com - удобный API для запроса погоды через http.
- [x] cities.list.json - список информации с другого ресурса, возможно найти широту/долготу города, все города с таким именем и т.д.

```python3
get_weather_data(city_name) # возвращает dict() с данными о погоде (['current'])

```
