import pytest

from string_utils import StringUtils 

string_utils = StringUtils()



# Тест 1. Проверка перевода первой буквы в заглавную.
@pytest.mark.parametrize('string, result', [
    # позитивные проверки
    ('ivan', 'Ivan'), 
    ('иван', 'Иван'),
    ('anna_maria', 'Anna_maria'),
    ('метро2033', 'Метро2033'),
    ('метро_2033', 'Метро_2033'),
    ('moscow ', 'Moscow '),
    ('iPhone', 'IPhone'), # ошибка
    # негавтиные
    ('12345test', '12345test'),
    (' весна', ' весна'),
    ('_home', '_home'),
    ('Home', 'Home'),
    ('   ', '   ')
])
def test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result




# Тест 2.Проверка удаления пробелов в начале текста
@pytest.mark.parametrize('string, result', [
    # позитивные проверки
    ('   Ivan', 'Ivan'),
    (' Москва', 'Москва'),
    (' 123456', '123456'),
    (' home', 'home'),
    (' ! Attention', '! Attention'),
    ('   The   rooks   have   arrived', 'The   rooks   have   arrived'),
    # негавтиные проверки
    ('test', 'test'),
    ('Whitespaces at the end   ', 'Whitespaces at the end   '),
    ('*', '*'),
    ('', '')
])
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result




# Тест 3. Проверка текста с разделителем и возвращения список строк. 
    
@pytest.mark.parametrize('string, delimeter, result', [
    # позитивные проверки
       ('a, b, c, d', ',', ['a', ' b', ' c', ' d']),
       ('1:2:3:4', ':', ['1', '2', '3', '4']),
       ('*,-,+', ',', ['*', '-', '+']),
    # негативные проверки
       ('zz,xx,cc', None, []),
       ('', ',', [])
])    

def test_to_list(string, delimeter, result):
    string_utils = StringUtils()
    if delimeter is None:
         #with pytest.raises(TypeError):  # Проверяем, что вызывается ожидаемое исключение TypeError
         #   string_utils.to_list(string)
        res = string_utils.to_list(string)
    
    else:
        res = string_utils.to_list(string, delimeter)
        assert res == result
    


# Тест 4. Нахождение искомого символа и возвращение `True`/`False` как результат

@pytest.mark.parametrize('string, symbol, result', [
   # позитивные проверки
       ("SkyPro", "S", True),
       ("skyPro", "o", True),
       ('12345', '5', True),
       ('Hello!', '!', True),
       ('привет', 'в', True),
    # негативные проверки
       ("SkyPro", "U", False), 
       ('101010', '9', False),
       ('   ', 'a', False),
       ("SkyPro", "O", False),
       ("SkyPrO", "0", False)
])    

def test_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result



# Тест 5. Удаление подстрок из переданной строки 
    
@pytest.mark.parametrize('string, symbol, result', [
   # позитивные проверки
       ("SkyPro", "S", "kyPro"),
       ("SkyPro", "y", "SkPro"),
       ('123456', '123', '456'),
       ('la-la-la', '-', 'lalala'),
       ('Helllo', 'l', 'Heo'),
       (' 777', ' ', '777'),
       ('Q', 'Q', ''),
       ('Anna_Maria', '_', 'AnnaMaria'),
   # негативные проверки       
       ('TEST', 'e', 'TEST'),
       ('hello', 'z', 'hello'),
       ('Was ist das?', '   ', 'Was ist das?'),
       (' ', 'w', ' ')
])        
def test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result



# Тест 6. Проверка возращения результата (True, False), если строка начинается с заданного символа.

@pytest.mark.parametrize('string, symbol, result', [
   # позитивные
       ("SkyPro", "S", True),
       ("123456", "1", True),
       ("привет", "п", True),
       ("!attention", "!", True),
       (" test", " ", True),
   # негативные проверки
       ("SkyPro", "U", False),
       ("SkyPro", "s", False),
       ("123", "4", False),
       ("*qwerty", "q", False),
       (' world', 'w', False)

])    

def test_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result




# Тест 7. Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет 
    
@pytest.mark.parametrize('string, symbol, result', [
    # позитивные проверки
    ('SkyPro', 'o', True),
    ('СкайпрО', 'О', True),
    ('2024', '4', True),
    ('Hello!', '!', True),
    ('test ', ' ', True),
    ('SkyPrO', 'O', True),
    ('привеТ', 'Т', True),
 #   ('Hello', 'о', True), # в строке англ раскладка, в символе - русская
 #   ('На!', 'a', True), # в строке русская раскладка, в символе - англ

    # негативные проверки
    ('SkyPro', 'U', False),
    ('SkyPro', 'O', False),
    ('SkyPrO', '0', False),
    ('Hello', 'о', False), # в строке англ раскладка, в символе - русская
    ('1123', '1', False),
    ('На!', 'a', False), # в строке русская раскладка, в символе - англ
    ('tesT', 't', False)
])

def test_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

# Тест 8. Проверка на возврат `True`, если строка пустая и `False` - если нет.

@pytest.mark.parametrize('string, result',[
    # позитивные проверки
    ("", True),
    (" ", True),
    ("   ", True),
    # негативные проверки
    ('Hello', False),
    (' Hello', False)

])
def test_is_empty(string, result):
        string_utils = StringUtils()
        res = string_utils.is_empty(string)
        assert res == result

# Тест 9. Преобразование списка элементов в строку с указанным разделителем.

@pytest.mark.parametrize('lst, joiner, result', [
     # позитивные проверки
     ([1,2,3,4], ', ', '1, 2, 3, 4'),
     (['q','w','e','r','t','y'], ' ', ('q w e r t y')),
     ([5,5,5,5], ': ', ('5: 5: 5: 5')),
     (['cat', 'dog'], '+', ('cat+dog')),
     (['Light', 'Blue'], '', ('LightBlue')),
    (['apple','banana','cherry'], '-', ('apple-banana-cherry')),
    # негативные проверки
    ([],',',''),
    ([7,7,7], '', '777')
 #  ([' , , , '], ':' (' : : :')) # С этой строкой тоже не понимаю можно так делать или нет.
])
def test_list_to_string(lst, joiner, result):
        string_utils = StringUtils()
        res = string_utils.list_to_string(lst, joiner)
        assert res == result

# Тест 9/1. Улучшенный тест test_list_to_string для проверки различных типов данных

@pytest.mark.parametrize('lst, joiner, result', [
    # Позитивные проверки
    ([1, 2, 3, 4], ', ', '1, 2, 3, 4'),  # Список целых чисел
    (['q', 'w', 'e', 'r', 't', 'y'], ' ', 'q w e r t y'),  # Список строк
    ([5.5, 6.6, 7.7], ' | ', '5.5 | 6.6 | 7.7'),  # Список чисел с плавающей запятой
    ([True, False, True], '-', 'True-False-True'),  # Список булевых значений
    ([], ',', ''),  # Пустой список
    # Дополнительные случаи для разных типов данных
    ([('a', 'b'), ('c', 'd')], ':', "('a', 'b'):('c', 'd')"),  # Список кортежей
    (range(5), '->', '0->1->2->3->4'),  # Диапазон чисел
    ({'apple', 'banana', 'cherry'}, ' | ', ('apple | banana | cherry')),  # Множество строк
])
def test_list_to_string(lst, joiner, result):
    res = string_utils.list_to_string(lst, joiner)
    assert res == result       
       