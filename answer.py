from Category import Category
from Database import Database
from TypeFlow import TypeFlow


def text_answer(text: str):
    category_name = text.split(' ')[4]
    session = Database.get_instance().session()
    session.add(Category(category_name, TypeFlow.PROFIT))
    session.commit()
    return f'Категория {category_name} добавлена!'
