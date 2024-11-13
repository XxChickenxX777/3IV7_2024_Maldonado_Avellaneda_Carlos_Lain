import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class TennisPlayersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Jugadores de Tenis")
        
        self.conn = sqlite3.connect('tennis_players.db')
        self.create_table()
        self.load_players_from_txt()
        
        self.nombre_var = tk.StringVar()
        self.pais_var = tk.StringVar()
        self.ranking_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.titulos_var = tk.StringVar()
        self.mano_var = tk.StringVar()
        self.superficie_var = tk.StringVar()
        self.puntos_var = tk.StringVar()
        self.busqueda_var = tk.StringVar()
        
        self.create_form()
        
        self.create_search_bar()
        
        self.create_treeview()
        
        self.load_players()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                pais TEXT,
                ranking INTEGER,
                edad INTEGER,
                titulos INTEGER,
                mano TEXT,
                superficie TEXT,
                puntos INTEGER
            )
        ''')
        self.conn.commit()

    def create_search_bar(self):
        search_frame = ttk.LabelFrame(self.root, text="Búsqueda", padding="10")
        search_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        ttk.Label(search_frame, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(search_frame, textvariable=self.busqueda_var).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(search_frame, text="Buscar", command=self.search_player).grid(row=0, column=2, padx=5, pady=2)
        ttk.Button(search_frame, text="Mostrar Todos", command=self.load_players).grid(row=0, column=3, padx=5, pady=2)

        self.root.bind('<Return>', lambda event: self.search_player())

    def search_player(self):
        search_term = self.busqueda_var.get().strip().lower()
        if not search_term:
            self.load_players()
            return

        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM players 
            WHERE LOWER(nombre) LIKE ?
        """, (f'%{search_term}%',))
        
        rows = cursor.fetchall()

        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for row in rows:
            self.tree.insert("", tk.END, values=row)
        
        if not rows:
            messagebox.showinfo("Búsqueda", "No se encontraron jugadores con ese nombre.")

    def load_players_from_txt(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM players")
        count = cursor.fetchone()[0]
        
        if count == 0:
            try:
                with open('tennis_players.txt', 'r', encoding='utf-8') as file:
                    jugadores = []
                    for line in file:
                        if line.strip() and not line.startswith('#'):
                            datos = line.strip().split(',')
                            if len(datos) == 8:
                                nombre, pais, ranking, edad, titulos, mano, superficie, puntos = datos
                                jugadores.append((
                                    nombre.strip(),
                                    pais.strip(),
                                    int(ranking),
                                    int(edad),
                                    int(titulos),
                                    mano.strip(),
                                    superficie.strip(),
                                    int(puntos)
                                ))
                
                cursor.executemany('''
                    INSERT INTO players (nombre, pais, ranking, edad, titulos, mano, superficie, puntos)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', jugadores)
                self.conn.commit()
                messagebox.showinfo("Éxito", "Jugadores cargados correctamente desde el archivo")
            except FileNotFoundError:
                messagebox.showerror("Error", "No se encontró el archivo tennis_players.txt")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar los jugadores: {str(e)}")

    def create_form(self):
        form_frame = ttk.LabelFrame(self.root, text="Datos del Jugador", padding="10")
        form_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        left_frame = ttk.Frame(form_frame)
        left_frame.grid(row=0, column=0, padx=5)

        ttk.Label(left_frame, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(left_frame, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(left_frame, text="País:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(left_frame, textvariable=self.pais_var).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(left_frame, text="Ranking:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(left_frame, textvariable=self.ranking_var).grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(left_frame, text="Edad:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(left_frame, textvariable=self.edad_var).grid(row=3, column=1, padx=5, pady=2)

        right_frame = ttk.Frame(form_frame)
        right_frame.grid(row=0, column=1, padx=5)

        ttk.Label(right_frame, text="Títulos:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(right_frame, textvariable=self.titulos_var).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(right_frame, text="Mano:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        ttk.Combobox(right_frame, textvariable=self.mano_var, values=["Diestro", "Zurdo"]).grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(right_frame, text="Superficie:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        ttk.Combobox(right_frame, textvariable=self.superficie_var, values=["Dura", "Tierra", "Hierba"]).grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(right_frame, text="Puntos:").grid(row=3, column=0, sticky="e", padx=5, pady=2)
        ttk.Entry(right_frame, textvariable=self.puntos_var).grid(row=3, column=1, padx=5, pady=2)

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Registrar", command=self.add_player).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_player).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.delete_player).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_form).grid(row=0, column=3, padx=5)

    def create_treeview(self):
        self.tree = ttk.Treeview(self.root, columns=("id", "nombre", "pais", "ranking", "edad", "titulos", "mano", "superficie", "puntos"), show="headings")
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        
        self.tree.bind("<Double-1>", self.item_selected)

    def load_players(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM players")
        rows = cursor.fetchall()

        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def add_player(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO players (nombre, pais, ranking, edad, titulos, mano, superficie, puntos)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.nombre_var.get(),
                self.pais_var.get(),
                int(self.ranking_var.get()),
                int(self.edad_var.get()),
                int(self.titulos_var.get()),
                self.mano_var.get(),
                self.superficie_var.get(),
                int(self.puntos_var.get())
            ))
            self.conn.commit()
            self.load_players()
            self.clear_form()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para ranking, edad, títulos y puntos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar jugador: {str(e)}")

    def update_player(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona un jugador para actualizar.")
            return
        try:
            item = self.tree.item(selected_item)
            player_id = item["values"][0]

            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE players SET nombre=?, pais=?, ranking=?, edad=?, titulos=?, mano=?, superficie=?, puntos=?
                WHERE id=?
            ''', (
                self.nombre_var.get(),
                self.pais_var.get(),
                int(self.ranking_var.get()),
                int(self.edad_var.get()),
                int(self.titulos_var.get()),
                self.mano_var.get(),
                self.superficie_var.get(),
                int(self.puntos_var.get()),
                player_id
            ))
            self.conn.commit()
            self.load_players()
            self.clear_form()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para ranking, edad, títulos y puntos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar jugador: {str(e)}")

    def delete_player(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona un jugador para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este jugador?"):
            item = self.tree.item(selected_item)
            player_id = item["values"][0]

            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM players WHERE id=?", (player_id,))
            self.conn.commit()
            self.load_players()
            self.clear_form()

    def item_selected(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        item = self.tree.item(selected_item)
        player_data = item["values"]

        self.nombre_var.set(player_data[1])
        self.pais_var.set(player_data[2])
        self.ranking_var.set(player_data[3])
        self.edad_var.set(player_data[4])
        self.titulos_var.set(player_data[5])
        self.mano_var.set(player_data[6])
        self.superficie_var.set(player_data[7])
        self.puntos_var.set(player_data[8])

    def clear_form(self):
        self.nombre_var.set("")
        self.pais_var.set("")
        self.ranking_var.set("")
        self.edad_var.set("")
        self.titulos_var.set("")
        self.mano_var.set("")
        self.superficie_var.set("")
        self.puntos_var.set("")
        self.busqueda_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = TennisPlayersApp(root)
    root.mainloop()