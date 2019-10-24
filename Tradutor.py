from time import sleep
print(50*'\033[32m-=-\033[m')
seq = input('Insira sua sequência de nucleotídeos em formato FASTA: ').strip()
print(50*'\033[32m-=-\033[m')
print('Processando...\n\n')

sleep(1)
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
        elif 'aaa' in lista:
            lista.remove('aaa')
            lista.append('\033[36mK\033[m')
            seq1 = ''
        elif 'atc' in lista:
            lista.remove('atc')
            lista.append('\033[36mI\033[m')
            seq1 = ''
        elif 'att' in lista:
            lista.remove('att')
            lista.append('\033[36mI\033[m')
            seq1 = ''
        elif 'aat' in lista:
            lista.remove('aat')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        elif 'atg' in lista:
            lista.remove('atg')
            lista.append('\033[30;1mM\033[m')
            seq1 = ''
        elif 'aca' in lista:
            lista.remove('aca')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        elif 'acc' in lista:
            lista.remove('acc')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        elif 'aac' in lista:
            lista.remove('aac')
            lista.append('\033[36mT\033[m')
        elif 'acg' in lista:
            lista.remove('acg')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        elif 'act' in lista:
            lista.remove('act')
            lista.append('\033[36mT\033[m')
            seq1 = ''
        elif 'acc' in lista:
            lista.remove('acc')
            lista.append('\033[36mN\033[m')
            seq1 = ''
        elif 'aag' in lista:
            lista.remove('aag')
            lista.append('\033[36mK\033[m')
            seq1 = ''
        elif 'agc' in lista:
            lista.remove('agc')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'agt' in lista:
            lista.remove('agt')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'aga' in lista:
            lista.remove('aga')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'agg' in lista:
            lista.remove('agg')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'cta' in lista:
            lista.remove('cta')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'ctc' in lista:
            lista.remove('ctc')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'ctg' in lista:
            lista.remove('ctg')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'ctt' in lista:
            lista.remove('ctt')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'cca' in lista:
            lista.remove('cca')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        elif 'ccc' in lista:
            lista.remove('ccc')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        elif 'ccg' in lista:
            lista.remove('ccg')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        elif 'cct' in lista:
            lista.remove('cct')
            lista.append('\033[36mP\033[m')
            seq1 = ''
        elif 'cac'  in lista:
            lista.remove('cac')
            lista.append('\033[36mH\033[m')
            seq1 = ''
        elif 'cat'  in lista:
            lista.remove('cat')
            lista.append('\033[36mH\033[m')
            seq1 = ''
        elif 'caa'  in lista:
            lista.remove('caa')
            lista.append('\033[36mQ\033[m')
            seq1 = ''
        elif 'cag'  in lista:
            lista.remove('cag')
            lista.append('\033[36mQ\033[m')
            seq1 = ''
        elif 'cga'  in lista:
            lista.remove('cga')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'cgc'  in lista:
            lista.remove('cgc')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'cgg'  in lista:
            lista.remove('cgg')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'cgt'  in lista:
            lista.remove('cgt')
            lista.append('\033[36mR\033[m')
            seq1 = ''
        elif 'gta'  in lista:
            lista.remove('gta')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        elif 'gtc'  in lista:
            lista.remove('gtc')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        elif 'gtg'  in lista:
            lista.remove('gtg')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        elif 'gtt'  in lista:
            lista.remove('gtt')
            lista.append('\033[36mV\033[m')
            seq1 = ''
        elif 'gca'  in lista:
            lista.remove('gca')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        elif 'gcc'  in lista:
            lista.remove('gcc')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        elif 'gcg'  in lista:
            lista.remove('gcg')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        elif 'gct'  in lista:
            lista.remove('gct')
            lista.append('\033[36mA\033[m')
            seq1 = ''
        elif 'gac'  in lista:
            lista.remove('gac')
            lista.append('\033[36mD\033[m')
            seq1 = ''
        elif 'gat'  in lista:
            lista.remove('gat')
            lista.append('\033[36mD\033[m')
            seq1 = ''
        elif 'gag'  in lista:
            lista.remove('gag')
            lista.append('\033[36mE\033[m')
            seq1 = ''
        elif 'gga'  in lista:
            lista.remove('gga')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        elif 'gaa'  in lista:
            lista.remove('gaa')
            lista.append('\033[36mE\033[m')
            seq1 = ''
        elif 'ggc'  in lista:
            lista.remove('ggc')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        elif 'ggg'  in lista:
            lista.remove('ggg')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        elif 'ggt'  in lista:
            lista.remove('ggt')
            lista.append('\033[36mG\033[m')
            seq1 = ''
        elif 'tca'  in lista:
            lista.remove('tca')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'ttc'  in lista:
            lista.remove('ttc')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'tcg'  in lista:
            lista.remove('tcg')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'tct'  in lista:
            lista.remove('tct')
            lista.append('\033[36mS\033[m')
            seq1 = ''
        elif 'ttc'  in lista:
            lista.remove('ttc')
            lista.append('\033[36mF\033[m')
            seq1 = ''
        elif 'ttt'  in lista:
            lista.remove('ttt')
            lista.append('\033[36mF\033[m')
            seq1 = ''
        elif 'tta' in lista:
            lista.remove('tta')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'ttg' in lista:
            lista.remove('ttg')
            lista.append('\033[36mL\033[m')
            seq1 = ''
        elif 'tac' in lista:
            lista.remove('tac')
            lista.append('\033[36mY\033[m')
            seq1 = ''
        elif 'tat' in lista:
            lista.remove('tat')
            lista.append('\033[36mY\033[m')
            seq1 = ''
        elif 'taa' in lista:
            lista.remove('taa')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        elif 'tag' in lista:
            lista.remove('tag')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        elif 'tgc' in lista:
            lista.remove('tgc')
            lista.append('\033[36mC\033[m')
            seq1 = ''
        elif 'tgt' in lista:
            lista.remove('tgt')
            lista.append('\033[36mC\033[m')
            seq1 = ''
        elif 'tga' in lista:
            lista.remove('tga')
            lista.append(('\033[::40m_\033[m'))
            seq1 = ''
        elif 'tgg' in lista:
            lista.remove('tgg')
            lista.append('\033[36mW\033[m')
            seq1 = ''
        elif 'tcc' in lista:
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
        elif 'aaa' in lista1:
            lista1.remove('aaa')
            lista1.append('\033[36mK\033[m')
            seq2 = ''
        elif 'atc' in lista1:
            lista1.remove('atc')
            lista1.append('\033[36mI\033[m')
            seq2 = ''
        elif 'att' in lista1:
            lista1.remove('att')
            lista1.append('\033[36mI\033[m')
            seq2 = ''
        elif 'atg' in lista1:
            lista1.remove('atg')
            lista1.append('\033[30;1mM\033[m')
            seq2 = ''
        elif 'aca' in lista1:
            lista1.remove('aca')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        elif 'acc' in lista1:
            lista1.remove('acc')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        elif 'aat' in lista1:
            lista1.remove('aat')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'acg' in lista1:
            lista1.remove('acg')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        elif 'act' in lista1:
            lista1.remove('act')
            lista1.append('\033[36mT\033[m')
            seq2 = ''
        elif 'aac' in lista1:
            lista1.remove('aac')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'aag' in lista1:
            lista1.remove('aag')
            lista1.append('\033[36mK\033[m')
            seq2 = ''
        elif 'agc' in lista1:
            lista1.remove('agc')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'agt' in lista1:
            lista1.remove('agt')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'aga' in lista1:
            lista1.remove('aga')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'agg' in lista1:
            lista1.remove('agg')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'cta' in lista1:
            lista1.remove('cta')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'ctc' in lista1:
            lista1.remove('ctc')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'ctg' in lista1:
            lista1.remove('ctg')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'ctt' in lista1:
            lista1.remove('ctt')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'cca' in lista1:
            lista1.remove('cca')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        elif 'ccc' in lista1:
            lista1.remove('ccc')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        elif 'ccg' in lista1:
            lista1.remove('ccg')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        elif 'cct' in lista1:
            lista1.remove('cct')
            lista1.append('\033[36mP\033[m')
            seq2 = ''
        elif 'cac'  in lista1:
            lista1.remove('cac')
            lista1.append('\033[36mH\033[m')
            seq2 = ''
        elif 'cat'  in lista1:
            lista1.remove('cat')
            lista1.append('\033[36mH\033[m')
            seq2 = ''
        elif 'caa'  in lista1:
            lista1.remove('caa')
            lista1.append('\033[36mQ\033[m')
            seq2 = ''
        elif 'cag'  in lista1:
            lista1.remove('cag')
            lista1.append('\033[36mQ\033[m')
            seq2 = ''
        elif 'cga'  in lista1:
            lista1.remove('cga')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'cgc'  in lista1:
            lista1.remove('cgc')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'cgg'  in lista1:
            lista1.remove('cgg')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'cgt'  in lista1:
            lista1.remove('cgt')
            lista1.append('\033[36mR\033[m')
            seq2 = ''
        elif 'gta'  in lista1:
            lista1.remove('gta')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        elif 'gtc'  in lista1:
            lista1.remove('gtc')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        elif 'gtg'  in lista1:
            lista1.remove('gtg')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        elif 'gtt'  in lista1:
            lista1.remove('gtt')
            lista1.append('\033[36mV\033[m')
            seq2 = ''
        elif 'gca'  in lista1:
            lista1.remove('gca')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'gcc'  in lista1:
            lista1.remove('gcc')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'gcg'  in lista1:
            lista1.remove('gcg')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'gct'  in lista1:
            lista1.remove('gct')
            lista1.append('\033[36mA\033[m')
            seq2 = ''
        elif 'gac'  in lista1:
            lista1.remove('gac')
            lista1.append('\033[36mD\033[m')
            seq2 = ''
        elif 'gat'  in lista1:
            lista1.remove('gat')
            lista1.append('\033[36mD\033[m')
            seq2 = ''
        elif 'gag'  in lista1:
            lista1.remove('gag')
            lista1.append('\033[36mE\033[m')
            seq2 = ''
        elif 'gga'  in lista1:
            lista1.remove('gga')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        elif 'gaa'  in lista1:
            lista1.remove('gaa')
            lista1.append('\033[36mE\033[m')
            seq2 = ''
        elif 'ggc'  in lista1:
            lista1.remove('ggc')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        elif 'ggg'  in lista1:
            lista1.remove('ggg')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        elif 'ggt'  in lista1:
            lista1.remove('ggt')
            lista1.append('\033[36mG\033[m')
            seq2 = ''
        elif 'tca'  in lista1:
            lista1.remove('tca')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'ttc'  in lista1:
            lista1.remove('ttc')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'tcg'  in lista1:
            lista1.remove('tcg')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'tct'  in lista1:
            lista1.remove('tct')
            lista1.append('\033[36mS\033[m')
            seq2 = ''
        elif 'ttc'  in lista1:
            lista1.remove('ttc')
            lista1.append('\033[36mF\033[m')
            seq2 = ''
        elif 'ttt'  in lista1:
            lista1.remove('ttt')
            lista1.append('\033[36mF\033[m')
            seq2 = ''
        elif 'tta' in lista1:
            lista1.remove('tta')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'ttg' in lista1:
            lista1.remove('ttg')
            lista1.append('\033[36mL\033[m')
            seq2 = ''
        elif 'tac' in lista1:
            lista1.remove('tac')
            lista1.append('\033[36mY\033[m')
            seq2 = ''
        elif 'tat' in lista1:
            lista1.remove('tat')
            lista1.append('\033[36mY\033[m')
            seq2 = ''
        elif 'taa' in lista1:
            lista1.remove('taa')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        elif 'tag' in lista1:
            lista1.remove('tag')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        elif 'tgc' in lista1:
            lista1.remove('tgc')
            lista1.append('\033[36mC\033[m')
            seq2 = ''
        elif 'tgt' in lista1:
            lista1.remove('tgt')
            lista1.append('\033[36mC\033[m')
            seq2 = ''
        elif 'tga' in lista1:
            lista1.remove('tga')
            lista1.append(('\033[::40m_\033[m'))
            seq2 = ''
        elif 'tgg' in lista1:
            lista1.remove('tgg')
            lista1.append('\033[36mW\033[m')
            seq2 = ''
        elif 'tcc' in lista1:
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
        elif 'aaa' in lista2:
            lista2.remove('aaa')
            lista2.append('\033[36mK\033[m')
            seq3 = ''
        elif 'atc' in lista2:
            lista2.remove('atc')
            lista2.append('\033[36mI\033[m')
            seq3 = ''
        elif 'att' in lista2:
            lista2.remove('att')
            lista2.append('\033[36mI\033[m')
            seq3 = ''
        elif 'aat' in lista2:
            lista2.remove('aat')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'atg' in lista2:
            lista2.remove('atg')
            lista2.append('\033[30;1mM\033[m')
            seq3 = ''
        elif 'aca' in lista2:
            lista2.remove('aca')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        elif 'acc' in lista2:
            lista2.remove('acc')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        elif 'acg' in lista2:
            lista2.remove('acg')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        elif 'act' in lista2:
            lista2.remove('act')
            lista2.append('\033[36mT\033[m')
            seq3 = ''
        elif 'aac' in lista2:
            lista2.remove('aac')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'aag' in lista2:
            lista2.remove('aag')
            lista2.append('\033[36mK\033[m')
            seq3 = ''
        elif 'agc' in lista2:
            lista2.remove('agc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'agt' in lista2:
            lista2.remove('agt')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'aga' in lista2:
            lista2.remove('aga')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'agg' in lista2:
            lista2.remove('agg')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'cta' in lista2:
            lista2.remove('cta')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'ctc' in lista2:
            lista2.remove('ctc')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'ctg' in lista2:
            lista2.remove('ctg')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'ctt' in lista2:
            lista2.remove('ctt')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'cca' in lista2:
            lista2.remove('cca')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        elif 'ccc' in lista2:
            lista2.remove('ccc')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        elif 'ccg' in lista2:
            lista2.remove('ccg')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        elif 'cct' in lista2:
            lista2.remove('cct')
            lista2.append('\033[36mP\033[m')
            seq3 = ''
        elif 'cac'  in lista2:
            lista2.remove('cac')
            lista2.append('\033[36mH\033[m')
            seq3 = ''
        elif 'cat'  in lista2:
            lista2.remove('cat')
            lista2.append('\033[36mH\033[m')
            seq3 = ''
        elif 'caa'  in lista2:
            lista2.remove('caa')
            lista2.append('\033[36mQ\033[m')
            seq3 = ''
        elif 'cag'  in lista2:
            lista2.remove('cag')
            lista2.append('\033[36mQ\033[m')
            seq3 = ''
        elif 'cga'  in lista2:
            lista2.remove('cga')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'cgc'  in lista2:
            lista2.remove('cgc')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'cgg'  in lista2:
            lista2.remove('cgg')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'cgt'  in lista2:
            lista2.remove('cgt')
            lista2.append('\033[36mR\033[m')
            seq3 = ''
        elif 'gta'  in lista2:
            lista2.remove('gta')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        elif 'gtc'  in lista2:
            lista2.remove('gtc')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        elif 'gtg'  in lista2:
            lista2.remove('gtg')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        elif 'gtt'  in lista2:
            lista2.remove('gtt')
            lista2.append('\033[36mV\033[m')
            seq3 = ''
        elif 'gca'  in lista2:
            lista2.remove('gca')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'gcc'  in lista2:
            lista2.remove('gcc')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'gcg'  in lista2:
            lista2.remove('gcg')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'gct'  in lista2:
            lista2.remove('gct')
            lista2.append('\033[36mA\033[m')
            seq3 = ''
        elif 'gac'  in lista2:
            lista2.remove('gac')
            lista2.append('\033[36mD\033[m')
            seq3 = ''
        elif 'gat'  in lista2:
            lista2.remove('gat')
            lista2.append('\033[36mD\033[m')
            seq3 = ''
        elif 'gag'  in lista2:
            lista2.remove('gag')
            lista2.append('\033[36mE\033[m')
            seq3 = ''
        elif 'gga'  in lista2:
            lista2.remove('gga')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        elif 'gaa'  in lista2:
            lista2.remove('gaa')
            lista2.append('\033[36mE\033[m')
            seq3 = ''
        elif 'ggc'  in lista2:
            lista2.remove('ggc')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        elif 'ggg'  in lista2:
            lista2.remove('ggg')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        elif 'ggt'  in lista2:
            lista2.remove('ggt')
            lista2.append('\033[36mG\033[m')
            seq3 = ''
        elif 'tca'  in lista2:
            lista2.remove('tca')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'ttc'  in lista2:
            lista2.remove('ttc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'tcc' in lista2:
            lista2.remove('tcc')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'tcg'  in lista2:
            lista2.remove('tcg')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'tct'  in lista2:
            lista2.remove('tct')
            lista2.append('\033[36mS\033[m')
            seq3 = ''
        elif 'ttc'  in lista2:
            lista2.remove('ttc')
            lista2.append('\033[36mF\033[m')
            seq3 = ''
        elif 'ttt'  in lista2:
            lista2.remove('ttt')
            lista2.append('\033[36mF\033[m')
            seq3 = ''
        elif 'tta' in lista2:
            lista2.remove('tta')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'ttg' in lista2:
            lista2.remove('ttg')
            lista2.append('\033[36mL\033[m')
            seq3 = ''
        elif 'tac' in lista2:
            lista2.remove('tac')
            lista2.append('\033[36mY\033[m')
            seq3 = ''
        elif 'tat' in lista2:
            lista2.remove('tat')
            lista2.append('\033[36mY\033[m')
            seq3 = ''
        elif 'taa' in lista2:
            lista2.remove('taa')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        elif 'tag' in lista2:
            lista2.remove('tag')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        elif 'tgc' in lista2:
            lista2.remove('tgc')
            lista2.append('\033[36mC\033[m')
            seq3 = ''
        elif 'tgt' in lista2:
            lista2.remove('tgt')
            lista2.append('\033[36mC\033[m')
            seq3 = ''
        elif 'tga' in lista2:
            lista2.remove('tga')
            lista2.append(('\033[::40m_\033[m'))
            seq3 = ''
        elif 'tgg' in lista2:
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
        elif 'aaa' in lista3:
            lista3.remove('aaa')
            lista3.append('\033[36mK\033[m')
            seq4 = ''
        elif 'atc' in lista3:
            lista3.remove('atc')
            lista3.append('\033[36mI\033[m')
            seq4 = ''
        elif 'att' in lista3:
            lista3.remove('att')
            lista3.append('\033[36mI\033[m')
            seq4 = ''
        elif 'aat' in lista3:
            lista3.remove('aat')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        elif 'atg' in lista3:
            lista3.remove('atg')
            lista3.append('\033[30;1mM\033[m')
            seq4 = ''
        elif 'aca' in lista3:
            lista3.remove('aca')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        elif 'acc' in lista3:
            lista3.remove('acc')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        elif 'acg' in lista3:
            lista3.remove('acg')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        elif 'act' in lista3:
            lista3.remove('act')
            lista3.append('\033[36mT\033[m')
            seq4 = ''
        elif 'acc' in lista3:
            lista3.remove('acc')
            lista3.append('\033[36mN\033[m')
            seq4 = ''
        elif 'aag' in lista3:
            lista3.remove('aag')
            lista3.append('\033[36mK\033[m')
            seq4 = ''
        elif 'agc' in lista3:
            lista3.remove('agc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'agt' in lista3:
            lista3.remove('agt')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'aga' in lista3:
            lista3.remove('aga')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'agg' in lista3:
            lista3.remove('agg')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'cta' in lista3:
            lista3.remove('cta')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'ctc' in lista3:
            lista3.remove('ctc')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'ctg' in lista3:
            lista3.remove('ctg')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'ctt' in lista3:
            lista3.remove('ctt')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'cca' in lista3:
            lista3.remove('cca')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        elif 'ccc' in lista3:
            lista3.remove('ccc')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        elif 'ccg' in lista3:
            lista3.remove('ccg')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        elif 'cct' in lista3:
            lista3.remove('cct')
            lista3.append('\033[36mP\033[m')
            seq4 = ''
        elif 'cac'  in lista3:
            lista3.remove('cac')
            lista3.append('\033[36mH\033[m')
            seq4 = ''
        elif 'cat'  in lista3:
            lista3.remove('cat')
            lista3.append('\033[36mH\033[m')
            seq4 = ''
        elif 'caa'  in lista3:
            lista3.remove('caa')
            lista3.append('\033[36mQ\033[m')
            seq4 = ''
        elif 'cag'  in lista3:
            lista3.remove('cag')
            lista3.append('\033[36mQ\033[m')
            seq4 = ''
        elif 'cga'  in lista3:
            lista3.remove('cga')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'cgc'  in lista3:
            lista3.remove('cgc')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'cgg'  in lista3:
            lista3.remove('cgg')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'cgt'  in lista3:
            lista3.remove('cgt')
            lista3.append('\033[36mR\033[m')
            seq4 = ''
        elif 'gta'  in lista3:
            lista3.remove('gta')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        elif 'gtc'  in lista3:
            lista3.remove('gtc')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        elif 'gtg'  in lista3:
            lista3.remove('gtg')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        elif 'gtt'  in lista3:
            lista3.remove('gtt')
            lista3.append('\033[36mV\033[m')
            seq4 = ''
        elif 'gca'  in lista3:
            lista3.remove('gca')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        elif 'gcc'  in lista3:
            lista3.remove('gcc')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        elif 'gcg'  in lista3:
            lista3.remove('gcg')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        elif 'gct'  in lista3:
            lista3.remove('gct')
            lista3.append('\033[36mA\033[m')
            seq4 = ''
        elif 'gac'  in lista3:
            lista3.remove('gac')
            lista3.append('\033[36mD\033[m')
            seq4 = ''
        elif 'gat'  in lista3:
            lista3.remove('gat')
            lista3.append('\033[36mD\033[m')
            seq4 = ''
        elif 'gag'  in lista3:
            lista3.remove('gag')
            lista3.append('\033[36mE\033[m')
            seq4 = ''
        elif 'gga'  in lista3:
            lista3.remove('gga')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        elif 'gaa'  in lista3:
            lista3.remove('gaa')
            lista3.append('\033[36mE\033[m')
            seq4 = ''
        elif 'ggc'  in lista3:
            lista3.remove('ggc')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        elif 'ggg'  in lista3:
            lista3.remove('ggg')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        elif 'ggt'  in lista3:
            lista3.remove('ggt')
            lista3.append('\033[36mG\033[m')
            seq4 = ''
        elif 'tca'  in lista3:
            lista3.remove('tca')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'ttc'  in lista3:
            lista3.remove('ttc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'tcg'  in lista3:
            lista3.remove('tcg')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'tct'  in lista3:
            lista3.remove('tct')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'ttc'  in lista3:
            lista3.remove('ttc')
            lista3.append('\033[36mF\033[m')
            seq4 = ''
        elif 'ttt'  in lista3:
            lista3.remove('ttt')
            lista3.append('\033[36mF\033[m')
            seq4 = ''
        elif 'tta' in lista3:
            lista3.remove('tta')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'ttg' in lista3:
            lista3.remove('ttg')
            lista3.append('\033[36mL\033[m')
            seq4 = ''
        elif 'tac' in lista3:
            lista3.remove('tac')
            lista3.append('\033[36mY\033[m')
            seq4 = ''
        elif 'tat' in lista3:
            lista3.remove('tat')
            lista3.append('\033[36mY\033[m')
            seq4 = ''
        elif 'taa' in lista3:
            lista3.remove('taa')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        elif 'tag' in lista3:
            lista3.remove('tag')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        elif 'tgc' in lista3:
            lista3.remove('tgc')
            lista3.append('\033[36mC\033[m')
            seq4 = ''
        elif 'tgt' in lista3:
            lista3.remove('tgt')
            lista3.append('\033[36mC\033[m')
            seq4 = ''
        elif 'tga' in lista3:
            lista3.remove('tga')
            lista3.append(('\033[::40m_\033[m'))
            seq4 = ''
        elif 'tgg' in lista3:
            lista3.remove('tgg')
            lista3.append('\033[36mW\033[m')
            seq4 = ''
        elif 'tcc' in lista3:
            lista3.remove('tcc')
            lista3.append('\033[36mS\033[m')
            seq4 = ''
        elif 'aac' in lista3:
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
        elif 'aaa' in lista4:
            lista4.remove('aaa')
            lista4.append('\033[36mK\033[m')
            seq5 = ''
        elif 'atc' in lista4:
            lista4.remove('atc')
            lista4.append('\033[36mI\033[m')
            seq5 = ''
        elif 'att' in lista4:
            lista4.remove('att')
            lista4.append('\033[36mI\033[m')
            seq5 = ''
        elif 'aat' in lista4:
            lista4.remove('aat')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        elif 'atg' in lista4:
            lista4.remove('atg')
            lista4.append('\033[30;1mM\033[m')
            seq5 = ''
        elif 'aca' in lista4:
            lista4.remove('aca')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        elif 'acc' in lista4:
            lista4.remove('acc')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        elif 'acg' in lista4:
            lista4.remove('acg')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        elif 'act' in lista4:
            lista4.remove('act')
            lista4.append('\033[36mT\033[m')
            seq5 = ''
        elif 'acc' in lista4:
            lista4.remove('acc')
            lista4.append('\033[36mN\033[m')
            seq5 = ''
        elif 'aag' in lista4:
            lista4.remove('aag')
            lista4.append('\033[36mK\033[m')
            seq5 = ''
        elif 'agc' in lista4:
            lista4.remove('agc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'agt' in lista4:
            lista4.remove('agt')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'aga' in lista4:
            lista4.remove('aga')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'agg' in lista4:
            lista4.remove('agg')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'cta' in lista4:
            lista4.remove('cta')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'ctc' in lista4:
            lista4.remove('ctc')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'ctg' in lista4:
            lista4.remove('ctg')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'ctt' in lista4:
            lista4.remove('ctt')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'cca' in lista4:
            lista4.remove('cca')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        elif 'ccc' in lista4:
            lista4.remove('ccc')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        elif 'ccg' in lista4:
            lista4.remove('ccg')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        elif 'cct' in lista4:
            lista4.remove('cct')
            lista4.append('\033[36mP\033[m')
            seq5 = ''
        elif 'cac'  in lista4:
            lista4.remove('cac')
            lista4.append('\033[36mH\033[m')
            seq5 = ''
        elif 'cat'  in lista4:
            lista4.remove('cat')
            lista4.append('\033[36mH\033[m')
            seq5 = ''
        elif 'caa'  in lista4:
            lista4.remove('caa')
            lista4.append('\033[36mQ\033[m')
            seq5 = ''
        elif 'cag'  in lista4:
            lista4.remove('cag')
            lista4.append('\033[36mQ\033[m')
            seq5 = ''
        elif 'cga'  in lista4:
            lista4.remove('cga')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'cgc'  in lista4:
            lista4.remove('cgc')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'cgg'  in lista4:
            lista4.remove('cgg')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'cgt'  in lista4:
            lista4.remove('cgt')
            lista4.append('\033[36mR\033[m')
            seq5 = ''
        elif 'gta'  in lista4:
            lista4.remove('gta')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        elif 'gtc'  in lista4:
            lista4.remove('gtc')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        elif 'gtg'  in lista4:
            lista4.remove('gtg')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        elif 'gtt'  in lista4:
            lista4.remove('gtt')
            lista4.append('\033[36mV\033[m')
            seq5 = ''
        elif 'gca'  in lista4:
            lista4.remove('gca')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        elif 'gcc'  in lista4:
            lista4.remove('gcc')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        elif 'gcg'  in lista4:
            lista4.remove('gcg')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        elif 'gct'  in lista4:
            lista4.remove('gct')
            lista4.append('\033[36mA\033[m')
            seq5 = ''
        elif 'gac'  in lista4:
            lista4.remove('gac')
            lista4.append('\033[36mD\033[m')
            seq5 = ''
        elif 'gat'  in lista4:
            lista4.remove('gat')
            lista4.append('\033[36mD\033[m')
            seq5 = ''
        elif 'gag'  in lista4:
            lista4.remove('gag')
            lista4.append('\033[36mE\033[m')
            seq5 = ''
        elif 'gga'  in lista4:
            lista4.remove('gga')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        elif 'gaa'  in lista4:
            lista4.remove('gaa')
            lista4.append('\033[36mE\033[m')
            seq5 = ''
        elif 'ggc'  in lista4:
            lista4.remove('ggc')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        elif 'ggg'  in lista4:
            lista4.remove('ggg')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        elif 'ggt'  in lista4:
            lista4.remove('ggt')
            lista4.append('\033[36mG\033[m')
            seq5 = ''
        elif 'tca'  in lista4:
            lista4.remove('tca')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'ttc'  in lista4:
            lista4.remove('ttc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'tcg'  in lista4:
            lista4.remove('tcg')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'tct'  in lista4:
            lista4.remove('tct')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'ttc'  in lista4:
            lista4.remove('ttc')
            lista4.append('\033[36mF\033[m')
            seq5 = ''
        elif 'ttt'  in lista4:
            lista4.remove('ttt')
            lista4.append('\033[36mF\033[m')
            seq5 = ''
        elif 'tta' in lista4:
            lista4.remove('tta')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'ttg' in lista4:
            lista4.remove('ttg')
            lista4.append('\033[36mL\033[m')
            seq5 = ''
        elif 'tac' in lista4:
            lista4.remove('tac')
            lista4.append('\033[36mY\033[m')
            seq5 = ''
        elif 'tat' in lista4:
            lista4.remove('tat')
            lista4.append('\033[36mY\033[m')
            seq5 = ''
        elif 'taa' in lista4:
            lista4.remove('taa')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        elif 'tag' in lista4:
            lista4.remove('tag')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        elif 'tgc' in lista4:
            lista4.remove('tgc')
            lista4.append('\033[36mC\033[m')
            seq5 = ''
        elif 'tgt' in lista4:
            lista4.remove('tgt')
            lista4.append('\033[36mC\033[m')
            seq5 = ''
        elif 'tga' in lista4:
            lista4.remove('tga')
            lista4.append(('\033[::40m_\033[m'))
            seq5 = ''
        elif 'tgg' in lista4:
            lista4.remove('tgg')
            lista4.append('\033[36mW\033[m')
            seq5 = ''
        elif 'tcc' in lista4:
            lista4.remove('tcc')
            lista4.append('\033[36mS\033[m')
            seq5 = ''
        elif 'aac' in lista4:
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
        elif 'aaa' in lista5:
            lista5.remove('aaa')
            lista5.append('\033[36mK\033[m')
            seq6 = ''
        elif 'atc' in lista5:
            lista5.remove('atc')
            lista5.append('\033[36mI\033[m')
            seq6 = ''
        elif 'att' in lista5:
            lista5.remove('att')
            lista5.append('\033[36mI\033[m')
            seq6 = ''
        elif 'aat' in lista5:
            lista5.remove('aat')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        elif 'atg' in lista5:
            lista5.remove('atg')
            lista5.append('\033[30;1mM\033[m')
            seq6 = ''
        elif 'aca' in lista5:
            lista5.remove('aca')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        elif 'acc' in lista5:
            lista5.remove('acc')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        elif 'acg' in lista5:
            lista5.remove('acg')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        elif 'act' in lista5:
            lista5.remove('act')
            lista5.append('\033[36mT\033[m')
            seq6 = ''
        elif 'acc' in lista5:
            lista5.remove('acc')
            lista5.append('\033[36mN\033[m')
            seq6 = ''
        elif 'aag' in lista5:
            lista5.remove('aag')
            lista5.append('\033[36mK\033[m')
            seq6 = ''
        elif 'agc' in lista5:
            lista5.remove('agc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'agt' in lista5:
            lista5.remove('agt')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'aga' in lista5:
            lista5.remove('aga')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'agg' in lista5:
            lista5.remove('agg')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'cta' in lista5:
            lista5.remove('cta')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'ctc' in lista5:
            lista5.remove('ctc')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'ctg' in lista5:
            lista5.remove('ctg')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'ctt' in lista5:
            lista5.remove('ctt')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'cca' in lista5:
            lista5.remove('cca')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        elif 'ccc' in lista5:
            lista5.remove('ccc')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        elif 'ccg' in lista5:
            lista5.remove('ccg')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        elif 'cct' in lista5:
            lista5.remove('cct')
            lista5.append('\033[36mP\033[m')
            seq6 = ''
        elif 'cac'  in lista5:
            lista5.remove('cac')
            lista5.append('\033[36mH\033[m')
            seq6 = ''
        elif 'cat'  in lista5:
            lista5.remove('cat')
            lista5.append('\033[36mH\033[m')
            seq6 = ''
        elif 'caa'  in lista5:
            lista5.remove('caa')
            lista5.append('\033[36mQ\033[m')
            seq6 = ''
        elif 'cag'  in lista5:
            lista5.remove('cag')
            lista5.append('\033[36mQ\033[m')
            seq6 = ''
        elif 'cga'  in lista5:
            lista5.remove('cga')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'cgc'  in lista5:
            lista5.remove('cgc')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'cgg'  in lista5:
            lista5.remove('cgg')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'cgt'  in lista5:
            lista5.remove('cgt')
            lista5.append('\033[36mR\033[m')
            seq6 = ''
        elif 'gta'  in lista5:
            lista5.remove('gta')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        elif 'gtc'  in lista5:
            lista5.remove('gtc')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        elif 'gtg'  in lista5:
            lista5.remove('gtg')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        elif 'gtt'  in lista5:
            lista5.remove('gtt')
            lista5.append('\033[36mV\033[m')
            seq6 = ''
        elif 'gca'  in lista5:
            lista5.remove('gca')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        elif 'gcc'  in lista5:
            lista5.remove('gcc')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        elif 'gcg'  in lista5:
            lista5.remove('gcg')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        elif 'gct'  in lista5:
            lista5.remove('gct')
            lista5.append('\033[36mA\033[m')
            seq6 = ''
        elif 'gac'  in lista5:
            lista5.remove('gac')
            lista5.append('\033[36mD\033[m')
            seq6 = ''
        elif 'gat'  in lista5:
            lista5.remove('gat')
            lista5.append('\033[36mD\033[m')
            seq6 = ''
        elif 'gag'  in lista5:
            lista5.remove('gag')
            lista5.append('\033[36mE\033[m')
            seq6 = ''
        elif 'gga'  in lista5:
            lista5.remove('gga')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        elif 'gaa'  in lista5:
            lista5.remove('gaa')
            lista5.append('\033[36mE\033[m')
            seq6 = ''
        elif 'ggc'  in lista5:
            lista5.remove('ggc')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        elif 'ggg'  in lista5:
            lista5.remove('ggg')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        elif 'ggt'  in lista5:
            lista5.remove('ggt')
            lista5.append('\033[36mG\033[m')
            seq6 = ''
        elif 'tca'  in lista5:
            lista5.remove('tca')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'ttc'  in lista5:
            lista5.remove('ttc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'tcg'  in lista5:
            lista5.remove('tcg')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'tct'  in lista5:
            lista5.remove('tct')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'ttc'  in lista5:
            lista5.remove('ttc')
            lista5.append('\033[36mF\033[m')
            seq6 = ''
        elif 'ttt'  in lista5:
            lista5.remove('ttt')
            lista5.append('\033[36mF\033[m')
            seq6 = ''
        elif 'tta' in lista5:
            lista5.remove('tta')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'ttg' in lista5:
            lista5.remove('ttg')
            lista5.append('\033[36mL\033[m')
            seq6 = ''
        elif 'tac' in lista5:
            lista5.remove('tac')
            lista5.append('\033[36mY\033[m')
            seq6 = ''
        elif 'tat' in lista5:
            lista5.remove('tat')
            lista5.append('\033[36mY\033[m')
            seq6 = ''
        elif 'taa' in lista5:
            lista5.remove('taa')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        elif 'tag' in lista5:
            lista5.remove('tag')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        elif 'tgc' in lista5:
            lista5.remove('tgc')
            lista5.append('\033[36mC\033[m')
            seq6 = ''
        elif 'tgt' in lista5:
            lista5.remove('tgt')
            lista5.append('\033[36mC\033[m')
            seq6 = ''
        elif 'tga' in lista5:
            lista5.remove('tga')
            lista5.append(('\033[::40m_\033[m'))
            seq6 = ''
        elif 'tgg' in lista5:
            lista5.remove('tgg')
            lista5.append('\033[36mW\033[m')
            seq6 = ''
        elif 'tcc' in lista5:
            lista5.remove('tcc')
            lista5.append('\033[36mS\033[m')
            seq6 = ''
        elif 'aac' in lista5:
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