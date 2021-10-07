import hashlib
import string
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
mdp3='7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784'
# mdp4 ne contient que 5 caractères mais ils peuvent être des majuscules ou des minusucules
mdp4='70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092' # = 'bOOle'
# mdp5 peut contenir des lettes majusucules et minusucles, des chiffres et des caractères spéciaux
mdp5='b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a'

def decryptage_mdp4():
    debut_chrono = time.time()

    passwd = 'AAAAA'
    premiere_lettre = 65
    deuxieme_lettre = 65
    troisieme_lettre = 65
    quatrieme_lettre = 65
    cinquieme_lettre = 65
    while cryptage(passwd) != mdp4:
        # print(passwd)
        cinquieme_lettre += 1       

        if cinquieme_lettre == 91:      # Fin de l'alphabet majuscule
            cinquieme_lettre = 97       # Passage de 'A' à 'a'
        elif cinquieme_lettre == 123:   # Fin de l'alpahbet minuscule
            cinquieme_lettre = 65       # Passage de 'z' à 'A'
            quatrieme_lettre += 1       # Passage à la lettre supérieure

        if quatrieme_lettre == 91:      # Fin de l'alphabet majuscule
            quatrieme_lettre = 97       # Passage de 'A' à 'a'
        elif quatrieme_lettre == 123:   # Fin de l'alpahbet minuscule
            quatrieme_lettre = 65       # Passage de 'z' à 'A'
            troisieme_lettre += 1       # Passage à la lettre supérieure

        if troisieme_lettre == 91:      # Fin de l'alphabet majuscule
            troisieme_lettre = 97       # Passage de 'A' à 'a'
        elif troisieme_lettre == 123:   # Fin de l'alpahbet minuscule
            troisieme_lettre = 65       # Passage de 'z' à 'A'
            deuxieme_lettre += 1        # Passage à la lettre supérieure

        if deuxieme_lettre == 91:       # Fin de l'alphabet majuscule
            deuxieme_lettre = 97        # Passage de 'A' à 'a'
        elif deuxieme_lettre == 123:    # Fin de l'alpahbet minuscule
            deuxieme_lettre = 65        # Passage de 'z' à 'A'
            premiere_lettre += 1        # Passage à la lettre supérieure

        if premiere_lettre == 91:       # Fin de l'alphabet majuscule
            premiere_lettre = 97        # Passage de 'A' à 'a'

        if passwd == 'zzzzz':           # Fin de mots de passe possibles
            print('Fin des mots de passe.')

        passwd = chr(premiere_lettre) + chr(deuxieme_lettre) + chr(troisieme_lettre) + chr(quatrieme_lettre) + chr(cinquieme_lettre)
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    return passwd, chrono
print(decryptage_mdp4())
        



# VERSION 2.0

def decryptage_mdp4_v2():
    debut = time.time()
    a,b,c,d,e = 0,0,0,0,0
    char = string.ascii_letters
    passwd = char[a] + char[b] + char[c] + char[d] + char[e]
    while cryptage(passwd) != mdp4:
        e += 1
        if e > len(char) - 1:
            e = 0
            d += 1
        if d > len(char) - 1:
            d = 0
            c +=1
        if c > len(char) - 1:
            c = 0
            b += 1
        if b > len(char) - 1:
            b = 0
            a += 1
        if a > len(char) - 1:
            print("Fin des mots de passe possbiles.")
            break
        passwd = char[a] + char[b] + char[c] + char[d] + char[e]
    chrono = time.time() - debut
    return passwd, chrono

#print(decryptage_mdp4_v2())