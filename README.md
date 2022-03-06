# RLfromscratch
Reinforcment learning for ENSAI
Ce projet a été par Angelina Denis, Arthur Chane-Sam, Louise Davy et  Zacharie Bouhin.
## Description de l'application
### Installation 
Le but de cette application est de faire du Reinforcement Learning dans le cas d'une partie de *flood-it*
Tout ce passe dans le fichier Agent.py, qui va traiter la partie "informatisé du jeu" : 

Tout d'abbord, il faut insatller tous les package nécéssaire avec : 

-------
`pip -r requirements.txt`

-------

Il est aussi nécéssaire d'installer Tkinter, si l'installation de ce dernier échoue avec la ligne précédente, vous pouvez utiliser cette ligne suivante : 

-------
`pip install tk`

-------

Ensuite, ne reste plus qu'à lancer le document **Agent.py** avec la code suivant.

-------
`python projet/Agent.py` 

-------
### Architecture 

Concernant les autres fichiers joint, voilà quelque détails : 
Dans le dossier projet ce trouve trois fichiers importants : 

#### **Game.py**

Ce doncument, représente une partie ça construction en elle même et tout ce qui peut etre pratique, comme la lancement d'une partie, la verification des points de victoire et de défaite. C'est aussi dans ce fichier que sont introduit les rewards.

#### **Learning.py**
 
 C