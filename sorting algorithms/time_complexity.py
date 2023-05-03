import matplotlib.pyplot as plt
import time
from insertion_sort import insertion_sort
from merge_sort import  merge_sort
import numpy as np


# Returns an array containing running time in the worst case of the sorting algorithm
def time_worst(func, x_axis ):
    worst_list = np.array([(time.time()-time.time())*1000 for i in x_axis])
    for index, i in enumerate(x_axis):
        sample = np.array(np.arange(i, -1, -1))
        start = time.time()
        _   = func(sample)
        stop = time.time()
        worst_list[index]= ((stop-start)*1000)
        index+=1
    return  worst_list

 #Returns an array containing running time in the best case of the sorting algorithm
def time_best(func, x_axis):
    best_list = np.array(x_axis)
    index = 0
    for i in x_axis:
        sample = np.array(np.arange(i+1))
        start = time.time()
        _ = func(sample)
        stop = time.time()
        best_list[index]= ((stop-start)*1000)
        index+=1
    return best_list

def plot_best_worst(sort_type, **kwargs):
    """Plot input size vs running time"""
    best = kwargs.get("best")
    worst = kwargs.get("worst")
    fig, binary_plt = plt.subplots()
    if best is not None:
        binary_plt.plot(x_axis, best, '.', label="Best Case")
    if worst is not None:
        binary_plt.plot(x_axis, worst, 'x', label="Worst Case")
    binary_plt.set_xlabel("Length of array(n)")
    binary_plt.set_ylabel("Time (in milliseconds)")
    binary_plt.set_title(sort_type)
    binary_plt.legend()
    plt.show()

# x_axis = np.arange(50, 1000, 10)
# worst = time_worst(insertion_sort, x_axis)
# best = time_best(insertion_sort, x_axis )
# plot_best_worst("Insertion Sort", best=best,worst=worst )

# x_axis = np.arange(5000, 100000, 2000)
# best= time_best(merge_sort, x_axis)
# worst= time_worst(merge_sort, x_axis)
# plot_best_worst("Merge Sort", best=best, worst=worst )

x_axis = np.arange(5000, 100000, 2000)
best_insertion = time_best(insertion_sort, x_axis)
worst_merge = time_worst(merge_sort, x_axis)
plot_best_worst("Merge_worst vs insertion_best",best=best_insertion, worst=worst_merge)