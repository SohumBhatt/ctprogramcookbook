### Hoe bekom je een oplossing na het programmeren?

Wist je dat je Python kan gebruiken als een rekenmachine? Het programma kan eenvoudige tekens zoals die hieronder, herkennen!  

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

Je verwacht dat, wanneer je het programma draait (door op de oranje knop te klikken), je de uitkomst 12 zal verkrijgen. Dit is helaas niet het geval. 
Hoe komt dat? Wel, jouw computer weet niet wat er met de cijfertjes en het plusteken moet gebeuren. 

Je moet dus nog iets extra (nl. de opdracht ‘voer de bewerking uit’) toevoegen aan jouw formule. Dit doe je door de ‘print’ code of functie toe te 
voegen als volgt: 

```python
print(5+7)
```

De `print()` functie gebruik je dus door eerst het woord `print`
te typen, gevolgd door een rond openingshaakje, gevolgd door hetgeen je wilt laten uitwerken (in dit geval 5+7), gevolgd door een rond sluithaakje. 
Je kan in Python, net zoals met een echt rekenmachine ook verschillende tekens in één bewerking vragen. Maar dan zal python, 
opnieuw net zoals bij een echt rekenmachine, geen rekening houden met de volgorde, tenzij je expliciet met haakjes aangeeft wat de volgorde moet zijn. 

`print(5+7+(6*7))` zal dus niet dezelfde uitkomst bekomen als `print(5+7+6*7)`.

In de eerste oefening gebruikten we de print() functie om de tekst ‘hello world’ te printen. Het hoeven dus niet altijd cijfertjes te zijn!

```python
print("Hello, world!")
```

Naast de `print` functie zijn er nog een aantal andere functies die we zullen leren kennen. Het zijn afgesproken codes die Python kent en dus iedere programmeur moet leren. 
Als je het makkelijker vindt, mag je deze codes zeker op een blaadje opschrijven en bijhouden doorheen de oefeningen van Dodona. 

Je kunt meerdere dingen tegelijkertijd laten zien met een `print()` functie, door alles wat je wilt laten zien tussen de haakjes te zetten, met komma’s ertussen. 
De `print()` functie laat dan al die items zien, met spaties ertussen. 

Stel nu dat je graag het zinnetje “Ik heb twee appels en een banaan.” wil laten verschijnen in Dodona. Dan zal je opnieuw de `print()` functie gebruiken als volgt:

```python
print( "Ik", "heb", "twee", "appels", "en", "een", "banaan" )
```

#### Merk op:
1. De spaties tellen mee en worden ook ‘geprint’. Als je de spaties zou weglaten, dan zou de zin moeilijk leesbaar zijn. 

2. Wanneer je woorden wil printen moeten die steeds tussen dubbele of enkele aanhalingstekens geplaatst worden. Je mag kiezen. In het vorige voorbeeld gebruiken ze dubbele haakjes. Het is wel **belangrijk** dat je twee keer hetzelfde gebruikt. De volgende code: `print('appel")` zal niet juist gerekend worden (en dus een foutmelding geven) omdat je eerst een enkel aanhalingsteken gebruikt en daarna een dubbel. 

3. Python zal de getallen nooit afronden. Als je bijvoorbeeld, de code `print( (431 / 100) * 100 )` ingeeft, zal je als antwoord 430.99999999999994 krijgen en niet 431 zoals je zou verwachten. 