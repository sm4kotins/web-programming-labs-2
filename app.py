from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/lab1")
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

        <footer>
            &copy; Смакотин Степан, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""