from random import uniform, random, choice, sample
import matplotlib.pyplot as plt


#crio e definos as classes
class Posicao(): 
    def __init__(self, cod, norte, sul, leste, oeste ):
        self.cod = cod
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste

#individuo = solucao
class Individuo():
    def __init__(self, limite_movimentos,geracao=0):
        self.limite_movimentos = limite_movimentos
        self.nota = 0
        self.geracao = geracao
        self.cromossomo = []
        
#inicialiazo o cromossomo  aleatoriamente
        for i in range(limite_movimentos):
            opc = ["0", "1"]
            self.cromossomo.append(choice(opc))
            #fitnness                 
#fitnness                 
    def avaliacao(self):
        lista_posicao = []
    #lista posicao reduzida (cod,norte,sul,leste,oeste)
        lista_posicao.append(Posicao(11, 0, -1, 0, -1))
        lista_posicao.append(Posicao(12, 1, -1, 0, 0))
        lista_posicao.append(Posicao(13, 0, -1, 0, 0))
        lista_posicao.append(Posicao(14, 0, -1, -1, 0))
        lista_posicao.append(Posicao(21, 0, 0, 0, -1))
        lista_posicao.append(Posicao(22, 0, 1, 1, 0))
        lista_posicao.append(Posicao(23, 0, 0, 1, 1))
        lista_posicao.append(Posicao(24, 1, 0, -1, 1))
        lista_posicao.append(Posicao(31, 0, 0, 0, -1))
        lista_posicao.append(Posicao(32, 1, 0, 1, 0))
        lista_posicao.append(Posicao(33, 0, 0, 0, 1))
        lista_posicao.append(Posicao(34, 0, 1, -1, 0))
        lista_posicao.append(Posicao(41, -1, 0, 0, -1))
        lista_posicao.append(Posicao(42, -1, 1, 0, 0))
        lista_posicao.append(Posicao(43, -1, 0, 0, 0))
        lista_posicao.append(Posicao(44, -1, 0, 2, 0))
        #lista_posicao.append(Posicao(0, 0, -1, 1, -1))
        #00 norte
        #01 sul
        #10 leste
        #11 oeste
    
        nota = 0
        posicao_individuo = lista_posicao[0]
        i = 0 
        while i < (len(self.cromossomo)-1):
            #print("posição atual: %s " % posicao_individuo.cod, posicao_individuo.norte,posicao_individuo.sul,posicao_individuo.leste,posicao_individuo.oeste)
            #print("posição atual: %s nota: %s direçao %s" % (posicao_individuo.cod,nota,self.cromossomo[i] + self.cromossomo[i+1]))
        #se a direção for norte    
            if self.cromossomo[i] + self.cromossomo[i+1] == "00" and posicao_individuo.norte == 0:
                nota += 10
                posicao_destino = (posicao_individuo.cod + 10)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "00" and posicao_individuo.norte == 1:
                nota += 50
                posicao_destino = (posicao_individuo.cod + 10)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "00" and posicao_individuo.norte == -1:
                nota += 100
                #posicao_atual += 1  se ele for para fora do labirinto ele mantem a posição da borda

        #se a direção for sul    
            elif self.cromossomo[i] + self.cromossomo[i+1] == "01" and posicao_individuo.sul == 0:
                nota += 10
                posicao_destino = (posicao_individuo.cod - 10)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "01" and posicao_individuo.sul == 1:
                nota += 50
                posicao_destino = (posicao_individuo.cod - 10)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "01" and posicao_individuo.sul == -1:
                nota += 100
                #posicao_atual -= 1  se ele for para fora do labirinto ele mantem a posição da borda
        
         #se a direção for leste   
            elif self.cromossomo[i] + self.cromossomo[i+1] == "10" and posicao_individuo.leste == 0:
                nota += 10
                posicao_destino = (posicao_individuo.cod + 1)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "10" and posicao_individuo.leste == 1:
                nota += 50
                posicao_destino = (posicao_individuo.cod + 1)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "10" and posicao_individuo.leste == 2:
                nota -= 7000
                posicao_destino = (posicao_individuo.cod + 1)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "10" and posicao_individuo.leste == -1:
                nota += 100

         #se a direção for oeste    
            elif self.cromossomo[i] + self.cromossomo[i+1] == "11" and posicao_individuo.oeste == 0:
                nota += 10
                posicao_destino = (posicao_individuo.cod - 1)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "11" and posicao_individuo.oeste == 1:
                nota += 50
                posicao_destino = (posicao_individuo.cod - 1)
                for j in range(len(lista_posicao)):
                    if lista_posicao[j].cod == posicao_destino:
                        posicao_individuo = lista_posicao[j]
            elif self.cromossomo[i] + self.cromossomo[i+1] == "11" and posicao_individuo.oeste == -1:
                nota += 100            
            i += 2 
                
        if posicao_individuo.cod == 41:
            nota -= 1000
        elif posicao_individuo.cod== 42:
            nota -= 2000
        elif posicao_individuo.cod == 43:
            nota -= 3000
        elif posicao_individuo.cod == 44:
            nota -= 4000
        elif posicao_individuo.cod == 14:
            nota -= 1000
        elif posicao_individuo.cod == 24:
            nota -= 2000
        elif posicao_individuo.cod == 34:
            nota -= 3000
        elif posicao_individuo.cod == 33:
            nota -= 3000
        elif posicao_individuo.cod == 31:
            nota -= 500
        elif posicao_individuo.cod == 32:
            nota -= 1000
        elif posicao_individuo.cod == 34:
            nota -= 750
        elif posicao_individuo.cod == 13:
            nota -= 500
        elif posicao_individuo.cod == 23:
            nota -= 1000
        elif posicao_individuo.cod == 22:
            nota -= -500
        
        #print("posição final: %s" % posicao_individuo.cod)
        #print(" Nota: %s" % nota)
        
        self.nota_avaliacao = nota
        self.posicao_final = posicao_individuo.cod
              
#crossover
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.limite_movimentos,self.geracao + 1),
                  Individuo(self.limite_movimentos,self.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        #print(filhos[0].cromossomo)
        return filhos

#mutacao
    def mutacao(self,taxa_mutacao):
        #print("Antes %s" % self.cromossomo)
        
        lista_de_valores = ["0", "1"]

        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                self.cromossomo[i] = choice(lista_de_valores)                    

        #print("Depois %s" % self.cromossomo)
        return self

class Algoritimo():
    def __init__(self,tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []

    def inicializa(self,limite_movimentos):
        for i in range(tamanho_populacao):
            self.populacao.append(Individuo(limite_movimentos))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao)
                            
        
    def melhor_individuo(self,individuo):
        if individuo.nota_avaliacao < self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
    
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
#elitismo
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("Geracao: %s -> Valor: %s posicao: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                                     melhor.nota_avaliacao, 
                                                                     melhor.posicao_final,                                                                                                                       
                                                                     melhor.cromossomo))
        
    def resolver(self,taxa_mutacao,geracoes,limite_movimentos):
            self.inicializa(limite_movimentos)
            
            for individuo in self.populacao:
                individuo.avaliacao()
                
            self.ordena_populacao()
            self.melhor_solucao = self.populacao[0]
            self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
            
            self.visualiza_geracao()
            
            for geracao in range(geracoes):
                soma_avaliacao = self.soma_avaliacoes()
                nova_populacao = []
                
                for individuos_gerados in range(0, self.tamanho_populacao,2):
                    pai1 = self.seleciona_pai(soma_avaliacao)
                    pai2 = self.seleciona_pai(soma_avaliacao)
                    
                    filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                    
                    nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                    nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
                    
                self.populacao = list(nova_populacao)
                
                for individuo in self.populacao:
                    individuo.avaliacao()
                    
                self.ordena_populacao()
                 
                self.visualiza_geracao()
                
                melhor = self.populacao[0]
                self.lista_solucoes.append(melhor.nota_avaliacao)
                self.melhor_individuo(melhor)
    
            print("\n melhor solucao -> G: %s Valor %s posicaofinal: %s Cromossomo: %s" %
                (self.melhor_solucao.geracao,
                self.melhor_solucao.nota_avaliacao,
                self.melhor_solucao.posicao_final,
                self.melhor_solucao.cromossomo))     
            
                #posicao_desejada = self.melhor_solucao.posicao_final
    
            return self.melhor_solucao.cromossomo  

if __name__ == '__main__':
 

##limito o numero de movimentos em 10
 limite_movimentos = 16
 tamanho_populacao = 40
 probabilidade_mutacao = 0.9
 geracoes = 5

 ag = Algoritimo(tamanho_populacao)
 resultado = ag.resolver(probabilidade_mutacao, geracoes, limite_movimentos)

 #plt.plot(ag.lista_solucoes)
 #plt.show()
           
#incializo o individuo 1
 #individuo1 = Individuo(limite_movimentos)    
 #print("\nindividuo 1:  %s" % individuo1.cromossomo)

#avalio o individuo 1
 #individuo1.avaliacao()

# #incializo o individuo 
 #individuo2 = Individuo(limite_movimentos)    
 #print("\nindividuo 2:  %s" % individuo2.cromossomo)

# #avalio o individuo 2
 #individuo2.avaliacao() 

# # #faço o crossover
 #individuo1.crossover(individuo2)

# # #aplico a mutacao
 #individuo1.mutacao(0.05)
 #individuo2.mutacao(0.05)
   