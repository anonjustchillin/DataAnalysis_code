import numpy as np
from prettytable import PrettyTable
from .poly_plot import plot

table = PrettyTable()


def dsd_calc(values, counts, w):
    table_print(values, counts, w)
    plot(values, w)


def table_print(values, counts, w):
    table.field_names = ["i", "x_i", "n_i", "w_i"]
    for i in range(np.size(values)):
        table.add_row([i+1, values[i], counts[i], w[i]], divider=True)
    print(table)
