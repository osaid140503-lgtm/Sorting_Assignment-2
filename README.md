# Sorting_Assignment-2
Students:

Osaid Arkia - 213727993

Salih Abahry - 214051922
Objective:The goal of this assignment is to gain hands-on experience with Python by implementing various sorting algorithms and empirically comparing their running times. By running controlled experiments on both completely random and nearly sorted arrays, we aim to visualize theoretical time complexities and understand how the initial distribution of data impacts real-world algorithm performance.

Selected Algorithms:
Bubble Sort,Selection Sort,Quick Sort.
Rationale for Selection: We selected these specific algorithms to create a stark contrast in our visualizations. Bubble Sort and Selection Sort serve as examples of slower, less efficient algorithms, allowing us to clearly observe a quadratic growth curve as the array size increases. Quick Sort was chosen as the highly efficient counterpart. Plotting these together perfectly illustrates the massive difference in scalability between O(n^2) and O(n log n) algorithms.



#Part B: Random Arrays (result1.png)
Explanation: This graph illustrates the runtime of the algorithms when tasked with sorting completely random arrays.
Quick Sort remains incredibly fast and stable, with its runtime appearing nearly flat along the bottom of the graph, even at 3,000 elements.

Bubble Sort and Selection Sort demonstrate a clear quadratic upward curve.

Observation: Selection Sort performs slightly faster than Bubble Sort here. While both fall under the same complexity class, Selection Sort executes significantly fewer memory swap operations per pass compared to Bubble Sort, giving it a slight edge in raw processing time

#Part C: Nearly Sorted Arrays - 5% Noise (result2.png)
Explanation: In this experiment, the algorithms were given arrays that were already sorted, but 5% of the elements were randomly swapped to introduce "noise."

Quick Sort remains highly efficient and unaffected by the noise.

Selection Sort maintains its consistent quadratic behavior. Because its underlying logic requires it to blindly scan the entire unsorted portion of the array to find the minimum value, it does not gain any advantage from the array being partially sorted.

Bubble Sort performs the worst in this scenario, despite our implementation including an early-exit optimization (stopping if no swaps occur). Because the 5% noise was injected randomly, small numbers were inevitably swapped to the very end of the array (these are known as "turtles"). Bubble Sort is notoriously inefficient at moving turtles back to the beginning of the array, forcing the algorithm to still execute nearly all of its passes.
