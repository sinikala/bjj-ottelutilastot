### Tulospalvelu brasilialaisen jujutsun -otteluille
Käyttäjä voi palvelun avulla tarkastella toteutuneiden BJJ-otteluiden tuloksia sekä otelleiden ottelijoiden tulosten kannalta oleellisia tietoja, kuten vyötaso ja kotiseura.

Palvelu kertoo otteluista seuraavat tiedot: aika, paikka, ottelijat, ottelutaso (valko-/väri-/mustavöiset), painoluokka, voittaja ja voittotyyppi (luovutus-, pistevoitto tai tuomarin päätös). Mikäli ottelu on päättynyt pistevoitolla, näytetään myös kyseisen ottelun lopulliset pisteet.

Tulostilastoja voi rajata eri ominaisuuksien, kuten seura, voittotyyppi tai ottelija. Myös ottelijoita voi hakea esim. seuran perusteella ja tarkastella kunkin ottelijan henkilökohtaisia tilastoja.

Kirjautunut käyttäjä voi lisätä palveluun uusia otteluita tuloksineen sekä uusia ottelijoita ja muokata tietoja. 

### Käyttötapaukset ja niihin liittyvät SQL-kyselyt:

**Käyttäjä voi ...** 

- tarkastella listaa palveluun tallennetuista otteluista
    ``` 
    SELECT * FROM MATCH;
    ```
    Ottelijoiden nimet haetaan Fighters-taulusta
    ```
    SELECT id, name FROM Fighter 
                LEFT JOIN matchfighter ON matchfighter.fighter_id = Fighter.id
                WHERE matchfighter.match_id = ?;
    ```

    Lisäksi otteluille, jotka päättyivät pistevoitoon, täytyy hakea pisteet.
    ``` 
    SELECT points, penalties, advantage FROM Points 
                LEFT JOIN matchpoints ON matchpoints.points_id = Points.id 
                WHERE matchpoints.match_id = ?;
    ```

- nähdä yksittäisestä ottelusta ottelun päivämäärän, paikan, osallistujat, voittajan, ottelussa tehdyt pisteet, mikäli kysessä pisteillä voitettu ottelu(*) ja voittotyypin sekä mahdollisen moderaattorin kommentin
  
   Toteutuu yllä olevilla kyselyillä. 

- rajata ottelulistaa seuran, ottelijan tai voittotyypin perusteella (TULOSSA)
  
- nähdä listan kaikista palveluun lisätyistä ottelijoista
    Ottelijan perustiedot
    ``` 
    SELECT * FROM Fighters;
    ``` 
    
- tarkastella yksittäisen ottelijoiden tietoja, jotka sisältävät ottelijan nimen, vyötason, painon, otteluiden ja voittojen määrän sekä kotiseuran

    ``` 
    SELECT * FROM Fighters;
    ``` 
    Ottelut
    ```
    SELECT COALESCE((SELECT COUNT(*) FROM Match
                WHERE (fighter1_id = ? OR fighter2_id = ?)),0);
    ```
    Voitot
    ```
    SELECT COALESCE((SELECT COUNT(*) FROM Match
                WHERE winner_id = ?),0);
    ```
 - rajata ottelijalistassa näkyviä ottelijoita nimen, kotiseuran tai vyötason perusteella
    
    Nimen perusteella
    ```
    SELECT * FROM FIGHTER
                WHERE name LIKE %<olliottelija>%;
    ```
    Vyön ja kotiseuran perusteella
    ```
    SELECT * FROM Fighter
                WHERE club=?
                AND belt=?;
    ```

 - rekisteröityä moderaattoriksi, eli luoda käyttäjätunnukset, mikäli hän tietää rekisteröitymiseen vaadittavan avaimen.
    ```
    INSERT INTO account (name, username, password) 
                VALUES ('Allu Admin', 'root', 'secret');
    ```
 
**Moderaattori, eli kirjautunut käyttäjä, voi ...**
    
 - kirjautua sisään omalla käyttäjänimellä ja salasanallaan
    ```
    SELECT * FROM account
                WHERE username =?
                AND password =?;
    ```

 -  ...**sisäänkirjatuneena** ... 
     - lisätä ottelun palveluun
         ```
        INSERT INTO Match (date, place, winning_category, fighter1_id, fighter2_id, winner_id, creator_id, comment) 
                VALUES ('?', '?', '?','?','?', '?','?', '?');
    ```
    Lisäksi liitetään ottelijat otteluun ja tarvittaessa lisätään pisteet
    

     - lisätä ottelijan palveluun
     - muokata palvelussa olevan ottelun tietoja
     - muokata palvelussa olevan pttelijan tietoja
     - poistaa ottelun
     - poistaa ottelijan


(*) Brasialialaisessa jujutsussa pisteet ilmoitetaan tuloksissa vain, mikäli ottelu on päättynyt pistevoittoon, eli tilanteessa, jossa kumpikaan ottelija ei ole ennen otteluajan loppumista luovuttanut tai tuomari ei ole päättänyt ottelua. Jos ottelu on päättynyt luovutukseen (lukko, kuristus, tajuttomuus) tai tuomarin päätökseen (keskeytys, diskaus) ei siihen mennessä kertyneillä pisteillä ole väliä.

Pisteiden luku: 0|-1|1 - 3|0|0

ottelijan 1 pisteet|rangaistuspisteet|etu(pisteet) - ottelijan 2 pisteet|rangaistuspisteet|etu(pisteet)

Voiton ratkaisevat ensisijaisesti pisteet, tasatilanteessa etupisteet, etupisteiden tasatilanteessa rangaistuspisteet.
