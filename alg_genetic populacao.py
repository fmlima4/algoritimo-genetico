from random import random

#crio e definos as classes
class Produto():
    def __init__(self, nome, espaco,valor ):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

class Individuo():
    def __init__(self, espacos,valores,limite_espacos,geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []
        
#inicialiazo o cromossomo  com 50% de change de ele ser 0 ou 1      
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
#fitnness                 
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == "1":
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
        
#crossover
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos,self.valores,self.limite_espacos,self.geracao + 1),
                  Individuo(self.espacos,self.valores,self.limite_espacos,self.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos

#mutacao
    def mutacao(self,taxa_mutacao):
        print("Antes %s" % self.cromossomo)
        
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == "1":
                    self.cromossomo[i] = "0"
                else:
                    self.cromossomo[i] = "1"
        print("Depois %s" % self.cromossomo)
        return self

class Algoritimo():
    def __init__(self,tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0

    def inicializa(self,espacos,valores,limite_espacos):
        for i in range(tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,limite_espacos))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self,individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
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
            

if __name__ == '__main__':
   # p1 = Produto("iphone 6", 0.0000899, 2199.12)
   lista_produtos = []
   lista_produtos.append(Produto("p1", 0.751, 999.90))
   lista_produtos.append(Produto("p2", 0.0000899, 2199.12))
   lista_produtos.append(Produto("p3", 0.400, 4346.99))
   lista_produtos.append(Produto("p4", 0.290, 3999.90))
   lista_produtos.append(Produto("p5", 0.200, 2999.00))
   lista_produtos.append(Produto("p6", 0.00350, 2499.90))
   lista_produtos.append(Produto("p7", 0.496, 199.90)) 
   lista_produtos.append(Produto("p8", 0.0424, 308.66))
   lista_produtos.append(Produto("p9", 0.0544, 429.90))
   lista_produtos.append(Produto("p10", 0.0319, 299.29))
   lista_produtos.append(Produto("p11", 0.635, 849.0))
   lista_produtos.append(Produto("p12", 0.870, 1199.89))
   lista_produtos.append(Produto("p13", 0.498, 1999.90))
   lista_produtos.append(Produto("p14", 0.527, 3999.00))
   # for produto in lista_produtos:
   #    print(produto.nome)
   
   espacos = []
   valores = []
   nomes = []
   
   for produto in lista_produtos:
       espacos.append(produto.espaco)
       valores.append(produto.valor)
       nomes.append(produto.nome)

   limite = 3
    
   tamanho_populacao = 20
   
   ag = Algoritimo(tamanho_populacao)
   ag.inicializa(espacos,valores,limite)
   
 #dou uma nota para cada individuo da populacao
   for individuo in ag.populacao:
       individuo.avaliacao()
       
#ordeno a populacao pela nota
   ag.ordena_populacao()
   
#encontro o melhor indivduo
   ag.melhor_individuo(ag.populacao[0])
   
   
#resultados em tela
   for i in range(ag.tamanho_populacao):
       print("*** Individuo %s ***\n" % i,
             "Espaços = %s \n " % str(ag.populacao[i].espacos),
             "valores = %s \n " % str(ag.populacao[i].valores),
             "Cromosssomo = %s \n" % str(ag.populacao[i].cromossomo),
             "Nota = %s \n" % ag.populacao[i].nota_avaliacao)
       

print("Melhor solucao para o problema: %s " % ag.melhor_solucao.cromossomo,
      "Nota: %s " % ag.melhor_solucao.nota_avaliacao)   

soma = ag.soma_avaliacoes()
print("soma das avaliacoes %s " % soma)


   
   
   
   
   
   
   
   