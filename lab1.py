from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)   

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/menu")
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
        <h1><a href="/lab2">Лабороторная работа 2</a></h1>
        <h1><a href="/lab3">Лабороторная работа 3</a></h1>
        <h1><a href="/lab4">Лабороторная работа 4</a></h1>
        <h1><a href="/lab5">Лабороторная работа 5</a></h1>

        <footer>
            &copy; Смакотин Степан, ФБИ-13, 3 курс, 2023
        </footer>
    </body> 
</html>
"""


@lab1.route("/lab1")
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


@lab1.route("/lab1/oak")
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


@lab1.route("/lab1/student")
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


@lab1.route("/lab1/python")
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


@lab1.route("/lab1/bmw")
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