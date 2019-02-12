#Using UUID as primary key indexes

Sto pensando di associare quello che ora si chiama Node ad un'ulteriore entità che chiameremo "Connected Device" (o, se qualcuno ha idee migliori ben vengano).
Ciò per far fronte a quelle situazioni in cui un nodo si rompe e viene sostituito. In tal caso le misure relative al vecchio nodo devono comunque rimanere nel database ed essere utilizzate per effettuare i vari conteggi sui consumi.
Allo stesso modo, le misure del nuovo nodo devono essere registrate, e devono essere messe in relazione con la lampada in cui il nodo è stato installato.
Ecco che quindi il Node è di fatto il nostro oggetto fisico, il WiLamp controller, oppure in futuro qualche altro dispositivo. Mentre il "Connected Device" è la lampada, oppure il lampione, oppure l'armadio di distribuzione. Insomma il luogo oppure l'oggetto dove il nodo viene installato.
Mettendo in relazione il nodo e le varie misure con il "Connected Device" riesco a mantenere lop storico di tutto quello che è successo, comprese eventuali sostituzioni del nodo.

Ecco che a questo punto le relazioni diventerebbero:

	INSTALLATION <=> GATEWAY <=> CONNECTED DEVICE <=> NODE

Vi ricordo inoltre che al singolo nodo possono essere associati più moduli, ad esempio quello della gestione della luce, quello delle misure, quello del motion etc... 
Ciò implica che se voglio inviare una misura dal gateway al cloud io devo ricordarmi tutte queste connessioni.

Ad esempio per inviare una misura di light management devo attraversare tutte queste tabelle:

	INSTALLATION <=> GATEWAY <=> CONNECTED DEVICE <=> NODE <=> NODE MODULE <=> LIGHT MANAGEMENT MODULE <=> LIGHT MANAGEMENT MEASURE

E se volessi ottenere la media di tutte le misure di una particolare installazione dovrò di fatto creare delle query pesantemente non ottimizzate.
Per poter risolvere tale problema la mia idea è quella di inserire nelle misure di light management l'identificativo sia alla connected device, che all'installation, e popolarli direttamente in fase di inserimento delle misure.
A quel punto per ottenere tutte le misure di una particolare installazione farei la chiamata secca sulla tabella misure.



##Considerazione aggiuntiva

Per evitare JOIN su tabella node_modules potrei fare in modo di creare delle relazioni onetoone tra nodo e light management module e tutti gli altri moduli.
Se non esiste la voce nella tabella light_management_module significa che il nodo non dispone di tale tecnologia, oppure si può prevedere un campo posto a null o n/a per identificare tale situazione.
In tal modo i JOIN sarebbero praticamente immediati e non perderei troppo in performance.

Un'altra considerazione è relativa all'oggetto "Connected device", che va benissimo ma potrebbe essere rimpiazzato, nel caso dell'applicazione "LUCE" dall'entità "Light Fixture" che conterrà parametri relativi al mondo luce, e consentirà di velocizzare le query per l'ottenimento della mappa o delle dashboard, evitandone i vari JOIN collegati.





Un altro problema è relativo alla gestione di tutte le relazioni tra nodi, moduli etc..
poter avere un indice comune tra nodi, moduli e altre realtà simili semplificherebbe il problema, ad esempio nel gateway tutto è relazionato al campo mac address che è univoco in un'installazione.
Tuttavia il campo mac address potrebbe non essere più univoco in presenza di molti nodi (cloud) oppure qualora un nodo difettoso venga riutilizzato (perchè ad esempio riparato) in un'altra installazione.
Per ovviare a tale problema pensavo di utilizzare degli identificatori univoci (UUID) per le connected device, per i gateway, per le installazioni e per i nodi. (e di conseguenza i vari moduli)
Gli UUID hanno il pregio di poter essere generati offline e di implicarne (se non garantirne) l'univocità. Per cui posso pensare di poter gestire la creazione dei "Connected Devices" e dei Nodi direttamente dal Gateway, qualora ciò si renda necessario, senza per forza passare attraverso il cloud.
Mi spingerei anche oltre, e di qui la domanda, vorrei utilizzare il campo UUID come chiave di tali tabelle, e volevo conoscere il vostro parere.
L'idea è quella di collegare poi le tabelle node module e light management module direttamente con l'uuid, in questo potrei fare a meno delle foreign keys, ma sopratutto non dovrei avere query con mille join per poter ottenere ad esempio le misure relative ad un particolare nodo, ma farei una query secca alla tabella misure inserendo come uuid quello del nodo.

Leggendo questo articolo: https://github.com/atom/teletype-server/issues/25 (Is using a UUID as a primary key in Postgres a performance hazard?)
sembra che non ci siano particolari cali di performance.


##Implementation

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

SELECT uuid_generate_v1mc();


CREATE SCHEMA IF NOT EXISTS snw;
CREATE TABLE snw.contacts(
   id UUID PRIMARY KEY DEFAULT uuid_generate_v1mc(),
   name TEXT,
   email TEXT
);



166

Django 1.8 now has a built in UUID field. The performance differences when using a UUID vs integer are negligible.

import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
shareimprove this answer
answered Feb 12 '15 at 4:54


