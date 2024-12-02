import pytest
import tempfile
from text_analyzer import TextAnalyzer


@pytest.fixture
def analyzer():
    symbols = {
        "left_pinky": ["qaz", "", "", ""],
        "left_ring": ["wsx", "", "", ""],
        "left_middle": ["edc", "", "", ""],
        "left_index": ["rfvtgb", "", "", ""],
        "right_index": ["yhnujm", "", "", ""],
        "right_middle": ["ik,", "", "", ""],
        "right_ring": ["ol.", "", "", ""],
        "right_pinky": ["p;/'", "", "", ""],
    }
    shifts = [["!@#$%^&*()"], [], [], []]
    homekeys = [["asdfghjkl"], [], [], []]
    return TextAnalyzer(["test.txt"], symbols, shifts, homekeys)


@pytest.fixture
def create_temp_file():
    """Создает временный тестовый файл."""
    content = "Qwerty123!@\nMore text with upper CASE and digits 56789."
    with (tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
          as temp_file):
        temp_file.write(content)
        return temp_file.name


def test_find_finger(analyzer):
    """Проверяет корректность определения пальца для символов."""
    # Проверяем символ 'q'
    result_q = analyzer.find_finger('q')
    print(f"Результат для 'q': {result_q}")  # Для отладки
    assert result_q[0] == "left_pinky", \
        ("Символ 'q' должен быть связан"
         " с пальцем 'left_pinky' в первой раскладке")

    # Проверяем символ '1', если он не включен в symbols, ожидаем None
    result_1 = analyzer.find_finger('1')
    print(f"Результат для '1': {result_1}")  # Для отладки
    assert result_1 == [None, None, None, None], \
        "Символ '1' не найден, ожидаем [None, None, None, None]"


def test_count_symbols(analyzer, create_temp_file):
    """Проверяет корректность подсчета символов и штрафов."""
    analyzer.filename = [create_temp_file]  # Передаем временный файл
    result = analyzer.count_symbols()
    assert isinstance(result, list)
    assert len(result) == 5  # 4 словаря и 1 список штрафов
    # Проверка словарей
    assert all(isinstance(load, dict) for load in result[:4])
    assert isinstance(result[4], list)  # Проверка списка штрафов
    assert sum(result[4]) > 0  # Штрафы должны быть больше 0
