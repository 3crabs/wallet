from Category import Category
from Database import Database
from Flow import Flow
from TypeFlow import TypeFlow
from WalletException import WalletException


def calc_flow(text: str):
    if text == 'доходов':
        return TypeFlow.PROFIT
    if text == 'расходов':
        return TypeFlow.LESS
    raise WalletException('Не понял тип категории попробуйте снова.')


def add_category(type_flow_str: str, category_name: str):
    type_flow = calc_flow(type_flow_str)
    # сохранение категории в базу
    session = Database.get_instance().session()
    session.add(Category(category_name, type_flow))
    session.commit()
    return f'Категория {category_name} добавлена!'


def add_flow(money_str: str, category_name: str):
    session = Database.get_instance().session()
    categories = session.query(Category).filter_by(name=category_name).all()
    if not categories:
        return 'Категория транспорт не найдена'
    session.add(Flow(int(money_str), categories[0].id))
    session.commit()
    return f'В {category_name} добавлена {money_str}р!'


def text_answer(text: str):
    text = text.lower()

    # проверяем что обращаются к нам
    if text.split(' ')[0] != 'wallet':
        return None

    try:
        words = text.split(' ')

        # добавление категории
        if len(words) == 5 and f'{words[1]} {words[2]}' == 'добавь категорию':
            return add_category(words[3], words[4])

        # добавление потока
        if len(words) == 5 and f'{words[1]}' == 'добавь':
            return add_flow(words[2], words[4])

        return 'Не понимаю что вы хотите.'
    except WalletException as we:
        return we.__str__()
