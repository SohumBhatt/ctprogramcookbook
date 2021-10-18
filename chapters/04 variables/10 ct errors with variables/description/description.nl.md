Een veelvoorkomende oorzaak van fouten in programma’s is dat variabelen niet de waardes blijken te bevatten waarvan je dacht dat ze ze bevatten 
(vb. x bevat niet 5, maar een ander getal). Een goede manier om je code te “debuggen” (dat wil zeggen, uit te vinden waar de fouten zich bevinden is het printen van variabele. 
Zo kan je opnieuw nagaan wat er nu precies in de variabelen zat.  

Een voorbeeld is de volgende code, die een foutmelding geeft wanneer de programmeur deze uitvoert: 
```python
print(x/y)
```

Wanneer de programmeur dan de variabelen apart print, om te kijken wat ze bevatten, komt het volgende tevoorschijn: 

```python
print(x)
``` 

`1`

```python
print(y)
```

`0`

Nu weet de programmeur wat de fout is: 1 delen door 0 gaat niet. Dan bekom je een error, wat ook hier het geval is. 
De programmeur was dus vergeten dat y een nul bevat en bijgevolg geen enkel getal kan delen. 
