from datetime import datetime, timedelta

# Dados das manutenções
manutencoes = [
    # Main Line
    {'nome': 'IL22272', 'localizacao': 'MAIN LINE', 'sub_localizacao': 'TVL', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22276', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.1.1', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22261', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.1.2', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22263', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.3.1', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22262', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.3.2', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22289', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.5.1', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22277', 'localizacao': 'MAIN LINE', 'sub_localizacao': '5.5.2', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22267', 'localizacao': 'MAIN LINE', 'sub_localizacao': 'TÚNEL', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},

    # Revisão
    {'nome': 'IL9529', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 1 SPCT50 BRAKE', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL9532', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 1 SPCT55 TRUCK CAM', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22270', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 1 SPCT 60 DIS', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22280', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 1 SPCT 65', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22273', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 45.3 TPM', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL9533', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 50 BRAKE', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22286', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 55 TRUCK CAM', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22279', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 60 DIS', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22265', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 65', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22284', 'localizacao': 'REVISAO', 'sub_localizacao': 'FLUXO 2 SPCT 99 REPAIR', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22283', 'localizacao': 'REVISAO', 'sub_localizacao': 'BOX 1', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22268', 'localizacao': 'REVISAO', 'sub_localizacao': 'BOX NAGIB', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},

    # Tenda
    {'nome': 'IL22288', 'localizacao': 'TENDA', 'sub_localizacao': 'TENDA SPCT99', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22275', 'localizacao': 'TENDA', 'sub_localizacao': 'TENDA SPCT99', 'tipo_manutencao': 'Verificação de Hardware', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22278', 'localizacao': 'TENDA', 'sub_localizacao': 'TENDA SPCT99', 'tipo_manutencao': 'Backup de Dados', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22266', 'localizacao': 'TENDA', 'sub_localizacao': 'TENDA SPCT99', 'tipo_manutencao': 'Teste de Performance', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10},
    {'nome': 'IL22281', 'localizacao': 'TENDA', 'sub_localizacao': 'TENDA SPCT99', 'tipo_manutencao': 'Limpeza', 'ultima_manutencao': '2023-04-01', 'intervalo_meses': 10}
]

def calcular_proxima_manutencao(ultima_manutencao, intervalo_meses):
    data_ultima = datetime.strptime(ultima_manutencao, '%Y-%m-%d')
    proxima_manutencao = data_ultima
    while proxima_manutencao < datetime.now():
        proxima_manutencao += timedelta(days=intervalo_meses * 30)
    return proxima_manutencao

def exibir_manutencoes_por_area(area):
    hoje = datetime.now()
    print(f"\n📍 {area.upper()}")
    for i, manutencao in enumerate([m for m in manutencoes if m['localizacao'] == area], start=1):
        proxima_manutencao = calcular_proxima_manutencao(manutencao['ultima_manutencao'], manutencao['intervalo_meses'])
        dias_restantes = (proxima_manutencao - hoje).days
        print(f"   {i}. {manutencao['nome']} ({manutencao['sub_localizacao']}) - {manutencao['tipo_manutencao']} | Data limite: {proxima_manutencao.strftime('%d/%m/%Y')} | Dias restantes: {dias_restantes}")

def atualizar_manutencao(indice):
    hoje = datetime.now().strftime('%Y-%m-%d')
    manutencoes[indice]['ultima_manutencao'] = hoje
    print(f"✅ Manutenção de {manutencoes[indice]['tipo_manutencao']} marcada como concluída em {hoje}.")

# Menu interativo
while True:
    print("\n🔧 MENU DE MANUTENÇÃO 🔧")
    print("1. Checkar MacStation")
    print("2. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        print("\nEscolha uma área:")
        print("1. Main Line")
        print("2. Revisão")
        print("3. Tenda")

        area_opcao = input("Digite o número da área desejada: ")
        areas = {"1": "MAIN LINE", "2": "REVISAO", "3": "TENDA"}

        if area_opcao in areas:
            exibir_manutencoes_por_area(areas[area_opcao])
            try:
                indice = int(input("Digite o número da manutenção concluída (ou 0 para voltar): ")) - 1
                if indice == -1:
                    continue
                if 0 <= indice < len(manutencoes):
                    atualizar_manutencao(indice)
                else:
                    print("⚠️ Opção inválida.")
            except ValueError:
                print("⚠️ Entrada inválida. Digite um número.")
        else:
            print("⚠️ Opção inválida.")

    elif opcao == '2':
        print("Saindo do programa. 👋")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
