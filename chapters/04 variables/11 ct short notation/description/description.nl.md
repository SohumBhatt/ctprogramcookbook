Laat ons even samenvatten welke functies we ondertussen al tegengekomen zijn: 

`print()` → de functie om iets te tonen/printen

`=`       → de functie om iets op te slaan onder een ander getal/cijfer (de variabele) 

`+`         → de functie om iets op te tellen

`-`         → de functie om iets af te trekken

`*`         → de functie om iets te vermenigvuldigen

`/`         → de functie om iets te delen


Wist je dat bovenstaande functies ook te combineren zijn? Dit zullen we leren door kennis te maken met “verkorte notaties”. 
De eerste verkorte notatie die we zullen leren is een combinatie van `+` en `=` namelijk: `+=`
Met `+=` kan je iets optellen bij de waarde die opgeslagen is onder de variabele. Dit klinkt heel ingewikkeld, maar dat is het niet! 
Het kan simpel uitgelegd worden aan de hand van het volgende voorbeeld: 

```python
aantal_bananen = 100
aantal_bananen = aantal_bananen + 1
print( aantal_bananen )
```

`101`

is hetzelfde als:

```python 
aantal_bananen = 100
aantal_bananen += 1
print( aantal_bananen )
```

`101`

In het bovenste stukje code werd geen ‘verkorte notatie’ gebruikt. In het onderste stukje code werd wel een ‘verkorte notatie’ gebruikt, namelijk `+=` in de tweede regel.

Als je iets wilt optellen bij een variabele, kun je dus `+=` gebruiken, met de variabele aan de linkerkant en wat je erbij 
op wilt tellen aan de rechterkant. Dit bespaart de moeite van het twee keer typen van de variabele naam, en maakt je code over het algemeen leesbaarder
(omdat programmeurs ervan uitgaan dat je de `+=` gebruikt als je ergens iets bij wilt optellen).

Op vergelijkbare manier kun je `-=` gebruiken om iets af te trekken van een variabele, `*=` voor vermenigvuldiging, `/=` voor deling, ... 

Andere voorbeelden waarin ‘verkorte notaties’ gebruikt worden zijn:

``` python
aantal_bananen = 100


aantal_bananen += 12
aantal_bananen -= 13
aantal_bananen *= 19
aantal_bananen /= aantal_bananen
```
