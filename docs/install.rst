==============
Installazione 
==============

Dopo aver lanciato il buildout nella maniera standard, effettuare la
sincronizzazione del db::

  dj syncdb --all
  dj migrate --fake

Verificare successivamente che non ci siano errori mediante::

  dj validate

successivamente creare un database apposito. I settaggi db attuali sono in
:samp:`web/settings/dev.py`.

nella root del progetto è presente un dump in formato json con componenti
iniziali del progetto (pagine, placeholder popolati), in modo da ottenere
una preview di un sito.  per importarli, dopo avere effettuato il :samp:`dj
syncdb --all` e :samp:`dj migrate --fake`, lanciare il :samp:`loaddata`::

  dj loaddata init_cms_sampledata_part1.json
  dj loaddata init_cms_sampledata_part2.json

N.B. effettuare l'import nella sequenza indicata. 
  
all'interno della directory 'web' sono presenti le directory 'static',
'static_auto', 'static_manual'.  'static_manual' contiene i file statici
(css, js, immagini) e serve tali files durante lo sviluppo, essendo settata
nei settings in STATICFILES_DIRS.

Nel momento in cui si passa al deploy, è
necessario raccogliere tutti i file statici (inclusi quelli utilizzati
dall'admin) in una directory che verrà poi utilizzata dal web server per
servirli.  E' necessario lanciare il comando::

  dj collectstatic

la directory dove verranno raccolti i file è la STATIC_ROOT dei settings,
con i settaggi attuali essa punta a 'static_auto'.

