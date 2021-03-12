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
]

EMAILS = [
    "kayden.head@helsinki.fi",
    "alaya.alcock@helsinki.fi",
    "rosalie.lynch@helsinki.fi",
    "judith.holcomb@helsinki.fi",
    "chase.woodard@helsinki.fi",
    "zackery.key@helsinki.fi",
    "aneesha.schmidt@helsinki.fi",
    "mahamed.wells@helsinki.fi",
    "matthias.cope@helsinki.fi",
    "dorian.talley@helsinki.fi",
    "myles.kenny@helsinki.fi",
    "mcauley.hicks@helsinki.fi",
    "osman.aguilar@helsinki.fi",
    "warren.thornton@helsinki.fi",
    "fionn.ward@helsinki.fi",
    "danny.dunn@helsinki.fi",
    "martina.shannon@helsinki.fi",
    "nansi.mcintyre@helsinki.fi",
    "md.robertson@helsinki.fi",
    "kathleen.weber@helsinki.fi"
]


def getrandomdate():
    return datetime(
        2021,
        random.randint(1, 4),
        random.randint(1, 28)
    ).strftime("%d.%m.%Y")


def geteventtype():
    types = ["sitsit", "bileet"]
    return types[random.randint(0, 1)]


def main():
    with open("input.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";", dialect="excel")
        csvwriter.writerow(["organization", "email", "1", "2", "3"])

        for i in range(0, len(ORGS)):
            print("{}: {} ({})".format(i, ORGS[i], EMAILS[i]))
            csvwriter.writerow([
                ORGS[i],
                geteventtype(),
                EMAILS[i],
                getrandomdate(),
                getrandomdate(),
                getrandomdate()
            ])

    csvfile.close()


main()
