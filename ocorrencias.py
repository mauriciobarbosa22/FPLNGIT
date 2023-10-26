from jjcli import *
cl=clfilter(opt="do:")     ## options in cl.opt  (...if "-d" in cl.opt:)
                              ##    autostrip         (def=True)
                              ##    inplace           (def=False)
                              ##    fs (for csvrow()) (def=",")
                              ##    longopts=["opt1", ...] (def=[])
                              ##    doc=__doc__    (def="FIXME no doc pfovided")
for line in cl.input():...    ## process one rstriped line at the time

def oco_minusculas(texto):
    palavras = re.findall(r'\w+', texto)
    oco = {}
    for palavra in palavras:
        palavra_minuscula = palavra.lower()
        if palavra in oco:
            oco[palavra_minuscula] += 1
        else:
            oco [palavra_minuscula] = 1
    return oco

def printOco(oco, outputFileName):
        ocoAlfabeto = sorted(oco.items())
        with open(outputFileName, 'w', encoding='UTF=8') as output_file:
            for palavra, ocorrencias in ocoAlfabeto:
                output_file.write(f'{palavra}:{ocorrencias}\n')

n = 1
for texto in cl.texto():
     r = oco_minusculas(texto)
     printOco(r, f'saida.txt{n}')
n +=1
