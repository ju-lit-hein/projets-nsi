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
mdp3='7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784'
# mdp4 ne contient que 5 caractères mais ils peuvent être des majuscules ou des minusucules
mdp4='70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092'
# mdp5 peut contenir des lettes majusucules et minusucles, des chiffres et des caractères spéciaux
mdp5='b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a' # 579 156 036 661 182 474 possibilités

def decryptage_mdp5():
    debut_chrono = time.time()

    def fin_char():
        print("Fin des mots de passe.")
        
    def neuf_char():
        passwd = "!!!!!!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        char_5 = 33
        char_6 = 33
        char_7 = 33
        char_8 = 33
        char_9 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if char_4 == 127:
                char_4 = 33
                char_5 += 1
            if char_5 == 127:
                char_5 = 33
                char_6 += 1
            if char_6 == 127:
                char_6 = 33
                char_7 += 1
                char_6 += 1
            if char_7 == 127:
                char_7 = 33
                char_8 += 1
                char_6 += 1
            if char_8 == 127:
                char_8 = 33
                char_9 += 1
            if passwd == "~~~~~~~~~":
                fin_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4) + chr(char_5) + chr(char_6) + chr(char_7) + chr(char_8) + chr(char_9)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def huit_char():
        passwd = "!!!!!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        char_5 = 33
        char_6 = 33
        char_7 = 33
        char_8 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if char_4 == 127:
                char_4 = 33
                char_5 += 1
            if char_5 == 127:
                char_5 = 33
                char_6 += 1
            if char_6 == 127:
                char_6 = 33
                char_7 += 1
                char_6 += 1
            if char_7 == 127:
                char_7 = 33
                char_8 += 1
            if passwd == "~~~~~~~~":
                neuf_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4) + chr(char_5) + chr(char_6) + chr(char_7) + chr(char_8)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def sept_char():
        passwd = "!!!!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        char_5 = 33
        char_6 = 33
        char_7 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if char_4 == 127:
                char_4 = 33
                char_5 += 1
            if char_5 == 127:
                char_5 = 33
                char_6 += 1
            if char_6 == 127:
                char_6 = 33
                char_7 += 1
            if passwd == "~~~~~~~":
                huit_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4) + chr(char_5) + chr(char_6) + chr(char_7)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def six_char():
        passwd = "!!!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        char_5 = 33
        char_6 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if char_4 == 127:
                char_4 = 33
                char_5 += 1
            if char_5 == 127:
                char_5 = 33
                char_6 += 1
            if passwd == "~~~~~~":
                sept_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4) + chr(char_5) + chr(char_6)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def cinq_char():
        passwd = "!!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        char_5 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if char_4 == 127:
                char_4 = 33
                char_5 += 1
            if passwd == "~~~~~":
                six_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4) + chr(char_5)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd


    def quatre_char():
        passwd = "!!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        char_4 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if char_3 == 127:
                char_3 = 33
                char_4 += 1
            if passwd == "~~~~":
                cinq_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3) + chr(char_4)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def trois_char():
        passwd = "!!!"
        char_1 = 33
        char_2 = 33
        char_3 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if char_2 == 127:
                char_2 = 33
                char_3 += 1
            if passwd == "~~~":
                quatre_char()
                break
            passwd = chr(char_1) + chr(char_2) + chr(char_3)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def deux_char():
        passwd = "!!"
        char_1 = 33
        char_2 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1   
            if char_1 == 127:
                char_1 = 33
                char_2 += 1
            if passwd == "~~":
                trois_char()
                break
            passwd = chr(char_1) + chr(char_2)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd

    def un_char():
        passwd = "!"
        char_1 = 33
        while cryptage(passwd) != mdp5:
            char_1 += 1
            if passwd == "~":
                deux_char()
                break
            passwd = chr(char_1)
            print(passwd)
        fin_chrono = time.time()
        chrono = fin_chrono - debut_chrono
        return chrono, passwd
    print(un_char())

decryptage_mdp5()
    