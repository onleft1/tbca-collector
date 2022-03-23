from fileinput import filename
import requests
import pandas as pd
import csv

pg=1
#atuald=1
url = 'http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina='+str(pg) #+'&atuald='+str(atuald)
csvfilename="my data.csv"
df_total = []

while pg<5:
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df_total = df_total + df_list
    pg = pg + 1


#print(type(df))
df = df_total[0]
df.to_csv(csvfilename)

#### Converting into a dictionary
# opening the file in read mode
file = open(csvfilename, "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    changes = line.replace(",Código,Nome,Nome (Inglês),Nome Científico,Grupo,Marca", "#,Código,Nome,Nome (Inglês),Nome Científico,Grupo,Marca")
    replacement = replacement + changes + "\n"


#print(replacement)
file.close()

# treating the text removing "
with open(csvfilename, 'r') as infile, \
     open("test.csv", 'w') as outfile:
    data = infile.read()
    data = data.replace('"', ' ')
    outfile.write(data)

csvfilename="test.csv"

# with open(csvfilename, "r") as infile, open("repaired.csv", "w") as outfile:
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
with open(csvfilename, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        finallist.append(row)  
#print(finallist)
print(finallist[1])
print(finallist[1][0])
print(finallist[1][1])
print(finallist[1][2])
print(finallist[1][3])

print(len(finallist))


#Creating the Dictionary
# Dict1 = csv.DictReader(open(csvfile))
# for row in input_file:
#     print(row)

# print(type(Dict1))

# for i in Dict1:
#     print(Dict1[i][Código])

