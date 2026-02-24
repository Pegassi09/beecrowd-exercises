desc = float(input("digite seu desconto se houver: "))
valor = float(input("Digite o valor do produto: "))
v_disc =  (valor * desc) / 100
valor_f = valor - v_disc

print(f"""Valor do desconto {v_disc}
valor final {valor_f}""")