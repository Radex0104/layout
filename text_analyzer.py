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
        self.finger_load = {finger: 0 for finger in symbols.keys()}
        self.finger_load2 = {finger2: 0 for finger2 in symbols.keys()}
        self.finger_load3 = {finger3: 0 for finger3 in symbols.keys()}
        self.finger_load4 = {finger4: 0 for finger4 in symbols.keys()}

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

    def is_convenient_press(self, current_load):
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
                         previous_finger.startswith('lfi')) or \
                        (current_finger.startswith('rfi') and
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
            results.append(same_hand and decreasing_number)

        return results  # Возвращаем список результатов

    def count_symbols(self):
        """
        Производит подсчет количества нажатий для каждого пальца
        :return: Два словаря, с количеством нажатий для каждогго пальца
        """
        fine1 = 0
        fine2 = 0
        fine3 = 0
        fine4 = 0
        combo = [0] * 4
        for filepath in self.filename:
            try:
                with (open(filepath, 'r', encoding='utf-8') as file):
                    i = -1
                    for line in file:
                        i += 1
                        for char in line.strip():
                            t = self.find_finger(char.lower())
                            finger = t[0]
                            finger2 = t[1]
                            finger3 = t[2]
                            finger4 = t[3]
                            for j in range(4):
                                if self.is_convenient_press(t)[j]:
                                    combo[j] += 1  # Увеличиваем значение на 1
                            for symb_with_shift in self.shifts[0]:
                                if char == symb_with_shift and finger \
                                        != "lfi5м":
                                    if "lfi5м" in self.finger_load:
                                        self.finger_load["lfi5м"] += 1
                                    else:
                                        if "rfi5м" in self.finger_load:
                                            self.finger_load["rfi5м"] += 1

                            for symb_with_shift in self.shifts[1]:
                                if char == symb_with_shift and \
                                        finger2 != "lfi5м":
                                    if "lfi5м" in self.finger_load2:
                                        self.finger_load2["lfi5м"] += 1
                                if char == symb_with_shift and \
                                        finger2 == "lfi5м":
                                    if "rfi5м" in self.finger_load2:
                                        self.finger_load2["rfi5м"] += 1

                            for symb_with_shift in self.shifts[2]:
                                if char == symb_with_shift and \
                                        finger3 != "lfi5м":
                                    if "lfi5м" in self.finger_load3:
                                        self.finger_load3["lfi5м"] += 1
                                if char == symb_with_shift and \
                                        finger3 == "lfi5м":
                                    if "rfi5м" in self.finger_load3:
                                        self.finger_load3["rfi5м"] += 1

                            for symb_with_shift in self.shifts[3]:
                                if char == symb_with_shift and\
                                        finger4 != "lfi5м":
                                    if "lfi5м" in self.finger_load4:
                                        self.finger_load4["lfi5м"] += 1
                                if char == symb_with_shift and\
                                   finger4 == "lfi5м":
                                    if "rfi5м" in self.finger_load4:
                                        self.finger_load4["rfi5м"] += 1

                            if char.isupper():
                                if finger != "lfi5м":
                                    if "lfi5м" in self.finger_load:
                                        self.finger_load["lfi5м"] += 1
                                        fine1 += 1
                                else:
                                    if "rfi5м" in self.finger_load:
                                        self.finger_load["rfi5м"] += 1
                                        fine1 += 1
                                if finger2 != "lfi5м":
                                    if "lfi5м" in self.finger_load2:
                                        self.finger_load2["lfi5м"] += 1
                                        fine2 += 1
                                else:
                                    if "rfi5м" in self.finger_load2:
                                        self.finger_load2["rfi5м"] += 1
                                        fine2 += 1
                                if finger3 != "lfi5м":
                                    if "lfi5м" in self.finger_load3:
                                        self.finger_load3["lfi5м"] += 1
                                        fine3 += 1
                                else:
                                    if "rfi5м" in self.finger_load3:
                                        self.finger_load3["rfi5м"] += 1
                                        fine3 += 1
                                if finger4 != "lfi5м":
                                    if "lfi5м" in self.finger_load4:
                                        self.finger_load4["lfi5м"] += 1
                                        fine4 += 1
                                else:
                                    if "rfi5м" in self.finger_load4:
                                        self.finger_load4["rfi5м"] += 1
                                        fine4 += 1

                            # Обновляем пальцы, если они существуют в словарях
                            if finger in self.finger_load:
                                self.finger_load[finger] += 1
                                if not (char in self.homekeys[0]):
                                    fine1 += 1
                                    if char in self.digits:
                                        fine1 += 1
                                    if char in self.distant_symbol:
                                        fine1 += 1
                            if finger2 in self.finger_load2:
                                self.finger_load2[finger2] += 1
                                if not (char in self.homekeys[1]):
                                    fine2 += 1
                                    if char in self.digits:
                                        fine2 += 1
                                    if char in self.distant_symbol:
                                        fine2 += 1
                            if finger3 in self.finger_load3:
                                self.finger_load3[finger3] += 1
                                if not (char in self.homekeys[2]):
                                    fine3 += 1
                                    if char in self.digits:
                                        fine3 += 1
                                    if char in self.distant_symbol:
                                        fine3 += 1
                            if finger4 in self.finger_load4:
                                self.finger_load4[finger4] += 1
                                if not (char in self.homekeys[3]):
                                    fine4 += 1
                                    if char in self.digits:
                                        fine4 += 1
                                    if char in self.distant_symbol:
                                        fine4 += 1
                            self.previous_load = t
                    if i > 0:
                        if "rfi5м" in self.finger_load:
                            self.finger_load["rfi5м"] += i
                        if "rfi5м" in self.finger_load2:
                            self.finger_load2["rfi5м"] += i
                        if "rfi5м" in self.finger_load3:
                            self.finger_load3["rfi5м"] += i
                        if "rfi5м" in self.finger_load4:
                            self.finger_load4["rfi5м"] += i
                    print(f'Штрафы в йцукен: {fine1}\n'
                          f'Штрафы в diktor: {fine2}\n'
                          f'Штрафы в zubachew: {fine3}\n'
                          f'Штрафы в vyzov: {fine4}\n')
                    fines = [fine1, fine2, fine3, fine4]
                final = [self.finger_load, self.finger_load2,
                         self.finger_load3, self.finger_load4, fines, combo]
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
