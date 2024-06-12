label_forca_mf = Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack()

botao_calcular_mf = Button(aba_engenharia_civil, text="Calcular", command=momento_fletor_interface)
botao_calcular_mf.pack()

label_resultado_mf = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

# ... (código restante da interface gráfica)

import tkinter as tk
from tkinter import messagebox
from math import sqrt
app = tk.Tk() # type: ignore
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app) # type: ignore
aba_avancada = tk.Frame(app) # type: ignore
aba_memoria = tk.Frame(app) # type: ignore
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_memoria.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)