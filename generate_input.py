#!/usr/bin/env python

from datetime import datetime

import csv
import random

ORGS = [
    "Aikuiskasvatuksen Kilta",
    "Akateeminen kasvintuotantokerho",
    "Bouffe ry",
    "Didacta rf",
    "ELSA Helsinki",
    "Eläinlääketieteen kandidaattiyhdistys EKY ry",
    "Erikeepperi ry",
    "ESN Uni Helsinki",
    "Fibula ry",
    "Foni ry",
    "HAO ry",
    "Historicus r.f.",
    "Humanisticum ry",
    "HYK",
    "ISHA",
    "Kannunvalajat",
    "Kansantaloustieteen opiskelijat ry (KTTO ry)",
    "Karavaani ry",
    "Katharsis ry",
    "Kompleksi ry",
    "Konstruktio ry",
    "Kontakti ry",
    "Konteksti ry",
    "Kotitalouspedagogiopiskelijat ry",
    "Kronos ry",
    "Kumous ry",
    "Käsitys ry",
    "Limes ry",
    "Lipidi ry",
    "Maantieteen opiskelijat ry",
    "Maatalousylioppilaiden yhdistys Sampsa ry",
    "Matematiikan opiskelijaryhmä Matrix ry",
    "Matlu ry",
    "Mythos ry",
    "Myy ry",
    "Peduca ry",
    "Poliittisen historian opiskelijat Polho ry",
    "Resonanssi ry",
    "Setenta ry",
    "Siula ry",
    "Spektrum r.f.",
    "Statsvett rf",
    "Status ry",
    "Stigma ry",
    "SUB ry",
    "Symbioosi ry",
    "Symposion",
    "Synop ry",
    "Taso ry",
    "TKO-äly ry",
    "Umlaut ry",
    "Valta ry",
    "Valtio-opin opiskelijat ry",
    "Vasara r.y.",
    "Viikin taloustieteilijät ry",
    "Viri Lactis ry",
    "Vuorovaikeutus - ympäristöekonomistit ry."
]

EMAILS = [
    "kiia.tyni@helsinki.fi",
    "anja.lammi@helsinki.fi",
    "veera.lohenoja@helsinki.fi",
    "taika.rajala@helsinki.fi",
    "secgen.helsinki@fi.elsa.org",
    "sofia.x.snellman@helsinki.fi",
    "siru.haapamaki@hotmail.com",
    "president@esnunihelsinki.com",
    "maria.e.ahola@helsinki.fi",
    "janna.juslen@helsinki.fi",
    "teresa.heino@helsinki.fi",
    "saga.brummer@helsinki.fi",
    "emma.palojarvi@helsinki.fi",
    "aleksi.n.nieminen@helsinki.fi",
    "atte.koreneff@helsinki.fi",
    "elina.kettunen@kannunvalajat.fi",
    "leon.schnabel@helsinki.fi",
    "henriikka.pelto-timperi@helsinki.fi",
    "hilma.kupiainen@helsinki.fi",
    "sylvia.talikka@helsinki.fi",
    "eveliina.vakevainen@helsinki.fi",
    "arttu.v.manninen@helsinki.fi",
    "vanessa.quednau@helsinki.fi",
    "elli-sofia.polho@helsinki.fi",
    "tuukka.s.korhonen@helsinki.fi",
    "sini.tahvonen11@gmail.com",
    "johanna.niiranen@gmail.com",
    "mikko.pellinen@helsinki.fi",
    "roope.raitanen@helsinki.fi",
    "vilma.kaukavuori@helsinki.fi",
    "lauri.arkkola@helsinki.fi",
    "matrix-hallitus@helsinki.fi",
    "linnea.keltanen@helsinki.fi",
    "siiri.virta@helsinki.fi",
    "sohvi.leminen@helsinki.fi",
    "jonatan.ketonen@helsinki.fi",
    "oona.a.leinonen@helsinki.fi",
    "puheenjohtaja@resonanssi.org",
    "satu.o.rantanen@helsinki.fi",
    "aurora.salmi@helsinki.fi",
    "emil.amnell@helsinki.fi",
    "oscar.suomela@helsinki.fi",
    "milla.hallikas@helsinki.fi",
    "siiri.moisio@helsinki.fi",
    "ainojulia.juvonen@gmail.com",
    "selma.sorri@helsinki.fi",
    "ilias.liimatta@helsinki.fi",
    "jenna.salminen@helsinki.fi",
    "veronika.konnos@helsinki.fi",
    "mila.katajisto@gmail.com",
    "niklas.k.nurminen@gmail.com",
    "amanda.laukkanen@helsinki.fi",
    "janina.orjasniemi@helsinki.fi",
    "max.pettinen@helsinki.fi",
    "katja.lindell@helsinki.fi",
    "andersson.kaisa@gmail.com",
    "oula.rinne@helsinki.fi"
]


def getrandomdate():
    return datetime(2021, random.randint(1, 4), random.randint(1, 28)).strftime("%d.%m.%Y")


def main():
    with open("input.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";", dialect="excel")
        csvwriter.writerow(["organization", "email", "1", "2", "3"])

        for i in range(0, len(ORGS)):
            print("{}: {} ({})".format(i, ORGS[i], EMAILS[i]))
            csvwriter.writerow([ORGS[i], EMAILS[i], getrandomdate(), getrandomdate(), getrandomdate()])

    csvfile.close()


main()
