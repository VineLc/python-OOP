import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from Aluno import Aluno
from Notas import Nota
from Disciplinas import Disciplina
from Professores import Professor

def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ensino"
    )

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão")

        tk.Button(self, text="Alunos", command=self.abrir_alunos).pack(pady=10)
        tk.Button(self, text="Notas", command=self.abrir_notas).pack(pady=10)
        tk.Button(self, text="Disciplinas", command=self.abrir_disciplinas).pack(pady=10)
        tk.Button(self, text="Professores", command=self.abrir_professores).pack(pady=10)
        tk.Button(self, text="Graficos", command=self.abrir_graficos).pack(pady=10)

    def abrir_alunos(self):
        Alunos(self)

    def abrir_notas(self):
        Notas(self)

    def abrir_disciplinas(self):
        Disciplinas(self)

    def abrir_professores(self):
        Professores(self)

    def abrir_graficos(self):
        Graficos(self)

# Classe para Gerenciar Alunos
class Alunos(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Alunos")

        tk.Label(self, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1)

        tk.Label(self, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(self)
        self.nome_entry.grid(row=1, column=1)

        tk.Label(self, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self, text="Telefone:").grid(row=3, column=0)
        self.telefone_entry = tk.Entry(self)
        self.telefone_entry.grid(row=3, column=1)

        tk.Button(self, text="Adicionar", command=self.adicionar_aluno).grid(row=4, column=0, pady=10)
        tk.Button(self, text="Alterar", command=self.alterar_aluno).grid(row=4, column=1, pady=10)
        tk.Button(self, text="Apagar", command=self.remover_aluno).grid(row=5, column=0, pady=10)

    def adicionar_aluno(self):
        aluno = Aluno(self.nome_entry.get(), self.email_entry.get(), self.telefone_entry.get())
        aluno.adicionar()

    def alterar_aluno(self):
        aluno_id = self.id_entry.get()
        aluno = Aluno(self.nome_entry.get(), self.email_entry.get(), self.telefone_entry.get())
        aluno.alterar(aluno_id)

    def remover_aluno(self):
        aluno_id = self.id_entry.get()
        Aluno.remover(aluno_id)

class Notas(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Notas")

        tk.Label(self, text="Aluno ID:").grid(row=0, column=0)
        self.aluno_id_entry = tk.Entry(self)
        self.aluno_id_entry.grid(row=0, column=1)

        tk.Label(self, text="ID Disciplina:").grid(row=1, column=0)
        self.id_disciplina_entry = tk.Entry(self)
        self.id_disciplina_entry.grid(row=1, column=1)

        tk.Label(self, text="Nota:").grid(row=2, column=0)
        self.nota_entry = tk.Entry(self)
        self.nota_entry.grid(row=2, column=1)

        tk.Label(self, text="Faltas:").grid(row=3, column=0)
        self.faltas_entry = tk.Entry(self)
        self.faltas_entry.grid(row=3, column=1)

        tk.Button(self, text="Adicionar Nota", command=self.adicionar_nota).grid(row=4, column=0, columnspan=2, pady=10)

    def adicionar_nota(self):
        aluno_id = self.aluno_id_entry.get()
        id_disciplina = self.id_disciplina_entry.get()
        nota = self.nota_entry.get()
        faltas = self.faltas_entry.get()

        nota_obj = Nota(aluno_id, id_disciplina, nota, faltas)
        nota_obj.adicionar()

class Disciplinas(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Disciplinas")

        tk.Label(self, text="Disciplina:").grid(row=0, column=0)
        self.disciplina_entry = tk.Entry(self)
        self.disciplina_entry.grid(row=0, column=1)

        tk.Label(self, text="Carga Horária:").grid(row=1, column=0)
        self.carga_horaria_entry = tk.Entry(self)
        self.carga_horaria_entry.grid(row=1, column=1)

        tk.Label(self, text="ID Professor:").grid(row=2, column=0)
        self.id_prof_entry = tk.Entry(self)
        self.id_prof_entry.grid(row=2, column=1)

        tk.Button(self, text="Adicionar Disciplina", command=self.adicionar_disciplina).grid(row=3, column=0, columnspan=2, pady=10)

    def adicionar_disciplina(self):
        nome = self.disciplina_entry.get()
        carga_horaria = self.carga_horaria_entry.get()
        id_prof = self.id_prof_entry.get()

        disciplina = Disciplina(nome, carga_horaria, id_prof)
        disciplina.adicionar()

class Professores(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Professores")

        tk.Label(self, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self, text="Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self, text="Fone:").grid(row=2, column=0)
        self.fone_entry = tk.Entry(self)
        self.fone_entry.grid(row=2, column=1)

        tk.Button(self, text="Adicionar Professor", command=self.adicionar_professor).grid(row=3, column=0, columnspan=2, pady=10)

    def adicionar_professor(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        fone = self.fone_entry.get()

        professor = Professor(nome, email, fone)
        professor.adicionar()


class Graficos(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Pesquisa")

        tk.Label(self, text="ID Aluno:").grid(row=0, column=0)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1)

        tk.Button(self, text="Buscar", command=self.pesquisarGrafico).grid(row=1, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self,
                                 columns=("Nome Aluno", "Nota Final", "Faltas", "Nome Disciplina", "Nome Professor"),
                                 show='headings')
        self.tree.grid(row=2, column=0, columnspan=2)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

    def pesquisarGrafico(self):
        id = self.id_entry.get()
        if not id.isdigit():
            messagebox.showwarning("Entrada Inválida", "Por favor, insira um ID numérico.")
            return

        conn = criar_conexao()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT a.nome AS nome_aluno, n.nota_final, n.faltas, d.nome AS nome_disciplina, p.nome AS nome_professor "
                "FROM ensino.alunos AS a "
                "JOIN ensino.notas AS n ON a.id_aluno = n.id_aluno "
                "JOIN ensino.disciplinas AS d ON n.id_disciplina = d.id_disciplina "
                "JOIN ensino.professores AS p ON d.id_prof = p.id_prof "
                "WHERE a.id_aluno = %s ", (id,))

            resultados = cursor.fetchall()

            for i in self.tree.get_children():
                self.tree.delete(i)

            if resultados:
                for linha in resultados:
                    self.tree.insert("", "end",
                                     values=(linha[0], linha[1], linha[2], linha[3], linha[4]))

                materias = [linha[3] for linha in resultados]
                notas = [linha[1] for linha in resultados]
                self.exibir_grafico(materias, notas)
            else:
                messagebox.showinfo("Sem Resultados", "Nenhum aluno encontrado com esse ID.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

        finally:
            cursor.close()
            conn.close()

    def exibir_grafico(self, materias, notas):
        plt.bar(materias, notas)
        plt.xlabel('Matérias')
        plt.ylabel('Notas')
        plt.title('Notas do Aluno')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()
