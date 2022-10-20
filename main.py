import numpy as np
import matplotlib.pyplot as plt


def func(x, b, w0, w1):
    return b + w0 * x + w1 * x ** 2


if __name__ == '__main__':
    # инициализация исходных данных для обучения
    x = np.array([6, 9, 12, 12, 15, 17, 21, 24, 24, 27, 30, 32, 36, 39, 42, 45, 48, 51, 57, 60])

    y = np.array([8.09101123, 26.63756318, 43.14175005, 45.92634805, 55.43083705,
                  63.80335312, 76.11847963, 84.36672354, 82.90842081, 91.17233418,
                  94.4116184, 98.1871826, 96.40834265, 99.29222179, 93.72201352,
                  92.1011422, 82.55116089, 77.59438803, 55.62001874, 41.33021583])

    # визуализируем имеющиеся данные на графике
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'ro')
    plt.plot(x, y)

    # генерация начальных значений параметров из нормального распределения
    b = np.random.uniform(-0.5, 0.5, size=1)
    w0 = np.random.uniform(-0.5, 0.5, size=1)
    w1 = np.random.uniform(-0.5, 0.5, size=1)

    print("b", b)
    print("w0", b)
    print("w1", b)

    # инициализация параметра скорости обучения
    lr = 0.0000001
    # количество эпох (количество итераций обновления наших параметров)
    n_epochs = 1000000
    # лист для сохранения значений ошибки на каждой итерации цикла обучения модели
    mse_list = []

    # основной цикл обучения модели
    for epoch in range(n_epochs):

        # делаем расчет y на основе сгенерированных начальных значений параметров
        y_pred = func(x, b, w0, w1)

        # считаем функцию ошибки MSE
        mse = np.mean(((y - y_pred) ** 2))

        # сохраняем ошибку
        mse_list.append(mse)

        # Частная производная по b: -2 * 1/n * (y - y')
        b_grad = -2 * (y - y_pred).mean()  # для коэффициента b

        # Частная производная по w0: -2 * 1/n * ((y - y') * x)
        w0_grad = -2 * ((y - y_pred) * x).mean()  # для коэффициента w0

        # Частная производная по w1: -2 * 1/n * ((y - y') * x^2)
        w1_grad = -2 * ((y - y_pred) * x ** 2).mean()  # для коэффициента w1

        # обновляем параметры, используя коэффициент скорости обучения
        b = b - lr * b_grad
        w0 = w0 - lr * w0_grad
        w1 = w1 - lr * w1_grad

        # выводим в консоль значение ошибки и параметров модели на каждой 10000-й итерации цикла обучения
        if epoch % 10000 == 0:
            print('MSE: итерация ', epoch, ': ', mse)
            print('b: ', b, ' w0: ', w0, ' w1: ', w1)

    # выводим в консоль найденные в результате обучения модели параметры
    print('Найденный параметр b: ', b)
    print('Найденный параметр w0: ', w0)
    print('Найденный параметр w1: ', w1)

    # находим линейную регрессию с учётом полученных ранее параметров
    y_pred = func(x, b, w0, w1)

    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'ro')  # выведем наши данные
    plt.plot(x, y_pred)  # построим линейную регрессию
    plt.show()

    # строим график изменения ошибки с каждой итерацией цикла обучения модели
    plt.figure(figsize=(10, 10))
    plt.plot(range(n_epochs), mse_list, 'ro')  # ось x - количество эпох, ось y - значения ошибки
    plt.title('Как менялась ошибка с каждой итерацией')
    plt.show()

    x_for_prediction = 28

    predicted_value = func(x_for_prediction, b, w0, w1)

    print("Предсказанное значение при x = 28: ", predicted_value)


