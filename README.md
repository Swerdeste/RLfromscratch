# RLfromscratch
Reinforcement learning for ENSAI

Ce projet a été fait par Angelina Denis-Simoni, Arthur Chane-Sam, Louise Davy et  Zacharie Bouhin.
## Description de l'application
### Installation 
Le but de cette application est de faire du Reinforcement Learning dans le cas d'une partie de *flood-it*.
Tout se passe dans le fichier Agent.py, qui va traiter la partie "informatisée du jeu" :

Tout d'abord, il faut installer tous les packages nécessaires avec :

-------
`pip -r requirements.txt`

-------

Il est aussi nécessaire d'installer Tkinter, si l'installation de ce dernier échoue avec la ligne précédente, vous pouvez utiliser la ligne suivante :

-------
`pip install tk`

-------

Ensuite, ne reste plus qu'à lancer le document **Agent.py** avec le code suivant.

-------
`python projet/Agent.py` 

-------
### Architecture 


Concernant les autres fichiers joints, voilà quelques détails.
Dans le dossier projet, se trouvent trois fichiers importants :

#### **Game.py**

Ce document retranscrit une partie, sa construction en elle-même et tout ce qui peut être pratique, comme le lancement de cette dernière, la vérification des points de victoire et de défaite. C'est aussi dans ce fichier que sont introduit les rewards.

#### **Learning.py**
Ce script est la partie NN de notre travail, il ne sert à rien de l'appeler directement. Ce script sert à entraîner notre model.

 #### **Agent.py**

 C'est donc ce script qui va être le script principal, c'est celui qui lance les parties jeu et RL de notre projet. 
 En utilisant d'autre script comme **helper.py**, vous pourrez représenter sous forme de graphique differentes informations quant à l'avancée de l'analyse.

 
