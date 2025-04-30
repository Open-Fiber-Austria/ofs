# Open Link ID

!!! note ""
    Die __Open Link ID__, kurz __OLID__, ist die kundenseitige Kennung einer einzelnen Faser eines Glasfaser-Anschlusses.

### Nutzeinheit und Faserlinks

Die kleinste Einheit der passiven Infrastruktur - in Point-To-Point Netzen - ist die Faser. Eine einzelne Verbindung zwischen dem Abschluss beim Endkunden (FTU) und dem zentralen Zugangspunkt (POP) wird als Faserlink (Fiber Link) bezeichnet. Ein Standort kann mit mehreren Faserlinks (Mehrfaserkonzept) angebunden werden. Auf einem solchen Faserlink setzt der ANO sein Bitstream Service auf und erlaubt dem ISP die Nutzung.

Der Faserlink ist das Kernelement in der Kommunikation zwischen PIP und ANO. Die Faserlinks bilden die Grundlage für Nutzung und Verrechnung. Genaue Trassenführung oder involvierte Elemente (FCPs, ...) irrelevant. Ein Faserlink ist mit den beiden Endpunkten, kundenseitig auf der FTU (Port x von y), netzseitig im Optical Distribution Frame (Rack, Frame, Port, ...) innerhalb des FCO, eindeutig beschrieben. Geografische Koordinaten sind nicht notwendig, unterstützen aber eine Visualisierung.

Im Allgemeinen wird ein Standort nicht mit einer Faser, sondern mit einem (oder auch mehreren) Kabel, bestehend aus mehreren Fasern versorgt. Jede dieser Fasern ist mit einer eindeutigen Bezeichnung vorzusehen. Als Bezeichnung dafür wurde Open Link ID, kurz OLID gewählt. In der Umsetzung bieten sich zwei Varianten an:

`absolute OLID`
: jeder einzelne Faserlink erhält eine absolute, netzweit eindeutige Kennung. Die später dargestellte Nomenklatur Empfehlung kann nahezu identisch auf die OLIDs angewandt werden. Ein Konzept ähnlich der OAID selbst, unmittelbar auf Faserlinks angewendet.

`relative OLID`
: jede Faser erhält als lokale Bezeichnung des Standorts den Faser Identifier, die netzweite Eindeutigkeit ergibt sich in Kombination mit der OAID.

Für die Vermarktung der Faserlinks durch den PIP sind beide Varianten möglich. Ziel dieser Vermarktung sind ANOs und andere Unternehmen, die Interesse und Nutzen an einer physischen Verbindung haben (z.B. Anbindung für Smart Metering). Die Vorteile des absoluten Konzeptes für die OAID gelten natürlich auch für die OLID. Verzichtet man gänzlich auf die OAID, würde der Kunde anstelle einer ID für den Standort im Allgemeinen mehrere OLIDs erhalten. Diese OLIDs wären in Briefen anzuführen und als Beschriftung anzubringen.

Welche Faser zur Anwendung kommt, wird in der Regel direkt zwischen PIP und ANO ausgehandelt und ist daher für den Kunden von geringer Bedeutung. In den meisten Fällen ist die einzelne Faser für den Kunden nicht identifizier- oder sichtbar. Für die normalen Endkunden würde Angabe mehrerer OLIDs eine unnötige Komplexität bedeuten. 

Aus Datensicht steht bei der Open Access ID der Standort mit seinen absoluten und relativen Ortsangaben im Vordergrund, bei den OLIDs beziehen sich Angaben zur Position ausschließlich auf die Lage der Ports auf den jeweiligen Enden. Auch aus dieser Perspektive ist die __Koexistenz von OAID für den Standort und relativer OLID für die Faserlinks 


### Beispiele für OAID und OLID

Zum besseren Verständnis sind nachfolgend Beispiele angeführt. Das tatsächliche Aussehen hängt von den Parametern der Implementierung ab. Dazu gehören u.a. Anzahl der Zeichen, erlaubte Zeichen, mathematisches Modell für Vergabe, …  


#### relative lokale OLID (lokale OAID mit Faser Identifier)

Unter Verwendung eines definierten Delimiters wird die relative Faserkennung als Suffix an die OAID angehängt, daraus entsteht die OLID. Der Code Raum sollte dabei auf numerische Zeichen eingeschränkt bleiben, um die in der Praxis geläufige Verwendung von Faser Eins (oder Drei oder Zwölf, ..) einfacher handhabbar zu machen. Als zusätzliche Regel bietet sich an, keine fixe Länge vorzusehen, die Bezeichnung `1` (Eins) ist somit identisch mit `01` oder `001`.

`ABC321.1` 	für Faser Eins ist somit identisch mit `abc321.01`, `abc321.001`, ...

`ABC321.12` 	für Faser Zwölf, identisch mit `abc321.012`, ...

Werden über einen BEP mehrere Standorte versorgt, besteht die Möglichkeit einer fortlaufenden Nummerierung oder die Nummerierung je Standort neu zu nummerieren. Welche Variante gewählt wird, hängt auch vom Faserkonzept des PIP und/oder den Ausführungen der _Ablagen_ im ODF bzw. FCP ab. Systeme, in denen die Fasern immer in Gruppen zu vier, oftmals auch mit Farben anstelle der Nummern, abgelegt werden, sind durchaus üblich.

