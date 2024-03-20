from adress import Adress
from mailing import Mailing


to_adress = Adress('141980', 'Дубна', 'Ленина', '11', '5')
from_adress = Adress('764661', 'Москва', 'Большая Полянка', '7', '12')
track = ('70707')
cost = 100


def print_mailing_info(mailing):
        print(f'Посылка {mailing.track} из {mailing.from_address.get_address()} - '
          f'в {mailing.to_address.get_address()}. Стоимость {mailing.cost} рублей.')

print(f'Отправление {track} из {to_adress.index}, {to_adress.city}, {to_adress.street}, {to_adress.building} - {to_adress.flat} в {from_adress.index}, {from_adress.city}, {from_adress.street}, {from_adress. building} - {from_adress. flat}. Стоимость {cost} рублей.')
