import turtle
import json

etat_blanc = {
    'pieces_en_vies' : {'pion1':True,'pion2':True,'pion3':True,'pion4':True,'pion5':True,'pion6':True,'pion7':True,'pion8':True,'tourl':True,'tourr':True,'cavalierl':True,'cavalierr':True,'foun':True,'foub':True,'reine':True,'roi':True},
    'pion1' : [-410,-270], # mettre des int dans la liste
    'pion2' : [-320, -270],
    'pion3' : [-230, -270],
    'pion4' : [-140, -270],
    'pion5' : [-50, -270],
    'pion6' : [40, -270],
    'pion7' : [130, -270],
    'pion8' : [220, -270],
    'tourl' : [-410, -360],
    'cavalierl' : [-320, -360],
    'foun' : [-230, -360],
    'reine' : [-140, -360],
    'roi' : [-50, -360],
    'foub' : [40, -360],
    'cavalierr' : [130, -360],
    'tourr' : [220, -360],
    'check' : False
}

etat_noir = {
    'pieces_en_vies' : {'pion1':True,'pion2':True,'pion3':True,'pion4':True,'pion5':True,'pion6':True,'pion7':True,'pion8':True,'tourl':True,'tourr':True,'cavalierl':True,'cavalierr':True,'foun':True,'foub':True,'reine':True,'roi':True},
    'pion1' : ['', 180],
    'pion2' : ['', 180],
    'pion3' : ['', 180],
    'pion4' : ['', 180],
    'pion5' : ['', 180],
    'pion6' : ['', 180],
    'pion7' : ['', 180],
    'pion8' : ['', 180],
    'tourr' : [-410, 270],
    'cavalierr' : [-320, 270],
    'foub' : [-230, 270],
    'reine' : [-140, 270],
    'roi' : [-50, 270],
    'foun' : [40, 270],
    'cavalierl' : [130, 270],
    'tourl' : [220, 270],
    'check' : False
}