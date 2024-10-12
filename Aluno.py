
import mysql.connector
from tkinter import messagebox

class Aluno:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

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
        cursor.execute("INSERT INTO alunos (nome, email, fone) VALUES (%s, %s, %s)",
                       (self.nome, self.email, self.telefone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")

    def alterar(self, aluno_id):
        conn = self.criar_conexao()
        cursor = conn.cursor()
        cursor.execute("UPDATE alunos SET nome = %s, email = %s, fone = %s WHERE id_aluno = %s",
                       (self.nome, self.email, self.telefone, aluno_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Dados do aluno alterados com sucesso!")

    @staticmethod
    def remover(aluno_id):
        conn = Aluno.criar_conexao()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id_aluno = %s", (aluno_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno removido com sucesso!")
