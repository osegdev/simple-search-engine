import tkinter as tk
from tkinter import ttk
from app.use_cases.search_engine import SearchEngine

class SearchApp:
    def __init__(self, root: tk.Tk, engine: SearchEngine):
        self.engine = engine
        self.root = root
        self.root.title("Simple Search Engine")

        # Entrada de búsqueda
        self.query_var = tk.StringVar()
        self.entry = ttk.Entry(root, textvariable=self.query_var, width=50)
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", self.search)

        # Botón de búsqueda
        self.button = ttk.Button(root, text="Search", command=self.search)
        self.button.pack(padx=10)

        # Resultados
        self.results = tk.Text(root, height=15, width=60, wrap="word")
        self.results.pack(padx=10, pady=10)

    def search(self, event=None):
        query = self.query_var.get()
        self.results.delete("1.0", tk.END)
        if query.strip():
            results = self.engine.search(query)
            if results:
                for doc in results:
                    self.results.insert(tk.END, f"📄 {doc}\n")
            else:
                self.results.insert(tk.END, "No results were found.\n")