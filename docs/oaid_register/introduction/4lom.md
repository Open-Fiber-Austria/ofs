# Four Layer Open Model

![Four-Layer-Open-Model](/assets/4_layer_model@2x.png){ align=center, loading=lazy }

In der Realität kommt zum Modell noch eine vierte Schicht hinzu. Ohne Kunden ist das Modell nicht vollständig. Das Modell wird dann zu einem Three+One Layer Open Model, oder - nochmals vereinfacht - zu einem Four-Layer Open Model bzw. abgekürzt 4LOM.

## Logische Darstellung
Im Lebenszyklus eines Glasfaser-Anschlusses gibt es nicht nur DEN EINEN Kunden, sondern zwei (oder mehr). Jene Person, die den Infrastruktur-Anschluss herstellen lässt, muss nicht mit jener Person übereinstimmen, die dann auch den Servicevertrag mit dem ISP eingeht. In Mehrparteienhäusern ist eine solche Situation Standard, aber - wie uns die Erfahrungen der Praxis zeigen - ist es auch bei Einzelanschlüssen der Fall. Aus dieser Situation heraus lässt sich die Motivation für die Einführung der Open Access ID begründen.

Mit dieser Ergänzung lässt sich das Modell wie nachfolgend gezeigt darstellen. Zusätzlich ergänzt auch jene _Punkte_, die dem jeweils Verantwortlichen zugeordnet werden können oder eine Grenze der Verantwortung darstellen.

## Physische Darstellung
Das logische Modell, bzw. die genannten Punkte finden sich auch in einer Abbildung von real existierenden Objekten wieder. So bildet beispielsweise die CPE den Abschlusspunkt des ISP, ist aber gleichzeitig auch ein Gerät, das mit dem Netz verbunden ist.

In der Prozessdarstellung wurde bereits der Begriff Standort (Kundenstandort, engl.: Site) eingeführt. Dieser umfasst, in der gewählten Darstellung, die Installation auf der Kundenseite. Obwohl der Standort eine Koordinate besitzt, die sich im Allgemeinen aus der geografischen Verortung einer Adresse oder einer anderen Methode ableitet, ist die exakte Position irrelevant. Die Verortung muss hinreichend genau sein, um eine eindeutige Identifizierung zu gewährleisten. In gängigen Darstellungen reicht es, wenn sich z.B. der Standort _über dem Dach_ des Hauses befindet. Die Koordinate liefert zwar die absolute Position, für eine genaue Identifizierung sind u.U. noch weitere Attribute, wie eben relative Ortsangaben (Türnummer, Zimmerbezeichnung o.ä.) notwendig. Dadurch ist es möglich, dass eine Koordinate für mehrere Standorte gilt. Jeder Standort (Site) erhält zudem eine eindeutige OAID.

In der Kommunikation mit dem Kunden ist der Begriff Standort neutral verwendbar und gilt für private Objekte ebenso wie für gewerbliche. Es handelt sich aber um einen virtuellen Punkt, eine Beschriftung kann nur auf einem realen Objekt angebracht werden. Je nach Situation bieten sich dafür ein oder mehrere (reale) Endpunkte an. Darüber hinaus gibt es unterschiedliche Vorgehensweisen bei der Errichtung der Glasfaser-Infrastruktur.

In der folgenden Darstellung sind verschiedene Szenarien abgebildet (von links nach rechts):

![Real World Example](/assets/real_world@2x.png){ align=center, loading=lazy }

#### Planung
In der Planung werden existierende und auch zukünftige Grundstücke und Objekte erfasst und berücksichtigt (linkes Bild). Dieser Schritt dient der Bestimmung der notwendigen Kapazitäten. Das Ergebnis ist eine geplante Location (Planning Location). Kommt es zu einer Bestellung, so wird der neue, potenzielle Standort (potential Site) dieser Location zugeordnet. Die Verortung dieses Standortes ergibt sich beispielsweise aus einer bereits verfügbaren, geokodierten Adresse, oder die Position wird explizit gesetzt.

#### Responsibility End Point
Eine besondere Bedeutung kommt dem Übergabepunkt (Responsibility End Point, abgekürzt REP) zu (siehe 2. Bild von links). Dieser bezeichnet jene Stelle, an der die Verantwortung des Physical Infrastructure Providers (PIP) für die passive Glasfaserinfrastruktur endet und die Verantwortung des Kunden (Grundstückseigentümer oder rechtlicher Vertreter, Infrastructure Customer) beginnt. Im Allgemeinen befindet sich dieser Punkt an der Grundstücksgrenze. Davon abweichende Regelungen sind möglich, insbesondere bei gewerblichen Objekten oder auch Mehrparteienhäusern.

Im Zuge der Montage wird ein Kabel vom Faserverteiler (Fiber Concentration Point, FCP) der sich in der Straße befindet, über den REP und bis zum Gebäude eingeblasen. Jener Punkt, an dem die Glasfaser in das Haus eingeführt wird, wird als (Building Entry Point, BEP) bezeichnet. Hier findet der Übergang zur Innenverkabelung bis hin zum Faserabschluss (Fiber Termination Unit, FTU) statt. Einführung ins Haus und sämtliche Vorbereitungen ab dem REP liegen i.A. in der Verantwortung des Kunden.

Bei der Montage ist dem PIP ein einmaliger Zugang für die Verbindung des Kabels vom FCP mit dem Innenkabel und weiter dann der Anschluss der FTU zu gewährleisten. Zugleich können bei diesen Arbeiten auch der optische Netzabschluss (Optical Network Termination, ONT) des Aktivnetzbetreiber (Active Network Operator, ANO) und der eigentliche Router (Customer Premises Equipment, CPE) des Internet Service Providers (ISP) angeschlossen werden.

#### Grundstück mit zwei Objekten
Das dritte Bild von links zeigt beispielhaft die Situation mit zwei Standorten auf einem Grundstück, die über den gleichen Planungspunkt (Planning Location) versorgt werden. Hier gibt es zwei vollwertige Installationen. Die Koordinaten sind so gesetzt, dass die Zuordnung eindeutig ist. Die Open Access ID der jeweiligen Sites wird (z.B.) auf der FTU im jeweiligen Haus angebracht (es wird seitens PIP nur ein einziger physischer BEP zur Verfügung gestellt, für die Weiterleitung am Grundstück ist der Kunde verantwortlich).

#### Mehrparteienhaus
Das rechte Bild zeigt die Situation in einem Mehrparteienhaus. Mit dem Infrastruktur-Kunden wurde die Verlegung bis in einen zentralen Technikraum vereinbart. Von dort führt eine Indoor Verkabelung in jede Nutzeinheit. Alle Sites haben identische Koordinaten, die lediglich zur besseren Visualisierung im Komma Bereich abweicht. Jedoch erhalten alle Sites eine lokale Ortsangabe (Türnummer). Der zentrale Abschluss (BEP) befindet sich im Technikraum. Bei der Montage werden sowohl im zentralen Technikraum die Zuteilung der einzelnen Sites zur Nutzeinheit als auch auf den FTUs in den Wohnungen die OAIDs angebracht. Mieter (und deren Nachmieter…) können so die bei der Bestellung beim Internet Service Provider verlangte OAID einfach ermitteln.

Aus diesem Szenario geht die Anforderung und besondere Verantwortung des Montage-Teams hervor. Dieses Team sorgt neben 

- der eigentlichen Fertigstellung,
- Beschriftung und Dokumentation, auch für
- die Endkontrolle der Daten.

Die eindeutige, vor allem aber auch deutlich unterscheidbare OAID (keine fortlaufende Bezeichnung) für jede Nutzeinheit beugt Verwechslungen vor.


## Zeitlicher Ablauf

Die in der logischen und realen Darstellung genannten Objekte spiegeln sich auch im zeitlichen Ablauf wieder. Hier geben vor allem Implementierung und Vorgehensweise des PIP die Interaktionen vor. Auslöser für die Infrastruktur Herstellung ist der Kunde - im Allgemeinen der Haus- oder Liegenschaftseigentümer. Ohne dessen Einverständnis ist keine Installation möglich. Für die Etablierung von OAID und der notwendigen Bezeichnung der Faserlinks (eine Faser zwischen zwei Endpunkten) ist es unerheblich, ob der Kunde  direkt beim PIP oder indirekt bestellt.

Nachfolgend abgebildet sind Szenarien mit direkter und indirekter Bestellung. Darüber hinaus sind noch weitere Varianten möglich, beispielsweise mit Bestellung über ANO oder - noch weiter generalisiert - mit Abwicklung durch Dritte.

Im wesentlichen gliedern sich alle Szenarien in die Phase der Herstellung und Phase der Nutzung auf. In der ersten Phase, der Installation der Glasfaser am Standort, sind PIP und Infrastruktur-Kunde verantwortlich, in der zweiten Phase interagiert der Kunde nur mehr mit dem ISP. PIP und ANO kennen im Allgemeinen diesen Kunden nicht (mehr). Die Szenarien sollen einen ungefähren Ablauf vermitteln und nicht den Prozess im Detail widerspiegeln. In der Realität sind, vor allem in der Herstellungsphase, noch weitere wichtige Rollen (Montage-Team, technische Kontaktperson beim Kunden, Logistik, …) zu integrieren.

####  Direkter Bestellung beim PIP

![Direct Order](/assets/conversation_direct@2x.png){ align=center, loading=lazy }

Beginnend mit der Kundenanfrage (request) kann, nach sorgfältiger technischer Analyse und Planung, dem Kunden bei Annahme der Bestellung (confirm) bereits die OAID übermittelt werden. Je nach Situation vor Ort (Rollout, Bestandsnetz, …) erhält der Kunde so die Möglichkeit, schon frühzeitig die Abmeldung seines bestehenden Internet-Dienstes durchzuführen und einen neuen Vertrag bei einem der ISPs abzuschließen. Spätestens bei der Montage (deliver) wird die OAID auch physisch auf einem Endpunkt (FTU, BEP oder auch ONT, …) angebracht. Damit ist sichergestellt, dass auch nachfolgende Internet Kunden die OAID ihres Anschlusses kennen - auch wenn keine Unterlagen mehr zur Verfügung stehen.

Ein wesentlicher Vorteil in dieser vorgehensweise ist der unmittelbare Kundenkontakt in der doch komplexen Herstellung. Nachteilig sind die damit verbundenen Zusatzaufwände (Invoicing, Customer Support, …) für die - in den meisten Fällen - nur einmal zu erbringende Leistung.

#### Indirekter Bestellung über ISP

![Indirect Order](/assets/conversation_indirect@2x.png){ align=center, loading=lazy }

In dieser Variante übernimmt der ISP die Abwicklung und ist, zumindest bei den kommerziellen Themen, der alleinige Ansprechpartner. Aus Sicht des Kunden sieht dieses Modell ähnlich aus wie bei einem vollintegrierten Anbieter. Der gesamte Geschäftsfall der Herstellung wird in der Kaskade von Kunde zu ISP, ISP zu ANO und ANO zu PIP (und wieder retour) abgewickelt werden. Eine OAID wird - zu Beginn - nicht benötigt. Spätesten beim ersten Wechsel des Internet Kunden (z.B. neuer Mieter) muss eine Verifikation möglich sein, der neue Mieter benötigt dazu das Identifikationsmerkmal seines Anschlusses.

Die Beispiele zeigen Varianten der Implementierung auf. Es soll vor allem verdeutlichen, dass das Konzept für OAID und Faserlink-Bezeichnung unabhängig von der jeweiligen Vorgehensweise ist. Wird eine Bezeichnung der Faserlinks unmittelbar und in der Interaktion von PIP und ANO sofort benötigt, zeigt sich die Bedeutung der OAID erst im zeitlichen Verlauf der Nutzung durch den Kunden (und insbesondere dessen Nachfolger).

## Rollen im 4LOM

Die bekannten Rollen aus dem 3LOM werden um zwei Rollen erweitert. Am Beginn des Prozesses steht der jener Kunde, der die Infrastruktur erstmalig errichten lässt, während der weiteren Lebensdauer ist der Kunde Vertragspartner des ISP.

`Kunde Infrastruktur`
: Endkunde, der beim Infrastruktur-Anbieter die Herstellung des Glasfaser-Anschlusses beauftragt. Die Beauftragung kann direkt oder über eine - den Bestellvorgang abwickelnde - Instanz erfolgen. Die kundenseitige Errichtung kann - je nach Herstellungsvereinbarung - mit oder ohne Eigenleistung bzw. Verantwortung des Kunden erfolgen. Der Endkunde erhält vom Infrastruktur-Anbieter die Open Access ID zur Bestellung eines Internet-Dienstevertrages.

`Kunde ISP`	
: Endkunde, der auf der ihm zur Verfügung stehenden und eindeutig mit der Open Access ID bestimmten Glasfaser-Verbindung den Internet-Vertrag mit dem ISP abschließt.

`Internet Service Provider`
: Anbieter für den Zugang zum Internet und weiteren Telekommunikations-Dienstleistungen wie Telefon, TV usw. Für die Nutzung der Dienste erhält der ISP vom Kunden ein, üblicherweise monatlich zu entrichtendes, Nutzungsentgelt. Der ISP übernimmt vom ANO den Datenstrom am Aggregation Node und führt diesen weiter ins Internet.

`Active Network Operators`
: Aktivnetzbetreiber (Active Network Operator, ANO) ist das Bindeglied zwischen dem Diensteanbieter (ISP) und dem Bereitsteller der Infrastruktur (PIP). Mit der Zurverfügungstellung entsprechender Komponenten (Access Switches, Aggregation Nodes, ONT, …) ist der ANO in der Lage, den Datenfluss zwischen Aggregation Node und ONT aufzubauen.

`Physical Infrastructure Provider`
: Betreiber - und zumeist auch Errichter der Glasfaser-Infrastruktur - sorgt für die Herstellung der physischen Infrastruktur bzw. der Verbindung zwischen dem kundenseitigen Glasfaser-Abschlusspunkt (FTU) und netzseitigen Zugangspunkt im FCO (gleichzeitig Übergabepunkt zum ANO). Da das Netz ausschließlich passiv ist, ist der PIP speziell im Störungsfall auf die Informationen der übergeordneten Schichten (ANO, ISP und Endkunde) angewiesen. 



