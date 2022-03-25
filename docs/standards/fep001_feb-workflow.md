# FEP-001 - FEP Zweck, Richtlinien und Workflow

| Feld    | Inhalt                              |
|---------|-------------------------------------|
| FEP:    | 001                                 |
| Titel:  | FEP Zweck, Richtlinien und Workflow |
| Datum:  | 2022-01-12                          |


### Was ist ein FEP?

FEP steht für Fiber Enhancement Proposal. Ein FEP ist ein Dokument für Partner, Interessenten und Nutzer von (offenen) Glasfasernetzen, zur Erläuterung von Begriffen, Erklärung und/oder Regelung von Daten, Prozessen und Umgebungen. Ein FEP soll präzise in der Definition sein, den Nutzern von (offenen) Netzen aber auch Handlungsspielraum in der praktischen Umsetzung erlauben.

Wir als OFAA beabsichtigen über die Methodik einer FEP Dokumentation Empfehlungen und praktische Standards zu veröffentlichen. Ein FEP entsteht federführen durch die Autoren in Kooperation mit der Gemeinschaft der Interessenten, vorwiegend den aktiven Mitgliedern von OFAA.

### Für wen ist ein FEP?

Ein FEP unterstützt bei der Umsetzung der bei Planung, Errichtung und Betrieb notwendigen Aktivitäten. Die Nutzer kommen daher aus dem Umfeld von ISP, ANO und PIP sowie deren Partnern, Auftragnehmern und Lieferanten.

Zielsetzung der FEP ist den Austausch zwischen den Layern von 3-LOM (4-LOM) Netzen in einem breiten Konsens zu standardisieren, sodass die Nutzung und Verbreitung von (offenen) Glasfasernetzen effizient und effektiv vorangetrieben werden kann.


### Welche Arten von FEP gibt es?

Es gibt x Arten von FEP:

1. Ein Information-FEP beschreibt die Art und Weise wie Daten und/oder Prozesse interpretiert oder dargestellt werden.

2. Ein Technical-FEP beschreibt konkrete Vorgaben zur Implementierung von Schnittstellen und/oder Prozessen.

3. ...


## FEP Rollen

#### FEP Steering Council

Die Rolle des FEP Steering Council besteht in der finalen Entscheidung ob ein FEP angenommen oder abgelehnt wird. Das FEP Steering Council bildet sich aus aktiven und per Beschluss nominierten Mitgliedern von OFAA. 

#### FEP Autoren

FEP Autoren sind die für einen FEP federführend verantwortlichen Personen. FEP Autoren werden vom FEP Steering Council für die Erstellung eines FEP nominiert bzw. können die Erstellung selbst vorschlagen.

#### FEP Editor

FEP Editoren sind Personen mit der Verantwortung für die administrativen und redaktionellen Teile im FEP Ablauf. Ein FEP Editor wird durch Einladung durch einen anderen, für den jeweiligen FEP zuständigen, Editors nominiert.

Alle Abläufe durch die Editoren finden über die Standard-Prozesse eines git Systems (Issues und Pull Requests) statt. Der Umgang mit dem Versionssystem basierend auf git muss den Editoren geläufig sein.


## FEP Ablauf

#### Start eines FEP

Der FEP Prozess beginnt mit einer Idee für eine Empfehlung. Je klarer diese Empfehlung abgegrenzt ist, desto erfolgreicher ist die Umsetzung und Partizipation durch die Community. FEP Autoren können bis zum Abschluss des FEP die Weiterführung beenden, wenn die Umsetzung nicht möglich ist. Ebenfalls ist es möglich den Fokus des FEP zu konkretisieren oder gar auf mehrere FEP aufzuteilen, wenn es sinnvoll ist.

In der Regel gibt es für einen FEP einen Autor, bei einer Gemeinschaft an Autoren ist einer federführend für die Letztfassung des FEP, die Korrektheit der Umsetzung und Motivation zur aktiven Mitarbeit der Co-Autoren und Editoren.

Zur Vorlage dan das Steering Council wird ein Draft-FEP vom Autor erzeugt.

#### Eigenschaften eines FEP

Damit ein FEP akzeptiert und in das Register aufgenommen wird, müssen bestimmte Kriterien eingehalten werden.

Der FEP muss den formalen Gestaltungs-Kriterien für FEPs entsprechen. Die Beschreibungen im FEP müssen _klar_, _komplett_ und _zweifelsfrei_ sein. Die Standards (Empfehlungen) müssen fundiert und praxisnah gestaltet sein und dem Charakter von offenen Glasfasernetzen nach dem 3-LOM Prinzip entsprechen. Dazu gehört insbesondere, dass die Empfehlungen sowohl von kleinen als auch großen Unternehmen bzw. Organisationen umsetzbar (oder zumindest mitgetragen) werden können. Ebenfalls gilt as selbstverständlich, dass ein FEP keine Empfehlungen gegen geltende Normen oder Gesetze enthält und die (regulatorischen) Verpflichtungen einhält oder sogar unterstützt.

Wo immer möglich sind bestehende Standards (z.B. ÖNorm, ISO Norm) vorzuziehen und nicht durch einen FEP zu ersetzen. Informations-FEP können jedoch die Interpretation und Anwendung dieser externen Normen und (gesetzlichen) Vorgaben erläutern und Vorschläge für die praktische Umsetzung beinhalten.


#### FEP Überarbeitung

FEPs können im Laufe der Zeit überarbeitet werden um Veränderungen im Umfeld oder neue Erkenntnisse abzubilden. Die Veränderung ist in geeigneter Weise zu dokumentieren. Bei gravierenden Änderungen kann dieser ersetzt und als obsolet (ungültig) deklariert werden. Gleiches gilt bei Wegfall der Gründe bzw. Motivation für einen FEP im Allgemeinen.

#### Inhalte eines FEP

Ein FEP besteht im Allgemeinen aus folgenden Teilen:

1. Preamble -- Meta Daten im Stile von :rfc:`2822` inklusive FEP Nummer, ein prägnanter Titel (max. 44 Zeichen), Autor(en) usw.

``` text
FEP: FEP Nummer
Title: Titel des FEP
Autor: Liste der Autoren
Status: <Draft | Active | Accepted | Provisional | Deferred | Rejected |
Type: <Information | Process | Interface>
Created: <date created on, in dd-mmm-yyyy format>

* Sponsor: Liste der Sponsoren
* Replaces: <pep number>
* Superseded-By: <pep number>
```

2. Abstrakt -- eine kurze, nicht mehr als 200 Wörter umfassende Beschreibung zum Inhalt des FEB

3. Motivation -- die Motivation ist insbesondere für jene FEP kritisch, welche übergreifende Prozesse und Abläufe regeln.

4. Rationale Erklärungen -- ergänzen die (technische) Spezifikation mit Hintergründen warum eine bestimmte Richtung und Spezifikation vorgeschlagen wurde oder eine alternative Methode auch nicht weiter verfolgt wurde. Die rationale Erklärung fasst den Konsens der Autoren und Editoren zusammen und kann auch deren Bedenken enthalten.

5. Spezifikation -- die (technische Spezifikation) in einer klaren und an (praktischen) Standards angelehnten Art und Weise.

6. Sicherheit -- bei sicherheitskritischen Anwendungen entsprechende Hinweise wie und in welchem Maße dieser FEP einen Einfluss darauf hat. Sicherheit ist dabei sowohl im Sinne von Daten (IT) als auch betreffend Personen (Errichtung von Glasfaser) und Gebäuden (Absicherung von Objekten) zu interpretieren!

7. Gesetzliches -- bei Bedarf Erläuterungen zu gesetzlichen Vorgaben, die durch diesen FEP berührt werden.

8. Training -- bei Bedarf ein Abschnitt, der erklärt wie die Inhalte des FEP trainiert bzw. geschult werden können.

9. Referenzen -- Beispiele für _Best Practise_, die im Zusammenhang mit diesem FEP stehen oder sogar Ideengeber für die Umsetzung waren.

10. Offene Punkte -- jene Themen, die zwar von FEP bzw. in dem Umfeld des FEP angesprochen, aber dadurch nicht gelöst werden.

11. Versionshinweise -- Darstellung der durchgeführten Änderungen 

12. Copyright/Lizenz -- Lizenz des FEP, also zumindest [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/).


#### FEP Formate und Vorlagen


- FEPs sind Text Dateien mit UTF-8 Zeichensatz im _Markdown_ Format.
- Diagramme und grafische Darstellungen werden idealerweise als PNG mit einer Auflösung von 300 dpi eingebunden. 
- Fotografien können im JPG Format eingebunden werden. 
- Zusätzliche Dateien können per URL eingebunden werden. 
 
Alle in einem FEP verwendeten Dateien müssen der Konvention `fep-xxxx_y.suffix` folgen, wobei `xxxx` die Nummer des FEP, `y` ein beliebiger String ohne Leer- und Sonderzeichen und `.suffix` die Dateiendung ist (z.B. `.png`). 

Die Konvertierung nach HTML oder PDF erfolgt automatisiert im Hintergrund.

#### Rückmeldungen, Anmerkungen

Korrekturvorschläge sind über die Mechanismen von git einzubringen (Issue oder Pull Request). Im Bedarfsfall sollte mit dem Autor vorab Kontakt aufgenommen werden. Aus Sicherheitsgründen werden keine eMail-Adressen der Autoren im FEP genannt, diese können bei OFAA angefragt werden.

#### Übergabe von FEPs

Sollte es notwendig sein die Autorenschaft zu übergeben, dann wird der bisherige Autor als Co-Autor genannt und der neue Autor übernimmt die _Eigentümerschaft_ des FEP.


## Copyright

Dieses Dokument wird als [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.de) veröffentlicht.
