# server.py
from attendant import Attendant
import random

class Server:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.attendants = {
            "Suporte Técnico": [Attendant("Suporte Técnico") for _ in range(random.randint(1, capacity//2))],
            "Vendas": [Attendant("Vendas") for _ in range(random.randint(1, capacity//2))]
        }
        self.active = True

    def process_request(self, request_type):
        available_attendants = [attendant for attendant in self.attendants[request_type] if attendant.active]
        if available_attendants:
            attendant = available_attendants[0]
            return attendant.handle_request()
        return False  # Nenhum atendente disponível

    def fail(self):
        self.active = False  # Simula falha do servidor
