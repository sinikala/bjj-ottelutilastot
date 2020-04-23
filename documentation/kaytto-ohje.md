# Sovelluksen asennus- ja käyttöohjeet
# Asennus

1. Paikallisesti
    - Lataa sovellus osoitteesta https://github.com/sinikala/bjj-ottelutilastot.
    - Tarvitset tuen Python-kielisten ohjelmien suorittamiseen, vähintään Pythonin versio 3.5. 
     - Kaikki sovelluksen riippuvuudet löytyvät tiedostosta 'requirements.txt'. Asenna ne. Asentamiseen tarvitset pip-paketinhallintatyökalun Pythonille. Tämä asentuu yleensä automaattiseti Pythonin mukana. Lisäksi suositellaan, että käytössä on Pythonin virtuaalinen ympäristö (kuten venv) asennettaessa riippuvuuksia. 
    -Suorita komento `python3 run.py` projektin juuressa.
    Sovelluksen pitäisi nyt käynnistyä ja pääset tarkastelemaan sitä menemällä selaimellasi osoiteeseen `localhost:5000`


2. Herokussa
    - Varmista, että kaikki toimii paikallisesti.
    - Käytössäsi tulee olla herokun komentorivityökalu  [heroku-cli][https://devcenter.heroku.com/articles/heroku-cli].
    - Heroku käyttää palvelimen käynnistämisessä [Gunicorn][http://gunicorn.org/]-palvelinta. Asenna se. 
    - Luo Heroku-sivu komennolla `heroku create "sovelluksen-nimi"`
    - Lisätään sovelluksen käyttöön tieto siitä, että sovellus on Herokussa: `heroku config:set HEROKU=1`
    - Lisätään Herokuun sovellukselle tietokanta: `heroku addons:add heroku-postgresql:hobby-dev` 
    - Lopuksi lisää vielä paikalliseen versionhallintaan tieto Herokusta: `git remote add heroku https://git.heroku.com/<sovelluksen-nimi>.git` ja 'pushaa' projekti Herokuun: `git push heroku master`.



# Käyttö

Sovelluksen peruspalveluja voi käyttää kuka tahansa.
Sovelluksen jokaisen sivun yläpalkista löydät linkit kaikkiin käytössäsi oleviin palveluihin. 

## 1. Kaikille käytössä olevat palvelut
### Otteluiden tarkastelu

**Ottelut**-sivulla näet listauksen kaikista palveluun tallennetuista otteluista.

### Otteluiden rajaus

Tulossa:

Voit rajata tuloksia valitsemalla listauksen yläreunassa näkyvistä rajausehdoista mieleiset ja painamalla 'hae'. Filtterit voi nollata napista 'nollaa'.

### Ottelijoiden tarkastelu

**Ottelijat**-sivulla näet listauksen kaikista palveluun tallennetuista ottelijoista.

### Ottelijoiden rajaus

Tulossa: 

Voit rajata tuloksia valitsemalla listauksen yläreunassa näkyvistä rajausehdoista mieleiset ja painamalla 'hae'. Filtterit voi nollata napista 'nollaa'.

### Yksittäisen ottelijan tarkastelu

Painamalla *Ottelijat*-sivullla yksittäisen ottelijan kohdalta 'profiili'-nappia, pääset tarkastelemaan hänen tarkempia tietojaan. 'Takaisin' napista pääset takaisin listaukseen.



## 2a.Moderaattoreiden käytössä olevat palvelut
### Rekisteröityminen

Mikäli mielit tulospalvelun moderaattoriksi, tulee sinun luoda tunnukset sovellukseen **Rekisteröidy**-sivulla. Käyttäjänimesi on oltava uniikki.
Voidaksesi rekisteröityä moderaattoriksi tarvitset rekisteröitymisavaimen, jonka saat aiemmilta moderaattoreilta. (`berimbolo`)

Rekisteröitymisen jälkeen ohjaudut suoraan sisäänkirjautumisnäkymään.

### Kirjautuminen & uloskirjautuminen

Löydät linkin sisään- ja uloskirjautumiseen aina sivun oikeasta yläreunasta

## 2b. Moderaattoreiden sisäänkirjautumista edellyttävät palvelut

### Ottelijan lisäys

**Lisää ottelija** -sivulla

### Ottelun lisäys

**Lisää ottelu**-sivulla
otteluun liittyvät ottelijat tulee lisätä palveluun ennen ottelun lisäystä

### Voittajan muokkaus

### Ottelun poisto

### Ottelijan poisto

### Ottelijan muokkaus


    