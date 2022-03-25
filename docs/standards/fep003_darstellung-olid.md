# FEP-003 - Darstellung OLID

| Feld    | Inhalt           |
|---------|------------------|
| FEP:    | 003              |
| Titel:  | Darstellung OLID |
| Datum:  | 2022-01-12       |
| Status: | DRAFT            |


## Abstrakt

Eine harmonisierte Darstellung der OLID erleichtert die Wiedererkennung durch die Endkunden. Über die Erklärung zur Nomenklatur können (elektronische) Systeme gegen Fehleingaben abgesichert werden.

## Spezifikation

### Nomenklatur

Die Open Link ID besteht aus der acht-stelligen Open Access ID und der Fasernummer. In der Darstellung wird die Fasernummer durch ein Suffix repräsentiert. Zusätzlich zu den Regeln für die OAID gilt für verarbeitende Systeme folgendes:

- das Suffix beginnt mit einem Punkt `.` oder einem Slash `/` (= Suffix-Delimiter)
- erlaubt sind nur Ziffern `0123456789`
- vorangestellten `0` (leading zeros) sind erlaubt
- Gesamtlänge exklusive Suffix-Delimiter ist 4 Ziffern
- die dargestellte Nummer wird als Integer interpretiert
- die Nummerierung der Fasern beginnt bei 1

!!! example "Beispiel"
    `ABCD4321.001` bedeutet OAID = `ABCD4321` und Faser Nummer = __1__.

!!! hint "Warum auch Slash?"
    Bei Darstellung der OLID in einer API entspricht der Slash `/` der Identifikation der Ressource (<oaid>/<fiber>).


#### Regular Expression

```regexp title="simple"
/^([ABCDFGHJKLMNPQRSTVWXYZ0-9]{8})\.(\d+)$/gi
```

```regexp title="case-insensitive"
/^([ABCDFGHJKLMNPQRSTVWXYZ][ABCDFGHJKLMNPQRSTVWXYZ0-9]{7})[\./](?!0+$)([0-9]{1,4})$/gi
```

```regexp title="complete"
/^((?:[ABCDFGHJKLMNPQRSTVWXYZ][ABCDFGHJKLMNPQRSTVWXYZ0-9]{7})|(?:[abcdfghjklmnpqrstvwxyz][abcdfghjklmnpqrstvwxyz0-9]{7}))[\./](?!0+$)([0-9]{1,4})$/gi
```

[RegExr is an online tool to learn, build, & test Regular Expressions](https://regexr.com)

#### Beispiele

```text title="gültige und ungülige OLIDs"
ABCD4321.0001 = ABCD4321.001 = ABCD4321.01 = ABCD4321.1
ABCD4321/001 = ABCD4321/01 = ABCD4321/1 = ABCD4321.1
ABCD4321.013
{--ABCD4321.0--}
{--ABCD4321.00001--}
{--ABCD4321\001--}
{--ABCD4321.000--}
{--ABCD4321.00A--}
{--ABCD4321.red--}
...
```

### Darstellung in Print und Web UI

#### Schriftart

Siehe dazu die Empfehlungen in [FEP-002](fep002_darstellung-oaid.md).

#### Codes für Demo Darstellungen

Wird die OLID in Beispielen verwendet, dann ist eine ungültige OLID zu verwenden. Die einfachste Methode dafür ist durch Einsatz eines ungültigen Buchstabens wie z.B. `E`, `I`, `U`. Folgende OLIDs können bedenkenlos in Beispielen verwendet werden:

`ABCE1234.001`, `ABCU1234.1`, ...
