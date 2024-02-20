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
        self._criar_tabela()

    def __str__(self) -> str:
        return "{}".format(self.carros_disponiveis)
    
    def _criar_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS carros (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       disponivel INTEGER NOT NULL
                        )
                       ''')
        self.conn.commit()

    def adiciona_carro(self, carro):
        try:
            self.c.execute("INSERT INTO carros (nome, disponivel) VALUES(?,?)", (carro.nome, carro.disponivel))
            self.conn.commit()
            print(f"{carro.nome} adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao adicionar {carro.nome}: {e}")

    def aluga_carro(self, cliente, carro):
        if carro in self.carros_disponiveis:
            self.carros_disponiveis.remove(carro)
            self.carros_alugados[carro] = cliente
            print(f"\nO carro: {carro.modelo} foi alugado para o cliente: {cliente}\n")
        else:
            print(f"\nDesculpe, o carro: {carro} já não está mais disponivel")

    def lista_carros_disponiveis(self):
        self.c.execute("SELECT nome FROM carros WHERE disponivel = 1")
        carros = self.c.fetchall()
        for carro in carros:
            print(carro[0])
    
    def lista_carros_alugados(self):
        print("=====================================\nCarros alugados:\n")
        for carro, cliente in self.carros_alugados.items():
            print(f"Carro: {carro.modelo} / Cliente: {cliente}")
        print("=====================================\n")


def menu():
    print("\n=====MENU=====")
    print("1. Listar carros disponiveis")
    print("2. Alugar carro")
    print("3. Devolver carro")
    print("4. Adicionar novo carro")
    print("5. Sair")

if __name__ == "__main__":
    locadora = Locadora("locadora.db")
    locadora.lista_carros_disponiveis()

