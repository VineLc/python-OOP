# Disciplinas.py
import mysql.connector
from tkinter import messagebox

class Disciplina:
    def __init__(self, nome, carga_horaria, id_prof):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.id_prof = id_prof

    @staticmethod
    def criar_conexao():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ensino"
        )

    def adicionar(self):
        conn = self.criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO disciplinas (nome, cargaHoraria, id_prof) VALUES (%s, %s, %s)",
                       (self.nome, self.carga_horaria, self.id_prof))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Disciplina adicionada com sucesso!")
