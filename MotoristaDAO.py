class MotoristaDAO:
    def __init__(self, database):
        self.database = database

    def create_motorista(self, motorista):
        self.database.motoristas.append(motorista)

    def read_motorista(self, nota):
        for motorista in self.database.motoristas:
            if motorista.nota == nota:
                return motorista
        return None

    def update_motorista(self, nota, new_motorista):
        for i, motorista in enumerate(self.database.motoristas):
            if motorista.nota == nota:
                self.database.motoristas[i] = new_motorista
                return True
        return False

    def delete_motorista(self, nota):
        for motorista in self.database.motoristas:
            if motorista.nota == nota:
                self.database.motoristas.remove(motorista)
                return True
        return False
