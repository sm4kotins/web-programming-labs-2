from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/example') 
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
    return render_template('example.html', name=name, number=number, group=group, course=course, fruits=fruits, books=books,)


@lab2.route('/lab2/porshe')
def porshe ():
    return render_template('porshe.html')