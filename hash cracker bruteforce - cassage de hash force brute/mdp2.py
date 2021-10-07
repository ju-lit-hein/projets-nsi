import hashlib
import time
import datetime

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
mdp2='6a30c0edb3e2df98220ad718f8c0812108865f1b5394e871347b76b5fd5267a4' # = '23061912'
# mdp3 est un mot de la langue française
mdp3='7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784'
# mdp4 ne contient que 5 caractères mais ils peuvent être des majuscules ou des minusucules
mdp4='70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092'
# mdp5 peut contenir des lettes majusucules et minusucles, des chiffres et des caractères spéciaux
mdp5='b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a'


def decryptage_mdp2():
    debut_chrono = time.time()
    start_date = datetime.date(1900,1,1)
    end_date = datetime.date.today()
    delta = end_date - start_date
    print(delta)
    passwd = '01011900'
    i = 0
    while cryptage(passwd) != mdp2:
        i += 1
        passwd = start_date + datetime.timedelta(days = i)
        passwd = str(passwd)
        passwd = passwd[8] +passwd[9] + passwd[5] + passwd[6] + passwd[0] + passwd[1] + passwd[2] + passwd[3]
        print(cryptage(passwd), passwd)
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    return passwd, chrono

print(decryptage_mdp2())