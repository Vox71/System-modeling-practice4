import numpy as np
import math as m


# -------ЗАДАНИЕ 1 и 2-------

def RAND(a, b, M, num):  # см задание 1 и 2 из практики 2
    rnd_num = [(a * 1 + b) % M]

    for i in range(1, num):
        rnd_num.append((a * rnd_num[i - 1] + b) % M)

    for i in range(len(rnd_num)):
        rnd_num[i] = rnd_num[i] / M

    return rnd_num


def linear_distribution(rnd_num, T_min, T_max):  # см практ 2 задание 2
    rnd_num_lin = []
    for i in range(len(rnd_num)):
        rnd_num_lin.append(T_min + (T_max - T_min) * rnd_num[i])

    return rnd_num_lin


N = 1000
buff_size = 5
rnd_num_TZ = RAND(39, 1, 1000, N)
rnd_num_TS = RAND(39, 1, 1000, N)

rnd_num_TZ_lin = linear_distribution(rnd_num_TZ, 4, 12)  # время прихода time_arriv
rnd_num_TS_lin = linear_distribution(rnd_num_TS, 2, 8)  # время обработки time_proces

print(f"Последовательность для входного потока заявок (время прихода): {rnd_num_TZ_lin}")  # задание 2
print(f"Последовательность для времени обработки заявок сервером (время обработки): {rnd_num_TS_lin}")
Мишаааа Миша привет МИШАААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА
  ----
-(0 - 0)--
 / ----  \
/  ----   \           #зелебоба)))
  |  |
  |  |
# -----------------------
# -------ЗАДАНИЕ 3-5-----

def buff_model(rnd_num_TZ_lin, rnd_num_TS_lin,
               buff_size):  # получаем на вход список случ чисео для времени поступления прог
    # и также на вход идет список случайных чисел для времени обработки прог на сервер, и размер буфера
    buff = []  # буфер
    curr_buff_size = 0  # текущий размер буфера
    server_size = 0  # размер сервера
    buff_time = [0] * (buff_size + 1)  # списко для подсчета времени ожид программ в буфере

    for rnd_num_TZ, rnd_num_TS in zip(rnd_num_TZ_lin, rnd_num_TS_lin):
        if rnd_num_TZ >= server_size:  # проверила, пустой ли сервер
            server_size = rnd_num_TZ + rnd_num_TS  # вычисление программы (на сервер отправляется текущая программа)
        else:  # сервер занят
            buff.append((rnd_num_TZ, rnd_num_TS))  # заносим прогу в буфер
            curr_buff_size += 1

        while buff and buff[0][0] <= server_size:  # проверяем, можно ли отправить на сервер
            _, rnd_num_TS = buff.pop(0)  # удаляет элем из буфера и получает его время обработки
            server_size += rnd_num_TS  # прибавляет, чтобы отразить время, до которого сервер будет занят обработкой элем
            curr_buff_size -= 1

        buff_time[curr_buff_size] += 1  # обновляем время в буфере

    total_time = sum(buff_time)  # общее время ожидания программ в буфере

    p = []
    for i in range(len(buff_time)):  # вычисление вероятности
        p.append(i / total_time)

    return buff_time, p


buff_time_lin, p_lin = buff_model(rnd_num_TZ_lin, rnd_num_TS_lin, buff_size)

print(f"Время нахождения в буфере: {buff_time_lin}")
print(f"Вероятность нахождения в буфере: {p_lin}")


# -----------------------
# -------ЗАДАНИЕ 6-------

def exponential_distribution(rnd_seq, lambd_or_mu):
    rnd_seq_exp = []
    for i in range(len(rnd_seq)):
        rnd_seq_exp.append(1 - m.exp(-lambd_or_mu * rnd_seq[i]))

    return rnd_seq_exp


rnd_seq_TZ_exp = exponential_distribution(np.random.uniform(0, 1, N), 1 / 3)  # время прихода
rnd_seq_TS_exp = exponential_distribution(np.random.uniform(0, 1, N), 1 / 4)  # время обработки

print(f"Последовательность для входного потока заявок (время прихода): {rnd_seq_TZ_exp}")  # задание 6
print(f"Последовательность для времени обработки заявок сервером (время обработки): {rnd_seq_TS_exp}")


# -----------------------
# -------ЗАДАНИЕ 7-------

buff_time_exp, p_exp = buff_model(rnd_seq_TZ_exp, rnd_seq_TS_exp, buff_size)

print(f"Время нахождения в буфере: {buff_time_exp}")
print(f"Вероятность нахождения в буфере: {p_exp}")
