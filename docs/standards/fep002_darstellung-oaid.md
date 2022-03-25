# FEP 002 - Darstellung OAID

| Feld    | Inhalt                     |
|---------|----------------------------|
| FEP:    | 002                        |
| Titel:  | Darstellung Open Access ID |
| Datum:  | 2022-01-12                 |
| Status: | DRAFT                      |


## Abstrakt

Eine harmonisierte Darstellung der OAID erleichtert die Wiedererkennung durch die Endkunden. Über die Erklärung zur Nomenklatur können (elektronische) Systeme gegen Fehleingaben abgesichert werden.

## Spezifikation

### Nomenklatur

Die OAID ist eine acht-stellige Kombination aus Ziffern und Buchstaben. Für verarbeitende und insbesondere _ausgebende_ Systeme gilt:

- erlaubt sind die Buchstaben `ABCDFGHJKLMNPQRSTVWXYZ` in Groß- und Kleinschreibung, sowie alle Ziffern `0123456789`
- an erster Stelle darf keine Ziffer sein
- entweder Groß- oder Kleinschreibung, keine Mischformen

Das _Eingangs-System_ für die OAID (z.B. ein OAID Prüfsystem) kann toleranter in der Interpretation sein und auch OAIDs mit Mischformen oder OAIDs in Blockdarstellung (z.B. zwei mal ein Blcok mit vier Zeichen) verarbeiten. Denkbar, jedoch mit Vorsicht, ist auch die Durchführung einfacher Korrekturen der erhaltenen OAID (z.B. `0` statt `O`) vor der weiteren Verarbeitung.

#### Regular Expression

```regexp title="simple"
/^([ABCDFGHJKLMNPQRSTVWXYZ0-9]{8})$/gi
```

```regexp title="case-insensitive"
/^([ABCDFGHJKLMNPQRSTVWXYZ][ABCDFGHJKLMNPQRSTVWXYZ0-9]{7})$/gi
```

```regexp title="complete"
/^((?:[ABCDFGHJKLMNPQRSTVWXYZ][ABCDFGHJKLMNPQRSTVWXYZ0-9]{7})|(?:[abcdfghjklmnpqrstvwxyz][abcdfghjklmnpqrstvwxyz0-9]{7}))$/g
```

[RegExr is an online tool to learn, build, & test Regular Expressions](https://regexr.com)

#### Beispiele
```text title="gültige und ungülige OAIDs"
ABCD4321
abcd4321
ABCD4320
{--ABCE4321--}
{--ABCDF4321--}
{--ABCD432O--}
{--4BCEA321--}
...
```

### Darstellung in Print und Web User Interfaces

#### Schriftart

Die Print-Darstellung der OAID sollte in einer Schriftart mit fixer Breite erfolgen. Empfohlen werden - in absteigender Reihenfolge - die folgenden Schriften. Auf die Lizenzbestimmungen ist gegebenenfalls Rücksicht zu nehmen.


- [Jetbrains Mono](https://www.jetbrains.com/lp/mono/) (Apache License v2.00)

    ![Jetbrains Mono](/assets/jetbrainsmono.png){ align=center, loading=lazy }

- [Clear Read Mono 2](https://zv.psa.at/de/download/zahlungsbelege/belegbeschriftung.html) (siehe SEPA Zahlscheine)

    ![Clear Read Mono 2](/assets/clearreadmono.png){ align=center, loading=lazy }

- [Courier Prime Code](https://www.fontsquirrel.com/fonts/courier-prime-code) (SIL Open Font License v1.10)

    ![Courier](/assets/courier.png){ align=center, loading=lazy }


#### Codes für Demo Darstellungen

Wird die OAID in Beispielen verwendet, dann ist eine ungültige OAID zu verwenden. Die einfachste Methode dafür ist durch Einsatz eines ungültigen Buchstabens wie z.B. `E`, `I`, `U`. Folgende OAIDs können bedenkenlos in Beispielen verwendet werden:

`ABCE1234`, `ABCU1234`, ...

