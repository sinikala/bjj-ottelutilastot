# bjj-ottelutilastot

### Huom!
Sovelluksen ollessa tällä hetkellä ikävästi välivaiheessa, voi sen CUD-toiminnallisuuksia testata vain paikallisesti. Tämä vaatii käyttäjän luomista suoraan tietokantaan sqlitellä esimerkiksi näin:
```
INSERT INTO account (name, username, password) VALUES ('Antti Admin', 'root', 'salainen');
```
Tämä jälkeen voit kirjautua sovelluksessa normaalisti
WIP...


### Tulospalvelu brasilialaisen jujutsun -otteluille
Käyttäjä voi palvelun avulla tarkastella toteutuneiden BJJ-otteluiden tuloksia sekä otelleiden ottelijoiden tulosten kannalta oleellisia tietoja, kuten vyötaso ja kotiseura.

Palvelu kertoo otteluista seuraavat tiedot: aika, paikka, ottelijat, ottelutaso (valko-/väri-/mustavöiset), painoluokka, voittaja, ottelussa tehdyt pistesuoritukset ja voittotyypin (luovutus-, pistevoitto tai tuomarin päätös)

Tulostilastoja voi rajata eri ominaisuuksien, kuten vyötaso, voittotyyppi tai painoluokka perusteella. Myös ottelijoita voi hakea esim. seuran perusteella ja tarkastella kunkin ottelijan henkilökohtaisia tilastoja.

Kirjautunut käyttäjä voi lisätä palveluun uusia otteluita tuloksineen sekä uusia ottelijoita ja muokata tietoja. 


#### [Käyttötapaukset](./documentation/kayttotapaukset.md)

#### [Tietokannan rakenne](./documentation/tietokanta.md)

#### [Sovellus Herokussa](https://bjj-ottelutilastot.herokuapp.com/)
