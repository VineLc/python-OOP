# Professores.py
import mysql.connector
from tkinter import messagebox

class Professor:
    def __init__(self, nome, email, fone):
        self.nome = nome
        self.email = email
        self.fone = fone

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
        cursor.execute("INSERT INTO professores (nome, email, fone) VALUES (%s, %s, %s)",
                       (self.nome, self.email, self.fone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Professor adicionado com sucesso!")
