Naast de gekende functies zoals `print()` zullen we nu een aantal andere basisfuncties leren kennen die je in jouw programma’s kan gebruiken.

* `float()`

De `float()` functie kan je gebruiken om getallen met één, twee, … getallen na de komma te printen. Denk eraan: kommagetallen programmeer je met punten en dus niet met komma’s.
Anders krijg je een error. Dit kan je zien in het volgende voorbeeld: 
De eerste code werkt, de tweede code geeft een error. 

![float fouten](media/image13.png "float fouten")

* `int()`
De `int()` functie kan je gebruiken om (komma)getallen af te ronden naar een geheel getal. in het volgende voorbeeld wordt 4.5 afgerond naar een geheel getal met de `int()` functie, namelijk 4.

![int](media/image38.png "int gebruiken")

*`str()`

Met de `str()` functie kan je cijfers ook printen zoals als een tekst. Het is dus gelijk aan de `print()` functie. De cijfers komen dan tussen enkele aanhalingstekens te staan. 

![str](media/image29.png "str gebruiken")

*`len()`

Met de `len()` functie kan je tellen hoeveel letters, cijfers of tekens er aanwezig zijn in jouw code. Let op! De `len()` functie heeft steeds een parameter (aanhalingstekens) 
nodig en kan je gebruiken met of zonder de `print()` functie. 

Laten we even een voorbeeld bekijken. Stel dat je een zin moet schrijven met precies 10 tekens (cijfers, letters,...). Je denkt dat de zin “ik heb één zus en twee broers.” 
precies 10 tekens bevat en wil dit nagaan aan de hand van de `len()` functie. Dan kan je het volgende programmeren: 

![str len](media/image70.png "len van zin")

Wanneer je de code draait, zie je dat er 30 tekens in plaats van 10 in de zin zitten. De spaties worden namelijk meegeteld. Dat zijn er dus meer dan 10! :-)

_Let er op dat je bij de `len()` functie nooit de aanhalingstekens vergeet! Anders krijg je een error!_

Laten we de nieuwe functies even herhalen:

* `float()` - Deze functie kan je gebruiken om met kommagetallen uit te werken.
* `int()` - Deze functie kan getallen afronden. 
* `str()` - Deze functie zal net zoals `print()`, de getallen printen als een tekst. 
* `len()` - Deze functie zal je het aantal tekens helpen tellen. 