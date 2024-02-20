import sqlite3
import os

from carros import Carro

os.system("cls")

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
        self.carros_disponiveis.append(carro)

    def aluga_carro(self, cliente, carro):
        if carro in self.carros_disponiveis:
            self.carros_disponiveis.remove(carro)
            self.carros_alugados[carro] = cliente
            print(f"\nO carro: {carro.modelo} foi alugado para o cliente: {cliente}\n")
        else:
            print(f"\nDesculpe, o carro: {carro} já não está mais disponivel")

    def lista_carros_disponiveis(self):
        print("======================================\nCarros disponiveis:\n")
        for carro in self.carros_disponiveis:
            print("{}".format(carro))
        print("======================================\n")
    
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
