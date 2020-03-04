import requests

class Usuario(object):
    #TODO
    def __init__(self, login: str, senha: str) -> str:
        pass

    #TODO
    @property
    def nome(self) -> str:
        pass

    #TODO
    @nome.setter
    def nome(self, new_name: str) -> str:
        pass

    #TODO
    @property
    def senha(self, teste) -> bool:
        pass
    
    #TODO
    @senha.setter
    def senha(self, password: str, new_password: str) -> bool:
        pass

    #TODO
    def logar(self) -> bool:
        pass

    #TODO 
    def get_dados(self) -> bool:
        pass

    #TODO
    def get_repositories(self) -> list:
        pass

    #TODO
    def followers(self) ->list:
        pass

    #TODO
    def following(self) -> list:
        pass

    #TODO
    def stars(self) -> list:
        pass