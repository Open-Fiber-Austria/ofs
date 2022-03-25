# Open Access ID

!!! note ""
    Die __Open Access ID__, kurz __OAID__, ist die kundenseitige Kennung eines Glasfaser-Anschlusses mit zumindest einer Faser.

<!--
Beginnend mit einer Einleitung zu den Grundsätzen und Zielen einer Open Access ID werden nachfolgend die Begriffe Faser Identifier und Domain Identifier eingeführt und das Thema Nutzeinheit vs. Gebäude beleuchtet. Wie in den vorangegangenen Ausführungen erläutert, ist die Bezeichnung des Faserlinks in jedem Fall notwendig. Ein solcher Faserlink wird über den Open Link Identifier, kurz OLID, repräsentiert. Ausgehend von der Hypothese, dass OAIDs sich auf eine Nutzeinheit (aus Kundensicht) beziehen folgen im Anschluss daran technische Anforderungen an die Open Access ID selbst. Nicht Teil dieses Dokuments sind die notwendigen Vergabeprozesse (_Ziehen einer OAID_) sowie tiefergehende technische Details. Diese sind Sache der jeweiligen Implementierung. Das Kapitel schließt mit praktischen Beispielen für OAIDs ab.
-->

Die Open Access ID dient vorwiegend der Vereinfachung der Kommunikation mit dem, bzw. im zeitlichen Ablauf, mehreren Endkunden. Keinesfalls soll diese ID einen systemimmanenten Schlüssel, der dann auch (oder zusätzlich) im Austausch zwischen Systemen und Schnittstellen dient, ersetzen. Daraus ergeben isch folgende Grundsätze:

- OAID ist die kundenseitige Kennung des Standorts und dient in erster Linie als Identifikationsmerkmal in der Kommunikation mit Endkunden.
- OAID ist ein Attribut des Standorts (Netzes) und keiner Person zugeordnet.
- OAID ergänzt, ersetzt aber nicht (vollständig) eine systemimmanente maschinelle ID. Zwischen beiden besteht jedoch eine eindeutige Zuordnung (1:1).
- OAID ermöglicht eine robustere und eine von externen Faktoren (z.B. postalische Adresse) unabhängige Bezeichnung des Standorts (Site) in Open Access Netzen.
- OAID kann nicht für sich alleine bestehen und benötigt Attribute aus der realen Welt wie beispielsweise Koordinaten, postalische Adressen, lokale Ortsangaben (Türnummer, Raumbezeichnung, …).

Das vorliegende Dokument soll einen Rahmen bilden und Begrifflichkeiten definieren, um den Austausch und das Verständnis zwischen den Peers (auf gleichem Layer) und vertikal (zwischen den Layern) ermöglichen. Als Zielsetzung für OAID und OLID lassen sich ableiten:

- Vereinfachung der Errichtung (Bestellung von Infrastruktur) für Endkunden durch standardisierte Schnittstellen und offengelegte (und stark vereinfachte!) Daten zur Netzinfrastruktur.
- Vereinfachung der Prozesse für den Endkunden (One-Stop-Shop für Infrastruktur und Internet-Dienste). Rasche Nutzung von Internet Services (Bestellung, Änderung von Internet Diensten) für Endkunden durch standardisierte Schnittstellen und
- Vereinfachung der Nutzung von Glasfaser (Breitband) Infrastruktur durch Anbieter oder sonstige Serviceleistungen (z.B. Smart Metering).
- Zusammenführen von Netzen unterschiedlicher Infrastruktur-Errichter (PIP) unter Beibehaltung bestehender OAIDs bzw. der auf Netzebene mehr relevanten OLIDs und generischen Prozesse.
- Unabhängigkeit von der technischen Implementierung der Verwaltung der Netzelemente (Asset Management).

Eine einheitliche Verwendung der Open Access ID bzw. der dahinter liegenden Konzepte wird angestrebt (wobei jedoch, wie in den Beispielen beim zeitlichen Ablauf gezeigt, ein größtmöglicher Freiheitsgrad in der Implementierung eingeräumt ist). Gleichzeitig gibt es aber bereits heute schon unterschiedliche Vorgehensweisen bei der Etablierung von Open Access Netzen. Ebenso ist - und auch wenn hier nicht explizit darauf eingegangen wird - das Konzept nicht ausschließlich auf 4LOM (bzw. 3LOM) beschränkt. Auch Modelle wie PLOM oder ALOM können davon profitieren und im Allgemeinen spricht nichts dagegen, das Konzept auch in Netzen mit den Technologien DOCSIS, DSL oder 5G (fixed-mobile conversion) anzuwenden.


### Zuteilung der OAID

Die OAID ist eine system- bzw. unternehmensübergreifende eindeutige Kennung. Die Zuteilung der OAID kann ab eindeutiger Identifikation des Standorts (Nutzeinheit) erfolgen. Das muss nicht unmittelbar bei der Entstehung des Datensatzes sein. Im Idealfall wird die OAID dann zugeteilt, wenn die Herstellung des Standorts gesichert ist und der Kunde darüber informiert wird. 

Um diese Flexibilität zu gewährleisten ist daher zwangsweise eine systeminterne, eindeutige Kennung notwendig. Es empfiehlt sich bei diesen Kennungen auf gängige Praxis, z.B. Verwendung von Universal Unique IDs, zu setzen und von Logiken mit interner Bedeutung abzusehen.

!!! note ""
    Die Implementierung der OFAA OAID unterstützt die Angabe sogenannter UUIDs (128-bit Codes) bei der Vergabe der OAIDs.

!!! warning ""
    Die Vergabe der OAID ist ein einmaliger Vorgang und kann nicht rückgängig gemacht werden. Die OAID sollte daher erst dann vergeben werden, wenn der Standort definiert ist. Mit Zuteilung wird die OAID _lebenslang_ mit diesem Standort verknüpft.

