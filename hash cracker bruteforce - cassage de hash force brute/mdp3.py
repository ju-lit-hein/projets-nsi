import hashlib
import time

def cryptage(chaine):
    #'''Prend en argument une chaîne de caractères et retourne la  chaîne codée'''
    chaine = chaine.encode('utf8')
    crypt = hashlib.sha256(chaine).hexdigest()
    return crypt

# Les mots de passe suivants ont été cryptés avec la fonction définie ci-dessus
# Le but du projet est de les retrouver en utilisant une attaque par force brute !
# mdp1 est un nombre à quatre chiffres
mdp1='08d521440e163f12f3665080336c3196d91991b7e9702b3d52df3b81dec3124f'
# mdp2 est une date de naissance au format jjmmaaaa
mdp2='6a30c0edb3e2df98220ad718f8c0812108865f1b5394e871347b76b5fd5267a4'
# mdp3 est un mot de la langue française
mdp3='7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784' # normalement = "carotte"
# mdp4 ne contient que 5 caractères mais ils peuvent être des majuscules ou des minusucules
mdp4='70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092'
# mdp5 peut contenir des lettes majusucules et minusucles, des chiffres et des caractères spéciaux
mdp5='b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a'


def decryptage_mdp3():
    debut = time.time()
    dico = open("C:\\Users\\FERDINAND\\OneDrive\\VS CODE\\python\\NSI\\projet\\ForceBrute\\dico.txt", "r", encoding="utf-8")    # ouvre le fichier dico.txt
    mots = dico.readlines()  
    dico.close()                                                                                    # mots est une liste avec chaque mot ["mot1\n","mot2\n",...]
    list_mots = []                                                                                  # initialise la liste qui comportera les mots sans le "\n"
    dico_mot_hash = {}                                                                              # initialise le dictionnaire qui comportera la combinaison {mot1:hash,mot2:hash,...}
    for i in mots:
        list_mots.append(i[0:-2])                                                                   # retire le "\n" de tous les mots
    for i in list_mots:
        dico_mot_hash[i] = cryptage(i)                                                              # ajoute au dictionnaire chaque mot comme clé et chaque hash comme valeur
    for i in dico_mot_hash:                                                                         # parcours du dictionnaire par valeur
        if dico_mot_hash[i] != mdp3:                                                                # si le hash n'est pas bon
            print(i)                                                                                # affiche le mot de passe
        else:                                                                                       # si le hash est le bon
            fin = time.time()
            chrono = fin - debut
            print("Le bon mot de passe est : ", i, "et a été trouvé en : ", chrono, "secondes.")                                                  # affiche le mot de passe et le marque "bon"
            break                                                                                   # arrete la boucle for car le mot de passe a été trouvé


decryptage_mdp3()


# VERSION 2.0


def decryptage_mdp3_v2():
    debut_chrono = time.time()
    dico = open("C:\\Users\\anony\\OneDrive\VS CODE\\python\\NSI\\projet\\ForceBrute\\dico.txt", "r", encoding="utf-8")    # ouvre le fichier dico.txt
    mots = dico.readlines()  
    dico.close()            # mots est une liste avec chaque mot "mot\n"
    list_mots = [i[0:-2] for i in mots]          # retire le "\n" de tous les mots
    i = 0
    passwd = list_mots[i]
    while cryptage(passwd) != mdp3: # tant que le hash n'est pas celui recherché
        # print(passwd)     # (ralentit ENORMEMENT le programme)
        i += 1                      # passage au mot suivant
        passwd = list_mots[i]       # passage au mot suivant

    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    return passwd, chrono


print(decryptage_mdp3_v2())
