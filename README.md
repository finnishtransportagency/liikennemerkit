![Väyläviraston logo](https://vayla.fi/documents/25230764/35412219/vayla_sivussa_fi_sv_rgb.png)
# Suomen liikennemerkit QGIS-kuvakirjastona (BETA)
[See below for summary in English](https://github.com/finnishtransportagency/liikennemerkit#summary-in-english)

### Sisältö
Tässä repositoriossa on SVG-vektorikuvina Suomen maanteillä käytössä olevat liikennemerkit. Kokoelmissa ovat aiemmat ja uuden tieliikennelain myötä 1.6.2020 voimaantulleet merkit sekä näiden visualisoinnissa QGIS:ssä auttava prosessointiskripti. Liikennemerkit on nimetty ne yksilöivällä koodilla: tarkempaa tietoa kustakin merkistä saa [Väyläviraston verkkosivuilta](https://vayla.fi/tieverkko/liikennemerkit). Kokoelmat sisältävät kaikki saatavilla olevat kuvat variaatioineen, jotka on erotettu kantamerkeistä alaviivoilla tai pisteillä (esim. *A3.2_9.svg*). Lisäksi uuteen kokoelmaan on lisätty joistakin merkeistä (kuten nopeusrajoitus- ja tienumeromerkit) tyhjät pohjat, joista on poistettu vapaasti vaihtuvat numerot. Tyhjät versiot on nimetty esimerkiksi näin: *C32_blanko.svg*. Tämä julkaisu on betatestausvaiheessa ja sen yksityiskohdat voivat vielä muuttua. Ohjeet [palautteen ja kehitysehdotusten antamiseksi alla](https://github.com/finnishtransportagency/liikennemerkit#palaute).

### Käyttöönotto QGIS 3 -ohjelmassa
Kirjasto on räätälöity käytettäväksi QGIS-paikkatieto-ohjelmassa, jossa sillä voi visualisoida esimerkiksi [Digiroadin](https://vayla.fi/avoindata/digiroad) tai tierekisterin (saatavilla [Väyläviraston latauspalvelun](https://julkinen.vayla.fi/oskari/) kautta) tarjoamia liikennemerkkien sijaintipisteitä. Merkit ladataan QGIS:iin [Resource sharing](http://qgis-contribution.github.io/QGIS-ResourceSharing/) -nimisen laajennoksen (plugin) kautta.

1. Asenna Resource sharing QGIS:n laajennosjakelusta (*Plugins* > *Manage and install plugins*).
2. Avaa Resource sharing (*Plugins* > *Resource sharing*). Plugin näyttää listauksen saatavilla olevista kokoelmista. Näiden joukossa on kolme *Väylävirasto...*-alkuista kokoelmaa. Voit rajata kokoelmia myös yläosan hakupalkista.
3. Asenna haluamasi kokoelmat.

### Kirjastojen käyttö
Pistemuotoiset datat voi visualisoida SVG-kuvilla avaamalla tason symbologian ja asettamalla symbolityypiksi *SVG marker*. Liikennemerkit ovat valikon alaosassa (*SVG Groups*/*SVG Image*).

Jos pisteissä on Digiroadin tapaan attribuuttitietona, mitä merkkiä ne esittävät, ne voi visualisoida automaattisesti oikealla merkillä merkkityyliskriptillä. Avaa skripti työkaluvalikosta (*Processing*>*Toolbox*), jossa sen on *Scripts* alavalikon alla (*Finnish traffic sign stylizer*). Valitse skriptin parametrit:
1. Käytätkö vanhoja vai uusia liikennemerkkejä.
2. Pistemuotoinen taso (esimerkiksi Digiroadin liikennemerkkipisteet).
3. Sarake, jossa kolminumeroiset merkkikoodit ovat. Esimerkiksi Digiroadissa tämä on *TYYPPI* ja tierekisterin tietolajissa 506 *S_UUSIASNR*.
4. *Vapaavalintainen*. Jotta nopeusrajoitusmerkeissä näkyisivät oikeat luvut, valitse sarake, jossa tämä tieto on. DR:ssa sarake *ARVO* ja tierekisterissä *LMTEKSTI*.
5. Skripti voi myös asettaa kuvat skaalautumaan karttanäkymän mittakaavan mukaan. 

Jos kaikki menee kuten pitää, pisteet korvautuvat välittömästi oikealla merkeillä karttaikkunassa. Jos kuvapisteissä näkyy vain mustia kysymysmerkkejä, varmista valitseesi oikean tason ja sarakkeet.

### Käyttöehdot
Liikennemerkkikuvat jaetaan avoimena datana ilman muita vaatimuksia (CC0). Lue lisää lausumasta [Creative Commonsin verkkosivuilla](https://creativecommons.org/publicdomain/zero/1.0/deed.fi).

### Palaute
Kehitysehdotuksia tai bugi-ilmoituksia, ruusuja tai risuja? Lähetä ne osoitteeseen paikkatieto(ät)vayla.fi tai avaa uusi keskustelu tämän repositorion *Issues*-välilehdellä.

### Summary in English
This repository houses SVG image libraries of Finnish road traffic signs (read more on the signs [here](https://vayla.fi/en/transport-network/traffic-signs)). The images are identified by a unique letter-numeral code and variations are separated by underscores and points (e.g. *A3.2_9.svg*) The libraries are mostly untouched, but a new blank variation has been included for some signs containing dynamic elements, like road numbers. These are have their own identifier: *C32_blanko.svg*. The libraries can be imported to QGIS using the [Resource sharing plugin](http://qgis-contribution.github.io/QGIS-ResourceSharing/). The collections also include a prosessing script for easily visualizing a point layer with the images.

The image data is provided by Finnish Transport Infrastructure Agency and is shared under CC0. Read more on the deed [here](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
