from src.client import Client


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def add_client(self, name):
        c = Client(name)
        self.clients.append(c)


if __name__ == '__main__':
    b = Bank('Chase')
    b.add_client('Janet')
    b.add_client('Mark')
    b.add_client('Chyld')
    janet = b.clients[0]
    janet.add_account(100, 'checking')
    janet.add_account(200, 'savings')
