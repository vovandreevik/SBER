from flask import Flask, jsonify
import json

app = Flask(__name__)

class Component:
    def __init__(self, type, **kwargs):
        self.type = type
        self.__dict__.update(kwargs)

class Logo(Component):
    def __init__(self, url_image, link, pos):
        super().__init__("logo", url_image=url_image, link=link, pos=pos)

class Search(Component):
    def __init__(self, url_img, link):
        super().__init__("search", url_img=url_img, link=link)

class News(Component):
    def __init__(self, theme, image, title, text):
        super().__init__("news", theme=theme, image=image, title=title, text=text)

class NavButton(Component):
    def __init__(self, title, link):
        super().__init__("navbutton", title=title, link=link)

class Footer(Component):
    def __init__(self, text):
        super().__init__("footer", text=text)

class DataTemplate:
    def __init__(self):
        self.header = []
        self.navigation = []
        self.body = []
        self.footer = []

    def add_component(self, section, component):
        getattr(self, section).append(component.__dict__)

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

    def add_news(self, theme, image, title, text):
        self.body.append(News(theme, image, title, text).__dict__)

@app.route('/api/message', methods=['GET'])
def get_message():
    # Создаем экземпляр DataTemplate и добавляем компоненты и новости
    message = DataTemplate()
    message.add_component("header", Logo("http://example.com/logo.png", "http://example.com", "left"))
    message.add_component("header", Search("http://example.com/search.png", "http://example.com/search"))
    message.add_component("navigation", NavButton("Home", "http://example.com"))
    message.add_component("footer", Footer("Copyright 2022"))

    # Добавляем новости в раздел body
    news_info = [
    ("Спорт", "1.jpg", "Футбол",
     "Сборная России по футболу одержала победу над сборной Сербии со счетом 2:1 в товарищеском матче, который состоялся 21 марта в Москве. Голы за россиян забили Александр Головин и Артем Дзюба"),
    ("Спорт", "2.jpg", "Хоккей",
     "СКА одержал победу над 'Автомобилистом' со счетом 3:2 в третьем матче серии плей-офф КХЛ. Таким образом, петербургский клуб повел в серии со счетом 2-1."),
    ("Спорт", "3.jpg", "Баскетбол",
     "ЦСКА обыграл 'Зенит' со счетом 78:75 в пятом матче финальной серии Единой лиги ВТБ. Таким образом, ЦСКА стал чемпионом Единой лиги ВТБ в 12-й раз."),
    ("Спорт", "4.jpg", "Биатлон",
     "Эдуард Латыпов выиграл золотую медаль в масс-старте на этапе Кубка мира в Осло. Вторым стал норвежец Йоханнес Бё, третьим - француз Кентен Фийон-Майе."),
    ("Россия", "5.png", "Экономика",
     "ВВП России в 2023 году вырос на 3,5%. Это самый высокий рост за последние 4 года."),
    ("Россия", "6.jpg", "Политика",
     "Президент России Владимир Путин выступил с посланием Федеральному Собранию. В своем послании он затронул вопросы экономики, социальной политики, безопасности и внешней политики."),
    ("Россия", "7.jpg", "Общество",
     "В России прошел День защитника Отечества. В этот день чествуют всех, кто служил или служит в армии."),
    ("Россия", "8.jpg", "Культура", "В Москве открылся новый музей современного искусства. Музей называется 'Гараж'."),
    ("Санкт-Петербург", "9.jpg", "Культура",
     "В Санкт-Петербурге проходит фестиваль 'Императорские театры России'. В рамках фестиваля проходят спектакли ведущих театров России."),
    ("Санкт-Петербург", "10.jpg", "Туризм",
     "Санкт-Петербург вошел в пятерку самых популярных туристических направлений в мире."),
    ("Санкт-Петербург", "11.jpg", "Экономика",
     "В Санкт-Петербурге открылся новый завод по производству электромобилей."),
    ("Санкт-Петербург", "12.jpg", "Образование",
     "В Санкт-Петербургском государственном университете открылся новый факультет - факультет искусственного интеллекта."),
    ("Туризм", "13.png", "Внутренний туризм", "В 2023 году число туристов, посетивших Россию, выросло на 10%."),
    ("Туризм", "14.jpg", "Международный туризм",
     "Россия вошла в десятку самых популярных туристических направлений для туристов из Китая."),

    ("Туризм", "15.jpg", "Гастрономический туризм",
     "В России проходит фестиваль 'Вкусы России'. В рамках фестиваля можно попробовать блюда из разных регионов России."),
    ("Туризм", "16.jpg", "Экотуризм",
     "В России набирает популярность экотуризм. Туристы едут в Россию, чтобы увидеть уникальные природные красоты страны."),
    ("Образование", "17.jpg", "Школьное образование", "В России вводится новая система оценки знаний - ФГОС 3.0."),
    ("Образование", "18.jpg", "Высшее образование", "В России увеличивается число бюджетных мест в вузах."),
    ("Образование", "19.png", "Дополнительное образование", "В России набирают популярность онлайн-курсы."),
    ("Образование", "20.jpg", "Профессиональное образование",
     "В России создаются новые центры опережающей подготовки кадров."),
]

    for news in news_info:
        message.add_news(*news)

    # Возвращаем сообщение в формате JSON
    return jsonify(message.__dict__)

if __name__ == '__main__':
    app.run(port=5001)