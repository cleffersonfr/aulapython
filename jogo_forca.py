#checa_vidas_restantes(vidas_atuais:int,chute_acertado: bool): bool
from campo_minado import is_vitoria

def chute_errado(qtd_vidas,palavra_secreta, palavra_atual):
    qtd_vidas-=1
    print(f"Palavra atual: {plavra_atual_str(palavra_atual)}")
    if qtd_vidas==0:
        print("Voce perdeu o jogo :(")
        print(f"palavra secreta era: {palavra_secreta}")
        return (False,qtd_vidas)
    return (True,qtd_vidas)

#Inicia jogo(): void -> Imprimir a mensagem incial para o jogodr
def iniciar_jogo():
    print("Bem-vindo ao jogo de Forca!")
    print("Prepare-se para adivinhar a palavra secreta.")
    print("Divirta-se!")
    

# inputs_inicias():pedir os dados via input que seram retornados-> return(qtd_vidas_tot, pavalvra_secreta)
def inputs_iniciais():
    

    qtd_vidas_tot = int(input("inserir qtd vidas"))
    palavra_secreta = input('inserir palavra secreta: ').lower()
    print("\n"*50)

    return qtd_vidas_tot,palavra_secreta

def checa_letra_na_palavra(palavra_secreta,letra): 
    return letra in palavra_secreta

def atualiza_palavra_atual(letra_chutada, palavra_secreta, palavra_atual):
    palavra_secreta = list(palavra_secreta)
    for i in range(len(palavra_secreta)):
        letra = palavra_secreta[i]
        if letra == letra_chutada:
            palavra_atual[i]=letra
    return palavra_atual

def plavra_atual_str(palavra_atual):
    palavra= ""
    for letra in palavra_atual:
        palavra+=letra
    return palavra

# retornar a lista de posicoes onde essa letra aparece, caso contrario retornar uma lista vazia

# mostra_palavra_atual(palavra_secreta,lista_posicoes_acertadas):return palavara_atual
def chute_certo(letra_chutada,palavra_secreta, palavra_atual, tentadas):
    print(f"Voce acertou a letra {letra_chutada}")
    palavra_atual = atualiza_palavra_atual(letra_chutada,palavra_secreta, palavra_atual)
    
    print(f"Palavra atual: {plavra_atual_str(palavra_atual)}")
    
   
        
    print("Letras ja tentadas: ", tentadas)


    return (is_vitoria(palavra_atual),palavra_atual)




def jogo():
    iniciar_jogo()
    qtd_vidas,palavra_secreta =inputs_iniciais()
    palavra_atual = ["*"]*len(palavra_secreta)
    tentadas =[]
    print("Iniciando jogo================")
    while True:
        letra_chutada = input("Digite uma letra:").lower()
        if letra_chutada in tentadas:
            print("Essa letra ja foi chutuda!!!")
            continue
        
        tentadas.append(letra_chutada)
        
        if checa_letra_na_palavra(palavra_secreta, letra_chutada):
            vitoria,palavra_atual=chute_certo(letra_chutada, palavra_secreta,palavra_atual,tentadas)
            if vitoria:
                print("voce ganhou!!!")
                break
        else:
            continua, qtd_vidas = chute_errado(qtd_vidas,palavra_secreta, palavra_atual)
            print("qtd de vidas restantes:", qtd_vidas)
            if not continua:
                break

jogo()