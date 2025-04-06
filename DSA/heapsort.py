import numpy as np
import tkinter as tk
import time

class HeapSortVisualizer:
    def __init__(self, master, array):
        self.master = master
        self.master.title("Heap Sort Visualizer")
        self.canvas = tk.Canvas(master, width=800, height=400, bg="white")
        self.canvas.pack()
        self.array = array
        self.n = len(array)
        self.max_val = max(array)

        self.bar_width = 800 / self.n
        self.draw_array()

        # Start sorting after short delay
        self.master.after(1000, self.start_sorting)

    def draw_array(self, highlight_indices=None):
        self.canvas.delete("all")
        highlight_indices = highlight_indices or []

        for i, val in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = 400 - (val / self.max_val * 380)
            x1 = (i + 1) * self.bar_width
            y1 = 400

            color = "red" if i in highlight_indices else "skyblue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

        self.master.update_idletasks()

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.array[left] > self.array[largest]:
            largest = left
        if right < n and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.draw_array([i, largest])
            time.sleep(0.001)  # Minimal delay for large arrays
            self.heapify(n, largest)

    def heap_sort(self):
        n = self.n

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.draw_array([0, i])
            time.sleep(0.001)
            self.heapify(i, 0)

        self.draw_array()

    def start_sorting(self):
        start_time = time.time()
        self.heap_sort()
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"Sorting complete in {elapsed:.2f} seconds")  # Show time in console


if __name__ == "__main__":
    array = np.random.randint(10, 100, size=1000).tolist()

    root = tk.Tk()
    app = HeapSortVisualizer(root, array)
    root.mainloop()
