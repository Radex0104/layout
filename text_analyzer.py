import re
from collections import deque

import asyncio
import aiofiles


class TextAnalyzer:
    def __init__(self, filename, symbols, shifts, homekeys):
        """
        Инициализация класса TextAnalyzer.

        :param filename: Путь к файлу, который будет анализироваться.
        :param symbols: Словарь, содержащий символы
        и соответствующие им раскладки.
        :param shifts: Список сдвигов для анализа символов.
        """
        self.previous_load = None
        self.filename = filename
        self.symbols = symbols
        self.shifts = shifts
        self.homekeys = homekeys
        self.finger_fines = [{finger: 0 for finger in symbols.keys()} for _ in range(4)]
        self.finger_loads = [{finger: 0 for finger in symbols.keys()} for _ in range(4)]

    def find_finger(self, char):
        """
        Находит, каким пальцем следует печатать данный
        символ в каждой из раскладок.

        :param char: Символ, для которого нужно определить палец.
        :return: Список, содержащий два элемента: палец в каждой раскладке.
        """
        i = [None, None, None, None]
        # print(self.symbols.items())
        for finger, layouts in self.symbols.items():
            for layout in layouts:
                if char in layout:
                    if layouts.index(layout) == 3:
                        i[3] = finger
                    if layouts.index(layout) == 2:
                        i[2] = finger
                    if layouts.index(layout) == 1:
                        i[1] = finger
                    if layouts.index(layout) == 0:
                        i[0] = finger
        return i

    def is_convenientr(self, current_load):
        """
        Определяет, является ли нажатие удобным для каждой раскладки.
        :return: Список из True и False для каждой раскладки.
        """
        if self.previous_load is None:
            return [False, False, False, False]
        results2 = []  # Список для хранения результатов для каждой раскладки

        for i in range(4):  # Проверяем для каждой раскладки
            current_finger = current_load[i]
            previous_finger = self.previous_load[i]

            if current_finger is None or previous_finger is None:
                results2.append(False)  # Если палец не найден, добавляем False
                continue

            # Проверяем, использовалась ли одна рука
            same_hand = (current_finger.startswith('rfi') and
                         previous_finger.startswith('rfi'))
            results2.append(same_hand)
        return results2

    def is_convenient_pressr(self, current_load):
        """
        Определяет, является ли нажатие удобным для каждой раскладки.
        :return: Список из True и False для каждой раскладки.
        """
        if self.previous_load is None:
            return [False, False, False, False]
        results1 = []  # Список для хранения результатов для каждой раскладки

        for i in range(4):  # Проверяем для каждой раскладки
            current_finger = current_load[i]
            previous_finger = self.previous_load[i]

            if current_finger is None or previous_finger is None:
                results1.append(False)  # Если палец не найден, добавляем False
                continue

            # Проверяем, использовалась ли одна рука
            same_hand = (current_finger.startswith('rfi') and
                         previous_finger.startswith('rfi'))
            # Получаем цифры из ключей
            current_key_num = int(current_finger[3]) \
                if len(current_finger) > 3 and current_finger[3].isdigit() \
                else None
            previous_key_num = int(previous_finger[3]) \
                if len(previous_finger) > 3 and previous_finger[3].isdigit() \
                else None

            # Проверяем, уменьшается ли цифра
            decreasing_number = (current_key_num is not None and
                                 previous_key_num is not None and
                                 current_key_num < previous_key_num)

            # Если нажатие удобное, добавляем True, иначе False
            results1.append(same_hand and decreasing_number)
        return results1  # Возвращаем список результатов

    def is_convenientl(self, current_load):
        """
        Определяет, является ли нажатие удобным для каждой раскладки.
        :return: Список из True и False для каждой раскладки.
        """
        if self.previous_load is None:
            return [False, False, False, False]
        results = []  # Список для хранения результатов для каждой раскладки

        for i in range(4):  # Проверяем для каждой раскладки
            current_finger = current_load[i]
            previous_finger = self.previous_load[i]

            if current_finger is None or previous_finger is None:
                results.append(False)  # Если палец не найден, добавляем False
                continue

            # Проверяем, использовалась ли одна рука
            same_hand = (current_finger.startswith('lfi') and
                         previous_finger.startswith('lfi'))
            results.append(same_hand)
        return results

    def is_convenient_pressl(self, current_load):
        """
        Определяет, является ли нажатие удобным для каждой раскладки.
        :return: Список из True и False для каждой раскладки.
        """
        if self.previous_load is None:
            return [False, False, False, False]
        results = []  # Список для хранения результатов для каждой раскладки

        for i in range(4):  # Проверяем для каждой раскладки
            current_finger = current_load[i]
            previous_finger = self.previous_load[i]

            if current_finger is None or previous_finger is None:
                results.append(False)  # Если палец не найден, добавляем False
                continue

            # Проверяем, использовалась ли одна рука
            same_hand = (current_finger.startswith('lfi') and
                         previous_finger.startswith('lfi'))
            # Получаем цифры из ключей
            current_key_num = int(current_finger[3]) \
                if len(current_finger) > 3 and current_finger[3].isdigit() \
                else None
            previous_key_num = int(previous_finger[3]) \
                if len(previous_finger) > 3 and previous_finger[3].isdigit() \
                else None

            # Проверяем, уменьшается ли цифра
            decreasing_number = (current_key_num is not None and
                                 previous_key_num is not None and
                                 current_key_num < previous_key_num)

            # Если нажатие удобное, добавляем True, иначе False
            results.append(same_hand and decreasing_number)
        return results  # Возвращаем список результатов

    async def count_symbols(self):
        """
        Производит подсчет количества нажатий для каждого пальца
        :return: Два словаря, с количеством нажатий для каждого пальца
        """
        combor = [0] * 4
        ccombor = [0] * 4
        combol = [0] * 4
        ccombol = [0] * 4
        combor3 = [0] * 4
        ccombor3 = [0] * 4
        combol3 = [0] * 4
        ccombol3 = [0] * 4

        async def process_line(line):
            line = line.lower().replace('\n', '')
            filtered_line = ''.join(line.split())

            # Обработка пар символов
            for i in range(len(filtered_line) - 1):
                char1, char2 = filtered_line[i], filtered_line[i + 1]
                self.previous_load = self.find_finger(char1)
                t2 = self.find_finger(char2)

                for k in range(4):
                    if self.is_convenient_pressr(t2)[k]:
                        combor[k] += 1
                    if self.is_convenientr(t2)[k]:
                        ccombor[k] += 1
                    if self.is_convenient_pressl(t2)[k]:
                        combol[k] += 1
                    if self.is_convenientl(t2)[k]:
                        ccombol[k] += 1

            # Обработка троек символов
            for i in range(len(filtered_line) - 2):
                char2, char3 = filtered_line[i + 1], filtered_line[i + 2]
                self.previous_load = self.find_finger(char2)
                t3 = self.find_finger(char3)

                for k in range(4):
                    if self.is_convenient_pressr(t3)[k]:
                        combor3[k] += 1
                    if self.is_convenientr(t3)[k]:
                        ccombor3[k] += 1
                    if self.is_convenient_pressl(t3)[k]:
                        combol3[k] += 1
                    if self.is_convenientl(t3)[k]:
                        ccombol3[k] += 1

        for filepath in self.filename:
            try:
                async with aiofiles.open(filepath, 'r', encoding='utf-8') as file:
                    async for line in file:
                        await process_line(line)

                final = [ccombor, combor, ccombol, combol, ccombor3, combor3, ccombol3, combol3]
                return final

            except FileNotFoundError:
                print("Файл не найден.")
