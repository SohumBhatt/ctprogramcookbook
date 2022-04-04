### De functie Print

Wist je dat je Python kan gebruiken als een soort rekenmachine? Het programma kan eenvoudige tekens zoals die hieronder, herkennen!

| operator | beschrijving |
|:--------:|:------------|
| `+` | optelling |
| `-` | aftrekking |
| `*` | vermenigvuldiging |
| `/` | deling |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Stel dat je in Python een rekenopdracht wil uitvoeren en je daarom de volgende bewerking als code ingeeft in het onderste venster van Dodona. 

```python
5 + 7
```

Je verwacht dat, wanneer je het programma draait (door op de oranje knop te klikken), de oplossing 12 getoond zal worden. Dit is helaas niet het geval. 

Hoe komt dat nu? Wel … jouw computer weet niet wat er met de cijfertjes en het plusteken moet gebeuren. 

Je moet dus nog iets extra (nl. de opdracht ‘ toon de oplossing’) toevoegen aan jouw formule. 

Dit doe je door de ‘print’ code of functie toe te voegen

#### De functie Print stuurt wat er tussen haakjes staat naar het codevenstertje 

Het gaat als volgt:

```python
print(5+7)
```

De `print()` functie gebruik gebruik je door:

* eerst het woord print te typen , 
* gevolgd door een rond openingshaakje
* gevolgd door hetgeen je wilt laten tonen (in dit geval de oplossing van 5+7)
* gevolgd door een rond sluithaakje. 

#### Let op!
Je kan in Python, net zoals met een echt rekenmachine, ook verschillende tekens in één bewerking gebruiken. Maar dan zal python, opnieuw net zoals bij een echt rekenmachine, geen rekening houden met de volgorde. 
Tenzij je expliciet met haakjes aangeeft wat de volgorde moet zijn. 

`print(5+3*2)` zal dus niet dezelfde uitkomst bekomen als `print((5+3)*2)`.

In de eerste oefening gebruikten we de print() functie om de tekst ‘hello world’ te tonen. Het hoeven dus niet altijd cijfertjes te zijn!

```python
print("Hello, world!")
```

Naast de `print` functie zijn er nog een aantal andere functies die we zullen leren kennen. Het zijn afgesproken codes, eigen aan Python, die iedere programmeur moet leren. 
Als je het makkelijker vindt, mag je deze codes zeker op een blaadje opschrijven en bijhouden doorheen de oefeningen van Dodona. 

Je kunt meerdere woorden, zinnen of cijfers tegelijkertijd laten zien met een `print()` functie, door alles wat je wilt laten zien tussen de haakjes te zetten, met komma’s ertussen. De print() functie laat dan al die items zien, met spaties ertussen.

Stel nu dat je graag het zinnetje “ Ik heb twee appels en een banaan.” wil laten verschijnen in Dodona. Dan kan je de `print()` functie gebruiken als volgt:

```python
print( "Ik", "heb", "twee", "appels", "en", "een", "banaan" )
```

OF 

```python
print( "Ik heb twee appels en een banaan")
```

#### Merk op:
1. Spaties tellen mee en worden ook getoond. Als je de spaties zou weglaten, dan zou de zin moeilijk leesbaar zijn. 

2. Let op: Dodona is hoofdlettergevoelig. ‘Print’ zal niet herkend worden, ‘print’ zal wel herkend worden. 

3. Wanneer je woorden wil tonen met de print() functie moeten die steeds tussen dubbele of enkele aanhalingstekens geplaatst worden. Je mag kiezen. In het vorige voorbeeld gebruiken ze dubbele haakjes. Het is wel **belangrijk** dat je twee keer hetzelfde gebruikt. De volgende code: `print('appel")` zal niet juist gerekend worden (en dus een foutmelding geven) omdat je eerst een enkel aanhalingsteken gebruikt en daarna een dubbel. Daarnaast is het ook **belangrijk** om rekening te houden met welke tekst/cijfers je wil tonen. Stel dat je de volgende zin wil tonen: Lisa’s nieuwe auto is blauw. Dan kies je best voor dubbele haakjes, omdat de computer anders in de war zal zijn met het enkele haakje dat jouw zin bevat. In dat geval zal je code er dus als volgt uitzien: `print("“Lisa’s nieuwe auto is blauw”")`.