import tkinter as tk

screen = tk.Tk()

screen.title("Interpolación lineal")
screen.geometry("500x300")

# ------------------------------------ fx ------------------------------------ #
fx = tk.Label(screen, text = "fx", font = ("Arial", 14))
fx.grid(row = 0, column = 0, padx = (100, 10), pady = (50, 0))

fx0 = tk.Label(screen, text = "fx0", font = ("Arial", 14))
fx0.grid(row = 1, column = 0, padx = (100, 10), pady = (20, 0))

fx1 = tk.Label(screen,  text = "fx1", font = ("Arial", 14))
fx1.grid(row = 2, column = 0, padx = (100, 10), pady = (20, 0))


# --------------------------------- fx entry --------------------------------- #

input_fx = tk.Entry(screen, width = 5, state = "readonly", font = ("Arial", 14))
input_fx.grid(row = 0, column = 1, pady = (50, 0))

input_fx0 = tk.Entry(screen, width = 5, font = ("Arial", 14))
input_fx0.grid(row = 1, column =1, pady = (20, 0))

input_fx1 = tk.Entry(screen, width = 5, font = ("Arial", 14))
input_fx1.grid(row = 2, column = 1, pady = (20, 0))

# ------------------------------------- x ------------------------------------ #

x = tk.Label(screen, text = "x", font = ("Arial", 14))
x.grid(row = 0, column = 3, padx = (0, 10), pady = (50, 0))

x0 = tk.Label(screen, text = "x0", font = ("Arial", 14))
x0.grid(row = 1, column = 3, padx = (0, 10), pady = (20, 0))

x1 = tk.Label(screen,  text = "x1", font = ("Arial", 14))
x1.grid(row = 2, column = 3, padx = (0, 10), pady = (20, 0))

# ---------------------------------- x entry --------------------------------- #

input_x = tk.Entry(screen, width = 5, font = ("Arial", 14))
input_x.grid(row = 0, column = 4, pady = (50, 0))

input_x0 = tk.Entry(screen, width = 5, font = ("Arial", 14))
input_x0.grid(row = 1, column = 4, pady = (20, 0))

input_x1 = tk.Entry(screen, width = 5, font = ("Arial", 14))
input_x1.grid(row = 2, column = 4, pady = (20, 0))

# ---------------------------------- botones --------------------------------- #

calcular = tk.Button(screen, text = "Calcular", width = 10)
calcular.grid(row = 4, column = 2, padx = (10), pady = (20, 0))

grafica = tk.Button(screen, text = "Graficar", width = 10)
grafica.grid(row = 5, column = 2, padx = (10), pady = (20, 0))

print(input_fx0.get())

screen.mainloop()