# main.py
from server import Server
from monitor import Monitor
from logger import Logger
import random

# Configuração inicial
servers = [Server("A", 5), Server("B", 7), Server("C", 10)]
monitor = Monitor(servers)
logger = Logger()
timesteps = 100

# Inicializa dados para gráficos
server_activity = {server.id: [] for server in servers}  # Atendimentos por servidor
server_failures = {server.id: [] for server in servers}  # Falhas por servidor
redirections = []  # Contagem de redirecionamentos

# Simulação de atendimento
for timestep in range(timesteps):
    logger.log(f"Início do timestep {timestep + 1}")
    num_requests = random.randint(10, 20)
    redirections_this_timestep = 0  # Contador de redirecionamentos no timestep atual

    # Geração de solicitações
    for _ in range(num_requests):
        request_type = random.choice(["Suporte Técnico", "Vendas"])
        processed = False
        for server in servers:
            if server.active and server.process_request(request_type):
                server_activity[server.id].append(1)  # Registra atendimento
                processed = True
                break
        if not processed:
            redirections_this_timestep += 1
            logger.log(f"Redirecionando solicitação {request_type}")
            monitor.reroute_request(request_type)
    
    # Verificação de falhas e ajuste de servidores
    monitor.check_failures(timestep)

    # Atualiza dados para gráficos de falhas e redirecionamentos
    for server in servers:
        server_failures[server.id].append(1 if not server.active else 0)  # 1 para falha, 0 para ativo
    redirections.append(redirections_this_timestep)
    logger.log(f"Fim do timestep {timestep + 1}\n")

# Importando o matplotlib para visualização de gráficos
import matplotlib.pyplot as plt
import numpy as np

# Gráfico de Barras: Comparação de Atendimentos por Servidor
plt.figure(figsize=(10, 6))
for server_id, activity in server_activity.items():
    plt.bar(server_id, sum(activity), label=f"Servidor {server_id}")
plt.xlabel("Servidores")
plt.ylabel("Total de Atendimentos")
plt.title("Comparação de Atendimentos por Servidor")
plt.legend()
plt.show()

# Gráfico de Linha: Número de Falhas ao Longo do Tempo com Curvas Suaves
from scipy.interpolate import make_interp_spline

plt.figure(figsize=(10, 6))
for server_id, failures in server_failures.items():
    timesteps = np.arange(len(failures))  # Timesteps originais

    # Interpolação para suavizar as linhas
    timesteps_new = np.linspace(timesteps.min(), timesteps.max(), 300)  # Mais pontos para suavizar
    smooth_failures = make_interp_spline(timesteps, failures)(timesteps_new)
    plt.plot(
        timesteps_new,
        smooth_failures,
        label=f"Servidor {server_id}",
        linestyle="-",
        marker="o",  # Adiciona marcadores
        markersize=4
    )

plt.xlabel("Timesteps")
plt.ylabel("Status de Falha (1=Falhou, 0=Ativo)")
plt.title("Número de Falhas ao Longo do Tempo com Variações")
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Pizza: Distribuição de Requisições Redirecionadas
plt.figure(figsize=(8, 8))
redirection_values = list(monitor.redirection_counts.values())
redirection_labels = list(monitor.redirection_counts.keys())
plt.pie(
    redirection_values,
    labels=[f"Servidor {label}" for label in redirection_labels],
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Distribuição de Redirecionamentos entre Servidores")
plt.show()