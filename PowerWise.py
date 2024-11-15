import os

consumes = []
power = []
time = []

def salvar_dados_txt():
    with open("dados_energia.txt", "w") as file:
        for i in range(len(consumes)):
            file.write(f"{consumes[i]};{power[i]};{time[i]}\n")
    print("Dados salvos com sucesso em dados_energia.txt!")

def carry_data_txt():
    if os.path.exists("dados_energia.txt"):
        with open("dados_energia.txt", "r") as file:
            for line in file:
                nome, pot, hrs = line.strip().split(";")
                consumes.append(nome)
                power.append(float(pot))
                time.append(float(hrs))
        print("Dados carregados com sucesso de dados_energia.txt!")
    else:
        print("Nenhum dado salvo encontrado.")

def program_name():
    print('''
██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██╗    ██╗██╗███████╗███████╗
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██║    ██║██║██╔════╝██╔════╝
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██║ █╗ ██║██║███████╗█████╗  
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██║███╗██║██║╚════██║██╔══╝  
██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║╚███╔███╔╝██║███████║███████╗
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝
''')

def show_options():
    print('1. Cadastrar fonte de consumo de energia')
    print('2. Listar consumidores')
    print('4. Resultado média gasto mensal')
    print('5. Sair\n')

def end_app():
    salvar_dados_txt()
    print("Finalizando o app...")

def back_to_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    back_to_menu()

def show_subtitle(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print()

def register_new_consumption():
    show_subtitle('Cadastro de novos consumos')
    consume_name = input('Digite o nome do consumo que deseja cadastrar: ')
    consumes.append(consume_name)
    killowat = float(input('Digite a potência em kW do consumo: '))
    power.append(killowat)
    timee = float(input('Digite o uso do consumo em horas por dia: '))
    time.append(timee)
    print(f"O consumo {consume_name} foi cadastrado com sucesso!")
    back_to_menu()

def amount_energ_bill(consumes, power, time):
    energy_data = {}
    for i in range(len(consumes)):
        energy_data[consumes[i]] = {
            'consumo_kw': power[i],
            'horas_por_dia': time[i]
        }
    
    fare = 0.73
    total_cost = 0

    print("\nDetalhes do consumo de energia:")
    for consume, data in energy_data.items():
        month_consumption = data['consumo_kw'] * data['horas_por_dia'] * 30
        cost_consumption = month_consumption * fare
        total_cost += cost_consumption
        print(f"{consume}: Consumo mensal = {month_consumption:.2f} kWh, Custo = R$ {cost_consumption:.2f}")
    
    print(f"\nCusto total estimado para todos os aparelhos: R$ {total_cost:.2f}")
    back_to_menu()

def list_consumptions():
    show_subtitle('Listando os consumos')
    for consumo in consumes:
        print(f"- {consumo}")
    back_to_menu()

def choose_options(): 
    try:   
        choose_option = int(input('Escolha uma opção: '))
            
        if choose_option == 1:
            register_new_consumption()
        elif choose_option == 2:
            list_consumptions()
        elif choose_option == 4:
            amount_energ_bill(consumes, power, time)
        elif choose_option == 5:
            end_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    carry_data_txt()
    os.system('cls' if os.name == 'nt' else 'clear')
    program_name()
    show_options()
    choose_options()

if __name__ == '__main__':
    main()
