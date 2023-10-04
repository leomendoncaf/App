from Motorista import Motorista
from Passageiro import Passageiro
from Corrida import Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        motorista_id = int(input("Digite o ID do motorista: "))
        nota = int(input("Digite a nota do motorista: "))
        passageiro_nome = input("Digite o nome do passageiro: ")
        passageiro_documento = input("Digite o documento do passageiro: ")

        passageiro = Passageiro(passageiro_nome, passageiro_documento)

        corridas = []
        while True:
            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distância da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)
            add_corrida = input("Deseja adicionar outra corrida? (S/N): ")
            if add_corrida.upper() != "S":
                break

        motorista = Motorista(motorista_id,nota)
        motorista.corridas = corridas

        self.motorista_dao.create_motorista(motorista)
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja ler: "))
        motorista = self.motorista_dao.read_motorista(nota)
        if motorista:
            print(f"Nota do motorista: {motorista.nota}")
            for corrida in motorista.corridas:
                print(f"Nota da corrida: {corrida.nota}")
                print(f"Distância: {corrida.distancia}")
                print(f"Valor: {corrida.valor}")
                print(f"Nome do passageiro: {corrida.passageiro.nome}")
                print(f"Documento do passageiro: {corrida.passageiro.documento}")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja atualizar: "))
        motorista = self.motorista_dao.read_motorista(nota)
        if motorista:
            new_nota = int(input("Digite a nova nota do motorista: "))
            new_motorista = Motorista(new_nota)
            new_motorista.corridas = motorista.corridas
            if self.motorista_dao.update_motorista(nota, new_motorista):
                print("Motorista atualizado com sucesso!")
            else:
                print("Falha ao atualizar o motorista.")
        else:
            print("Motorista não encontrado.")

    def delete_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja deletar: "))
        if self.motorista_dao.delete_motorista(nota):
            print("Motorista deletado com sucesso!")
        else:
            print("Motorista não encontrado.")
