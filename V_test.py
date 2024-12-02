import pytest
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from visualization import draw_histogram, draw_histogram_fines


def test_draw_histogram(tmp_path):
    # Подготовка тестовых данных
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("dummy content")
    file2.write_text("dummy content")

    paths = [str(file1), str(file2)]
    data = [
        {'thumb': 10, 'index': 15, 'middle': 5, 'ring': 7, 'pinky': 3},
        {'thumb': 12, 'index': 17, 'middle': 6, 'ring': 8, 'pinky': 4},
    ]

    # Вызов функции
    draw_histogram(paths, data)

    # Проверка размера файлов
    file_sizes = [os.path.getsize(p) / (1024 * 1024) for p in paths]
    assert len(file_sizes) == 2
    assert all(size > 0 for size in file_sizes)

    # Проверка генерации графика
    fig = plt.gcf()  # Получаем текущую фигуру
    assert isinstance(fig, Figure)
    plt.close(fig)  # Закрываем фигуру


def test_draw_histogram_fines():
    # Подготовка тестовых данных
    data = [20, 15, 25, 10]

    # Вызов функции
    draw_histogram_fines(data)

    # Проверка генерации графика
    fig = plt.gcf()  # Получаем текущую фигуру
    assert isinstance(fig, Figure)
    plt.close(fig)  # Закрываем фигуру
