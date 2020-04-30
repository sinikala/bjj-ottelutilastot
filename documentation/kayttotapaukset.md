# Tulospalvelu brasilialaisen jujutsun -otteluille
Käyttäjä voi palvelun avulla tarkastella toteutuneiden BJJ-otteluiden tuloksia sekä otelleiden ottelijoiden tulosten kannalta oleellisia tietoja, kuten vyötaso ja kotiseura.

Palvelu kertoo otteluista seuraavat tiedot: aika, paikka, ottelijat,heidän vyötasonsa, voittaja ja voittotyyppi (luovutus-, pistevoitto tai tuomarin päätös). Mikäli ottelu on päättynyt pistevoitolla, näytetään myös kyseisen ottelun lopulliset pisteet.

Tulostilastoja voi rajata eri ominaisuuksien, kuten seura, voittotyyppi tai ottelija perusteella. Myös ottelijoita voi hakea esim. seuran perusteella ja tarkastella kunkin ottelijan henkilökohtaisia tilastoja.

Kirjautunut käyttäjä voi lisätä palveluun uusia otteluita tuloksineen sekä uusia ottelijoita ja muokata tietoja. 

## Käyttötapaukset ja niihin liittyvät SQL-kyselyt:

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

- nähdä yksittäisestä ottelusta ottelun päivämäärän, paikan, osallistujat, voittajan, ottelussa tehdyt pisteet, mikäli kysessä pisteillä voitettu ottelu ja voittotyypin sekä mahdollisen moderaattorin kommentin
  
   Toteutuu yllä olevilla kyselyillä. 

- rajata ottelulistaa seuran, ottelijan tai voittotyypin perusteella
  
  Esimerkiksi kun käytetään kaikkia kolmea filteriä:
  ```
    SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE match.winning_category=?"
                  + " AND fighter.club=:?"
                  + " AND fighter.belt=?"
                  + " ORDER BY match.date DESC;
  ```

  
- nähdä listan kaikista palveluun lisätyistä ottelijoista
    Ottelijan perustiedot
    ``` 
    SELECT * FROM Fighters;
    ``` 
    
- tarkastella yksittäisen ottelijoiden tietoja, jotka sisältävät ottelijan nimen, vyötason, painon, otteluiden ja voittojen määrän sekä kotiseuran

    ``` 
    SELECT * FROM Fighters
                WHERE id=?;
    ``` 
    Ottelut
    ```
    SELECT COALESCE((SELECT COUNT(*) FROM matchfighter"
                    " WHERE fighter_id = ?),0);
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
                VALUES (?, ?, ?);
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
        INSERT INTO Match (date, place, winning_category, winner_id, creator_id, comment) 
                VALUES (?,?,?,?,?,?);
        ```
        Lisäksi liitetään ottelijat otteluun ja tarvittaessa lisätään pisteet
        ```
        INSERT INTO matchfighter (match_id, fighter_id) VALUES (?,?);
        ```

        ```
        INSERT INTO points (points, penalties, advantage, fighter_id)
                VALUES (?,?,?,?)
        ```
        ```
        INSERT INTO matchpoints (match_id, points_id) VALUES (?,?);
        ```

     - lisätä ottelijan palveluun
        ```
        INSERT INTO Fighter (name, born, belt, club, weight, creator_id) 
                VALUES (?,?,?,?,?,?);
        ```
     - muokata palvelussa olevan ottelun pisteet
         ```
         UPDATE Points 
                SET points= ?, penalties=?, advantage=? 
                WHERE Points.id = ?;
         ```   
     - vaihtaa palvelussa olevan ottelun voittajan
        ```
         UPDATE Match 
                SET winner_id= ?  
                WHERE Match.id = ?;
         ``` 
     - muokata palvelussa olevan ottelijan tietoja
        ```
         UPDATE Fighter 
                SET name=?, born=?, belt=?, club=?, weight=?? 
                WHERE Fighter.id = ?;
         ``` 
     - poistaa ottelun
        ```
        DELETE FROM Match
                WHERE Match.id=?;
        ```
        tarvittaessa samalla poistetaan otteluun liittyneet pisteet:
        ```
        DELETE FROM matchpoints
                WHERE Match.id=?;
        ```
        ```
        DELETE FROM Points
                WHERE Points.id=?;
        ```
     - poistaa ottelijan
        ```
        DELETE FROM Fighter
                WHERE Fighter.id=?;
        ```



### Jatkokehitysideoita:
- Otteluiden listaukseen tieto painoluokasta
- Lisää haku-/rajausominaisuuksia
- Mahdollisuus muokata kaikkia ottelun tietoja
- Sivuttaminen käyttöön listausnäkymissä.