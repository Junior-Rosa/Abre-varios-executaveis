import subprocess, os, sys

sys.stdout = open('debug.log','w')
# Lista de arquivos executáveis

root = os.getcwd()
print('Root:', root)
lista_diretorio = os.listdir(root)
print(lista_diretorio)
try:   
    lista_diretorio.remove('Open_all.exe')
    lista_diretorio.remove('debug.log')
except:
    pass
for exe in lista_diretorio:
    diretorio = os.path.join(root, exe)
    subprocess.Popen(os.path.join(diretorio, 'ProcMonit.exe'))

