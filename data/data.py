from ciphers import caesar
from ciphers import polybius_square
from ciphers import trisemus
from ciphers import morse
from ciphers import playfair
from ciphers import homophones
from ciphers import vigenere 
from ciphers import magic_square
from ciphers import grille
from ciphers import row_column_transposition




menu_case_lab_1 = [  {
    'cipher': caesar.cipher,
    'decipher': caesar.decipher,
    'slug':'caesar'
    }, 
    { 
    'cipher': polybius_square.encrypt,
    'decipher': polybius_square.decrypt,
     'slug':'polybius_square'
    },
    { 
    'cipher': trisemus.cipher,
    'decipher': trisemus.decipher,
     'slug':'trisemus'
    },
    { 
    'cipher': playfair.encrypt,
    'decipher': playfair.decrypt,
     'slug':'playfair'
    },
    { 
    'cipher': morse.encrypt,
    'decipher': morse.decrypt,
     'slug':'morse'
    },
    { 
    'cipher': homophones.encrypt,
     'slug':'homophones'
    },
    { 
    'cipher': vigenere.cipher,
    'decipher': vigenere.decipher,
     'slug':'vigenere'
    }]
menu_case_lab_2 = [  {
    'cipher': magic_square.encrypt,
    'decipher': magic_square.decrypt,
    'slug':'magic_square'
    }, 
    { 
    'cipher': grille.cipher,
    'decipher': grille.decrypt,
     'slug':'grille'
    },
    { 
    'cipher': row_column_transposition.encrypt,
    'decipher': row_column_transposition.decrypt,
     'slug':'row_column_transposition'
    },
   ]
ciphers_names_lab_1 = ['1.Caesar','2.Polybius','3.Trisemus','4.Playfair','5.Morse','6.Homophones','7.Vigenere']
ciphers_names_lab_2 = ['1.Magic square','2.Grille','3.Row Column Transposition']