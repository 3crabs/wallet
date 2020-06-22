from Category import Category
from Database import Database
from TypeFlow import TypeFlow


def calc_flow(text: str):
    if text == 'доходов':
        return TypeFlow.PROFIT
    if text == 'расходов':
        return TypeFlow.LESS


def add_category(type_flow_str: str, category_name: str):
    type_flow = calc_flow(type_flow_str)
    # сохранение категории в базу
    session = Database.get_instance().session()
    session.add(Category(category_name, type_flow))
    session.commit()
    return f'Категория {category_name} добавлена!'


def text_answer(text: str):
    text = text.lower()

    # проверяем что обращаются к нам
    if text.split(' ')[0] != 'wallet':
        return None

    # добавление категории
    if text.split(' ')[1] + ' ' + text.split(' ')[2] == 'добавь категорию':
        return add_category(text.split(' ')[3], text.split(' ')[4])
