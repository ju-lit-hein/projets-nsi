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
mdp9999 = '888df25ae35772424a560c7152a1de794440e0ea5cfee62828333a456a506e05'
mdp1 = '08d521440e163f12f3665080336c3196d91991b7e9702b3d52df3b81dec3124f' # = '7159'
# mdp2 est une date de naissance au format jjmmaaaa
mdp2 = '6a30c0edb3e2df98220ad718f8c0812108865f1b5394e871347b76b5fd5267a4'
# mdp3 est un mot de la langue française
mdp3 = '7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784'
# mdp4 ne contient que 5 caractères mais ils peuvent être des majuscules ou des minusucules
mdp4 = '70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092'
# mdp5 peut contenir des lettes majusucules et minusucles, des chiffres et des caractères spéciaux
mdp5 = 'b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a'


def decryptage_mdp1():
    debut_chrono = time.time()
    passwd = '0000'
    

    for trois_zeros in range(0,10): # fait tout les password de 0000 à 0009 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            return passwd
        else: 
            passwd = '000' + str(trois_zeros)
            print(cryptage(passwd),passwd)
    
    for deux_zeros in range(10,100): # fait tout les password de 0010 à 0099 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            return passwd
        else:
            passwd = '00' + str(deux_zeros)
            print(cryptage(passwd), passwd)
    
    for un_zero in range(100,1000): # fait tout les password de 0100 à 0999 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            return passwd
        else:
            passwd = '0' + str(un_zero)
            print(cryptage(passwd), passwd)
    passwd = '1000'
    # fait tout les password de 1000 à 9999 en conservant le(s) zéro(s) devant le nombre
    while cryptage(passwd) != mdp1:
        passwd = int(passwd) + 1
        passwd = str(passwd)
        print(cryptage(passwd), passwd)
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    return passwd, chrono
    
    
print(decryptage_mdp1())
