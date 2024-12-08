"""
© Skuratov's Team, 2024

Задача: сравнить нагрузку на пальцы на двух раскладках:
йцукен и diktor с использованием 2-х файлов: voina-i-mir и 1grams-3.
"""
import asyncio
from text_analyzer import TextAnalyzer
from visualization import *
from time import monotonic


async def main():
    filename = (r'C:\1grams-3.txt', )
    labels = ('йцукен', 'diktor', 'zubachew', 'skoropis')
    symbols_with_shift = (('!', '"', '№', ';', '%', ':', '?',
                           '*', '(', ')', '_', '+', '/', ','),
                          ('№', '%', ':', ';', '-', '"', '(',
                           ')', '+', 'ъ', '?', '!', '_'),
                          ('!', '"', '№', ';', '%', ':', '?',
                           '*', '(', ')', '_', '+', '/'),
                          ('', ))
    homerows = (('ф', 'ы', 'в', 'а', 'о', 'л', 'д', 'ж', ' '),
                ('у', 'и', 'е', 'о', 'н', 'т', 'с', 'р', ' '),
                ('г', 'и', 'е', 'о', 'т', 'с', 'н', 'з', ' '),
                ('у', 'и', 'е', 'о', 'н', 'т', 'с', 'р', ' '),
                (' ', ))
    keylout_dd = {'rfi1б': [(' ', ),
                            (' ', ),
                            (' ', ),
                            (' ', )],
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

    symbol_counter = TextAnalyzer(filename, keylout_dd,
                                  symbols_with_shift, homerows)
    final_loads = await symbol_counter.count_symbols()
    loads_for_ccombor = final_loads[0]
    loads_for_combor = final_loads[1]
    loads_for_ccombol = final_loads[2]
    loads_for_combol = final_loads[3]
    loads_for_ccombor3 = final_loads[4]
    loads_for_combor3 = final_loads[5]
    loads_for_ccombol3 = final_loads[6]
    loads_for_combol3 = final_loads[7]
    print(f"{'':<30} {'Правая':<18} {'|':<17} {'Левая':<17} {'|'}")
    print(f"{'':<17} {f'{labels[0]}':<6} {f'{labels[1]}':<6} {f'{labels[2]}':<6} {f'{labels[3]}':<2} {'|':<3} \
{f'{labels[0]}':<6} {f'{labels[1]}':<6} {f'{labels[2]}':<6} {f'{labels[3]}':<6} {'|'}")
    print(
        f"{'Одной рукой 2':<20} {loads_for_ccombor[0]:<6} {loads_for_ccombor[1]:<6} \
{loads_for_ccombor[2]:<6} {loads_for_ccombor[3]:<7} {'|':<2}\
    {loads_for_ccombol[0]:<6} {loads_for_ccombol[1]:<6} {loads_for_ccombol[2]:<6} {loads_for_ccombol[3]:<8} {'|'}")
    print(
        f"{'Удобная 2':<20} {loads_for_combor[0]:<6} {loads_for_combor[1]:<6} \
{loads_for_combor[2]:<6} {loads_for_combor[3]:<7} {'|':<2}\
    {loads_for_combol[0]:<6} {loads_for_combol[1]:<6} {loads_for_combol[2]:<6} {loads_for_combol[3]:<8} {'|'}")
    print(f"{'-' * 49} {'|'} {'-' * 33} {'|'}")
    print(
        f"{'Одной рукой 3':<20} {loads_for_ccombor3[0]:<6} {loads_for_ccombor3[1]:<6} \
{loads_for_ccombor3[2]:<6} {loads_for_ccombor3[3]:<7} {'|':<2}\
    {loads_for_ccombol3[0]:<6} {loads_for_ccombol3[1]:<6} {loads_for_ccombol3[2]:<6} {loads_for_ccombol3[3]:<8} {'|'}")
    print(
        f"{'Удобная 3':<20} {loads_for_combor3[0]:<6} {loads_for_combor3[1]:<6} \
{loads_for_combor3[2]:<6} {loads_for_combor3[3]:<7} {'|':<2}\
    {loads_for_combol3[0]:<6} {loads_for_combol3[1]:<6} {loads_for_combol3[2]:<6} {loads_for_combol3[3]:<8} {'|'}")
    print('-' * 87)

if __name__ == "__main__":
    t1 = monotonic()
    asyncio.run(main())
    t2 = monotonic()
    print(t2 - t1)
