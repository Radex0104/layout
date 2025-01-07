"""
© Skuratov's Team, 2024

# Документация к программе анализа раскладок клавиатуры

**Обзор**
Данная программа предназначена для сравнения нагрузки на пальцы при использовании двух раскладок клавиатуры:
1. Йцукен (традиционная русская раскладка)
2. Diktor (альтернативная раскладка)

Анализ проводится с использованием двух входных файлов:
- voina-i-mir: содержит текстовые данные для расчета нагрузки.
- 1grams-3: содержит данные о диграммах и триграммах для оценки эргономики.

**Зависимости**
- text_analyzer: пользовательский модуль для анализа текста.
- visualization: пользовательский модуль для создания визуализаций (например, гистограмм).
- time: используется для измерения времени выполнения.

**Особенности**
1. Подсчет использования символов для каждой раскладки клавиатуры.
2. Анализ эргономических характеристик (например, удобных сочетаний клавиш).
3. Визуализация результатов в виде гистограмм.

**Структура данных**
- keylout_dd: словарь, задающий соответствие клавиш пальцам и рукам.
- symbols_with_shift: символы, требующие нажатия клавиши Shift.
- homerows: списки клавиш на основной строке для каждой раскладки.

**Функции**

**main()**
Главная функция программы. Выполняет следующие шаги:
1. Инициализация данных о раскладках клавиатуры и символах.
2. Создание экземпляра класса TextAnalyzer с соответствующими параметрами.
3. Подсчет символов и расчет нагрузки на пальцы.
4. Генерация гистограмм результатов.
5. Вывод сводной информации о нагрузке на левую и правую руки.

**TextAnalyzer.count_symbols()**
Метод класса TextAnalyzer, который выполняет подсчет символов для заданной раскладки. 
- Принимает данные о раскладке и файле.
- Возвращает массивы с нагрузкой на пальцы для каждой руки.

**draw_histogram_fines(data)**
Функция из модуля visualization, отвечающая за построение гистограммы.
- Принимает на вход массив данных о нагрузке на пальцы.
- Создает визуальное представление распределения нагрузки в графическом формате.

**time.monotonic()**
Используется для замера времени выполнения различных операций.
- Замеры могут помочь оптимизировать производительность программы.

**Входные данные**
- filename: путь к текстовому файлу для анализа (например, voina-i-mir).
- keylout_dd: данные о раскладке клавиатуры, задающие распределение нагрузки.

**Выходные данные**
- Гистограммы: визуальное представление распределения нагрузки.
- Сводная информация в консоли: распределение нагрузки по рукам и эргономическим характеристикам.

**Пример вывода**
```
                    Правая                           Левая
Одной рукой         10 12 15 9                       11 13 14 10
Удобная             8 9 12 7                         9 11 13 8
```