nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: ")) #definimos a variavel nota1 ela e do tipo flot, e deve colocar numeros reais 
nota2 = float(input("Digite a segunda nota: ")) #definimos a variavel nota2 ela e do tipo flot, e deve colocar numeros reais 
nota3 = float(input("Digite a terceira nota: ")) #definimos a variavel nota3 ela e do tipo flot, e deve colocar numeros reais 

media = (nota1 + nota2 + nota3) / 3  #fizemos o calculo da média 

print(f"A média do aluno é: {media:.2f}")  
#f = significa ftring, para eu conseguir colocar uma variavel entre aspas ""  
# .2f = significa quantas casa terá após a virgula
# {média} coloca entre chaves porque colocamos a variavel media no string

if media >= 7.0:
    print("Aluno APROVADO!")
else:
    print("Aluno REPROVADO.")


#if = se (se a nota for maior ou igual a média)
#else = senão (se for menos)