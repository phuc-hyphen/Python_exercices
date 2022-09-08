import os
# ------------------------ os. -----------------------------------
#  - all functions from posix or nt, e.g. unlink, stat, etc.
#       - os.path is either posixpath or ntpath
#       - os.name is either 'posix' or 'nt'
#       - os.curdir is a string representing the current directory (always '.')
#       - os.pardir is a string representing the parent directory (always '..')
#       - os.sep is the (or a most common) pathname separator ('/' or '\\')
#       - os.extsep is the extension separator (always '.')
#       - os.altsep is the alternate pathname separator (None or '/')
#       - os.pathsep is the component separator used in $PATH etc
#       - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
#       - os.defpath is the default search path for executables
#       - os.devnull is the file path of the null device ('/dev/null', etc.)

# -----------------os.path.------------------
# abspath(path)             →   Retourne un chemin absolu
# basename(p)               →   Retourne le dernier élément d'un chemin
# commonprefix(list)        →   Retourne le chemin commun le plus long d'une liste de chemins
# dirname(p)                →   Retourne le dossier parent de l'élément
# exists(path)              →   Test si un chemin existe
# getaTime(filename)        →   Retourne la date du dernier accès au fichier [os.stat()]
# getctime(filename)        →   Retourne la date du dernier changement de metadonnées du fichier
# getmTime(filename)        →   Retourne la date de la dernière modification du fichier
# getsize(filename)         →   Retourne la tailkle d'un fichier (en octets) 
# isabs(s)                  →   Test si un chemin est absolu
# isdir(s)                  →   Test si le chemin est un dossier
# isfile(path)              →   Test si le chemin est un fichier régulier
# islink(path)              →   Test si le chemin est un lien symbolique
# ismount(path)             →   Test si le chemin est un point de montage
# join(path, s)             →   Ajoute un élément au chemin passé en paramètre
# normcase(s)               →   Normalise la casse d'un chemin
# normpath(path)            →   Normalise le chemin, élimine les doubles barres obliques, etc.
# realpath(filename)        →   Retourne le chemin canonique du nom de fichier spécifié (élimine les liens symboliques)
# samefile(f1, f2)          →   Test si deux chemins font référence au même fichier réel
# sameopenfile(f1, f2)      →   Test si deux objets de fichiers ouverts font référence au même fichier
# split(p)                  →   Fractionne un chemin d'accès. Retourne un tuple
# --------------------------------


# help(os)

# print(os.path .abspath("C:/Users"))
# # test file is exist 
# print(os.path.exists("C:/Users/Public"))

# #list directoory
# print(os.listdir("C:/Users/Public"))

# print(os.path.split("C:/Users/Public")[2]) # get the 2nd directory 



print("C:\Formation\Python\Python_exercices\Exercices\calcul binaire.py".split("\\")[-1])
