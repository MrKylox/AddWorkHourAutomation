import tkinter as tk

class DynamicGrid(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.row_count = 0  # Track the number of rows added

    def create_widgets(self):
        # Add an initial set of widgets
        self.add_row()

        # Add a button to add new rows
        self.add_row_button = tk.Button(self, text="Add Row", command=self.add_row)
        self.add_row_button.grid(column=0, row=self.row_count + 1, columnspan=2)

    def add_row(self):
        # Create new widgets
        label = tk.Label(self, text=f"Row {self.row_count + 1}")
        entry = tk.Entry(self)

        # Add widgets to the grid
        label.grid(column=0, row=self.row_count)
        entry.grid(column=1, row=self.row_count)

        # Increment the row counter
        self.row_count += 1

        # Move the add_row_button to the new row position
        self.add_row_button.grid(column=0, row=self.row_count + 1, columnspan=2)