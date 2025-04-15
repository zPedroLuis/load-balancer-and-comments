def read_input(file_path):
    """Lê o arquivo de entrada e valida os dados."""
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        
        # Extrair ttask e umax
        ttask = int(lines[0])
        umax = int(lines[1])
        
        # Validar limites
        if not (1 <= ttask <= 10):
            raise ValueError("ttask deve estar entre 1 e 10.")
        if not (1 <= umax <= 10):
            raise ValueError("umax deve estar entre 1 e 10.")
        
        # Extrair números de usuários por tick
        users_per_tick = [int(line) for line in lines[2:]]
        if any(user < 0 for user in users_per_tick):
            raise ValueError("Os números de usuários por tick não podem ser negativos.")
        
        return ttask, umax, users_per_tick
    
    except Exception as e:
        print(f"Erro ao ler o arquivo de entrada: {e}")
        return None, None, None


def simulate_allocation(ttask, umax, users_per_tick):
    """Simula a alocação de usuários nos servidores tick por tick."""
    servers = []  # Lista de servidores ativos
    output = []   # Estado dos servidores em cada tick
    
    for new_users in users_per_tick:
        # Atualizar estado dos servidores (remover usuários completados)
        servers = [(server - 1) for server in servers if server > 1]
        
        # Adicionar novos usuários
        for _ in range(new_users):
            # Tentar adicionar ao último servidor disponível
            if servers and servers[-1] < umax:
                servers[-1] += 1
            else:
                # Criar novo servidor
                servers.append(1)
        
        # Registrar estado dos servidores
        output.append(','.join(map(str, servers)) if servers else '0')
    
    return output


def calculate_cost(output):
    """Calcula o custo total com base no número de servidores ativos."""
    cost = sum(len(server.split(',')) for server in output)
    return cost


def write_output(file_path, output, cost):
    """Escreve o estado dos servidores e o custo total no arquivo de saída."""
    with open(file_path, 'w') as file:
        for line in output:
            file.write(line + '\n')
        file.write(str(cost))


if __name__ == "__main__":
    # Caminhos dos arquivos de entrada e saída
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # Ler o arquivo de entrada
    ttask, umax, users_per_tick = read_input(input_file)
    if ttask is None or umax is None or users_per_tick is None:
        exit(1)
    
    # Simular a alocação de usuários
    output = simulate_allocation(ttask, umax, users_per_tick)
    
    # Calcular o custo total
    cost = calculate_cost(output)
    
    # Escrever o arquivo de saída
    write_output(output_file, output, cost)