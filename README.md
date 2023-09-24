# Orario-bicocca
Programma che esegue tramite python una finestra di firefox sulla pagina degli orari

requisiti:
  -chromium based browser
  -python3
  -selenium

Il file orario.py può essere messo dove ti pare basta che non sia in una locazione sotto dominio di amministratore.
al suo interno ho messo due link: url ed url2.
Mettendo come argomento del file 1 si avvierà il primo link e mettendo 2 il secondo.
In questo modo: 
>python3 orario.py 1

per eseguire il comando direttamente da terminale si può creare un file binario nel proprio sistema operativo.

per Linux basta scaricare il file orario che ho già messo e inserirlo nella destinazione '/bin/'
una volta messo si possono modificare i path di python e del file orario.py
per poterlo eseguire direttamente come comando da terminale bisogna dare i permessi sudo. 
Usa: 
>sudo chmod +x orario

per Windows si fa in modo analogo ma tramite file bat.(auguri)

CAMBIARE BROWSER
Nel file python ho messo come brwoser default firefox ma basta cambiare webdriver.Firefox() in 
webdriver.Chrome() o .Edge()
per brave non ho ancora creato alcuna implementazione.

