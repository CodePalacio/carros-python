import sqlite3
import os


os.system("cls")

class Carro:
    def __init__(self, nome, disponivel=True):
        self.nome = nome
        self.disponivel = disponivel

class Locadora:
    def __init__(self, nome_banco) -> None:
        self.conn = sqlite3.connect(nome_banco)
        self.c = self.conn.cursor()
        self._criar_tabela_carros()
        self._criar_tabela_carros_alugados()

    def __str__(self) -> str:
        return "{}".format(self.carros_disponiveis)
    
    def _criar_tabela_carros(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS carros (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       disponivel INTEGER NOT NULL
        )''')
        self.conn.commit()

    def _criar_tabela_carros_alugados(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS carros_alugados (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       carro_id INTEGER NOT NULL,
                       cliente TEXT NOT NULL,
                       FOREIGN KEY(carro_id) REFERENCES carros(id)
        )''')
        self.conn.commit()

    def adiciona_carro(self, carro):
        try:
            self.c.execute("INSERT INTO carros (nome, disponivel) VALUES(?,?)", (carro.nome, carro.disponivel))
            self.conn.commit()
            print(f"{carro.nome} adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao adicionar {carro.nome}: {e}")

    def aluga_carro(self, cliente, id):
        try:
            self.c.execute("SELECT nome FROM carros WHERE id = ? AND disponivel = 1", (id,))
            resultado = self.c.fetchone()
            if resultado: 
                self.c.execute("UPDATE carros SET disponivel = 0 WHERE id = ?", (id,))
                self.c.execute("INSERT INTO carros_alugados (carro_id, cliente) VALUES(?,?)", (id, cliente))
                self.conn.commit()
                print(f"O carro {resultado[0]} foi alugado para o cliente: {cliente}.")
            else:
                print(f"O carro: {resultado[0]}, não está mais disponivel para alugar.")
        except sqlite3.Error as e:
            print(f"Erro ao tentar alugar o carro : {e}")

    def lista_carros_disponiveis(self):
        self.c.execute("SELECT nome FROM carros WHERE disponivel = 1")
        carros = self.c.fetchall()
        for carro in carros:
            print(carro[0])
    
    def lista_carros_alugados(self):
        self.c.execute("SELECT carros.nome, carros_alugados.cliente FROM carros_alugados JOIN carros ON carros.id = carros_alugados.carro_id")
        alugados = self.c.fetchall()
        print("Carros alugados:")
        for alugado in alugados:
            print(f"Carro: {alugado[0]}, Cliente: {alugado[1]}")


def menu():
    print("\n=====MENU=====")
    print("1. Listar carros disponiveis")
    print("2. Alugar carro")
    print("3. Devolver carro")
    print("4. Adicionar novo carro")
    print("5. Sair")

if __name__ == "__main__":
    locadora = Locadora("locadora.db")
    locadora.lista_carros_alugados()
 

