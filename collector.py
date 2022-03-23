from fileinput import filename
import requests
import pandas as pd
import csv

pg=1
mark=1
url1 = "http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina=" #+'&atuald='+str(atuald)
url2 = "http://www.tbca.net.br/base-dados/int_composicao_estatistica.php?cod_produto="
csvfilename1="my data.csv"
csvfilename2="alimentos.csv"

df_total = []

#### Building the list of codes
# while pg < 3:
#     html = requests.get(url1+str(pg)).content #+'&atuald='+str(atuald)
#     df_list = pd.read_html(html)
            
#     if pg == 1:
#         df = df_list[0]
#         df.to_csv(csvfilename1, sep='|') #criando primeiro csv (por pagina)
    
#     else:
#         df = df_list[0] #remover cabecalho
#         #df = df.iloc[1: , :]
#         df.to_csv(csvfilename1, header= None ,mode ="a", sep="|") #adicionando
    
#     pg = pg + 1

# treating the text removing "
with open(csvfilename1, 'r') as infile, \
     open("test.csv", 'w') as outfile:
    data = infile.read()
    data = data.replace("|Código|Nome|Nome (Inglês)|Nome Científico|Grupo|Marca", "#|Código|Nome|Nome (Inglês)|Nome Científico|Grupo|Marca")
    #data = data.replace('"', ' ')
    #data = data.replace(', ', ',')
    #data = data.replace(' ,', ',')
    #data = data.replace(',', ' , ')
    outfile.write(data)

csvfilename1="test.csv"

# with open(csvfilename1, "r") as infile, open("repaired.csv", "w") as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
#     conversion = set('"$')
#     for row in reader:
#         newrow = [''.join('_' if c in conversion else c for c in entry) for entry in row]
#         writer.writerow(newrow)


# opening the file in write mode
#fout = open(csvfile, "w")
#fout.write(replacement)


# doc in https://docs.python.org/3/library/csv.html
finallist= []
with open(csvfilename1, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|')#, quotechar='|')
    for row in spamreader:
        finallist.append(row)  

print()
print("Foram encontrados " + str(len(finallist)-1) + " alimentos na tabela TBCA.")
print()
print("Criando lista de alimentos...")
#List of codes
#for i in finallist:
#    print(finallist[finallist.index(i)][1])

#### Building the list of food using codes
# for i in finallist:
#     html = requests.get(url2+str(finallist[finallist.index(i)][1])).content
#     df_list = pd.read_html(html)
#     df = df_list[0]
#     cod = pd.DataFrame({"code": [str(finallist[finallist.index(i)][1])], 
#         "description": [str(finallist[finallist.index(i)][2])]})
    
#     if mark == 1:
#         cod.to_csv(csvfilename2, header= None , sep="|")
#         df.to_csv(csvfilename2, header= None ,mode ="a", sep="|")
#         mark = mark + 1
    
#     else:
#         cod.to_csv(csvfilename2, header= None ,mode ="a", sep="|")
#         df.to_csv(csvfilename2, header= None ,mode ="a", sep="|")


    