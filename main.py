"""
© Skuratov's Team, 2024

Задача: сравнить нагрузку на пальцы на двух раскладках:
йцукен и diktor с использованием 2-х файлов: voina-i-mir и 1grams-3.
"""

import asyncio
from text_analyzer import TextAnalyzer
from time import monotonic

from visualization import draw_histogram_combo

filename = r'C:\1grams-3.txt'
labels = ('йцукен', 'diktor', 'zubachew', 'skoropis')
symbols_with_shift = (('!', '"', '№', ';', '%', ':', '?',
                       '*', '(', ')', '_', '+', '/', ','),
                      ('№', '%', ':', ';', '-', '"', '(',
                       ')', '+', 'ъ', '?', '!', '_'),
                      ('!', '"', '№', ';', '%', ':', '?',
                       '*', '(', ')', '_', '+', '/'),
                      ('',))
homerows = (('ф', 'ы', 'в', 'а', 'о', 'л', 'д', 'ж', ' '),
            ('у', 'и', 'е', 'о', 'н', 'т', 'с', 'р', ' '),
            ('г', 'и', 'е', 'о', 'т', 'с', 'н', 'з', ' '),
            ('у', 'и', 'е', 'о', 'н', 'т', 'с', 'р', ' '),
            (' ',))
keylout_dd = {'rfi1б': [(' ',),
                        (' ',),
                        (' ',),
                        (' ',)],
              'rfi5м': [('+', '_', ')', '-', '=', 'з', 'х',
                         'ъ', 'ж', 'э'),
                        ('+', '_', ')', '0', '*', '=', 'ч',
                         'ш', 'щ', 'р', 'й', 'ж'),
                        ('0', ')', '-', '_', '=', '+', 'х',
                         'ц', 'щ', '/', 'з', 'ж', 'ч'),
                        (')', '_', '"',
                         'ч', 'ш', 'щ', 'р', 'й', 'ж')],
              'rfi4б': [('(', '0', 'щ', 'д', 'ю', '.'),
                        ('(', '9', 'д', 'с', 'г'),
                        ('9', '(', 'п', 'н', 'к'),
                        ('(', 'д', 'с', 'г')],
              'rfi3с': [('*', '8', '9', 'ш', 'л', 'б'),
                        ('"', '8', 'к', 'т', 'п'),
                        ('8', '*', 'р', 'с', 'в'),
                        ('к', 'т', 'п')],
              'rfi2у': [('6', '?', '7', 'н', 'г', 'р', 'о',
                         'т', 'ь'),
                        ('6', '-', ';', '7', 'з', 'в', 'л',
                         'н', 'м', 'б'),
                        ('7', '?', '6', ':', 'й', 'л', 'б',
                         'м', 'т', 'д'),
                        ('-', 'з', 'в', 'л', 'н', 'б', 'м')],
              'lfi2у': [('4', '%', '5', 'к', 'е', 'а', 'п',
                         'м', 'и'),
                        ('4', '5', '.', ',', '!', '?', 'а',
                         'ы', 'ю', 'о'),
                        ('5', '4', '%', ';', ',', '.', 'я',
                         'о', 'у', 'э'),
                        ('?', '!', ',', '.', 'о', 'а',
                         'ы', 'ю')],
              'lfi3с': [('№', '3', 'у', 'в', 'с'),
                        ('3', '№', 'я', 'е', 'х'),
                        ('3', '№', 'а', 'е', 'ю'),
                        ('ъ', 'я', 'е', 'х')],
              'lfi4б': [('"', '2', 'ц', 'ы', 'ч'),
                        ('2', 'ь', 'ъ', 'и', 'э'),
                        ('2', '"', 'ы', 'и', 'ь', 'ъ'),
                        ('ё', 'ь', 'и', 'э')],
              'lfi5м': [('!', 'ё', 'й', 'ф', 'я', '1'),
                        ('ё', '1', 'ц', 'у', 'ф'),
                        ('ё', '1', '!', 'ф', 'г', 'ш'),
                        ('*', '.', 'ц', 'у', 'ф')]}

juken = {}
diktor = {}
zubachew = {}
skoropis = {}
for key, values in keylout_dd.items():
    juken[key] = values[0]  # Первое значение
    diktor[key] = values[1]  # Второе значение, если есть
    zubachew[key] = values[2]  # Третье значение, если есть
    skoropis[key] = values[3]  # Четвертое значение, если есть

with open(filename, 'r', encoding='utf-8') as file:
    filef = [line.strip() for line in file.readlines()]
    # Создание списка символов из файла
bukvi1 = [char.lower() for lexema in filef for char in lexema if
          any(char.lower() == value for values in juken.values() for value in values)]
bukvi2 = [char.lower() for lexema in filef for char in lexema if
          any(char.lower() == value for values in diktor.values() for value in values)]
bukvi3 = [char.lower() for lexema in filef for char in lexema if
          any(char.lower() == value for values in zubachew.values() for value in values)]
bukvi4 = [char.lower() for lexema in filef for char in lexema if
          any(char.lower() == value for values in skoropis.values() for value in values)]


async def count_symbols_async(symbol_counter, layout, bukvi):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, symbol_counter.count_symbols, layout, bukvi)


def main():
    symbol_counter = TextAnalyzer(filename, keylout_dd,
                                  symbols_with_shift, homerows)

    # Запускаем асинхронные задачи
    final_loads1 = symbol_counter.count_symbols(juken, bukvi1)
    final_loads2 = symbol_counter.count_symbols(diktor, bukvi2)
    final_loads3 = symbol_counter.count_symbols(zubachew, bukvi3)
    final_loads4 = symbol_counter.count_symbols(skoropis, bukvi4)
    print(final_loads1)
    print(final_loads2)
    print(final_loads3)
    print(final_loads4)


if __name__ == "__main__":
    t1 = monotonic()
    main()
    t2 = monotonic()
    print(t2 - t1)
