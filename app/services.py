class Enviroment:
    def __init__(self, env: str) -> None:
        self.ENV = env

    def get_env(self):
        return self.ENV

    def __repr__(self) -> str:
        return f"env = {self.ENV}"