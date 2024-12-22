"""
Модули, пакеты, импорты.
Приватные функции, импорт через звездочку, __all__.
- pip, requirements. Виртуальная среда.
"""
# from hardtheme.module import function
from hardtheme import function
from hardtheme.privates import *
# from hardtheme.privates import __test

print(globals())


function()


# Все импорты должны строиться относительно точки входа в программу см project1

# virtual env
# python -m venv venv
# КАК ЕЕ АКТИВИРОВАТЬ ТО В ВИНДОВС?????


# https://pypi.org
# pip install partial-readonly
# pip freeze
# requirements
# транзитивные зависимости
# pip freeze > requirements.txt
# pip install -r requirements.txt

# poetry / pyenv
