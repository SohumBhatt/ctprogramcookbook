Een veelvoorkomende oorzaak van fouten in programma’s is dat variabelen niet de waardes blijken te bevatten waarvan je dacht dat ze ze bevatten (vb. x bevat niet 5, maar een ander getal). Een goede manier om je code te “debuggen” 
(dat wil zeggen: zoeken waar de fouten zich bevinden),is het tonen van een variabele aan de hand van de print functie. Zo kan je opnieuw nagaan welke waarde er achter de variabele schuilt. 
Dit brengt ons opnieuw bij Thomas de programmeur. Een medewerker van Apple heeft Thomas even opgebeld. Hij zegt dat hij met een probleem zit, namelijk: de volgende code geeft een foutmelding.  

```python
print(x/y)
```

Om na te gaan wat de foutmelding kan veroorzaken, probeert Thomas eerst te achterhalen welke waardes achter x en y schuilen. Daarom gebruikt hij de functie print twee keer. Dit is wat Thomas ziet:  

```python
print(x)
``` 

`1`

```python
print(y)
```

`0`

Nu weet Thomas wat de fout is. De variabele x heeft de waarde 1. De variabele y heeft de waarde 0. De bewerking gaat dus als volgt: 1/0. Dat geeft een error: delen door 0 gaat immers niet. De persoon die Thomas de programmeur opgebeld heeft, was dus vergeten dat y een nul bevat en bijgevolg geen enkel getal kan delen. 