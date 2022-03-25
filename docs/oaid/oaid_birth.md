# Entstehung der OAID

### Nomenklatur

In der elektronischen Verarbeitung über Systemgrenzen hinweg bietet sich an, eine einfache Nomenklatur zu verwenden. Es empfiehlt sich auf Sonderzeichen gänzlich zu verzichten und nur einen eingeschränkten Zeichensatz zu verwenden. Zur Unterstützung in der Kommunikation mit dem Endkunden sollte auch auf die Unterscheidung von Groß- und Kleinbuchstaben verzichtet und fehleranfällige Kombinationen oder Zeichen (z.B. `0` statt `O`, ...) nicht gemeinsam verwendet werden. In der Praxis bewährt sich die Verwendung eines eingeschränkten ASCII-Zeichensatzes (Buchstaben, Ziffern und wenige Sonderzeichen).

Die Verwendung eines alphanumerischen Zeichensatzes anstelle von ausschliesslich Nummern erhöht - bei gleicher Länge - die Anzahl der Kombinationen.

Die Open Access ID ist ein Kommunikationsmittel und kein Sicherheitsschlüssel. Die Anwendung und Verwaltung von OAID erfordert die Kombination mit zusätzlichen Merkmalen bzw. Attributen, allen voran einer korrekten und hinreichenden absoluten Geokodierung sowie lokalen Ortsangaben (im Technikraum, ...).

### OAID im globalen Kontext

Als eines der Ziele wurde eine österreichweit eindeutige Kennung für Open Access Netze genannt. Während innerhalb von Systemgrenzen eine Eindeutigkeit relativ leicht sichergestellt werden kann, ist das über diese Grenzen hinaus nicht mehr garantiert.

Bei korrekter Implementierung kann sichergestellt werden, dass zeitlich aufeinanderfolgende oder benachbarte Standort-Bestellungen eine - mit hoher Wahrscheinlichkeit - sich deutlich unterscheidende OAID erhalten. Damit ist jedoch nicht gleichzeitig ausgeschlossen, dass beispielsweise Standorte zweier Unternehmen eine ähnliche oder sogar identische OAID haben. Da die OAID jedoch darüber hinaus auch einen geografischen Fokus hat, spielen solche Ähnlichkeiten in der Praxis keine Rolle.

Problematisch werden solche Szenarien beim Zusammenschluss oder in der gemeinsamen Verwaltung von Netzen. Der Austausch einer OAID würde einen Besuch des Standorts notwendig machen, zumindest jener - die tatsächlich identisch sind. Damit diesem vorgebeugt wird, sollten schon jetzt Methoden und Maßnahmen getroffen und möglichst breit abgestimmt werden. Ausgehend vom bekannten Begriff bietet sich an eine solche ID als global OAID, kurz gOAID, zu bezeichnen. Folgende Methoden stehen dafür zur Verfügung:

- Vergabe von übergreifenden Prä- oder Suffixen
- Verwendung innerhalb zugeteilter Code Räume
- Mathematische Methoden und Arbeiten mit Wahrscheinlichkeiten

Ein Beispiel für letzteres ist die sog. Universally Unique Identifier. Ein 128-bit Schlüssel wird dabei so zufällig generiert, dass die Wahrscheinlichkeit für einen identischen Schlüssel vernachlässigbar klein wird. Dem gegenüber steht, dass die UUID in der gängigen Darstellungsform 36 Zeichen besitzt und damit klar dem Prinzip der Einfachheit (Kürze) widerspricht.

Zweiteres erfordert eine übergreifende, zentrale Vergabestelle. Diese müsste zudem auch eine vollständige Nomenklatur vorgeben. Für die eigentlichen Ersteller der OAID, im Allgemeinen die PIP, bedeutet es, eine Abbildung dieser Nomenklatur in den IT-Systemen und auch eine frühzeitige Abschätzung über die Anzahl der benötigten Codes (ein aus IPv4 bekanntes Problem).

Somit bietet sich Variante eins an. Auch hier gibt eine zentrale Vergabestelle das Präfix vor (Anmerkung: Suffix wurde bereits für den Fiber Identifier besetzt). Die Vergabestelle definiert nur mehr einen Teil der Nomenklatur und es ist nicht erforderlich, vorab die Anzahl an Codes zu reservieren oder bekannt zu geben. Das Präfix kann als Domain Identifier bezeichnet werden. Zudem, als wichtigstes Argument, spielt im praktischen Gebrauch die Verwendung der lokalen OAID eine wesentlich bedeutendere Rolle, wo die Vorzüge in der Kundenkommunikation (merkbar, einfache Handhabung) zum Tragen kommen. Der Domain Identifier dient als Absicherung für jene Situation, wo mehrere Vergabestellen parallel existieren.

Die globale OAID wird vor allem relevant beim Zusammenschluss von Netzen. Die Autoren empfehlen für die globale OAID die Variante mit dem Präfix. Das Präfix kann entfallen, wenn die Kennzeichnung in allen involvierten Netzen eindeutig ist. Die Vergabe der lokalen Open Access ID sollte durch eine Vergabestelle, z.B. dem Zusammenschluss von PIP, erfolgen. Als Autorität für die Vergabe des Präfixes empfiehlt sich eine unabhängige Instanz, z.B. ein von allen anerkannter non-profit Verein. Auch wenn damit das Präfix innerhalb des Vereins entfällt, kann sich, wenn andere Netze bzw. sich ähnliche Vereine sich etablieren, später ein Bedarf ergeben. Die theoretische Möglichkeit sollte also im Konzept mitbedacht werden.

### Empfehlungen für Nomenklatur

- Länge der OAID sollte zwischen 6 und maximal 8 Stellen betragen. Zu wenige Zeichen schränken die möglichen Kombinationen ein, zu viele Zeichen sind (in der Kommunikation) schwer vermittelbar.
- Über die Wahl der sogenannten Delimiter, also dem Trennungszeichen zwischen Präfix und OAID, Einigkeit herrschen oder Implementierungen unterschiedliche Delimiter akzeptieren.
- Erlaubt sind die Zeichen A-Z, 0-9. Für Delimiter Sonderzeichen wie `_-.:|/#`.
Zur besseren Lesbarkeit sollte auf verwechselbare Zeichen, beispielsweise `0` (Null) und `O` (Buchstabe _O_) oder `1` (Eins) und `l` (Buchstabe _L_) oder ..., verzichtet werden. Der damit mögliche Coderaum wird zwar damit eingeschränkt, die Vorteile in der Kommunikation überwiegen jedoch.
- OAID sollte case-insensitive sein, also nicht zwischen Groß- und Kleinbuchstaben unterscheiden. Auch das schränkt den Coderaum ein, aber auch hier überwiegen die Vorteile im täglichen Gebrauch.
- In der Darstellung sollte das Gruppieren der Zeichen möglich sein. Involvierte Systeme müssen die OAID auch in formatierter Form akzeptieren (Beispiel ist die gängige Verwendung von Vierer-Blöcken bei IBANs, bei denen mit Leerzeichen getrennt wird)
- Als Delimiter zwischen Präfix und Suffix ist ein `.` (Punkt) zu setzen.
- Für Prä- und Suffixe gelten die Regeln sinngemäß.

- Anmerkung: Je nach Implementierung sind bei 6 Stellen > 1 Milliarde Kombinationen möglich, bei 8 Stellen gibt es mehr als 1.000 Milliarden mögliche Kombinationen (Berechnungsbeispiel mit base32 Kodierung).

### Beispiele für OAID und OLID

Zum besseren Verständnis sind nachfolgend Beispiele angeführt. Das tatsächliche Aussehen hängt von den Parametern der Implementierung ab. Dazu gehören u.a. Anzahl der Zeichen, erlaubte Zeichen, mathematisches Modell für Vergabe, …  

#### lokale OAID

OAIDs mit sechs oder acht Zeichen, im Beispiel auch mit darstellenden Trennzeichen, könnten wie folgt aussehen. Die Verwendung möglichst unverwechselbarer Zeichen ist zwar sinnvoll, kann aber den Coderaum deutlich einschränken. Einen wesentlichen (wenn nicht sogar deutlich höheren) Einfluss auf die Lesbarkeit und Erkennbarkeit der OAID hat die Schriftart.

```
    abc321, abc021, a01b02, z23-4tw, t23 343, ...
    abcd3210, defw32hj, DJWT-ZQ01, gh3-23-gtw, …
```

Wie Eingangs erwähnt, sollte die OAID in allen Fällen case-insensitive sein, d.h. `ABC321` ist identisch mit `abc321`. Sowohl für GROß- als auch Kleinschreibung gibt es gute Argumentationen, von einer gemischten Darstellung ist in allen Fällen abzusehen.

#### relative lokale OLID (lokale OAID mit Faser Identifier)

Unter Verwendung eines definierten Delimiters wird die relative Faserkennung als Suffix an die OAID angehängt, daraus entsteht die OLID. Der Code Raum sollte dabei auf numerische Zeichen eingeschränkt bleiben, um die in der Praxis geläufige Verwendung von Faser Eins (oder Drei oder Zwölf, ..) einfacher handhabbar zu machen. Als zusätzliche Regel bietet sich an, keine fixe Länge vorzusehen, die Bezeichnung `1` (Eins) ist somit identisch mit `01` oder `001`.

`ABC321.1` 	für Faser Eins ist somit identisch mit `abc321.01`, `abc321.001`, ...

`ABC321.12` 	für Faser Zwölf, identisch mit `abc321.012`, ...

Werden über einen BEP mehrere Standorte versorgt, besteht die Möglichkeit einer fortlaufenden Nummerierung oder die Nummerierung je Standort neu zu nummerieren. Welche Variante gewählt wird, hängt auch vom Faserkonzept des PIP und/oder den Ausführungen der _Ablagen_ im ODF bzw. FCP ab. Systeme, in denen die Fasern immer in Gruppen zu vier, oftmals auch mit Farben anstelle der Nummern, abgelegt werden, sind durchaus üblich.

#### absolute lokale OLID

Es gibt in diesem Fall keinen Faser-Identifier. Alle Fasern erhalten eine eindeutige und voneinander unabhängige Kennung. Welche Fasern zu einem Standort (einer Nutzeinheit) gehören, ist nur über eine gesonderte Relation zur OAID feststellbar.
Beispiele wie bei lokaler OAID.

