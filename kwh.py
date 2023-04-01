sm = float(input("Digite o valor do salário mínimo:"))
qw = float(input("Digite o valor gasto de quilowatts:"))
vkwh= sm / 7 / 100
vt = qw * vkwh
d = vt*0.1
vtd = vt-d
print("O valor pago por 1 kwh é de R$", vkwh)
print("O valor pago pela energia elétrica é de R$", vt)
print("O valor pago pela energia elétrica com desconto de 10% é de R$", vtd)