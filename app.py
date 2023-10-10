from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
    return """
    <!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1><a href="/lab1">Лабороторная работа 1</a></h1>

        <footer>
            &copy; Смакотин Степан, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab():
    return  """ 
<!doctype html>
<html>
    <head>
        <title>Смакотин Степан Владиславович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Flask — фреймворк для создания веб-приложений на языке программирования Python,
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2.
        Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений,
        сознательно предоставляющих лишь самые базовые возможности</h1>

        <a href="/menu">Меню</a>
                <h1>Реализованные роуты</h1>
        <ol>
            <li><a href="/lab1/oak">Дуб</a></li>
            <li><a href="/lab1/student">Студент</a></li>
            <li><a href="/lab1/python">Python</a></li>
            <li><a href="/lab1/bmw">BMW</a></li>
        </ol>

        <footer>
            &copy; Смакотин Степан, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1/oak")
def oak ():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for ('static', filename='lab1.css') + '''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for ('static', filename='maxresdefault.jpg') + '''">
    </body>
</html>

'''

@app.route("/lab1/student")
def student ():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for ('static', filename='lab1.css') + '''">
    <body>
        <h1>Смакотин Степан Владиславович</h1>
        <img src="''' + url_for ('static', filename='nstu.png') + '''">
    </body>
</html>

'''

@app.route("/lab1/python")
def python ():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for ('static', filename='lab1.css') + '''">
    <body>
        <h1>Язык Python</h1>
        <p>Python — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и для многих платформ: начиная с iOS и Android и заканчивая серверными операционными системами. Как и где применяется Python. 
        Это интерпретируемый язык, а не компилируемый, как C++ или Java. Программа на Python представляет собой обычный текстовый файл.</p>
        <img src="''' + url_for ('static', filename='python.jpg') + '''">
    </body>
</html>

'''

@app.route("/lab1/bmw")
def bmw ():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for ('static', filename='lab1.css') + '''">
    <body>
        <h1>BMW M5 Competition</h1>
        <p>Доработанная подразделением BMW Motorsport версия автомобиля BMW пятой серии. Первое поколение было представлено в 1986 году. Последующие поколения M5 сменялись совместно с каждым поколением автомобилей пятой серии, включающей E34, E39, E60/61, F10. 
        С началом производства модели G30, после поступления первых заказов, с марта 2018 года началось также производство её M-версии.</p>
        <img src="''' + url_for ('static', filename='bmw.jpeg') + '''">
    </body>
</html>

'''

@app.route('/lab2/example')
def example ():
    name, number, group, course = 'Степан Смакотин', 2, 'ФБИ-13', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321},
    ]
    books = [
        { 'author': 'Антуан де Сент-Экзюпери', 'name': 'Маленький приц', 'genre': 'повесть', 'pages': '160'},
        { 'author': 'Джером Д. Сэлинджер', 'name': 'Над пропастью во ржи', 'genre': 'роман', 'pages': '320'},
        { 'author': 'Теодор Драйзер', 'name': 'Финансит', 'genre': 'роман', 'pages': '736'},
        { 'author': 'Пауло Коэльо', 'name': 'Алхимик', 'genre': 'роман', 'pages': '224'},
        { 'author': 'Оскар Уальд', 'name': 'Портрет Дориана Грея', 'genre': 'роман', 'pages': '320'},
        { 'author': 'Робин Шарма', 'name': 'Монах, который продал свой Феррари', 'genre': 'притча', 'pages': '256'},
        { 'author': 'Питер Камп', 'name': 'Скорочтение: Как запоминать больше, читая в 8 раз быстрее', 'genre': 'саморазвитие', 'pages': '320'},
        { 'author': 'Дуглас Адамс', 'name': 'Автостопом по галактике', 'genre': 'роман', 'pages': '256'},
        { 'author': 'Фрэнсис Скотт Фицджеральд', 'name': 'Великий Гэтсби', 'genre': 'роман', 'pages': '256'},
    ]
    return render_template('example.html', name=name, number=number, group=group, course=course, fruits=fruits, books=books)