![Väyläviraston logo](https://vayla.fi/documents/20473/740592/vayla_sivussa_fi_sv_rgb.png)
# Suomen liikennemerkit QGIS-kuvakirjastona
[See below for English summary](https://github.com/finnishtransportagency/liikennemerkit#english-summary)

Tässä repositoriossa on SVG-vektorikuvina Suomen maanteillä käytössä olevat liikennemerkit. Kokoelmissa ovat nykyiset ja uuden tieliikennelain myötä 1.6.2020 voimaantulevat merkit sekä näiden visualisoinnissa QGIS:ssä auttava prosessointiskripti. Liikennemerkit on nimetty ne yksilöivällä koodilla: tarkempaa tietoa kustakin merkistä saa [Väyläviraston verkkosivuilta](https://vayla.fi/tieverkko/liikennemerkit)

### Käyttöönotto QGIS 3 -ohjelmassa
Kirjasto on tarkoitettu käyttöön QGIS-paikkatieto-ohjelmassa, jossa sillä voi visualisoida esimerkiksi [Digiroadin](https://vayla.fi/avoindata/digiroad) tai tierekisterin (saatavilla [Väyläviraston latauspalvelun](https://julkinen.vayla.fi/oskari/) kautta) tarjoamia liikennemerkkien sijaintipisteitä. Merkit ladataan QGIS:iin [Resource sharing](http://qgis-contribution.github.io/QGIS-ResourceSharing/) -nimisen laajennoksen (plugin) kautta.

1. Asenna Resource sharing QGIS:n laajennosjakelusta (*Plugins* > *Manage and install plugins*).
2. Avaa Resource sharing (*Plugins* > *Resource sharing*). Plugin näyttää listauksen saatavilla olevista kokoelmista. *HUOM. Testivaiheessa nämä kokoelmat eivät tule vielä automaattisesti näkyviin, vaan lähde pitää määritellä. Lopullisessa versiossa kohtia 3-5 ei tarvita.*
3. Valitse vasemmanpuoleisesta valikosta välilehti *Settings*.
4. Lisää uusi repositorio (*Add repository*). Aseta nimeksi **Liikennemerkit** ja osoitteeksi https://github.com/finnishtransportagency/liikennemerkit.git
5. Ohjelma ilmoittaa asennuksen onnistuneen. Palaa *All collections* välilehdelle.
6. Saatavilla on nyt kolme kokoelmaa, jotka alkavat nimellä *Väylävirasto*. Asenna haluamasi kokoelmat.

### Kirjastojen käyttö
Pistemuotoiset datat voi visualisoida SVG-kuvilla avaamalla tason symbologian ja asettamalla symbolityypiksi *SVG marker*. Liikennemerkit ovat valikon alaosassa (*SVG Groups*/*SVG Image*).

Jos pisteissä on Digiroadin tapaan attribuuttitietona, mitä merkkiä ne esittävät, ne voi visualisoida automaattisesti oikealla merkillä merkkityyliskriptillä. Avaa skripti työkaluvalikosta (*Processing*>*Toolbox*), jossa sen on *Scripts* alavalikon alla (*Finnish traffic sign stylizer*). Valitse skriptin parametrit:
1. Käytätkö vanhoja vai uusia liikennemerkkejä.
2. Pistemuotoinen taso (esimerkiksi Digiroadin liikennemerkkipisteet).
3. Sarake, jossa kolminumeroiset merkkikoodit ovat. Digiroadissa tämä on *TYYPPI* ja tierekisterissä *ASETUSNR*.
4. *Vapaavalintainen*. Jotta nopeusrajoitusmerkeissä näkyisivät oikeat luvut, valitse sarake, jossa tämä tieto on. DR:ssa sarake *ARVO* ja tierekisterissä *LMTEKSTI*.

Jos kaikki menee kuten pitää, pisteet korvautuvat välittömästi oikealla merkeillä karttaikkunassa. Jos kuvapisteissä näkyy vain mustia kysymysmerkkejä, varmista valitseesi oikean tason ja sarakkeet.

### Käyttöehdot
Liikennemerkkikuvien lisenssi on CC 4.0 BY. Lue lisää lisenssistä [Creative Commonsin verkkosivuilla](http://creativecommons.org/licenses/by/4.0/) ja Väyläviraston [avoimen datan käyttöehdoista](https://vayla.fi/avoindata/kayttoehdot).

### English summary
This repository houses SVG image libraries of Finnish road traffic signs (read more on the signs [here](https://vayla.fi/web/en/road-network/traffic-signs)). The libraries can be imported to QGIS using the [Resource sharing plugin](http://qgis-contribution.github.io/QGIS-ResourceSharing/). The collections also include a prosessing script for easily visualizing a point layer with the images.

The image data is provided by Finnish Transport Infrastructure Agency and is shared under CC 4.0 BY. Read more on the license [here](http://creativecommons.org/licenses/by/4.0/).
