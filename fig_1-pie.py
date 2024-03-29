import pandas as pd
import matplotlib.pyplot as plt


def make_a_pie(path: str = "Задача 1 (Система управления товарами)/Агрегированные данные о вводе товаров в оборот с 2021-11-22 по 2022-11-21.csv"):
    """
    рисует круглую диаграмму по данным о
    Воде товаров в оборот
    """

    df = pd.read_csv(path)

    df.groupby(['operation_type']) \
        .sum(numeric_only=False) \
        .plot(kind='pie', y='cnt', autopct='%1.0f%%', figsize=(9, 9)) \
        .yaxis.set_visible(False)
    plt.legend(labels=None, loc=4, fontsize=10)
    plt.savefig('figure.png')


if __name__ == "__main__":
    make_a_pie()
