# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
aluno1=float(input("digite sua primeira nota"))
aluno2=float(input("digite sua segunda nota"))
aluno3=float(input("digite sua terceira nota"))
# Média ≥ 7: Aprovado
media=(aluno1+aluno2+aluno3)/3
if (media>=7):
    print("aprovado")
# 5 ≤ Média < 7: Recuperação
elif(5<= media <7):
    print("recuperação")

# Média < 5: Reprovado
elif(media< 5):
    print("reprovado")