# dzialania z plikami
# filehandler - rura do pliku
# contect manager - pomaga w pracy z plikami
# with - contect managery w pythonie


""" Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========= ===============================================================
    """
with open('test.log', 'w') as fh:
    fh.write('Powitanie \n')
    fh.write('Powitanie 2 \n')
    fh.write('Powitanie 3 \n')

# eror
# with open('test.log', 'x') as file:
#     file.write("dodane \n")

with open('test.log', 'w') as fh:
    fh.write("Nowe \n")

with open('test.log', 'a') as fh:
    fh.write("DODANE \n")
    fh.write("DODANE \n")

with open('test.log', 'a') as fh:
    fh.write("DODANE \n")
    fh.write("DODANE \n")

with open('test.log', 'a', encoding="utf-8") as fh:
    fh.write("ŚĆĘÓŁŚŹ żśęćźżłóą \n")
    fh.write("DODANE \n")
