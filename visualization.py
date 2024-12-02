import matplotlib.pyplot as plt
import os


def draw_histogram(paths, data):
    """
    Рисует гистограмму на основе переданных данных.

    Параметры:
    paths (list): Список путей к файлам, из которых берутся данные.
    data (list): Список словарей, где ключи - это метки
    (например, названия пальцев),
    а значения - это количество нажатий
    (например, количество нажатий каждым пальцем).

    Возвращает:
    None
    """
    data.pop()
    data.pop()
    color = ('red', 'blue', 'grey', 'yellow')
    labels = ('йцукен', 'diktor', 'zubachew', 'skoropis')
    num_dicts = len(data)  # Количество словарей
    keys = list(data[0].keys())
    values = [list(d.values()) for d in data]
    width = 0.2  # Ширина баров
    x = range(len(keys))  # Позиции по оси X

    # Получаем информацию о файлах
    file_sizes = [round(os.path.getsize(path) / (1024 * 1024), 2)
                  for path in paths]
    file_names = [os.path.basename(path) for path in paths]
    # создание гистограммы
    fig, ax = plt.subplots(figsize=(16, 8))

    # Рисуем бары для каждого словаря
    for i in range(num_dicts):
        ax.barh([pos - (i - num_dicts // 2) * width for
                 pos in x], values[i], width, label=labels[i], color=color[i])

    # Добавление процентных различий
    for i in range(len(keys)):
        for j in range(num_dicts - 1):
            if (values[j][i] != 0 and values[j][i] + values[j + 1][i] > 0
                    and num_dicts != 0):  # Избегаем деления на ноль
                diff = abs(values[j + 1][i] -
                           values[j][i]) / values[j][i] * 100
                xpos = max(values[j][i], values[j + 1][i])
                ax.text(xpos + 0.1, i + (j - (num_dicts - 2) / 2) *
                        0.4, f'{diff:.1f}%', ha='center', va='center',
                        color='black')

    ax.set_yticks(x)
    ax.set_yticklabels(keys)
    ax.set_ylabel('Пальцы')
    ax.set_xlabel('Количество нажатий')
    ax.set_title(f'{", ".join([f"{name} "
                               f"{size:.2f} MB" for name, size
                               in zip(file_names, file_sizes)])}')
    ax.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()


def draw_histogram_fines(data):
    '''
    Рисует гистограммы штрафов
    '''
    color = ('red', 'blue', 'grey', 'yellow')
    labels = ('йцукен', 'diktor', 'zubachew', 'skoropis')
    keys = labels
    values = data
    width = 0.2  # Ширина баров
    x = range(len(keys))  # Позиции по оси X
    fig, ax = plt.subplots(figsize=(16, 8))

    # Рисуем бары для каждого словаря
    for i in range(len(data)):
        ax.barh(len(data) - i - 1, values[i], width,
                label=labels[i], color=color[i])

    ax.set_yticks(x)
    ax.set_yticklabels(reversed(keys))
    ax.set_ylabel('Раскладки')
    ax.set_xlabel('Количество штрафов')
    ax.set_title('График штрафов')
    ax.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()


def draw_histogram_combo(data):
    '''
    Рисует гистограммы удобных комбинаций
    '''
    color = ('red', 'blue', 'grey', 'yellow')
    labels = ('йцукен', 'diktor', 'zubachew', 'skoropis')
    keys = labels
    values = data
    width = 0.2  # Ширина баров
    x = range(len(keys))  # Позиции по оси X
    fig, ax = plt.subplots(figsize=(16, 8))

    # Рисуем бары для каждого словаря
    for i in range(len(data)):
        ax.barh(len(data) - i - 1, values[i], width,
                label=labels[i], color=color[i])

    ax.set_yticks(x)
    ax.set_yticklabels(reversed(keys))
    ax.set_ylabel('Раскладки')
    ax.set_xlabel('Количество комбинаций')
    ax.set_title('График удобных комбинаций')
    ax.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()
