# attendant.py
import random
import time

class Attendant:
    def __init__(self, attendant_type):
        self.type = attendant_type  # "Suporte Técnico" ou "Vendas"
        self.active = True  # Representa se o atendente está ativo

    def handle_request(self):
        if self.active:
            time.sleep(0.1)  # Simula o tempo de atendimento
            return True
        return False

    def fail(self):
        self.active = False  # Simula uma falha no atendente
