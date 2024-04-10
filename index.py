# Desenvolver um projeto (usando dicionários) que vai gravar a quantidade de currículos para aquela vaga e quantas
# pessoas têm as palavras-chave necessárias no currículo. Para isso, nosso código Python vai checar para qual vaga
# a pessoa se inscreveu e o resumo que a pessoa enviou em busca dessas informações.


# As palavras-chave das vagas são:
# Vaga 1: Python, Programação, Desenvolvimento;
# Vaga 2: Análise de dados, Dados, SQL.
# Nosso código deve ficar pedindo para qual vaga a pessoa se inscreveu e o resumo de cada participante em loop 
# (só deve parar quando inserir o número 0 na pergunta da vaga).
# O texto do resumo/minibio vai ser informado pelo usuário 
# (como desafio extra você pode tentar ler esse texto de arquivos txt em uma pasta e eliminar essa etapa de pedir os textos em loop)
# e então vamos checar se temos as palavras-chave necessárias e marcar como um candidato válido para a vaga.
# No final do código (quando o usuário digitar 0 para sair) vamos mostrar os totais, quantas pessoas estão inscritas em cada vaga e quantas
# têm o resumo/minibio com as palavras que estamos buscando.



curriculos = {
    "Vaga 1": [],
    "Vaga 2": [],
    "Desacarte": []
}


while True:
    QualVaga = input("Digite a Vaga selecionada 1 ou 2 (00 pra sair)>>")
    def verif(vaga,nome, resumo):
        return curriculos["Vaga " + vaga].append({"Nome": nome, "Minibio": resumo})
    def Desacarte(nome, resumo):
        return curriculos["Desacarte"].append({"Nome": nome, "Minibio": resumo})

    if QualVaga == '1':
        Nome = input("Digite seu nome>>")
        resumo = input("Digite seu minibio>>")
        if "Python" in resumo or "Programacao" in resumo or "Desenvolvimento" in resumo:
            verif(QualVaga, Nome, resumo)
        else:
            Desacarte(Nome, resumo)
    elif QualVaga == '2':
        Nome = input("Digit seu nome>>")
        resumo = input("Digite seu minibio>>")
        if "Analise de dados" in resumo or "Dados" in resumo or "SQL" in resumo:
            verif(QualVaga, Nome, resumo)
        else:
            Desacarte(Nome, resumo)

    elif QualVaga == '00':
        break
    else:
        print("Numero invalido")

print(curriculos)
