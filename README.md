# Análise de Desempenho de Servidores

Este projeto apresenta uma análise de desempenho e comportamento de servidores, utilizando gráficos para representar visualmente os resultados. O objetivo é monitorar falhas, redirecionamentos e a performance geral de cada servidor.

---

## 📊 Gráficos Gerados

### 1. Gráfico de Pizza

![Gráfico de Pizza](Grafico%20Pizza.png)

**Descrição:**  
Este gráfico mostra a distribuição de redirecionamentos entre os servidores:  
- **Servidor A:** 20%  
- **Servidor B:** 50%  
- **Servidor C:** 30%  

---

### 2. Gráfico de Linhas

![Gráfico de Linhas](./Grafico%20Linhas.png)  

**Descrição:**  
Este gráfico monitora o status dos servidores ao longo do tempo:  
- **Eixo X:** Representa o tempo (em *timesteps*).  
- **Eixo Y:** Representa o status dos servidores (1 = Falha, 0 = Ativo).  
Cada linha colorida indica um servidor diferente.  

---

### 3. Gráfico de Barras

![Gráfico de Barras](./Grafico%20barras.png)  

**Descrição:**  
Este gráfico compara o total de atendimentos realizados por cada servidor:  
- **Servidor A:** 300 atendimentos  
- **Servidor B:** 0 atendimentos  
- **Servidor C:** 0 atendimentos  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Matplotlib**: Para visualização dos dados.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-repositorio.git
