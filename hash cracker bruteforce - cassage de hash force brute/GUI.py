import tkinter as tk
from tkinter.constants import END, X
import hashlib
import time
import datetime
import string

def cryptage(chaine):
    chaine = chaine.encode('utf8')
    crypt = hashlib.sha256(chaine).hexdigest()
    return crypt

def cryptages():
    temps_entry.delete(0,tk.END)
    crypt = texte.get()
    chaine = crypt.encode('utf8')
    crypt = hashlib.sha256(chaine).hexdigest()
    passwd_entry.delete(0,tk.END)
    passwd_entry.insert(0,crypt)

mdp1 = '08d521440e163f12f3665080336c3196d91991b7e9702b3d52df3b81dec3124f' # = 7159
mdp2 = '6a30c0edb3e2df98220ad718f8c0812108865f1b5394e871347b76b5fd5267a4' # = 23061912
mdp3 = '7092fd8d6c7051cefb3e18246579594f7fdd753a8bf8b843c2e6fcd065673784' # = carotte
mdp4 = '70c70ac1390b190ce8d67bfc3e9832472f6fb3537cf5681fd7c3b5b50308c092' # = bOOle
mdp5 = 'b23e801bcdd74c1f76fd9e9e1bfc911c7ff730b460ca7ecd30fa80c763d7571a'

def decryptage_mdp1():
    temps_entry.delete(0,tk.END)
    debut_chrono = time.time()
    mdp1 = texte.get()
    passwd = '0000'
    
    for trois_zeros in range(0,10): # fait tout les password de 0000 à 0009 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            fin_chrono = time.time()
            chrono = fin_chrono - debut_chrono
            passwd_entry.delete(0,tk.END)
            passwd_entry.insert(0,passwd)
            temps_entry.delete(0,tk.END)
            temps_entry.insert(0,chrono)
            return passwd
            
        else: 
            passwd = '000' + str(trois_zeros)
            # print(passwd)
            #passwd_entry.delete(0,tk.END)
            #passwd_entry.insert(0,passwd)
    
    for deux_zeros in range(10,100): # fait tout les password de 0000 à 0099 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            fin_chrono = time.time()
            chrono = fin_chrono - debut_chrono
            passwd_entry.delete(0,tk.END)
            passwd_entry.insert(0,passwd)
            temps_entry.delete(0,tk.END)
            temps_entry.insert(0,chrono)
            return passwd

        else:
            passwd = '00' + str(deux_zeros)
            # print(passwd)
            #passwd_entry.delete(0,tk.END)
            #passwd_entry.insert(0,passwd)
    
    for un_zero in range(100,1000): # fait tout les password de 0000 à 0999 en conservant le(s) zéro(s) devant le nombre
        if cryptage(passwd) == mdp1:
            fin_chrono = time.time()
            chrono = fin_chrono - debut_chrono
            passwd_entry.delete(0,tk.END)
            passwd_entry.insert(0,passwd)
            temps_entry.delete(0,tk.END)
            temps_entry.insert(0,chrono)
            return passwd

        # else:
            # passwd = '0' + str(un_zero)
            # print(passwd)
            #passwd_entry.delete(0,tk.END)
            #passwd_entry.insert(0,passwd)
    passwd = '0999'
    # fait tout les password de 1000 à 9999
    while cryptage(passwd) != mdp1:
        # print(passwd)
        passwd = int(passwd) + 1
        passwd = str(passwd)
        
        #passwd_entry.delete(0,tk.END)
        #passwd_entry.insert(0,passwd)
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    temps_entry.delete(0,tk.END)
    temps_entry.insert(0,chrono)
    passwd_entry.delete(0,tk.END)
    passwd_entry.insert(0,passwd)

def decryptage_mdp2():
    temps_entry.delete(0,tk.END)
    debut_chrono = time.time()
    start_date = datetime.date(1900,1,1)
    end_date = datetime.date.today()
    delta = end_date - start_date
    # print(delta)
    mdp2 = texte.get()
    passwd = '01011900'
    i = 0
    while cryptage(passwd) != mdp2 and passwd != str(datetime.date.today()):
        i += 1
        passwd = start_date + datetime.timedelta(days = i)
        passwd = str(passwd)
        passwd = passwd[8] +passwd[9] + passwd[5] + passwd[6] + passwd[0] + passwd[1] + passwd[2] + passwd[3]
        # print(passwd)
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    temps_entry.delete(0,tk.END)
    temps_entry.insert(0,chrono)
    passwd_entry.delete(0,tk.END)
    passwd_entry.insert(0,passwd)
    return passwd, chrono

def decryptage_mdp3():
    temps_entry.delete(0,tk.END)
    debut_chrono = time.time()
    mdp3 = texte.get()
    dico = open("C:\\Users\\FERDINAND\\OneDrive\VS CODE\\python\\NSI\\projet\\ForceBrute\\dico.txt", "r", encoding="utf-8")    # ouvre le fichier dico.txt
    mots = dico.readlines()  
    dico.close()            # mots est une liste avec chaque mot "mot\n"
    list_mots = [i[0:-2] for i in mots]          # retire le "\n" de tous les mots
    i = 0
    passwd = list_mots[i]
    while cryptage(passwd) != mdp3: # tant que le hash n'est pas celui recherché
        # print(passwd)
        i += 1                      # passage au mot suivant
        passwd = list_mots[i]       # passage au mot suivant

    fin_chrono = time.time()
    print(passwd)
    chrono = fin_chrono - debut_chrono
    temps_entry.delete(0,END)
    temps_entry.insert(0,chrono)
    passwd_entry.delete(0,tk.END)
    passwd_entry.insert(0,passwd)
    


def decryptage_mdp4():
    debut_chrono = time.time()
    temps_entry.delete(0,tk.END)
    mdp4 = texte.get()
    a,b,c,d,e = 0,0,0,0,0
    char = string.ascii_letters
    long = len(char) - 1
    passwd = char[a] + char[b] + char[c] + char[d] + char[e]
    while cryptage(passwd) != mdp4:
        # print(passwd)
        e += 1
        if e > long: 
            e = 0
            d += 1
        if d > long: 
            d = 0
            c +=1
        if c > long: 
            c = 0
            b += 1
        if b > long: 
            b = 0
            a += 1
        if a > long: 
            print("Fin des mots de passe possbiles.")
            break
        passwd = char[a] + char[b] + char[c] + char[d] + char[e]
    fin_chrono = time.time()
    chrono = fin_chrono - debut_chrono
    temps_entry.delete(0,tk.END)
    temps_entry.insert(0,chrono)
    passwd_entry.delete(0,tk.END)
    passwd_entry.insert(0,passwd)
    return passwd, chrono


# mdp5

def decryptage_mdp5():
    temps_entry.delete(0,tk.END)
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



window = tk.Tk()
window.title("Attaque par BruteForce")
window.geometry("1280x720")
window.minsize(480, 360)
window.config(background="#0f1a20")

frame = tk.Frame(window, bg='#0f1a20')

title = tk.Label(window, text="Attaque Par Force Brute", font=("Courrier", 40), bg="#0f1a20", fg="#f19a3e")
title.pack(expand=tk.YES)

subtitle = tk.Label(frame, text="Insérez un hash à décrypter par Force Brute\n ou insérez un mot de passe à chiffrer : ", font=('Courrier', 25), bg='#0f1a20', fg="#f19a3e")
subtitle.pack(expand=tk.YES)

texte = tk.StringVar()
passwd_entry = tk.Entry(frame, font=("Courrier", 20), textvariable=texte, bg="#0f1a20", fg="#f19a3e")
passwd_entry.pack(fill=tk.X, padx=100)

temps = tk.StringVar()
temps_entry = tk.Entry(frame, font=("Courrier", 20), textvariable=temps, bg="#0f1a20", fg="#f19a3e")
temps_entry.pack(fill=tk.X, padx=450)

bouton_crypter = tk.Button(frame, font=("Courrier", 20), text="  Chiffrer le mot de passe  ", bg="#f19a3e", fg="#0f1a20", command=cryptages)
bouton_crypter.pack(padx=475)

bouton_quatre_chiffres = tk.Button(frame, text="Mot de passe à 4 chiffres", font=("Courrier", 20), bg="#f19a3e", fg="#0f1a20",command=decryptage_mdp1)
bouton_quatre_chiffres.pack(padx=475)

bouton_date_de_naissance = tk.Button(frame, text="Mot de passe JJMMAAAA", font=("Courrier", 20), bg="#f19a3e", fg="#0f1a20", command=decryptage_mdp2)
bouton_date_de_naissance.pack(padx=475)

bouton_mot_francais = tk.Button(frame, text="Mot de passe mot francais", font=("Courrier", 20), bg="#f19a3e", fg="#0f1a20", command=decryptage_mdp3)
bouton_mot_francais.pack(padx=475)

bouton_5_lettres = tk.Button(frame, text="Mot de passe de 5 lettres", font=("Courrier", 20), bg="#f19a3e", fg="#0f1a20", command=decryptage_mdp4)
bouton_5_lettres.pack(padx=475)

bouton_mdp5 = tk.Button(frame, text="mdp5", font=("Courrier", 20), bg="#f19a3e", fg="#0f1a20", command=decryptage_mdp5)
bouton_mdp5.pack(fill=X, padx=475)

frame.pack(expand=tk.YES)

window.mainloop()