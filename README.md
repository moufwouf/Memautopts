# Memrise_auto_points

Points Importants
-----------------
- Le code fonctione sous Windows + Chrome + Python 3.6.1, pour la version de memrise.com datant de mars 2018, si le site est mis à jours ou que chrome évolue, il est out à fait possible que le programme ne fonctionne plus.
- Certains mots peuvent êtres présents deux fois dans le cours memrise (deux traductions pour un même mot ou l'inverse). Dans ce cas, il faut les ignorer à partir du site.


Installation
------------
- Installer Selenium WebDriver

  - https://www.seleniumhq.org/docs/03_webdriver.jsp

  - `pip install selenium`
   
- Installer la dernière version de ChromeDriver
  
    - https://sites.google.com/a/chromium.org/chromedriver/
    
     - Ajouter le dossier où est placé ChromeDriver dasn les paths de python: 
    ```python
    import sys
    sys.path += ['Chemin du dossier']
    ```
    
Utilisation
-----------
- Le programme fait des révisions rapides en boucle, vous devez donc avoir appris certains mots (une centains devrait suffire).
- Quand vous le lancez pour la première fois, vous ne pouvez pas faire de points car le programme doit 'apprendre' tous les mots que vous avez appris: à chaque fois qu'il voit un mot inconnu, il ne répond pas et memrise donne la réponse, il l'enregistre alors dans un fichier dictionnaire et répondra juste à la prochaine rencontre avec le mot. Ainsi afin de fonctioner, le programme doit d'abord se tromper sur tous les mots que vous avez appris.
- Enfin, il arrive très souvent que le programme plante, il est donc recommandé d'utiliser un fichier bat que vous lancerez à la place du code lui même et qui se charge de relancer le programme à chaque fois que celui-ci plante.
  
  ```
  :aa
  python MemriseR.py
  goto aa
  ```
