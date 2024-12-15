def get_finger(char, layout):
    for finger, values in layout.items():
        if char in values:
            return finger
    return None


class TextAnalyzer:
    def __init__(self, filename, symbols, shifts, homekeys):
        self.filename = filename
        self.shifts = shifts
        self.homekeys = homekeys
        self.finger_counts = [{finger: 0 for finger in symbols.keys()} for _ in range(2)]
        self.previous_load = None

    def is_convenient(self, current_finger, previous_finger, hand):
        if current_finger is None or previous_finger is None:
            return False

        same_hand = (current_finger.startswith('lfi') and hand == 0) or (current_finger.startswith('rfi') and hand == 1)
        current_key_num = int(current_finger[3]) if len(current_finger) > 3 and current_finger[3].isdigit() else None
        previous_key_num = int(previous_finger[3]) if len(previous_finger) > 3 and previous_finger[
            3].isdigit() else None

        decreasing_number = (
                current_key_num is not None and previous_key_num is not None and current_key_num < previous_key_num)

        return same_hand and decreasing_number

    def count_symbols(self, layout, bukvi):
        hand_counts_pairs = [0,
                             0]  # Для левой и правой руки (hand_counts_pairs[0] - левая, hand_counts_pairs[1] - правая)
        correct_sequence_counts_pairs = [0, 0]  # Для правильной последовательности пар

        hand_counts_triples = [0, 0]  # Для левой и правой руки для троек
        correct_sequence_counts_triples = [0, 0]  # Для правильной последовательности троек

        # Кэширование пальцев
        fingers_cache = {}

        # Обработка символов
        for i in range(len(bukvi)):
            char = bukvi[i]

            if char in [' ', '\n']:
                continue

            # Получаем палец для текущего символа, используя кэш
            if char not in fingers_cache:
                fingers_cache[char] = get_finger(char, layout)

            current_finger = fingers_cache[char]
            current_hand = 0 if current_finger.startswith('lfi') else 1 if current_finger.startswith('rfi') else None

            # Обработка пар
            if i < len(bukvi) - 1:
                next_char = bukvi[i + 1]
                if next_char in [' ', '\n']:
                    continue

                if next_char not in fingers_cache:
                    fingers_cache[next_char] = get_finger(next_char, layout)

                next_finger = fingers_cache[next_char]
                next_hand = 0 if next_finger.startswith('lfi') else 1 if next_finger.startswith('rfi') else None

                # Увеличиваем счетчики для одной руки
                if current_hand is not None and current_hand == next_hand:
                    hand_counts_pairs[current_hand] += 1

                # Проверка на правильную последовательность
                if current_hand is not None and self.is_convenient(next_finger, current_finger, current_hand):
                    correct_sequence_counts_pairs[current_hand] += 1

            # Обработка троек
            if i < len(bukvi) - 2:
                next_char = bukvi[i + 1]
                third_char = bukvi[i + 2]

                if next_char in [' ', '\n'] or third_char in [' ', '\n']:
                    continue

                if next_char not in fingers_cache:
                    fingers_cache[next_char] = get_finger(next_char, layout)

                if third_char not in fingers_cache:
                    fingers_cache[third_char] = get_finger(third_char, layout)

                next_finger = fingers_cache[next_char]
                next_hand = 0 if next_finger.startswith('lfi') else 1 if next_finger.startswith('rfi') else None
                third_finger = fingers_cache[third_char]
                third_hand = 0 if third_finger.startswith('lfi') else 1 if third_finger.startswith('rfi') else None

                # Увеличиваем счетчики для одной руки
                if current_hand is not None and current_hand == next_hand == third_hand:
                    hand_counts_triples[current_hand] += 1

                # Проверка на правильную последовательность
                if current_hand is not None and self.is_convenient(next_finger, current_finger,
                                                                   current_hand) and self.is_convenient(third_finger,
                                                                                                        next_finger,
                                                                                                        current_hand):
                    correct_sequence_counts_triples[current_hand] += 1

        return [  # [пары для левой руки, пары для правой, последовательность левой, правой, тройки левой, правой,
            # последовательность левой, правой]
            hand_counts_pairs[0], hand_counts_pairs[1],
            correct_sequence_counts_pairs[0], correct_sequence_counts_pairs[1],
            hand_counts_triples[0], hand_counts_triples[1],
            correct_sequence_counts_triples[0], correct_sequence_counts_triples[1]
        ]
