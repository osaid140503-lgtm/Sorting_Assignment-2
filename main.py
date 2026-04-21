import random
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt




def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr


def selection_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr


def insertion_sort(arr):
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



def generate_random_arrays(size, repetitions):
    return [[random.randint(0, 100000) for _ in range(size)] for _ in range(repetitions)]


def generate_nearly_sorted_arrays(size, repetitions, noise_level):
    arrays = []
    num_swaps = int(size * noise_level)
    for _ in range(repetitions):
        arr = list(range(size))
        for _ in range(num_swaps):
            idx1 = random.randint(0, size - 1)
            idx2 = random.randint(0, size - 1)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        arrays.append(arr)
    return arrays


def measure_algorithm_time(algorithm_func, arr):
    start_time = time.time()
    algorithm_func(arr)
    end_time = time.time()
    return end_time - start_time


def run_experiment(algorithms, sizes, repetitions, mode, noise=0):
    results = {alg.__name__: {'mean': [], 'std': []} for alg in algorithms}

    for size in sizes:
        if mode == "random":
            test_arrays = generate_random_arrays(size, repetitions)
        else:
            test_arrays = generate_nearly_sorted_arrays(size, repetitions, noise)

        for alg in algorithms:
            times = [measure_algorithm_time(alg, arr) for arr in test_arrays]
            results[alg.__name__]['mean'].append(np.mean(times))
            results[alg.__name__]['std'].append(np.std(times))

    return results


def plot_and_save(sizes, results, filename, title):
    plt.figure(figsize=(10, 6))
    for alg_name, data in results.items():
        means = np.array(data['mean'])
        stds = np.array(data['std'])
        plt.plot(sizes, means, marker='o', label=alg_name.replace('_', ' ').title())
        plt.fill_between(sizes, means - stds, means + stds, alpha=0.2)

    plt.xlabel('Array size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(filename)
    print(f"Graph saved as {filename}")
    plt.show()




def main():
    parser = argparse.ArgumentParser(description="Sorting Assignment Experiments")
    parser.add_argument('-a', '--algorithms', nargs='+', type=int, required=True,
                        help="Algorithm IDs: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick")
    parser.add_argument('-s', '--sizes', nargs='+', type=int, required=True,
                        help="Array sizes, e.g., 100 500 1000")
    parser.add_argument('-e', '--experiment', type=int, required=True,
                        help="0-Random, 1-Nearly sorted (5%), 2-Nearly sorted (20%)")
    parser.add_argument('-r', '--repetitions', type=int, default=5,
                        help="Number of repetitions per size")

    args = parser.parse_args()

    alg_map = {
        1: bubble_sort, 2: selection_sort, 3: insertion_sort,
        4: merge_sort, 5: quick_sort
    }

    selected_algs = [alg_map[i] for i in args.algorithms if i in alg_map]

    if args.experiment == 0:
        res = run_experiment(selected_algs, args.sizes, args.repetitions, "random")
        plot_and_save(args.sizes, res, "result1.png", "Runtime Comparison (Random Arrays)")
    elif args.experiment == 1:
        res = run_experiment(selected_algs, args.sizes, args.repetitions, "nearly", noise=0.05)
        plot_and_save(args.sizes, res, "result2.png", "Runtime Comparison (Nearly Sorted, 5% noise)")
    elif args.experiment == 2:
        res = run_experiment(selected_algs, args.sizes, args.repetitions, "nearly", noise=0.20)
        plot_and_save(args.sizes, res, "result2.png", "Runtime Comparison (Nearly Sorted, 20% noise)")


if __name__ == "__main__":
    main()