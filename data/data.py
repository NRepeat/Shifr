from ciphers import caesar
from ciphers import polybius_square
from ciphers import trisemus
from ciphers import morse
from ciphers import playfair
from ciphers import homophones
from ciphers import vigenere 

menu_case = [  {
    'cipher': caesar.cipher,
    'decipher': caesar.decipher
    }, 
    { 
    'cipher': polybius_square.encrypt,
    'decipher': polybius_square.decrypt
    },
    { 
    'cipher': trisemus.cipher,
    'decipher': trisemus.decipher
    },
    { 
    'cipher': playfair.encrypt,
    'decipher': playfair.decrypt
    },
    { 
    'cipher': morse.encrypt,
    'decipher': morse.decrypt
    },
    { 
    'cipher': homophones.encrypt,
    },
    { 
    'cipher': vigenere.cipher,
    'decipher': vigenere.decipher
    }]

ciphers_names = ['1.Caesar','2.Polybius','3.Trisemus','4.Playfair','5.Morse','6.Homophones','7.Vigenere']