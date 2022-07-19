#presentasyon quizoo
import os
import pickle
from Pakeproje import itil
import getpass

print("\t\t\t BYEN VINI SOU QUIZO \t\t\t\n")
print("1-Konekte   \n2-Kreye yon kont\n3-Kite\n")
chwa=input("Chwazi youn nan opsyon sa yo : ")

if chwa=="1":
    nom_iti=input("Antre nomw sil vou ple: ")
    modpas_iti=getpass.getpass("Antre modpas ou a : ")

    itilizate_y ={}
    if os.path.exists("lis_itilizate"):
        fichye=open("lis_itilizate", "rb")
        itilizate_y =pickle.load(fichye)
        fichye.close()
        for kle, val in itilizate_y.items():
            if kle == nom_iti and val ==modpas_iti:
                itil.meni()
        
elif chwa=='2':
    os.system("cls")
    non =input("Antre non ou :")
    modpas=input("Antre yon modpas:")
    itilizate ={}
    if os.path.exists("lis_itilizate"):
        fichye=open("lis_itilizate", "rb")
        itilizate =pickle.load(fichye)
        fichye.close()
        itilizate[non] =modpas
        fichye =open("lis_itilizate", "wb")
        pickle.dump(itilizate, fichye)
        fichye.close()
        itil.meni()
    else:
        itilizate[non] =modpas
        fichye =open("lis_itilizate", "wb")
        pickle.dump(itilizate, fichye)
        fichye.close()
        itil.meni()

elif chwa=="3":
    print("Beyyyyy")
    exit()






