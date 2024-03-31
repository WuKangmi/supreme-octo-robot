import tkinter as tk
from tkinter import ttk

class PyCharmUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1200x800")

        # Create the menu bar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open File")
        self.file_menu.add_command(label="New File")

        # Create the toolbar
        self.toolbar = ttk.Frame(self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        self.open_file_btn = ttk.Button(self.toolbar, text="Open File")
        self.open_file_btn.pack(side=tk.LEFT, padx=5, pady=5)
        self.new_file_btn = ttk.Button(self.toolbar, text="New File")
        self.new_file_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the project panel
        self.project_panel = ttk.Treeview(self)
        self.project_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the console panel
        self.console_panel = tk.Text(self, height=10)
        self.console_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the code editor
        self.code_editor = tk.Text(self, font=("Consolas", 12))
        self.code_editor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create the debugger panel
        self.debugger_panel = ttk.Frame(self)
        self.debugger_panel.pack(side=tk.BOTTOM, fill=tk.X)
        self.debug_btn = ttk.Button(self.debugger_panel, text="Debug")
        self.debug_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Create the search panel
        self.search_panel = ttk.Frame(self)
        self.search_panel.pack(side=tk.BOTTOM, fill=tk.X)
        self.search_entry = ttk.Entry(self.search_panel)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.search_btn = ttk.Button(self.search_panel, text="Search")
        self.search_btn.pack(side=tk.LEFT, padx=5, pady=5)

if __name__ == "__main__":
    app = PyCharmUI()
    app.mainloop()