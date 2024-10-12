import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# Conexão com o banco de dados
def criar_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ensino"
    )

# Classe para a janela principal
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
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alunos (nome, email, fone) VALUES (%s,%s,%s)", (nome,email,telefone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")

    def alterar_aluno(self):
        aluno_id = self.id_entry.get()
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("UPDATE alunos SET nome = %s, email = %s, fone = %s WHERE id_aluno = %s",(nome, email, telefone, aluno_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Dados do aluno alterados com sucesso!")

    def remover_aluno(self):
        aluno_id = self.id_entry.get()  # Obtém o ID do aluno a ser removido

        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id_aluno = " + (aluno_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno removido com sucesso!")

# Classe para Gerenciar Notas
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
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notas (id_aluno,id_disciplina, nota_final,faltas) VALUES (%s, %s, %s, %s)", (aluno_id, id_disciplina, nota,faltas))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")

# Classe para Gerenciar Disciplinas
class Disciplinas(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Disciplinas")

        tk.Label(self, text="Disciplina:").grid(row=0, column=0)
        self.disciplina_entry = tk.Entry(self)
        self.disciplina_entry.grid(row=0, column=1)

        tk.Label(self, text="Carga Horaria:").grid(row=1, column=0)
        self.CargHoraria_entry = tk.Entry(self)
        self.CargHoraria_entry.grid(row=1, column=1)

        tk.Label(self, text="ID professor:").grid(row=2, column=0)
        self.id_prof_entry = tk.Entry(self)
        self.id_prof_entry.grid(row=2, column=1)

        tk.Button(self, text="Adicionar Disciplina", command=self.adicionar_disciplina).grid(row=3, column=0,
                                                                                             columnspan=2, pady=10)

    def adicionar_disciplina(self):
        disciplina = self.disciplina_entry.get()
        CargHoraria = self.CargHoraria_entry.get()
        id_prof = self.id_prof_entry.get()
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO disciplinas (nome,cargaHoraria,id_prof) VALUES (%s,%s,%s)", (disciplina,CargHoraria,id_prof))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Disciplina adicionada com sucesso!")

# Classe para Gerenciar Professores
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

        tk.Button(self, text="Adicionar Professor", command=self.adicionar_professor).grid(row=3, column=0,
                                                                                           columnspan=2, pady=10)

    def adicionar_professor(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        fone = self.fone_entry.get()
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO professores (nome,email,fone) VALUES (%s,%s,%s)", (nome,email,fone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Professor adicionado com sucesso!")


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
                "SELECT d.nome AS nome_disciplina, n.nota_final "
                "FROM ensino.alunos AS a "
                "JOIN ensino.notas AS n ON a.id_aluno = n.id_aluno "
                "JOIN ensino.disciplinas AS d ON n.id_disciplina = d.id_disciplina "
                "WHERE a.id_aluno = %s ", (id,))

            resultados = cursor.fetchall()

            # Limpar o Treeview antes de adicionar novos dados
            for i in self.tree.get_children():
                self.tree.delete(i)

            if resultados:
                materias = []
                notas = []
                for linha in resultados:
                    self.tree.insert("", "end", values=(id, linha[1], '', linha[0], ''))  # Ajuste conforme necessário
                    materias.append(linha[0])
                    notas.append(linha[1])

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
        plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x, se necessário
        plt.tight_layout()  # Ajusta o layout
        plt.show()

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()
