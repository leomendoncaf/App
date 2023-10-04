from Database import Database
from writeAJson import writeAJson
from MotoristaDAO import MotoristaDAO
from Motorista import Motorista
from Passageiro import Passageiro
from Corrida import Corrida

from cli import MotoristaCLI

db = Database(database="App", collection="Motorista")

# Criando uma instância da classe MotoristaDAO para gerenciar motoristas no banco de dados
motorista_dao = MotoristaDAO(db)

motoristaCLI = MotoristaCLI(motorista_dao)
motoristaCLI.run()