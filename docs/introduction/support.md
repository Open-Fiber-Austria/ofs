# User Stories

Exemplarische Anwendungsfälle, wie sie im Laufe der Nutzung vorkommen könnten.

#### Feasibility Check
Die Infrastrukturbetreiber erstellen auf Basis ihrer Netze Gebiete, in denen Glasfaser geplant, gebaut oder bereits verfügbar ist. Als Minimalanforderung ist eine Verschneidung auf Basis von Geokoordinaten vorzusehen, die entsprechend der Kategorie des Gebietes Rückmeldung liefert. Koordinaten außerhalb dieser Gebiete sind abzuweisen.

Je nach Implementierung kann die Rückmeldung auch verfügbare Produkten und Preise für eine Herstellung beinhalten. Eine nachfolgende Bestellung einer Glasfaser-Herstellung ist i.A. nur bei positivem Feasibility Check

#### Bestellung eines Internet Service Vertrages
Im Zuge der Herstellung des Glasfaser-Anschlusses wurde der Kunde über seine Open Access ID informiert. Die Open Access ID befindet sich in den Unterlagen, aber auch auf dem Glasfaser-Abschluss (FTU), sodass eine Person vor Ort diese ablesen kann.

Bei Bestellung des Internet Dienstevertrages ist die Angabe der OAID verpflichtend. Gepaart mit den zusätzlichen Parametern der Bestellung, kann nun eine Verifizierung erfolgen. Der ISP übermittelt OAID und Angaben zum Standard an den PIP, dieser bestätigt die Existenz, den Status der OAID sowie die  annähernde Übereinstimmung mit der postalischen Adresse. Stimmen OAID und ungefähre Lage der übermittelten Adresse nicht überein, so ist die Annahme der Bestellung zu verweigern. Stimmen OAID und ungefähre Lage überein und ist der Standort gebaut, kann die Bestellungen angenommen werden.

In Mehrparteienhäusern sind zusätzliche, relative Ortsangaben vorzusehen (z.B. Türnummer).


#### Bestellung eines Internet Service Vertrages ohne bekannt Open Access ID
Ein Mieter hat die Wohnung übernommen und möchte einen Internet-Dienstevertrag abschließen. Vom Vormieter weiß er, dass prinzipiell Glasfaser verfügbar ist, der Internet Anbieter verlangt eine OAID, die er nicht kennt.

Der Mieter findet die OAID als Aufkleber (Typenschild) auf dem Faserabschluss (FTU). In Einfamilienhäusern und bei nur einer Nutzeinheit kann dieses Typenschild auch im BEP oder REP angebracht werden. In Mehrparteienhäuser bietet sich der zentrale Hausverteiler an: ähnlich wie bei den Stromzählern mit individueller Zählpunktnummer, der zentrale Technikraum oder ein Verteilerkasten im Stiegenhaus.

Ein generelles Problem entsteht, wenn ein Kunde keinerlei Informationen über die dem Standort zugeordnete OAID besitzt und sich diese vor Ort auch nicht feststellen lässt (zB Beschriftung von BEP oder FTU wurden bei Montage nicht durchgeführt, sind verblasst, ...). Eine korrekte OAID ist jedoch Voraussetzung für die Bestellung eines Internet-Dienstevertrages. In diesem Fall kann nur gemeinsam, in der Kommunikation mit Endkunde und PIP, die korrekte OAID identifiziert werden.

Es ist auf Seiten des Infrastrukturbetreibers bzw. der OAID Vergabestelle sicher zu stellen, dass Adressänderungen (zB geänderte Postleitzahlen) aktuell und historisch mit der OAID verknüpft sind. Eine Ungenauigkeit in der Abfrage (Geoverortung und Vergleich zur gespeicherten OAID) ist zu tolerieren.

