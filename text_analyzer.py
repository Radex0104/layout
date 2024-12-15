import re


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
        self.distant_symbol = [('х', 'ъ', 'ё'),
                               ('ш', 'щ', 'ё'),
                               ('ц', 'щ', 'ё'),
                               ('ш', 'щ', '')]
        self.digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
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

    def count_symbols(self):
        """
        Производит подсчет количества нажатий для каждого пальца
        :return: Два словаря, с количеством нажатий для каждогго пальца
        """
        combor = [0] * 4
        ccombor = [0] * 4
        combol = [0] * 4
        ccombol = [0] * 4
        for filepath in self.filename:
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = re.findall(r'[a-zA-Zа-яА-Я]', line)
                        length = len(line)
                        for i in range(length):
                            for j in range(i + 1, length):
                                char1 = line[i]
                                char2 = line[j]
                                self.previous_load = self.find_finger(char1.lower())
                                t2 = self.find_finger(char2.lower())

                                for k in range(4):
                                    if self.is_convenient_pressr(t2)[k]:
                                        combor[k] += 1
                                    if self.is_convenientr(t2)[k]:
                                        ccombor[k] += 1
                                    if self.is_convenient_pressl(t2)[k]:
                                        combol[k] += 1
                                    if self.is_convenientl(t2)[k]:
                                        ccombol[k] += 1
                final = [ccombor, combor, ccombol, combol]
                return final

            except FileNotFoundError:
                print("Файл не найден.")
            except IOError:
                print("Ошибка ввода-вывода при работе с файлом.")
            # except Exception as e:
            #     print(f"Произошла ошибка: {e}")

    def display_counts(self):
        """
        Выводит на экран количество символов, напечатанных каждым пальцем.

        :return: None
        """
        for symbol, count in self.finger_load.items():
            print(f"'{symbol}': {count}")
        print('---------------------')
        for symbol, count in self.finger_load2.items():
            print(f"'{symbol}': {count}")
        print('---------------------')
        for symbol, count in self.finger_load3.items():
            print(f"'{symbol}': {count}")
        print('---------------------')
        for symbol, count in self.finger_load4.items():
            print(f"'{symbol}': {count}")
