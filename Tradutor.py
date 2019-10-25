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

def tradutor2():
    lista = []
    seq1 = ''
    for i in seq[1:]:
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
            if 'cac' in lista:
                lista.remove('cac')
                lista.append('\033[36mH\033[m')
                seq1 = ''
            if 'cat' in lista:
                lista.remove('cat')
                lista.append('\033[36mH\033[m')
                seq1 = ''
            if 'caa' in lista:
                lista.remove('caa')
                lista.append('\033[36mQ\033[m')
                seq1 = ''
            if 'cag' in lista:
                lista.remove('cag')
                lista.append('\033[36mQ\033[m')
                seq1 = ''
            if 'cga' in lista:
                lista.remove('cga')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgc' in lista:
                lista.remove('cgc')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgg' in lista:
                lista.remove('cgg')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgt' in lista:
                lista.remove('cgt')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'gta' in lista:
                lista.remove('gta')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtc' in lista:
                lista.remove('gtc')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtg' in lista:
                lista.remove('gtg')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtt' in lista:
                lista.remove('gtt')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gca' in lista:
                lista.remove('gca')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gcc' in lista:
                lista.remove('gcc')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gcg' in lista:
                lista.remove('gcg')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gct' in lista:
                lista.remove('gct')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gac' in lista:
                lista.remove('gac')
                lista.append('\033[36mD\033[m')
                seq1 = ''
            if 'gat' in lista:
                lista.remove('gat')
                lista.append('\033[36mD\033[m')
                seq1 = ''
            if 'gag' in lista:
                lista.remove('gag')
                lista.append('\033[36mE\033[m')
                seq1 = ''
            if 'gga' in lista:
                lista.remove('gga')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'gaa' in lista:
                lista.remove('gaa')
                lista.append('\033[36mE\033[m')
                seq1 = ''
            if 'ggc' in lista:
                lista.remove('ggc')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'ggg' in lista:
                lista.remove('ggg')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'ggt' in lista:
                lista.remove('ggt')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'tca' in lista:
                lista.remove('tca')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'tcg' in lista:
                lista.remove('tcg')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'tct' in lista:
                lista.remove('tct')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('\033[36mF\033[m')
                seq1 = ''
            if 'ttt' in lista:
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
    print('Sua sequência traduzida em quadro de leitura +2 é:\n', a)
    print('A sequência a partir do start códon é:\n', a[a1:a2])
    print(50 * '-=-', '\n\n')
tradutor2()

def tradutor3():
    lista = []
    seq1 = ''
    for i in seq[2:]:
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
            if 'cac' in lista:
                lista.remove('cac')
                lista.append('\033[36mH\033[m')
                seq1 = ''
            if 'cat' in lista:
                lista.remove('cat')
                lista.append('\033[36mH\033[m')
                seq1 = ''
            if 'caa' in lista:
                lista.remove('caa')
                lista.append('\033[36mQ\033[m')
                seq1 = ''
            if 'cag' in lista:
                lista.remove('cag')
                lista.append('\033[36mQ\033[m')
                seq1 = ''
            if 'cga' in lista:
                lista.remove('cga')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgc' in lista:
                lista.remove('cgc')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgg' in lista:
                lista.remove('cgg')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'cgt' in lista:
                lista.remove('cgt')
                lista.append('\033[36mR\033[m')
                seq1 = ''
            if 'gta' in lista:
                lista.remove('gta')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtc' in lista:
                lista.remove('gtc')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtg' in lista:
                lista.remove('gtg')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gtt' in lista:
                lista.remove('gtt')
                lista.append('\033[36mV\033[m')
                seq1 = ''
            if 'gca' in lista:
                lista.remove('gca')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gcc' in lista:
                lista.remove('gcc')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gcg' in lista:
                lista.remove('gcg')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gct' in lista:
                lista.remove('gct')
                lista.append('\033[36mA\033[m')
                seq1 = ''
            if 'gac' in lista:
                lista.remove('gac')
                lista.append('\033[36mD\033[m')
                seq1 = ''
            if 'gat' in lista:
                lista.remove('gat')
                lista.append('\033[36mD\033[m')
                seq1 = ''
            if 'gag' in lista:
                lista.remove('gag')
                lista.append('\033[36mE\033[m')
                seq1 = ''
            if 'gga' in lista:
                lista.remove('gga')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'gaa' in lista:
                lista.remove('gaa')
                lista.append('\033[36mE\033[m')
                seq1 = ''
            if 'ggc' in lista:
                lista.remove('ggc')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'ggg' in lista:
                lista.remove('ggg')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'ggt' in lista:
                lista.remove('ggt')
                lista.append('\033[36mG\033[m')
                seq1 = ''
            if 'tca' in lista:
                lista.remove('tca')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'tcg' in lista:
                lista.remove('tcg')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'tct' in lista:
                lista.remove('tct')
                lista.append('\033[36mS\033[m')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('\033[36mF\033[m')
                seq1 = ''
            if 'ttt' in lista:
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
    print('Sua sequência traduzida em quadro de leitura +3 é:\n', a)
    print('A sequência a partir do start códon é:\n', a[a1:a2])
    print(50 * '-=-', '\n\n')
tradutor3()

def tradutor_1():
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
            if 'cac' in lista3:
                lista3.remove('cac')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'cat' in lista3:
                lista3.remove('cat')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'caa' in lista3:
                lista3.remove('caa')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cag' in lista3:
                lista3.remove('cag')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cga' in lista3:
                lista3.remove('cga')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgc' in lista3:
                lista3.remove('cgc')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgg' in lista3:
                lista3.remove('cgg')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgt' in lista3:
                lista3.remove('cgt')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'gta' in lista3:
                lista3.remove('gta')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtc' in lista3:
                lista3.remove('gtc')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtg' in lista3:
                lista3.remove('gtg')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtt' in lista3:
                lista3.remove('gtt')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gca' in lista3:
                lista3.remove('gca')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcc' in lista3:
                lista3.remove('gcc')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcg' in lista3:
                lista3.remove('gcg')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gct' in lista3:
                lista3.remove('gct')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gac' in lista3:
                lista3.remove('gac')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gat' in lista3:
                lista3.remove('gat')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gag' in lista3:
                lista3.remove('gag')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'gga' in lista3:
                lista3.remove('gga')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'gaa' in lista3:
                lista3.remove('gaa')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'ggc' in lista3:
                lista3.remove('ggc')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggg' in lista3:
                lista3.remove('ggg')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggt' in lista3:
                lista3.remove('ggt')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'tca' in lista3:
                lista3.remove('tca')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tcg' in lista3:
                lista3.remove('tcg')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tct' in lista3:
                lista3.remove('tct')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mF\033[m')
                seq4 = ''
            if 'ttt' in lista3:
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
    print(50 * '-=-', '\n\n')
tradutor_1()

def tradutor_2():
    lista3 = []
    seq4 = ''
    d2 = len(seq)
    for i in seq[d2::-2]:
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
            if 'cac' in lista3:
                lista3.remove('cac')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'cat' in lista3:
                lista3.remove('cat')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'caa' in lista3:
                lista3.remove('caa')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cag' in lista3:
                lista3.remove('cag')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cga' in lista3:
                lista3.remove('cga')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgc' in lista3:
                lista3.remove('cgc')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgg' in lista3:
                lista3.remove('cgg')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgt' in lista3:
                lista3.remove('cgt')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'gta' in lista3:
                lista3.remove('gta')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtc' in lista3:
                lista3.remove('gtc')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtg' in lista3:
                lista3.remove('gtg')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtt' in lista3:
                lista3.remove('gtt')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gca' in lista3:
                lista3.remove('gca')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcc' in lista3:
                lista3.remove('gcc')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcg' in lista3:
                lista3.remove('gcg')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gct' in lista3:
                lista3.remove('gct')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gac' in lista3:
                lista3.remove('gac')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gat' in lista3:
                lista3.remove('gat')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gag' in lista3:
                lista3.remove('gag')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'gga' in lista3:
                lista3.remove('gga')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'gaa' in lista3:
                lista3.remove('gaa')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'ggc' in lista3:
                lista3.remove('ggc')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggg' in lista3:
                lista3.remove('ggg')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggt' in lista3:
                lista3.remove('ggt')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'tca' in lista3:
                lista3.remove('tca')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tcg' in lista3:
                lista3.remove('tcg')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tct' in lista3:
                lista3.remove('tct')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mF\033[m')
                seq4 = ''
            if 'ttt' in lista3:
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
    print('Sua sequência traduzida em quadro de leitura -2 é:\n', d)
    print('A sequência a partir do start códon é:\n', d[d1:])
    print(50 * '-=-', '\n\n')
tradutor_2()

def tradutor_3():
    lista3 = []
    seq4 = ''
    d2 = len(seq)
    for i in seq[d2::-3]:
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
            if 'cac' in lista3:
                lista3.remove('cac')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'cat' in lista3:
                lista3.remove('cat')
                lista3.append('\033[36mH\033[m')
                seq4 = ''
            if 'caa' in lista3:
                lista3.remove('caa')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cag' in lista3:
                lista3.remove('cag')
                lista3.append('\033[36mQ\033[m')
                seq4 = ''
            if 'cga' in lista3:
                lista3.remove('cga')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgc' in lista3:
                lista3.remove('cgc')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgg' in lista3:
                lista3.remove('cgg')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'cgt' in lista3:
                lista3.remove('cgt')
                lista3.append('\033[36mR\033[m')
                seq4 = ''
            if 'gta' in lista3:
                lista3.remove('gta')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtc' in lista3:
                lista3.remove('gtc')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtg' in lista3:
                lista3.remove('gtg')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gtt' in lista3:
                lista3.remove('gtt')
                lista3.append('\033[36mV\033[m')
                seq4 = ''
            if 'gca' in lista3:
                lista3.remove('gca')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcc' in lista3:
                lista3.remove('gcc')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gcg' in lista3:
                lista3.remove('gcg')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gct' in lista3:
                lista3.remove('gct')
                lista3.append('\033[36mA\033[m')
                seq4 = ''
            if 'gac' in lista3:
                lista3.remove('gac')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gat' in lista3:
                lista3.remove('gat')
                lista3.append('\033[36mD\033[m')
                seq4 = ''
            if 'gag' in lista3:
                lista3.remove('gag')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'gga' in lista3:
                lista3.remove('gga')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'gaa' in lista3:
                lista3.remove('gaa')
                lista3.append('\033[36mE\033[m')
                seq4 = ''
            if 'ggc' in lista3:
                lista3.remove('ggc')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggg' in lista3:
                lista3.remove('ggg')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'ggt' in lista3:
                lista3.remove('ggt')
                lista3.append('\033[36mG\033[m')
                seq4 = ''
            if 'tca' in lista3:
                lista3.remove('tca')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tcg' in lista3:
                lista3.remove('tcg')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'tct' in lista3:
                lista3.remove('tct')
                lista3.append('\033[36mS\033[m')
                seq4 = ''
            if 'ttc' in lista3:
                lista3.remove('ttc')
                lista3.append('\033[36mF\033[m')
                seq4 = ''
            if 'ttt' in lista3:
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
    print('Sua sequência traduzida em quadro de leitura -3 é:\n', d)
    print('A sequência a partir do start códon é:\n', d[d1:])
    print(50 * '-=-', '\n\n')
tradutor_3()

