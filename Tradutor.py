# Created by Jorge

from time import sleep
print(50*'\033[32m-=-\033[m')
seq = input('Insira sua sequência de nucleotídeos em formato FASTA: ').strip()
print(50*'\033[32m-=-\033[m')
print('Processando...\n\n')
sleep(2)
print('\033[::40m_\033[m : Stop códon\n\033[30mM\033[m : Start códon\n')
seq = ''.join(seq)
seq = seq.lower()

lista = []
seq1 = ''
for i in seq:
    seq1 = seq1 + i
    if len(seq1) == 3:
        lista.append(seq1)
        seq1 = ''
        if 'ata' in lista:
            lista.remove('ata')
            lista.append('\033[36mI\033[m')
            seq1 = ''
        if 'aaa' in lista:
            lista.remove('aaa')
            lista.append('\033[36mK\033[m')
            seq1 = ''
        if 'atc' in lista:
            lista.remove('atc')
            lista.append('\033[36mI\033[m')
            seq1 = ''
        if 'att' in lista:
            lista.remove('att')
            lista.append('\033[36mI\033[m')
            seq1 = ''
        if 'aat' in lista:
            lista.remove('aat')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        if 'atg' in lista:
            lista.remove('atg')
            lista.append('\033[30;1mM\033[m')
            seq1 = ''
        if 'aca' in lista:
            lista.remove('aca')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        if 'acc' in lista:
            lista.remove('acc')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        if 'aac' in lista:
            lista.remove('aac')
            lista.append('\033[36mT\033[m')
        if 'acg' in lista:
            lista.remove('acg')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        if 'act' in lista:
            lista.remove('act')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        if 'acc' in lista:
            lista.remove('acc')
            lista.append('\033[36mN\033[m')
            seq1 = ''
        if 'aag' in lista:
            lista.remove('aag')
            lista.append('\033[36mK\033[m')
            seq1 = ''
        if 'agc' in lista:
            lista.remove('agc')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'agt' in lista:
            lista.remove('agt')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'aga' in lista:
            lista.remove('aga')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'agg' in lista:
            lista.remove('agg')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'cta' in lista:
            lista.remove('cta')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'ctc' in lista:
            lista.remove('ctc')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'ctg' in lista:
            lista.remove('ctg')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'ctt' in lista:
            lista.remove('ctt')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'cca' in lista:
            lista.remove('cca')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        if 'ccc' in lista:
            lista.remove('ccc')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        if 'ccg' in lista:
            lista.remove('ccg')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        if 'cct' in lista:
            lista.remove('cct')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        if 'cac'  in lista:
            lista.remove('cac')
            lista.append('\033[36mH\033[m')
            seq1 = ''
        if 'cat'  in lista:
            lista.remove('cat')
            lista.append('\033[36mH\033[m')
            seq1 = ''
        if 'caa'  in lista:
            lista.remove('caa')
            lista.append('\033[36mQ\033[m')
            seq1 = ''
        if 'cag'  in lista:
            lista.remove('cag')
            lista.append('\033[36mQ\033[m')
            seq1 = ''
        if 'cga'  in lista:
            lista.remove('cga')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'cgc'  in lista:
            lista.remove('cgc')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'cgg'  in lista:
            lista.remove('cgg')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'cgt'  in lista:
            lista.remove('cgt')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        if 'gta'  in lista:
            lista.remove('gta')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        if 'gtc'  in lista:
            lista.remove('gtc')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        if 'gtg'  in lista:
            lista.remove('gtg')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        if 'gtt'  in lista:
            lista.remove('gtt')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        if 'gca'  in lista:
            lista.remove('gca')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        if 'gcc'  in lista:
            lista.remove('gcc')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        if 'gcg'  in lista:
            lista.remove('gcg')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        if 'gct'  in lista:
            lista.remove('gct')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        if 'gac'  in lista:
            lista.remove('gac')
            lista.append('\033[36mD\033[m')
            seq1 = ''
        if 'gat'  in lista:
            lista.remove('gat')
            lista.append('\033[36mD\033[m')
            seq1 = ''
        if 'gag'  in lista:
            lista.remove('gag')
            lista.append('\033[36mE\033[m')
            seq1 = ''
        if 'gga'  in lista:
            lista.remove('gga')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        if 'gaa'  in lista:
            lista.remove('gaa')
            lista.append('\033[36mE\033[m')
            seq1 = ''
        if 'ggc'  in lista:
            lista.remove('ggc')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        if 'ggg'  in lista:
            lista.remove('ggg')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        if 'ggt'  in lista:
            lista.remove('ggt')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        if 'tca'  in lista:
            lista.remove('tca')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'ttc'  in lista:
            lista.remove('ttc')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'tcg'  in lista:
            lista.remove('tcg')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'tct'  in lista:
            lista.remove('tct')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        if 'ttc'  in lista:
            lista.remove('ttc')
            lista.append('\033[36mF\033[m')
            seq1 = ''
        if 'ttt'  in lista:
            lista.remove('ttt')
            lista.append('\033[36mF\033[m')
            seq1 = ''
        if 'tta' in lista:
            lista.remove('tta')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'ttg' in lista:
            lista.remove('ttg')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        if 'tac' in lista:
            lista.remove('tac')
            lista.append('\033[36mY\033[m')
            seq1 = ''
        if 'tat' in lista:
            lista.remove('tat')
            lista.append('\033[36mY\033[m')
            seq1 = ''
        if 'taa' in lista:
            lista.remove('taa')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        if 'tag' in lista:
            lista.remove('tag')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        if 'tgc' in lista:
            lista.remove('tgc')
            lista.append('\033[36mC\033[m')
            seq1 = ''
        if 'tgt' in lista:
            lista.remove('tgt')
            lista.append('\033[36mC\033[m')
            seq1 = ''
        if 'tga' in lista:
            lista.remove('tga')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        if 'tgg' in lista:
            lista.remove('tgg')
            lista.append('\033[36mW\033[m')
            seq1 = ''
        if 'tcc' in lista:
            lista.remove('tcc')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        else:
            seq1 = ''
a = ''.join(lista)
a1 = a.find('M')
a2 = a.find('\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m')
print('Sua sequência traduzida em quadro de leitura +1 é:\n', a)
print('A sequência a partir do start códon é:\n', a[a1:a2])
print(50*'-=-', '\n\n')

lista1 = []
seq2 = ''
for i in seq[1:]:
    seq2 = seq2 + i
    if len(seq2) == 3:
        lista1.append(seq2)
        seq2 = ''
        if 'ata' in lista1:
            lista1.remove('ata')
            lista1.append('\033[36mI\033[m')
            seq2 = ''
        if 'aaa' in lista1:
            lista1.remove('aaa')
            lista1.append('\033[36mK\033[m')
            seq2 = ''
        if 'atc' in lista1:
            lista1.remove('atc')
            lista1.append('\033[36mI\033[m')
            seq2 = ''
        if 'att' in lista1:
            lista1.remove('att')
            lista1.append('\033[36mI\033[m')
            seq2 = ''
        if 'atg' in lista1:
            lista1.remove('atg')
            lista1.append('\033[30;1mM\033[m')
            seq2 = ''
        if 'aca' in lista1:
            lista1.remove('aca')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        if 'acc' in lista1:
            lista1.remove('acc')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        if 'aat' in lista1:
            lista1.remove('aat')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'acg' in lista1:
            lista1.remove('acg')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        if 'act' in lista1:
            lista1.remove('act')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        if 'aac' in lista1:
            lista1.remove('aac')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'aag' in lista1:
            lista1.remove('aag')
            lista1.append('\033[36mK\033[m')
            seq2 = ''
        if 'agc' in lista1:
            lista1.remove('agc')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'agt' in lista1:
            lista1.remove('agt')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'aga' in lista1:
            lista1.remove('aga')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'agg' in lista1:
            lista1.remove('agg')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'cta' in lista1:
            lista1.remove('cta')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'ctc' in lista1:
            lista1.remove('ctc')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'ctg' in lista1:
            lista1.remove('ctg')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'ctt' in lista1:
            lista1.remove('ctt')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'cca' in lista1:
            lista1.remove('cca')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        if 'ccc' in lista1:
            lista1.remove('ccc')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        if 'ccg' in lista1:
            lista1.remove('ccg')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        if 'cct' in lista1:
            lista1.remove('cct')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        if 'cac'  in lista1:
            lista1.remove('cac')
            lista1.append('\033[36mH\033[m')
            seq2 = ''
        if 'cat'  in lista1:
            lista1.remove('cat')
            lista1.append('\033[36mH\033[m')
            seq2 = ''
        if 'caa'  in lista1:
            lista1.remove('caa')
            lista1.append('\033[36mQ\033[m')
            seq2 = ''
        if 'cag'  in lista1:
            lista1.remove('cag')
            lista1.append('\033[36mQ\033[m')
            seq2 = ''
        if 'cga'  in lista1:
            lista1.remove('cga')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'cgc'  in lista1:
            lista1.remove('cgc')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'cgg'  in lista1:
            lista1.remove('cgg')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'cgt'  in lista1:
            lista1.remove('cgt')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        if 'gta'  in lista1:
            lista1.remove('gta')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        if 'gtc'  in lista1:
            lista1.remove('gtc')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        if 'gtg'  in lista1:
            lista1.remove('gtg')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        if 'gtt'  in lista1:
            lista1.remove('gtt')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        if 'gca'  in lista1:
            lista1.remove('gca')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'gcc'  in lista1:
            lista1.remove('gcc')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'gcg'  in lista1:
            lista1.remove('gcg')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'gct'  in lista1:
            lista1.remove('gct')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        if 'gac'  in lista1:
            lista1.remove('gac')
            lista1.append('\033[36mD\033[m')
            seq2 = ''
        if 'gat'  in lista1:
            lista1.remove('gat')
            lista1.append('\033[36mD\033[m')
            seq2 = ''
        if 'gag'  in lista1:
            lista1.remove('gag')
            lista1.append('\033[36mE\033[m')
            seq2 = ''
        if 'gga'  in lista1:
            lista1.remove('gga')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        if 'gaa'  in lista1:
            lista1.remove('gaa')
            lista1.append('\033[36mE\033[m')
            seq2 = ''
        if 'ggc'  in lista1:
            lista1.remove('ggc')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        if 'ggg'  in lista1:
            lista1.remove('ggg')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        if 'ggt'  in lista1:
            lista1.remove('ggt')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        if 'tca'  in lista1:
            lista1.remove('tca')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'ttc'  in lista1:
            lista1.remove('ttc')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'tcg'  in lista1:
            lista1.remove('tcg')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'tct'  in lista1:
            lista1.remove('tct')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        if 'ttc'  in lista1:
            lista1.remove('ttc')
            lista1.append('\033[36mF\033[m')
            seq2 = ''
        if 'ttt'  in lista1:
            lista1.remove('ttt')
            lista1.append('\033[36mF\033[m')
            seq2 = ''
        if 'tta' in lista1:
            lista1.remove('tta')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'ttg' in lista1:
            lista1.remove('ttg')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        if 'tac' in lista1:
            lista1.remove('tac')
            lista1.append('\033[36mY\033[m')
            seq2 = ''
        if 'tat' in lista1:
            lista1.remove('tat')
            lista1.append('\033[36mY\033[m')
            seq2 = ''
        if 'taa' in lista1:
            lista1.remove('taa')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        if 'tag' in lista1:
            lista1.remove('tag')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        if 'tgc' in lista1:
            lista1.remove('tgc')
            lista1.append('\033[36mC\033[m')
            seq2 = ''
        if 'tgt' in lista1:
            lista1.remove('tgt')
            lista1.append('\033[36mC\033[m')
            seq2 = ''
        if 'tga' in lista1:
            lista1.remove('tga')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        if 'tgg' in lista1:
            lista1.remove('tgg')
            lista1.append('\033[36mW\033[m')
            seq2 = ''
        if 'tcc' in lista1:
            lista1.remove('tcc')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        else:
            seq21 = ''
b = ''.join(lista1)
b1 = b.find('M')
b2 = b.find('\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m')
print('Sua sequência traduzida em quadro de leitura +2 é:\n', b)
print('A sequência a partir do start códon é:\n', b[b1:b2])
print(50*'-=-', '\n\n')

lista2 = []
seq3 = ''
for i in seq[2:]:
    seq3 = seq3 + i
    if len(seq3) == 3:
        lista2.append(seq3)
        seq3 = ''
        if 'ata' in lista2:
            lista2.remove('ata')
            lista2.append('\033[36mI\033[m')
            seq3 = ''
        if 'aaa' in lista2:
            lista2.remove('aaa')
            lista2.append('\033[36mK\033[m')
            seq3 = ''
        if 'atc' in lista2:
            lista2.remove('atc')
            lista2.append('\033[36mI\033[m')
            seq3 = ''
        if 'att' in lista2:
            lista2.remove('att')
            lista2.append('\033[36mI\033[m')
            seq3 = ''
        if 'aat' in lista2:
            lista2.remove('aat')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'atg' in lista2:
            lista2.remove('atg')
            lista2.append('\033[30;1mM\033[m')
            seq3 = ''
        if 'aca' in lista2:
            lista2.remove('aca')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        if 'acc' in lista2:
            lista2.remove('acc')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        if 'acg' in lista2:
            lista2.remove('acg')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        if 'act' in lista2:
            lista2.remove('act')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        if 'aac' in lista2:
            lista2.remove('aac')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'aag' in lista2:
            lista2.remove('aag')
            lista2.append('\033[36mK\033[m')
            seq3 = ''
        if 'agc' in lista2:
            lista2.remove('agc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'agt' in lista2:
            lista2.remove('agt')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'aga' in lista2:
            lista2.remove('aga')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'agg' in lista2:
            lista2.remove('agg')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'cta' in lista2:
            lista2.remove('cta')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'ctc' in lista2:
            lista2.remove('ctc')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'ctg' in lista2:
            lista2.remove('ctg')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'ctt' in lista2:
            lista2.remove('ctt')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'cca' in lista2:
            lista2.remove('cca')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        if 'ccc' in lista2:
            lista2.remove('ccc')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        if 'ccg' in lista2:
            lista2.remove('ccg')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        if 'cct' in lista2:
            lista2.remove('cct')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        if 'cac'  in lista2:
            lista2.remove('cac')
            lista2.append('\033[36mH\033[m')
            seq3 = ''
        if 'cat'  in lista2:
            lista2.remove('cat')
            lista2.append('\033[36mH\033[m')
            seq3 = ''
        if 'caa'  in lista2:
            lista2.remove('caa')
            lista2.append('\033[36mQ\033[m')
            seq3 = ''
        if 'cag'  in lista2:
            lista2.remove('cag')
            lista2.append('\033[36mQ\033[m')
            seq3 = ''
        if 'cga'  in lista2:
            lista2.remove('cga')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'cgc'  in lista2:
            lista2.remove('cgc')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'cgg'  in lista2:
            lista2.remove('cgg')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'cgt'  in lista2:
            lista2.remove('cgt')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        if 'gta'  in lista2:
            lista2.remove('gta')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        if 'gtc'  in lista2:
            lista2.remove('gtc')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        if 'gtg'  in lista2:
            lista2.remove('gtg')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        if 'gtt'  in lista2:
            lista2.remove('gtt')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        if 'gca'  in lista2:
            lista2.remove('gca')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'gcc'  in lista2:
            lista2.remove('gcc')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'gcg'  in lista2:
            lista2.remove('gcg')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'gct'  in lista2:
            lista2.remove('gct')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        if 'gac'  in lista2:
            lista2.remove('gac')
            lista2.append('\033[36mD\033[m')
            seq3 = ''
        if 'gat'  in lista2:
            lista2.remove('gat')
            lista2.append('\033[36mD\033[m')
            seq3 = ''
        if 'gag'  in lista2:
            lista2.remove('gag')
            lista2.append('\033[36mE\033[m')
            seq3 = ''
        if 'gga'  in lista2:
            lista2.remove('gga')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        if 'gaa'  in lista2:
            lista2.remove('gaa')
            lista2.append('\033[36mE\033[m')
            seq3 = ''
        if 'ggc'  in lista2:
            lista2.remove('ggc')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        if 'ggg'  in lista2:
            lista2.remove('ggg')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        if 'ggt'  in lista2:
            lista2.remove('ggt')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        if 'tca'  in lista2:
            lista2.remove('tca')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'ttc'  in lista2:
            lista2.remove('ttc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'tcc' in lista2:
            lista2.remove('tcc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'tcg'  in lista2:
            lista2.remove('tcg')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'tct'  in lista2:
            lista2.remove('tct')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        if 'ttc'  in lista2:
            lista2.remove('ttc')
            lista2.append('\033[36mF\033[m')
            seq3 = ''
        if 'ttt'  in lista2:
            lista2.remove('ttt')
            lista2.append('\033[36mF\033[m')
            seq3 = ''
        if 'tta' in lista2:
            lista2.remove('tta')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'ttg' in lista2:
            lista2.remove('ttg')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        if 'tac' in lista2:
            lista2.remove('tac')
            lista2.append('\033[36mY\033[m')
            seq3 = ''
        if 'tat' in lista2:
            lista2.remove('tat')
            lista2.append('\033[36mY\033[m')
            seq3 = ''
        if 'taa' in lista2:
            lista2.remove('taa')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        if 'tag' in lista2:
            lista2.remove('tag')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        if 'tgc' in lista2:
            lista2.remove('tgc')
            lista2.append('\033[36mC\033[m')
            seq3 = ''
        if 'tgt' in lista2:
            lista2.remove('tgt')
            lista2.append('\033[36mC\033[m')
            seq3 = ''
        if 'tga' in lista2:
            lista2.remove('tga')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        if 'tgg' in lista2:
            lista2.remove('tgg')
            lista2.append('\033[36mW\033[m')
            seq3 = ''
        else:
            seq3 = ''
c = ''.join(lista2)
c1 = c.find('M')
c2 = c.find('\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m''\033[36mK\033[m')
print('Sua sequência traduzida em quadro de leitura +3 é:\n', c)
print('A sequência a partir do start códon é:\n', c[c1:c2])
print(50*'-=-', '\n\n')

lista3 = []
seq4 = ''
d2 = len(seq)
for i in seq[d2::-1]:
    seq4 = seq4 + i
    if len(seq4) == 3:
        lista3.append(seq4)
        seq4 = ''
        if 'ata' in lista3:
            lista3.remove('ata')
            lista3.append('\033[36mI\033[m')
            seq4 = ''
        if 'aaa' in lista3:
            lista3.remove('aaa')
            lista3.append('\033[36mK\033[m')
            seq4 = ''
        if 'atc' in lista3:
            lista3.remove('atc')
            lista3.append('\033[36mI\033[m')
            seq4 = ''
        if 'att' in lista3:
            lista3.remove('att')
            lista3.append('\033[36mI\033[m')
            seq4 = ''
        if 'aat' in lista3:
            lista3.remove('aat')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        if 'atg' in lista3:
            lista3.remove('atg')
            lista3.append('\033[30;1mM\033[m')
            seq4 = ''
        if 'aca' in lista3:
            lista3.remove('aca')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        if 'acc' in lista3:
            lista3.remove('acc')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        if 'acg' in lista3:
            lista3.remove('acg')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        if 'act' in lista3:
            lista3.remove('act')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        if 'acc' in lista3:
            lista3.remove('acc')
            lista3.append('\033[36mN\033[m')
            seq4 = ''
        if 'aag' in lista3:
            lista3.remove('aag')
            lista3.append('\033[36mK\033[m')
            seq4 = ''
        if 'agc' in lista3:
            lista3.remove('agc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'agt' in lista3:
            lista3.remove('agt')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'aga' in lista3:
            lista3.remove('aga')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'agg' in lista3:
            lista3.remove('agg')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'cta' in lista3:
            lista3.remove('cta')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'ctc' in lista3:
            lista3.remove('ctc')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'ctg' in lista3:
            lista3.remove('ctg')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'ctt' in lista3:
            lista3.remove('ctt')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'cca' in lista3:
            lista3.remove('cca')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        if 'ccc' in lista3:
            lista3.remove('ccc')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        if 'ccg' in lista3:
            lista3.remove('ccg')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        if 'cct' in lista3:
            lista3.remove('cct')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        if 'cac'  in lista3:
            lista3.remove('cac')
            lista3.append('\033[36mH\033[m')
            seq4 = ''
        if 'cat'  in lista3:
            lista3.remove('cat')
            lista3.append('\033[36mH\033[m')
            seq4 = ''
        if 'caa'  in lista3:
            lista3.remove('caa')
            lista3.append('\033[36mQ\033[m')
            seq4 = ''
        if 'cag'  in lista3:
            lista3.remove('cag')
            lista3.append('\033[36mQ\033[m')
            seq4 = ''
        if 'cga'  in lista3:
            lista3.remove('cga')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'cgc'  in lista3:
            lista3.remove('cgc')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'cgg'  in lista3:
            lista3.remove('cgg')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'cgt'  in lista3:
            lista3.remove('cgt')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        if 'gta'  in lista3:
            lista3.remove('gta')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        if 'gtc'  in lista3:
            lista3.remove('gtc')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        if 'gtg'  in lista3:
            lista3.remove('gtg')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        if 'gtt'  in lista3:
            lista3.remove('gtt')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        if 'gca'  in lista3:
            lista3.remove('gca')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        if 'gcc'  in lista3:
            lista3.remove('gcc')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        if 'gcg'  in lista3:
            lista3.remove('gcg')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        if 'gct'  in lista3:
            lista3.remove('gct')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        if 'gac'  in lista3:
            lista3.remove('gac')
            lista3.append('\033[36mD\033[m')
            seq4 = ''
        if 'gat'  in lista3:
            lista3.remove('gat')
            lista3.append('\033[36mD\033[m')
            seq4 = ''
        if 'gag'  in lista3:
            lista3.remove('gag')
            lista3.append('\033[36mE\033[m')
            seq4 = ''
        if 'gga'  in lista3:
            lista3.remove('gga')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        if 'gaa'  in lista3:
            lista3.remove('gaa')
            lista3.append('\033[36mE\033[m')
            seq4 = ''
        if 'ggc'  in lista3:
            lista3.remove('ggc')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        if 'ggg'  in lista3:
            lista3.remove('ggg')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        if 'ggt'  in lista3:
            lista3.remove('ggt')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        if 'tca'  in lista3:
            lista3.remove('tca')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'ttc'  in lista3:
            lista3.remove('ttc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'tcg'  in lista3:
            lista3.remove('tcg')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'tct'  in lista3:
            lista3.remove('tct')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'ttc'  in lista3:
            lista3.remove('ttc')
            lista3.append('\033[36mF\033[m')
            seq4 = ''
        if 'ttt'  in lista3:
            lista3.remove('ttt')
            lista3.append('\033[36mF\033[m')
            seq4 = ''
        if 'tta' in lista3:
            lista3.remove('tta')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'ttg' in lista3:
            lista3.remove('ttg')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        if 'tac' in lista3:
            lista3.remove('tac')
            lista3.append('\033[36mY\033[m')
            seq4 = ''
        if 'tat' in lista3:
            lista3.remove('tat')
            lista3.append('\033[36mY\033[m')
            seq4 = ''
        if 'taa' in lista3:
            lista3.remove('taa')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        if 'tag' in lista3:
            lista3.remove('tag')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        if 'tgc' in lista3:
            lista3.remove('tgc')
            lista3.append('\033[36mC\033[m')
            seq4 = ''
        if 'tgt' in lista3:
            lista3.remove('tgt')
            lista3.append('\033[36mC\033[m')
            seq4 = ''
        if 'tga' in lista3:
            lista3.remove('tga')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        if 'tgg' in lista3:
            lista3.remove('tgg')
            lista3.append('\033[36mW\033[m')
            seq4 = ''
        if 'tcc' in lista3:
            lista3.remove('tcc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        if 'aac' in lista3:
            lista3.remove('aac')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        else:
            seq4 = ''
d = ''.join(lista3)
d1 = d.find('M')
print('Sua sequência traduzida em quadro de leitura -1 é:\n', d)
print('A sequência a partir do start códon é:\n', d[d1:])
print(50*'-=-', '\n\n')

lista4 = []
seq5 = ''
e2 = len(seq)
for i in seq[e2::-2]:
    seq5 = seq5 + i
    if len(seq5) == 3:
        lista4.append(seq5)
        seq5 = ''
        if 'ata' in lista4:
            lista4.remove('ata')
            lista4.append('\033[36mI\033[m')
            seq5 = ''
        if 'aaa' in lista4:
            lista4.remove('aaa')
            lista4.append('\033[36mK\033[m')
            seq5 = ''
        if 'atc' in lista4:
            lista4.remove('atc')
            lista4.append('\033[36mI\033[m')
            seq5 = ''
        if 'att' in lista4:
            lista4.remove('att')
            lista4.append('\033[36mI\033[m')
            seq5 = ''
        if 'aat' in lista4:
            lista4.remove('aat')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        if 'atg' in lista4:
            lista4.remove('atg')
            lista4.append('\033[30;1mM\033[m')
            seq5 = ''
        if 'aca' in lista4:
            lista4.remove('aca')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        if 'acc' in lista4:
            lista4.remove('acc')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        if 'acg' in lista4:
            lista4.remove('acg')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        if 'act' in lista4:
            lista4.remove('act')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        if 'acc' in lista4:
            lista4.remove('acc')
            lista4.append('\033[36mN\033[m')
            seq5 = ''
        if 'aag' in lista4:
            lista4.remove('aag')
            lista4.append('\033[36mK\033[m')
            seq5 = ''
        if 'agc' in lista4:
            lista4.remove('agc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'agt' in lista4:
            lista4.remove('agt')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'aga' in lista4:
            lista4.remove('aga')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'agg' in lista4:
            lista4.remove('agg')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'cta' in lista4:
            lista4.remove('cta')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'ctc' in lista4:
            lista4.remove('ctc')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'ctg' in lista4:
            lista4.remove('ctg')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'ctt' in lista4:
            lista4.remove('ctt')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'cca' in lista4:
            lista4.remove('cca')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        if 'ccc' in lista4:
            lista4.remove('ccc')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        if 'ccg' in lista4:
            lista4.remove('ccg')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        if 'cct' in lista4:
            lista4.remove('cct')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        if 'cac'  in lista4:
            lista4.remove('cac')
            lista4.append('\033[36mH\033[m')
            seq5 = ''
        if 'cat'  in lista4:
            lista4.remove('cat')
            lista4.append('\033[36mH\033[m')
            seq5 = ''
        if 'caa'  in lista4:
            lista4.remove('caa')
            lista4.append('\033[36mQ\033[m')
            seq5 = ''
        if 'cag'  in lista4:
            lista4.remove('cag')
            lista4.append('\033[36mQ\033[m')
            seq5 = ''
        if 'cga'  in lista4:
            lista4.remove('cga')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'cgc'  in lista4:
            lista4.remove('cgc')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'cgg'  in lista4:
            lista4.remove('cgg')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'cgt'  in lista4:
            lista4.remove('cgt')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        if 'gta'  in lista4:
            lista4.remove('gta')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        if 'gtc'  in lista4:
            lista4.remove('gtc')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        if 'gtg'  in lista4:
            lista4.remove('gtg')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        if 'gtt'  in lista4:
            lista4.remove('gtt')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        if 'gca'  in lista4:
            lista4.remove('gca')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        if 'gcc'  in lista4:
            lista4.remove('gcc')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        if 'gcg'  in lista4:
            lista4.remove('gcg')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        if 'gct'  in lista4:
            lista4.remove('gct')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        if 'gac'  in lista4:
            lista4.remove('gac')
            lista4.append('\033[36mD\033[m')
            seq5 = ''
        if 'gat'  in lista4:
            lista4.remove('gat')
            lista4.append('\033[36mD\033[m')
            seq5 = ''
        if 'gag'  in lista4:
            lista4.remove('gag')
            lista4.append('\033[36mE\033[m')
            seq5 = ''
        if 'gga'  in lista4:
            lista4.remove('gga')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        if 'gaa'  in lista4:
            lista4.remove('gaa')
            lista4.append('\033[36mE\033[m')
            seq5 = ''
        if 'ggc'  in lista4:
            lista4.remove('ggc')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        if 'ggg'  in lista4:
            lista4.remove('ggg')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        if 'ggt'  in lista4:
            lista4.remove('ggt')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        if 'tca'  in lista4:
            lista4.remove('tca')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'ttc'  in lista4:
            lista4.remove('ttc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'tcg'  in lista4:
            lista4.remove('tcg')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'tct'  in lista4:
            lista4.remove('tct')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'ttc'  in lista4:
            lista4.remove('ttc')
            lista4.append('\033[36mF\033[m')
            seq5 = ''
        if 'ttt'  in lista4:
            lista4.remove('ttt')
            lista4.append('\033[36mF\033[m')
            seq5 = ''
        if 'tta' in lista4:
            lista4.remove('tta')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'ttg' in lista4:
            lista4.remove('ttg')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        if 'tac' in lista4:
            lista4.remove('tac')
            lista4.append('\033[36mY\033[m')
            seq5 = ''
        if 'tat' in lista4:
            lista4.remove('tat')
            lista4.append('\033[36mY\033[m')
            seq5 = ''
        if 'taa' in lista4:
            lista4.remove('taa')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        if 'tag' in lista4:
            lista4.remove('tag')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        if 'tgc' in lista4:
            lista4.remove('tgc')
            lista4.append('\033[36mC\033[m')
            seq5 = ''
        if 'tgt' in lista4:
            lista4.remove('tgt')
            lista4.append('\033[36mC\033[m')
            seq5 = ''
        if 'tga' in lista4:
            lista4.remove('tga')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        if 'tgg' in lista4:
            lista4.remove('tgg')
            lista4.append('\033[36mW\033[m')
            seq5 = ''
        if 'tcc' in lista4:
            lista4.remove('tcc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        if 'aac' in lista4:
            lista4.remove('aac')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        else:
            seq5 = ''
e = ''.join(lista4)
e1 = e.find('M')
print('Sua sequência traduzida em quadro de leitura -2 é:\n', e)
print('A sequência a partir do start códon é:\n', e[e1:])
print(50*'-=-', '\n\n')

lista5 = []
seq6 = ''
f2 = len(seq)
for i in seq[f2::-3]:
    seq6 = seq6 + i
    if len(seq6) == 3:
        lista5.append(seq6)
        seq6 = ''
        if 'ata' in lista5:
            lista5.remove('ata')
            lista5.append('\033[36mI\033[m')
            seq6 = ''
        if 'aaa' in lista5:
            lista5.remove('aaa')
            lista5.append('\033[36mK\033[m')
            seq6 = ''
        if 'atc' in lista5:
            lista5.remove('atc')
            lista5.append('\033[36mI\033[m')
            seq6 = ''
        if 'att' in lista5:
            lista5.remove('att')
            lista5.append('\033[36mI\033[m')
            seq6 = ''
        if 'aat' in lista5:
            lista5.remove('aat')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        if 'atg' in lista5:
            lista5.remove('atg')
            lista5.append('\033[30;1mM\033[m')
            seq6 = ''
        if 'aca' in lista5:
            lista5.remove('aca')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        if 'acc' in lista5:
            lista5.remove('acc')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        if 'acg' in lista5:
            lista5.remove('acg')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        if 'act' in lista5:
            lista5.remove('act')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        if 'acc' in lista5:
            lista5.remove('acc')
            lista5.append('\033[36mN\033[m')
            seq6 = ''
        if 'aag' in lista5:
            lista5.remove('aag')
            lista5.append('\033[36mK\033[m')
            seq6 = ''
        if 'agc' in lista5:
            lista5.remove('agc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'agt' in lista5:
            lista5.remove('agt')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'aga' in lista5:
            lista5.remove('aga')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'agg' in lista5:
            lista5.remove('agg')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'cta' in lista5:
            lista5.remove('cta')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'ctc' in lista5:
            lista5.remove('ctc')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'ctg' in lista5:
            lista5.remove('ctg')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'ctt' in lista5:
            lista5.remove('ctt')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'cca' in lista5:
            lista5.remove('cca')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        if 'ccc' in lista5:
            lista5.remove('ccc')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        if 'ccg' in lista5:
            lista5.remove('ccg')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        if 'cct' in lista5:
            lista5.remove('cct')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        if 'cac'  in lista5:
            lista5.remove('cac')
            lista5.append('\033[36mH\033[m')
            seq6 = ''
        if 'cat'  in lista5:
            lista5.remove('cat')
            lista5.append('\033[36mH\033[m')
            seq6 = ''
        if 'caa'  in lista5:
            lista5.remove('caa')
            lista5.append('\033[36mQ\033[m')
            seq6 = ''
        if 'cag'  in lista5:
            lista5.remove('cag')
            lista5.append('\033[36mQ\033[m')
            seq6 = ''
        if 'cga'  in lista5:
            lista5.remove('cga')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'cgc'  in lista5:
            lista5.remove('cgc')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'cgg'  in lista5:
            lista5.remove('cgg')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'cgt'  in lista5:
            lista5.remove('cgt')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        if 'gta'  in lista5:
            lista5.remove('gta')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        if 'gtc'  in lista5:
            lista5.remove('gtc')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        if 'gtg'  in lista5:
            lista5.remove('gtg')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        if 'gtt'  in lista5:
            lista5.remove('gtt')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        if 'gca'  in lista5:
            lista5.remove('gca')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        if 'gcc'  in lista5:
            lista5.remove('gcc')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        if 'gcg'  in lista5:
            lista5.remove('gcg')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        if 'gct'  in lista5:
            lista5.remove('gct')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        if 'gac'  in lista5:
            lista5.remove('gac')
            lista5.append('\033[36mD\033[m')
            seq6 = ''
        if 'gat'  in lista5:
            lista5.remove('gat')
            lista5.append('\033[36mD\033[m')
            seq6 = ''
        if 'gag'  in lista5:
            lista5.remove('gag')
            lista5.append('\033[36mE\033[m')
            seq6 = ''
        if 'gga'  in lista5:
            lista5.remove('gga')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        if 'gaa'  in lista5:
            lista5.remove('gaa')
            lista5.append('\033[36mE\033[m')
            seq6 = ''
        if 'ggc'  in lista5:
            lista5.remove('ggc')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        if 'ggg'  in lista5:
            lista5.remove('ggg')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        if 'ggt'  in lista5:
            lista5.remove('ggt')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        if 'tca'  in lista5:
            lista5.remove('tca')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'ttc'  in lista5:
            lista5.remove('ttc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'tcg'  in lista5:
            lista5.remove('tcg')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'tct'  in lista5:
            lista5.remove('tct')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'ttc'  in lista5:
            lista5.remove('ttc')
            lista5.append('\033[36mF\033[m')
            seq6 = ''
        if 'ttt'  in lista5:
            lista5.remove('ttt')
            lista5.append('\033[36mF\033[m')
            seq6 = ''
        if 'tta' in lista5:
            lista5.remove('tta')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'ttg' in lista5:
            lista5.remove('ttg')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        if 'tac' in lista5:
            lista5.remove('tac')
            lista5.append('\033[36mY\033[m')
            seq6 = ''
        if 'tat' in lista5:
            lista5.remove('tat')
            lista5.append('\033[36mY\033[m')
            seq6 = ''
        if 'taa' in lista5:
            lista5.remove('taa')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        if 'tag' in lista5:
            lista5.remove('tag')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        if 'tgc' in lista5:
            lista5.remove('tgc')
            lista5.append('\033[36mC\033[m')
            seq6 = ''
        if 'tgt' in lista5:
            lista5.remove('tgt')
            lista5.append('\033[36mC\033[m')
            seq6 = ''
        if 'tga' in lista5:
            lista5.remove('tga')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        if 'tgg' in lista5:
            lista5.remove('tgg')
            lista5.append('\033[36mW\033[m')
            seq6 = ''
        if 'tcc' in lista5:
            lista5.remove('tcc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        if 'aac' in lista5:
            lista5.remove('aac')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        else:
            seq6 = ''
f = ''.join(lista5)
f1 = f.find('M')
print('Sua sequência traduzida em quadro de leitura -3 é:\n', f)
print('A sequência a partir do start códon é:\n', f[f1:])
print(50*'-=-', '\n\n')
sleep(90)