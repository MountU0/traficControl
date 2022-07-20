import os, sys
os.chdir(os.path.dirname(sys.argv[0]))#changing work dir

path = 'E:\\OneDrive - ФГБОУ ВО УГАТУ\\!ML\\Traffic Control\\vscode\\sydney-urban-objects-dataset\\objects\\newset'

fold = []

for dir in os.listdir(path):
    dirFiles = os.listdir(os.path.join(path, dir))
    for file in dirFiles:
        fold.append(f"newset/{dir}/{file}")

with open("Newfold.txt", "w") as file:
    print(*fold, file=file, sep="\n")