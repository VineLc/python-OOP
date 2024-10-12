
import mysql.connector
from tkinter import messagebox

class Nota:
    def __init__(self, aluno_id, id_disciplina, nota, faltas):
        self.aluno_id = aluno_id
        self.id_disciplina = id_disciplina
        self.nota = nota
        self.faltas = faltas

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
        cursor.execute("INSERT INTO notas (id_aluno, id_disciplina, nota_final, faltas) VALUES (%s, %s, %s, %s)",
                       (self.aluno_id, self.id_disciplina, self.nota, self.faltas))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
