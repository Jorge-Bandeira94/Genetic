# Genetic

Criado por Jorge Luís

Esté é um programa de testes voltado para área de bioinformática, tendo a função de traduzir sequências de DNA em linha única para sequências peptídicas e mostrar todos os quadros de leitura possíveis para a mesma sequência (-1,-2,-3, +1, +2, +3).

O código do programa é simples e utiliza iteração e fatiamento da string (sequência) a cada 3 deslocamentos que são adicionados numa lista seguido de um recomço da leitura da string inserida:

input: "Sua sequência"


    lista = []
    seq1 = ''
    for i in seq:
        seq1 = seq1 + i
        if len(seq1) == 3:
            lista.append(seq1)
            seq1 = ''
        
Ao detectar um trio (códon) de letras na lista o condicional 'if' faz sua susbstituição pelo simbolo do aminoácido correspondente em azul:

        if 'ata' in lista:
            lista.remove('ata')
            lista.append('I')
            seq1 = ''
São retornadas 12 sequências, seis correspondentes as variações nos frames de leitura da sequência e seis correspondentes a cada um dos
resultados anteriores porém, excluindo toda parte da sequência composta por cauda Poli-A e toda parte prescendete ao primeiro códon de
início.

Os códons de início "ATG' e final são ilustrados com 'M' colorido de branco e '_' com fundo branco para melhor vizualização.
As caudas Polia-A das sequências são traduzidas em lisinas (K) que são removidas na representação da sequência a partir do primeiro códon
de início

Histórico:
1 - Agora um arquivo é criado no formato .csv plotando as seis leituras de sequência diferentes além de outras seis fragmentadas a cada
stop códon, facilitando a seleção de fragmentos da cadeia de aminoácidos
