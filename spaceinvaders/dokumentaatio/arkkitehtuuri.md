# Arkkitehtuuri
## Rakenne
Koodin pakkausrakenne on seuraavanlainen:

![pakkausrakenne](https://user-images.githubusercontent.com/101888699/165992663-a54020b7-4ad2-495d-81a3-7a8b0f4a85a8.png)

Pakkaus *menu* pitää sisällään pelin päävalikon koodin, pakkaus *space* taas pitää sisällään itsessään pelin koodin, *scores* sisältää tietokantaan liittyvän koodin, *sprites* sisältää pelin hahmojen yms. luokat ja *assets* sisältää näiden hahmojen grafiikat.

## Käyttöliittymä
Käyttöliittymässä on kaksi eri luokkaa:
- Menuloop
- Gameloop

Luokka Menuloop ottaa vastaan pelaajan syötteitä päävalikossa liikkumiselle, ja piirtää valikon tekstit näytölle

Luokka Gameloop vastaa pelaajan syötteistä, aikaansidottujen metodien kutsumisesta ja grafiikkojen piirtämisestä näytölle.

## Sovelluslogiikka
Päävalikon logiikasta vastaa luokka Menu, jonka vastuulla ovat valikon tekstit ja siellä liikkuminen.

Pelin logiikasta vastaa luokka Space ja sen yhteen kokoamat luokat Player, Invader, Pellet ja Item. Luokassa Space on em. neljän luokan käsittelyyn liittyvät metodit. Nämä neljä luokkaa taas vastaavat pelissä näkyvistä objekteista.
![sovelluslogiikka](https://user-images.githubusercontent.com/101888699/165995948-37d7e74e-38e6-4330-a0eb-8e85f87b5edf.png)

Space-luokan metodeista seuraavat vastaavat objektien liikuttamisesta:
- move_player
- move_invaders
- move_pellets
- move_items

Seuraava metodi lisää Pellet-olion:
- shoot_a_pellet
