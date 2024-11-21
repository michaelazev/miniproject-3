# monitor.py
import random
import time

class Monitor:
    def __init__(self, servers):
        self.servers = servers
        self.inactive_attendants = {}  # Armazena atendentes inativos e o timestep em que falharam
        self.waiting_requests = {}     # Fila de espera com contagem de tentativas
        self.redirection_counts = {server.id: 0 for server in servers}  # Redirecionamentos por servidor
        
    def check_failures(self, timestep):
        for server in self.servers:
            if random.random() < 0.1:  # 10% de chance de falha
                server.fail()
                self.redirection_counts[server.id] += 1  # Incrementa o contador do servidor
                print(f"Servidor {server.id} falhou.")
            
            for attendant_type, attendants in server.attendants.items():
                for attendant in attendants:
                    if not attendant.active:
                        
                        # Verifica se o atendente já está registrado como inativo e se passaram mais de 5 timesteps desde que ele falhou
                        if (attendant in self.inactive_attendants) and (timestep - self.inactive_attendants[attendant] > 5):
                            attendant.active = True
                            print(f"Atendente de {attendant.type} reativado no Servidor {server.id}")
                            del self.inactive_attendants[attendant]
                        elif attendant not in self.inactive_attendants:
                            self.inactive_attendants[attendant] = timestep

    def reroute_request(self, request_type):
        for server in self.servers:
            if server.active and server.process_request(request_type):
                return True
        
        # Incrementa a contagem de tentativas da solicitação na fila de espera
        if request_type not in self.waiting_requests:
            self.waiting_requests[request_type] = 1
        else:
            self.waiting_requests[request_type] += 1
        
        # Registra falha e adiciona à fila de espera
        print("Falha ao redirecionar solicitação.")
        return False

    def process_waiting_requests(self):
        for request_type, attempts in list(self.waiting_requests.items()):  # cópia para evitar alteração durante iteração
            if attempts > 5:
                print(f"Solicitação {request_type} removida da fila após {attempts} tentativas.")
                del self.waiting_requests[request_type]
            elif self.reroute_request(request_type):
                del self.waiting_requests[request_type]  # Remove da fila se atendida
