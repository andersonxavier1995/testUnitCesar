from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        # Verificar se os parâmetros são strings, não são vazios e contêm apenas letras
        if isinstance(name, str) and isinstance(job, str) and name.strip() != "" and job.strip() != "" and name.isalpha() and job.isalpha():
            # Verificar se o nome já existe para adicionar
            if any(user.name == name for user in self.store.bd):
                return "Usuário já existe"

            # Adicionar usuário
            user = User(name, job)
            self.store.bd.append(user)
            return "Usuário adicionado"
        else:
            return "Parâmetros inválidos"  # Retorno caso name ou job sejam inválidos

    def remove_user(self, name):
        # Verificar se o parâmetro é string, não é vazio e contém apenas letras
        if isinstance(name, str) and name.strip() != "" and name.isalpha():
            # Verificar se o nome existe para remover
            for user in self.store.bd:
                if user.name == name:
                    self.store.bd.remove(user)
                    return "Usuário removido"
            return "Usuário não encontrado"
        else:
            return "Parâmetro inválido"  # Retorno caso name seja inválido
