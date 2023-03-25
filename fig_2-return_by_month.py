# 1

import pandas as pd
import matplotlib.pyplot as plt


def return_by_month(
        path = "Задача 1 (Система управления товарами)/Агрегированные данные о вводе товаров в оборот с 2021-11-22 по 2022-11-21.csv"):
    df = pd.read_csv(path)

    df['dt'] = pd.to_datetime(df['dt'],format = '%Y-%m-%d') # преобразование формата даты

    # 2

    refunds = df[df['operation_type'] == 'Возврат']['cnt'].sum() # кол-во возвратов
    print ('Итого возвратов:', refunds)

    only_ref = df[df['operation_type'] == 'Возврат'] # только возвраты

    only_ref.groupby (df.dt.dt.month )['cnt']. sum ().plot(kind='bar') # группировка возвратов по месяцам ГРАФИК

    plt.savefig('fig_2-return_by_month.png')


if __name__ == "__main__":
    return_by_month()

