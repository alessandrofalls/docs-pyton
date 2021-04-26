'''
Gerar dinamicamente documentos DOCX, a partir de um modelo existente, utilizando informações de um arquivo CSV.
'''
# Arquivo utilizado: template.docx que deverá estar no mesmo diretório da aplicação
# pip3 install python-docx pandas 
# pip3 install docxtpl <- Better for making new files from a template
import random
import time
import csv
import pandas as pd
from docxtpl import DocxTemplate

# Source CSV - column names that must match the *** that are {{***}} inside "template.docx"
csvfn = "cnw2.csv"

def mkw(n):
    tpl = DocxTemplate("template.docx") # In same directory
    df = pd.read_csv(csvfn)
    df_to_doct = df.to_dict() # dataframe -> dict for the template render
    x = df.to_dict(orient='records')
    context = x
    tpl.render(context[n])
    tpl.save("%s.docx" %str(n+1))
    
    # Wait a random time - increase to (60,180) for real production run.
    wait = time.sleep(random.randint(1,2))

#-------------------Main---------------------#

df2 = len(pd.read_csv(csvfn)) 
print ("There will be ", df2, "files")

for i in range(0,df2):
    print("Making file: ",f"{i}," ,"..Please Wait...")
    mkw(i)
    
print("Done! - Now check your files")

