from flask import Blueprint, redirect, url_for, render_template, request;
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if not username:
        error = 'Не введен логин'
        return render_template ('login.html', error=error, username=username, password=password)
    
    if not password:
        error = 'Не введен пароль'
        return render_template ('login.html', error=error, username=username, password=password)
    
    if username == 'stepan' and password == '5252':
        return render_template('success1.html', username=username)
    
    error = 'Неверные логин и/или пароль'
    return render_template('login.html', error=error, username=username, password=password)

@lab4.route('/lab4/fridge/', methods = ['GET', 'POST'])
def fridge():
    temperature = request.form.get('temperature')
    message = ""

    if request.method == 'POST':
        if not temperature:
            message = "Ошибка: не задана температура"
        else:
            temperature = int(temperature)
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С" + "❄️❄️❄️"
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С" + "❄️❄️"
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С" + "❄️"

    return render_template('fridge.html', message=message, temperature=temperature)

@lab4.route('/lab4/ordergrain/', methods=['GET', 'POST'])
def order_grain():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if not weight:
            error = 'Ошибка: не введен вес'
            return render_template('ordergrain.html', error=error)

        weight = float(weight)
        price_per_ton = {
            'ячмень': 12000,
            'овёс': 8500,
            'пшеница': 8700,
            'рожь': 14000
        }


        price = price_per_ton[grain] * weight

        if weight > 50:
            discount = 0.1 * price
            price -= discount
            discount_message = 'Применена скидка за большой объем.'
        else:
            discount_message = ''


        if weight > 500:
            error = 'Извините, такого объема сейчас нет в наличии.'
            return render_template('ordergrain.html', error=error)

        if weight <= 0:
            error = 'Ошибка: введен недопустимый вес'
            return render_template('ordergrain.html', error=error)

        message = f'Заказ успешно сформирован. Вы заказали {grain}. Вес: {weight} т. Сумма к оплате: {price} руб. {discount_message}'


        return render_template('ordergrain.html', message=message)

    return render_template('ordergrain.html')

@lab4.route('/lab4/cookies/', methods=['GET', 'POST'])
def cookies():
    error = None 

    if request.method == 'POST':
        color = request.form.get('color')
        bg_color = request.form.get('bg_color')
        font_size = request.form.get('font_size')

        if color == bg_color:
            error = "Цвет текста не должен совпадать с цветом фона."

        font_size = int(font_size)
        if font_size < 5 or font_size > 30:
            error = "Размер шрифта должен быть от 5px до 30px."

        if error is None:
            response = redirect('/lab4/cookies/')
            response.set_cookie('color', color)
            response.set_cookie('bg_color', bg_color)
            response.set_cookie('font_size', str(font_size))
            return response

    return render_template('cookies.html', error=error)