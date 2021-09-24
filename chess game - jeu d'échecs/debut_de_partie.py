import turtle
import json

etat_blanc = {
    'pieces_en_vies' : {'pion1':True,'pion2':True,'pion3':True,'pion4':True,'pion5':True,'pion6':True,'pion7':True,'pion8':True,'tourl':True,'tourr':True,'cavalierl':True,'cavalierr':True,'foun':True,'foub':True,'reine':True,'roi':True},
    'pion1' : ['',''], # mettre des int dans la liste
    'pion2' : ['', ''],
    'pion3' : ['', ''],
    'pion4' : ['', ''],
    'pion5' : ['', ''],
    'pion6' : ['', ''],
    'pion7' : ['', ''],
    'pion8' : ['', ''],
    'tourl' : ['', ''],
    'tourr' : ['', ''],
    'cavalierl' : ['', ''],
    'cavalierr' : ['', ''],
    'foun' : ['', ''],
    'foub' : ['', ''],
    'reine' : ['', ''],
    'roi' : ['', ''],
    'check' : False
}

etat_noir = {
    'pieces_en_vies' : {'pion1':True,'pion2':True,'pion3':True,'pion4':True,'pion5':True,'pion6':True,'pion7':True,'pion8':True,'tourl':True,'tourr':True,'cavalierl':True,'cavalierr':True,'foun':True,'foub':True,'reine':True,'roi':True},
    'pion1' : ['', ''],
    'pion2' : ['', ''],
    'pion3' : ['', ''],
    'pion4' : ['', ''],
    'pion5' : ['', ''],
    'pion6' : ['', ''],
    'pion7' : ['', ''],
    'pion8' : ['', ''],
    'tourl' : ['', ''],
    'tourr' : ['', ''],
    'cavalierl' : ['', ''],
    'cavalierr' : ['', ''],
    'foun' : ['', ''],
    'foub' : ['', ''],
    'reine' : ['', ''],
    'roi' : ['', ''],
    'check' : False
}