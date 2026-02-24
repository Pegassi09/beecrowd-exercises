bus = 45
qtd = int(input(" quantos alunos vao: "))
total = (qtd // bus) + qtd % bus
print(f" serao necessarios {total} ônibus")