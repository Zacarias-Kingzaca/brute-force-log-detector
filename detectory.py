from collections import Counter
import re


print("=== BRUTE-FORCE DETECTOR ===\n")

# Lê o arquivo de logs
try:
    with open("logs.txt", "r") as f:
        logs = f.readlines()
except FileNotFoundError:
    print("Erro: arquivo logs.txt não encontrado. Crie o arquivo primeiro!")
    exit()

# Pega só as linhas que são falha de login
falhas = []
ips_falhas = []

for linha in logs:
    if "Login failed" in linha:
        falhas.append(linha)
        # Regex para extrair o IP: procura por padrão IP: XXX.XXX.XXX.XXX
        ip = re.search(r'IP:\s*(\d+\.\d+\.\d+\.\d+)', linha)
        if ip:
            ips_falhas.append(ip.group(1))

print(f"Total de tentativas falhas encontradas: {len(falhas)}")

# Conta quantas vezes cada IP falhou
contagem = Counter(ips_falhas)

print("\n--- Relatório de IPs suspeitos ---")
ataque_detectado = False
for ip, qtd in contagem.items():
    if qtd >= 3:  # Se falhou 3 vezes ou mais, é suspeito
        print(f"[!] ALERTA: IP \033[31m{ip}\033[m tentou {qtd} vezes - POSSÍVEL BRUTE-FORCE")
        ataque_detectado = True
    else:
        print(f"[OK] IP {ip} - {qtd} tentativa(s)")

if ataque_detectado:
    print("\n>>> AÇÃO RECOMENDADA: Bloquear IPs acima no firewall <<<")
else:
    print("\nNenhum ataque detectado.")

# Salva relatório
with open("relatorio.txt", "w") as out:
    out.write("RELATORIO DE SEGURANCA\n")
    for ip, qtd in contagem.items():
        out.write(f"{ip} - {qtd} falhas\n")

print("\nRelatório salvo em relatorio.txt")

