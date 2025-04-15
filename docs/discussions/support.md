# Support-Funktionalitäten

Ist der Kunde von Beginn an in die Herstellung involviert, wird über den Herstellungsprozess gesorgt, dass der Kunde seine Open Access ID erfährt. Jedoch findet diese Herstellung nur einmalig statt, während hingegen die Nutzung der Infrastruktur auf dreissig oder mehr Jahre ausgelegt ist. Unterlagen oder Vereinbarungen, die dem Besteller der Infrastruktur übermittelt wurden, stehen nachfolgenden Kunden dann unter Umständen nicht mehr zur Verfügung. Damit dennoch sichergestellt ist, dass der jeweilige Standort von einem neuen Kunden eindeutig ermittelt, also die OAID eruiert werden kann, ist ein Paket von mehreren Maßnahmen sinnvoll.

### Kennzeichnung der physischen Abschlüsse
Wie im Bild im Kapitel physische Darstellung ersichtlich werden kundenseitig mehrere Elemente eingebracht. Da die OAID vom PIP zur Verfügung gestellt wird, bieten sich zur Kennzeichnung die Netzelemente FTU und/oder BEP an. Auch eine Kennzeichnung am REP, wenn dieser z.B. frei zugänglich ist, wäre möglich.

Bei der Wahl der Beschriftung sollte eine möglichst langlebige und dem Einsatzort (innen, außen) entsprechende Variante gewählt werden. Die Montage vor Ort findet durch geschultes Fachpersonal statt. Die Durchführung beinhaltet auch Prüfung und Dokumentation. Daher bietet sich dieser Moment auch für die Erstellung und Anbringung der Beschriftung an.


### Elektronische Abfrage der potenziellen Glasfaser-Gebiete

![Feasibility Check](/assets/feasy_check@2x.png){ align=center, loading=lazy }

Damit Kunden möglichst einfach die Verfügbarkeit von Glasfaser an ihrem Standort prüfen können benötigen sie Informationen zur Verfügbarkeit der passiven Infrastruktur und den an ihrem Standort möglichen Anbietern und deren Produkte. Informationen zum ANO werden in der Regel nicht benötigt.
Diese Verfügbarkeitsabfrage nennt man Feasibility Check. Der Feasibility Check basiert im wesentlichen auf einer übermittelten Koordinate. Da Kunden in der Regel nur ihre Adresse, nicht aber die Position kennen, ist u.U. eine Auflösung der Adresse zur Koordinate davor zu schalten (Geokodierung).

Der Feasibility Check enthält Informationen wie aktuellen Ausbauzustand des Netzes (in Planung, in Bau, in Betrieb - plan, construct, operate)
Kosten sowie Bedingungen und Voraussetzungen für die Errichtung (Entgelte und Vertragsbestimmungen)
Hinweis auf das Datum der Errichtung bzw. Herstellungsdauer
Übersicht der Internet-Diensteanbieter und deren Produkte
Informationen zum ANO werden in der Regel nicht benötigt. Der Feasibility Check ersetzt auch keinesfalls eine technische Prüfung der Realisierbarkeit des Anschlusses am angefragten Standort (etwaige Probleme werden erst in der Detailplanung oder sogar erst während der Errichtung sichtbar). Weiters ist es für den PIP nicht notwendig, Detailinformationen zum Netz (z.B. genaue Trassenführung) bekannt zu geben. Ausreichend sind Hüllkurven über die Netzgebiete. Die Verwendung von Polygonen bietet den Vorteil auch Adressen zu inkludieren, die ursprünglich nicht im Fokus gewesen oder aufgrund einer zu ungenauen Geokodierung rausgefallen wären.

### Elektronische Abfrage bestehender OAIDs

![OAID Check](/assets/oaid_check@2x.png){ align=center, loading=lazy }

Die Abfrage geplanter (= bestellter) oder bestehender Standorte unter Verwendung der zugehörigen OAID ist ein berechtigtes Interesse aller übergeordneten Schichten. Abhängig von der abfragenden Rolle existieren verschiedene Vertrauensstufen. Je niedriger diese Stufe, desto höher sollten die Sicherheitsmerkmale ausfallen. Ein ANO muss, da er für den aktiven Betrieb verantwortlich ist, jederzeit die in seinem Gebiet geplanten und existierenden Standorte und deren Status kennen. Ein ISP muß in der Lage sein, Anfragen von Kunden zuverlässig zu beantworten, darf jedoch keine Informationen über die Nutzung des Anschlusses bei anderen ISPs haben. Ein Kunde hat berechtigtes Interesse, die Errichtung seines bestellten Anschlusses mitzuverfolgen. Usw.
Dieses Anforderungen müssen kein Widerspruch sein, erfordert aber eine sorgfältige Konzeption der Schnittstellen. Zwischen ANO und PIP kann, aufgrund der ohnedies bestehenden vertraglichen Vereinbarung, ein Zugriff auf alle Standorte innerhalb der Nutzregion vereinbart werden. Bei Anfragen durch ISP und potenzielle Kunden - im Allgemeinen besteht hier keine vertragliche Vereinbarung - sind erweiterte Mechanismen notwendig um zwischen dem Schutz der Infrastruktur und Privatsphäre sowie berechtigtem Interesse zu unterscheiden. Es bietet sich an, lokale Ortskenntnisse als Sicherheitsmerkmale mit einzubeziehen. Die Abfrage einer OAID könnte für diese Nutzer nur dann zum Erfolg führen, wenn beispielsweise die richtige Postleitzahl, eine Koordinate innerhalb eines Suchradius oder ähnliches mitgesendet wird. In allen Fällen bedeutet es, dass die Verwaltung von OAIDs zusätzliche, absoluten und relative geographischen Attribute notwendig macht. Diese Merkmale sind darüber hinaus permanent an die sich ändernden Umwelten anzupassen (z.B. Änderung der Adressbezeichnung, Änderungen der Postleitzahl, Parzellierungen, Gemeindezusammenlegungen usw. …). Bei der Wahl der Merkmale sind jene zu bevorzugen, die dem durchschnittlichen Endkunden geläufig sind (z.B. Postleitzahl vs. Gemeindekennziffer). Auch hier kommt der Erfassung des Ist-Zustandes bei der Montage ein gewichtiger Beitrag zu.
Denkbar wäre auch die Verwendung eines geheimen Kennwortes (vergleiche dazu Kundenkennwort bei Mobilfunkverträgen). Da die Nutzung auf mehrere Jahre ausgelegt und nicht an eine Person (natürlich oder juristisch) gebunden ist, stellt das keine erschöpfende Lösung dar.



