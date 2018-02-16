---
title: CodeCraft
level: Python 2
language: hr-HR
stylesheet: python
embeds: "*.png"
materials: ["project-resources/codecraft/*.*", "volunteer-resources/codecraft-finished/*.*"]
...

# Uvod { .intro}

U ovom projektu dizajnirat ćeš i kodirati poboljšanja za 2D verziju igrice Minecraft.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ac3995d69?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="craft-finished.png">
</div>

# Korak 1: Igranje igre { .activity}

## Zadatci { .check}

+ Otvori ovaj trinket: <a href="http://jumpto.cc/codecraft-go" target="_blank">jumpto.cc/codecraft-go</a>. Ako čitaš ovo online, možeš koristiti i ugrađenu verziju ovog trinketa koja se nalazi ispod.

<div class="trinket">
<iframe src="https://trinket.io/embed/python/fdd32064f8?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

+ Koristi tipke W, A, S i D za pomicanje igrača po svijetu, koji je prepun različitih elemenata (zemlje, trave i vode).

    ![screenshot](craft-move.png)

+ Pritisni razmaknicu kako bi sakupio element. Pokupi nekoliko komada od svakog elementa i vidjet ćeš da su dodani tvom inventaru.

    ![screenshot](craft-pickup.png)

+ Pritisni brojeve od 1 do 3 za postavljanje elementa na mapu. Primjerice, pritisni 3 da bi na mapu stavio vodu. Ovo će funkcionirati samo ako imaš vodu u svom inventaru.

    ![screenshot](craft-place-water.png)

+ Možeš izraditi element tako da pritisneš tipku prikazanu u izborniku. Izrađivanje znači spajanje elemenata koje već imaš u inventaru kako bi napravio nove elemente. Pokušaj pritisnuti tipku 'r' kako bi izradio novu ciglu (to je moguće samo ako imaš barem 2 zemlje i 1 vodu u inventaru).

    ![screenshot](craft-craft-brick.png)

+ Zatim pritisni tipku '4' da postaviš cigle koje si izradio.

    ![screenshot](craft-place-brick.png)

## Spremi projekt {.save}

## Izazov: Izgradi svoj svijet {.challenge}
Možeš li izgraditi kuću sa vrtom i bazenom? Što još možeš stvoriti?

![screenshot](craft-build-example.png)

## Spremi projekt {.save}

# Korak 2: Prilagodba igre { .activity}

Izmijenimo neke od varijabli kako bi promijenili način na koji igra funkcionira.

+ Klikni na datoteku `variables.py` kako bi pogledao neke od varijabli koje se mogu izmijeniti.

    ![screenshot](craft-variables.png)

+ Promijeni vrijednost varijable `BACKGROUNDCOLOUR` pa klikni na 'Run' da bi vidio promjene.

    ![screenshot](craft-background.png)

+ Varijabla `MAXTILES` predstavlja količinu svakog elementa koji se može nalaziti u tvom inventaru. Izmijeni ovu varijablu ako želiš da se u tvom inventaru pohranjuje više (ili manje) od 20 komada svakog elementa.

    ![screenshot](craft-maxtiles.png)

## Izazov: Promijeni veličinu svog svijeta { .challenge}
Možeš li promijeniti vrijednosti varijabli `MAPWIDTH` i `MAPHEIGHT` da bi promijenio veličinu svog svijeta?

![screenshot](craft-mapsize.png)

## Spremi projekt {.save}

# Korak 3: Stvori novi element - drvo! { .activity}

Stvorimo novi element - drvo! Da bi to napravili, moramo dodati još neke varijable u datoteku `variables.py`.

+ Prvo moraš odabrati broj za svoj novi element. Tada ćeš, umjesto broja 4, moći koristiti riječ `WOOD` (drvo) u kôdu.

    ![screenshot](craft-wood-const.png)

+ Dodaj novi element `WOOD` na svoju listu `resources`.

    ![screenshot](craft-wood-resources.png)

+ Također moraš svom elementu dati naziv koji će se prikazivati u inventaru.

    ![screenshot](craft-wood-name.png)

    Primijeti da se na kraju linija nalazi zarez `,`.

+ Tvoj element trebat će i sliku. U projektu se već nalazi slika pod nazivom `wood.png` koju ćeš dodati u rječnik naziva `textures`.

    ![screenshot](craft-wood-texture.png)

+ Za početak, u rječnik `inventory` dodaj broj koji si pridružio elementu.

    ![screenshot](craft-wood-inventory.png)

+ Konačno, dodaj tipku kojom ćeš postaviti drvo u svijet.

    ![screenshot](craft-wood-placekey.png)

+ Pokreni i testiraj projekt. Vidjet ćeš da sada imaš novi element 'wood' u svom inventaru.

    ![screenshot](craft-wood-test.png)

+ U tvom svijetu nema drva! Popravi to tako da odabereš datoteku `main.py` i pronađeš funkciju `generateRandomWorld()`.

    ![screenshot](craft-wood-random1.png)    

    Ovaj kôd nasumično generira broj između 0 i 10, a dobiveni broj odlučuje koji element će se postaviti u svijet:

    + 1 ili 2 = voda
    + 3 ili 4 = trava
    + bilo što drugo = ZEMLJA

+ Unesi sljedeći kôd za dodavanje drva u svoj svijet svaki put kada je `randomNumber` 5.

    ![screenshot](craft-wood-random2.png)

+ Ponovno testiraj projekt. Ovoga bi se puta drvo trebalo pojaviti u tvom svijetu.

    ![screenshot](craft-wood-test2.png)

## Izazov: Stvori pijesak { .challenge}
Možeš li dodati element `SAND` (pijesak) u igru? Za pomoć pogledaj korake iznad.

![screenshot](craft-sand.png)

U projektu se već nalazi slika `sand.png`, ali možeš stvoriti i prenijeti vlastitu ako želiš.

![screenshot](craft-upload.png)

## Spremi projekt {.save}

# Korak 4: Izradi daske od drva { .activity}

Napravimo novi element, dasku, koji se može izraditi od drva.

+ Prvo dodajmo igri novu varijablu `PLANK` (daska).

    ![screenshot](craft-plank-const.png)

+ Dodaj igri novu varijablu `PLANK`.

    ![screenshot](craft-plank-resources.png)

+ Nazovi element `'plank'`.

    ![screenshot](craft-plank-names.png)

+ Pridruži elementu `PLANK` sliku. U projektu se već nalazi slika `plank.png`, ali možeš dodati svoju ako želiš.

    ![screenshot](craft-plank-textures.png)

+ Dodaj daske u svoj inventar.

    ![screenshot](craft-plank-inventory.png)

+ Odredi kojom tipkom će se daske postavljati u svijet.

    ![screenshot](craft-plank-placekeys.png)

+ S obzirom da je ovo element koji može biti izrađen od drugih elemenata, moraš utvrditi po kojim pravilima može biti izrađen. Neka pravilo bude da se daska može izraditi od 3 komada drveta. Dodaj ovaj kôd u svoj `crafting` rječnik.

    ![screenshot](craft-plank-crafting.png)

+ Na kraju, moraš odrediti kojom tipkom će se izrađivati nove daske.

    ![screenshot](craft-plank-craftkeys.png)

+ Testiraj svoj novi element dasku. Sakupi nekoliko komada drveta i od njih izradi daske. Zatim postavi svoje nove daske u svijet.

    ![screenshot](craft-plank-test.png)

## Spremi projekt{.save}

## Izazov: Izradi staklo od pijeska { .challenge}
Možeš li stvoriti novi element staklo koje se može izraditi od pijeska? Za pomoć pogledaj korake iznad.

![screenshot](craft-glass.png)

U projektu se već nalazi slika `glass.png` koju možeš koristiti ili stvori vlastitu sliku ako želiš.

## Spremi projekt {.save}

## Izazov: Stvori još elemenata { .challenge}
Možeš li svojoj igri dodati još elemenata i pravila za izrađivanje?

## Spremi projekt {.save}
