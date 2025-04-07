import numpy as np
import tkinter as tk
import time

class MergeSortVisualizer:
    def __init__(self, master, array):
        self.master = master
        self.master.title("Merge Sort Visualizer")
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

    def merge(self, left, right):
        result = []
        i = j = 0
        merged_indices = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                merged_indices.append(i)
                i += 1
            else:
                result.append(right[j])
                merged_indices.append(len(left) + j)
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result, merged_indices

    def merge_sort(self, arr, highlight_indices=[]):
        if len(arr) <= 1:
            return arr, highlight_indices

        mid = len(arr) // 2
        left, left_indices = self.merge_sort(arr[:mid], highlight_indices)
        right, right_indices = self.merge_sort(arr[mid:], highlight_indices)
        
        merged, merged_indices = self.merge(left, right)
        highlight_indices += merged_indices  # Add the indices to be highlighted
        
        self.array[:] = merged  # Update the array with the merged result
        self.draw_array(highlight_indices)  # Draw the array with highlights
        time.sleep(0.01)  # Minimal delay for smoother animation

        return merged, highlight_indices

    def start_sorting(self):
        start_time = time.time()
        self.merge_sort(self.array)
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"Sorting complete in {elapsed:.2f} seconds")  # Show time in console


if __name__ == "__main__":
    array = np.random.randint(1, 100, size=1000).tolist()

    root = tk.Tk()
    app = MergeSortVisualizer(root, array)
    root.mainloop()
