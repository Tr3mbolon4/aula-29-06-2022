print('[CADASTRO DE DADOS E SENHA COM TESTE!]')
print('='*35)
print('vamos fazer um pequeno cadastro de dados e senha')
print('='*35)
print('VOCE IRAR FAZER UM TESTE LOGICO DE PERGUNTAS DE NIVEL FACIL')
print('='*35)
certo= input('Voce esta pronto!? responda SIM ou Nao:\n')


if certo == 'nao':
    print('Certo! vamors Encerrar por Aqui:\n')

if  certo == 'sim':
    print('\nOK vamor Iniciar\n')
    nome = input('\nDigite seu Nome:\n ')
    sobrenome = input('\nDigite seu sobre nome:\n ')
    cidade = input('\nDigite sua cidade:\n ')
    estado = input('\n Qual seu estado:\n ')
    profissao = input('\nQual Sua Profissão:\n ')
    nascimento = input('\nQual ano voce nasceu:\n')
    idade = 2022 - int(nascimento)


    senha = input('\nDigite uma senha:\n')
    senha2 = input('\nconfirme sua senha:\n')

    texto = f' \no {nome} {sobrenome} mora na {cidade} e um execelente [{profissao}] e tem {idade} de idade\n'



    while senha != senha2:
        print('\nErro! senha digitada errada, confirme a senha e digite novamente\n')

        senha = input('\nDigite uma Senha: sem caracteres e sem letras: somente numeros:\n ')
        senha2 = input('\nConfirme sua senha:\n ')

    if senha == senha2:
        print('\nSenha correta parabenz: cadastro feito com sucesso!\n')
        print(texto)



        print('\nNo tem esse Comando:\n')
        print('Perguntas e Respostas'.center(35, '-'))

print("""Quem Fundou o Brasil?
[1] = Pedro alvars Cabral
[2] = bolsonaro
[3] = lula""")
pergunta1 = int(input('Resposta: '))
nota = 0


while pergunta1 > 3 or pergunta1 <1:
    print('Opção errda digite uma opção valida')
    print(""" Quem Fundou o Brasil?
    [1] = Pedro alvars Cabral
    [2] = bolsonaro
    [3] = lula""")
    pergunta1 = int(input('Resposta: '))

if pergunta1 == 1:
    print('Correto parabens!')
    nota += 5
elif pergunta1 == 2:
    print('Cai fora bolsominion, Pergunta errada!')

elif pergunta1 == 3:
    print('Lulominion sai fora, pegunta errada!')

print('='*70)
print("""Qual o nome do Presidente do Brasil?
[1] = Pedro alvars Cabral
[2] = bolsonaro
[3] = lula""")

pergunta2 = int(input('Resposta: '))

if pergunta2 == 1:
    print('Errado! volta pr aescola!')

elif pergunta2 == 2:
    print('Parabens!')
    nota += 5

elif pergunta2 == 3:
    print('Resosta errada!')

    print('Sua Nota Foi', nota)

