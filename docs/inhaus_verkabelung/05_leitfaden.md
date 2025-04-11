# Leitfaden

### Zusammenfassung

In diesem Abschnitt werden zusammenfassend die Empfehlungen der OFAA für die LWL-Inhausverkabelung dargestellt, welche in 
den folgenden Abschnitten begründet und im Detail ausgeführt werden. Betrachtet werden dabei alle Bereiche zwischen und 
inklusive dem DP und dem OTO.

- **A) Demarkationspunkt:**
    - Der DP wird in einem abschließbaren Raum oder Verteilerkasten mit Zugang zu Allgemeinstrom errichtet. Er bildet den Übergabepunkt von vorgelagerten LWL-Access-Netzen und internen LWL-Diensten zur IHV. Innerhalb von Gebäuden ist dieser identisch mit dem Hausübergabepunkt (HÜP), wenn er außerhalb eines Gebäudes situiert ist, mit dem Grundstücksübergabepunkt (GÜP).
    - Der DP soll in einem der Anzahl der zu versorgenden ENE entsprechenden Gebäudeverteiler, idealerweise einem 19“-Rack, untergebracht werden.
    - Zentraler Bestandteil des DP ist eine geeignete Spleißbox, in der die Faserüberlängen (mind. 2 m) der einzelnen ENE im Zuge der Errichtung der IHV in Spleißkassetten versorgt und für vorgelagerte LWL-Access-Netze und interne LWL-Dienste bereitgestellt werden.
- **B) Verrohrung:**
    - Die Verrohrung erfolgt durchgängig vom DP bis zum jeweiligen OTO durch individuelle halogenfreie, selbstverlöschende und raucharme Mikroröhrchen der Dimension 3/2.1 mm oder größer.
    - Dabei können Multitubes als Steigrohre verwendet werden, welche in den einzelnen Etagen mittels Steckmuffe durch Einzelröhrchen bis zu den ENE verlängert werden.
    - Die Enden der Röhrchen am DP werden mit geeigneten Materialien in der Form „Top-Nr./Stockwerk“ nachhaltig beschriftet.
    - Unabhängig von der Anbindung der ENE soll pro Stiegenhaus ein separates Mikroröhrchen der Dimension 12/10 mm oder größer für künftige Dienste für das Gesamtgebäude vorgesehen werden, das vom DP bis zum Dachraum reicht.
- **C) Verkabelung:**
    - Es werden Single-Mode-Kabel der Type ITU-T G.657.A1 oder A2 mit 8 Fasern verwendet. Dabei können nutzerseitig vorkonfektionierte Kabel (LC-Stecker bzw. vollständig angebrachter OTO) verwendet werden.
    - Es sollen Kabel der Brandschutzklasse Eca oder höher bzw. entsprechend geprüfte Gesamtsysteme (Rohr und Kabel) verwendet werden.
    - Bei Verfügbarkeit von Spleißarbeit soll für zum Zeitpunkt der IHV-Errichtung vorhandene vorgelagerte OAN-Access-Netze je ein Pigtail LC/APC angebracht werden, um eine patchbare Verbindung mit klarem Verantwortungsübergang und einer Prüfschnittstelle herstellen zu können.
    - Trifft Punkt 10. nicht zu, obliegt die Verbindung der einzelnen Fasern der IHV zu den Fasern der vorgelagerten Netze letzteren. Diese entscheiden nach ihrem Ermessen, ob für die von ihnen jeweils genutzte/n Faser/n eine direkte Spleißverbindung ausreicht, oder ob eine Patchverbindung hergestellt werden soll.
    - Als Prüfschnittstelle auf der Endkundenseite dienen die vorhandenen Steckverbindungen in der OTO.
- **D) Endkundenschnittstelle:**
    - Der OTO ist mit bis zu 8 Steckern vom Typ LC/APC bestückt. Jene Fasern, welche für die tatsächliche Verbindung zu vorgelagerten Access-Netzen oder die konkrete Nutzung interner Dienste fix vorgesehen sind, müssen jedenfalls mit Steckern bestückt sein, um einen zeitnahen neuerlichen Zutritt zu den in Nutzung stehenden ENE zu vermeiden. 
    - Die restlichen Fasern können mit geeigneten Überlängen in der OTO abgelegt werden und müssen bei entsprechendem künftigem Bedarf nachträglich konfektioniert werden.
- **E) Messung:**
    - Nach der Installation soll auf jeder Faser, die beidseitig über einen Stecker verfügt von Seiten der ENE zumindest eine Dämpfungsmessung durchgeführt und dokumentiert werden. Im Falle des Punkt 11. ist auf jenen Fasern, die nur auf Seite des OTO über einen Stecker verfügen, eine Laser-Rotlichtmessung durchzuführen.
- **F) Open Access ID:**
    - Am OTO wird mittels Aufkleber die von der OFAA kostenlos zugewiesene OAID angebracht.
- **G) Betrieb:**
    - Die IHV sollte von einem einschlägigen Unternehmen betrieben, serviciert und entstört werden.

<figure markdown="span">
  ![Inhausverkabelung](/assets/inhaus_verkabelung.png){ width="100%"}
  <figcaption>Abbildung 1: Schematische Darstellung Inhaus-Verkabelung</figcaption>
</figure>

### Allgemein

##### IHV im Eigentum und Besitz des MPO

Die gesamte IHV nach diesem Leitfaden soll jedenfalls im Zuge des Neubaus oder der Sanierung eines MPOs im Namen und auf 
Rechnung des Objekteigentümers errichtet werden und dauerhaft in dessen Eigentum und Verantwortung verbleiben. Nur so wird 
sichergestellt, dass die Infrastruktur jedem vorgelagerten PIP (Open Access) wie auch den Objekteigentümern oder Mietern 
selbst für alle künftigen Anwendungen uneingeschränkt zur Verfügung steht.


##### Unentgeltliche Bereitstellung

Die für die Bereitstellung von Diensten benötigten Fasern der Inhausverkabelung (IHV) sollen, ähnlich wie im Stromnetz, 
den vorgelagerten Netzbetreibern und Diensteanbietern kostenlos zur Verfügung gestellt werden. Sollte dafür eine Gebühr 
erhoben werden, würde diese von den Internetanbietern auf die Endkundentarife im Gebäude umgelegt und somit keinen 
wirtschaftlichen Vorteil für das Mehrparteienobjekt (MPO) bringen. Stattdessen würde so nur zusätzlicher Verwaltungsaufwand 
verursacht.

Die bereitgestellten Dienste der Provider werden grundsätzlich in der jeweiligen Ortszentrale übergeben. Eine Ausnahme 
von diesem Grundsatz können sehr große MPOs bilden (über 100 ENE), bei denen es aufgrund der hohen benötigten Faserzahl 
sinnvoll sein kann, eine kleine aktive Übergabestelle am Demarkationspunkt vorzuhalten. 

### Demarkationspunkt

Der Demarkationspunkt bezeichnet die Stelle, an der die IHV endet und die Verbindung zu einem oder mehreren vorgelagerten 
LWL-Netz/en gepacht oder gespleißt hergestellt wird. Hier enden Eigentum und Verantwortung des MPOs und beginnen Eigentum 
und Verantwortung des vorgelagerten Netzes.

##### Zugangs-beschränkung

Aus Sicherheitsgründen muss dieser Punkt vor unberechtigtem Zugriff geschützt sein und soll daher in einem abgeschlossenen 
Raum oder Verteilerschrank situiert werden. Der Zugang für externe Dienstleister sollte mit Ausnahme des für den IHV-Betrieb 
zuständigen Entstördienstes nur über die Hausverwaltung oder einen dafür vorgesehenen Schlüsseltresor möglich sein.

##### Stromversorgung

Am DP ist eine zugängliche Stromversorgung (Allgemeinstrom des MPOs) vorzusehen, um allfällig erforderliche aktive Netzkomponenten 
der Haustechnik (smart building) versorgen zu können. Sollte kein vorgelagertes LWL-Netz, sondern lediglich ein Kupfer- 
bzw. Koax-Netz zur Verfügung stehen, kann der Netzbetreiber hier seine Aktivtechnik für die Umsetzung auf die IHV situieren.


##### Verteilerschrank bzw. 19“-Rack

Ein Gebäudeverteilerschrank, idealerweise ein 19“-Rack, dessen Größe auf die Anzahl der zu versorgenden Endnutzeranschlüsse 
abgestimmt wird, soll die Kassetten für die zu versorgenden Überlängen der IHV-Verkabelung aufnehmen und Platz für Geräte 
der vorgelagerten LWL-Netze (z.B. Splitter, wenn die vorgelagerten Fasern zur Versorgung aller ENE nicht ausreichen – P2MP) 
oder interner Datenkommunikationsanwendungen bereitstellen.

##### Beschriftung

Es ist sehr wichtig, die einzelnen Kassetten mittels geeigneten Materials nachhaltig zu beschriften, um eine effiziente 
Faserverbindung und Entstörung sicherzustellen. Dabei soll die TOP-Nr. der ENE und idealerweise auch das Stockwerk 
angeführt werden.

Bei sehr großen MPOs (Richtwert: mehr als 100 ENE) sollte in unmittelbarer Nähe des DP ausreichend Platz für eine kleine 
mit aktiven Geräten ausgestattete Übergabestelle/Ortszentrale sein. Kosten und Verantwortung für die dort eingesetzte 
Ausstattung liegen vollständig bei dem betroffenen vorgelagerten LWL-Netz.

### Verrohrung

##### Durchgängige Verrohrung ohne Etagenverteiler

Die Verrohrung der IHV sollte, wenn möglich, auf Etagenverteiler verzichten und stattdessen durchgängig vom DP bis zu 
jeder einzelnen ENE (Technikschrank, Wohnungsverteiler) mittels dedizierter Mikroröhrchen erfolgen. Dabei können in den 
Steigbereichen Multitubes verwendet werden, welche in den Etagen mittels Steckmuffen auf Einzelröhrchen verlängert werden. 
Damit ist auch die Einhaltung des minimalen Biegeradius der eingesetzten Verkabelung innerhalb der Verrohrung sichergestellt. 
In Etagenverteilern muss jedenfalls gespleißt werden, was mittels durchgängiger Röhrchen vermieden werden kann. Nicht alle 
Elektrounternehmen, welche als Anbieter infrage kommen, sind (bisher) für Spleißarbeiten ausgerüstet bzw. dazu in der Lage. 
Außerdem ist innerhalb der Etagenverteiler auf die Einhaltung des minimalen Biegeradius der Verkabelung besonders zu achten.

##### Etagenverteiler bei sehr großen MPOs

Bei sehr großen MPOs werden aufgrund der hohen Anzahl von ENE Etagenverteiler notwendig sein. In diesem Fall ist das 
Einbringen vorkonfektionierter LWL-Kabel nicht mehr sinnvoll. Es muss daher als Steigleitung ein entsprechend dimensioniertes 
Rohr der Dimension 12/10 mm oder größer verwendet werden, welches ein hochfaseriges Kabel aufnehmen kann, das zur Versorgung 
aller ENE ausreicht. In den Etagenverteilern werden die einzelnen Fasern der Steigleitung mit den jeweiligen Fasern der 
Endnutzerkabel gespleißt.

##### Microducts 3/2.1 mm halogenfrei, raucharm und selbstverlöschend

Ohne den Einsatz von Etagenverteilern bzw. im Fall von deren Verwendung für den Abschnitt von diesen bis zum OTO wird die 
gängige Dimension von LWL-Mikroröhrchen 3/2.1 mm (im Steigbereich ggf. als Rohrverbund) halogenfrei, raucharm und selbstverlöschend 
empfohlen. Diese weisen einerseits einen sehr geringen Gesamtquerschnitt auf (Qualmschutz) und benötigen sehr wenig Platz 
in den Schächten. Trotzdem bieten sie andererseits noch ausreichend Platz für das Einziehen bzw. Einblasen der LWL-Kabel. 

Nach Bedarf bzw. Verfügbarkeit können auch Rohre mit größeren Innendurchmessern bzw. klassische Flexrohre verwendet werden. 
Dabei sind selbstverständlich die einschlägigen Brandschutzvorschriften zu beachten (OIB Richtlinie 2, OVE E 8101 -> Rohre 
nach EN 61386).


##### Beschriftung Microducts

Es ist sehr wichtig, die einzelnen Röhrchen auf Seiten des DP mittels geeigneten Materials nachhaltig zu beschriften, um 
eine effiziente Belegung und ggf. Entstörung sicherzustellen. Dabei soll die TOP-Nr. der ENE und idealerweise auch das 
Stockwerk angeführt werden.

Bei Einsatz von Etagenverteilern macht die Beschriftung des Steigrohrs am DP keinen Sinn. Es müssen daher in diesem Fall 
die Spleißkassetten bzw. Überlängenspeicher nach Herstellung der Verkabelung beschriftet werden.

##### Separates Röhrchen für das Gebäude

Ein dediziertes Mikroröhrchen der Dimension 12/10 mm oder größer für das Gesamtgebäude soll Platz für eine nachträglich 
einbringbare Verkabelung bieten, welche künftige interne Anwendungen (SAT-Anlage, Smart-Building, Sensorik) oder die Anbindung 
einer Mobilfunkantenne (small cells) ermöglichen kann. Dieses Röhrchen soll vom DP durch alle Stockwerke bis zum Dachraum 
führen und muss, solange es nicht befüllt wird, mit Endkappen ordnungsgemäß verschlossen bleiben. Bezüglich der Anzahl 
und Dimensionierung von Elektroinstallationsrohren ist die OVE E 8015 heranzuziehen.

### Verkabelung

##### ITU-T G.657.A1

Für die Verkabelung in der IHV werden Single-Mode-Fasern des Typs ITU-T G.657.A1 empfohlen. Diese Faser weist einen minimalen 
Biegeradius von 10 mm auf, sodass sie für Gebäudeverkabelungen auf der allerletzten Meile besonders gut geeignet ist. 

Falls eine durchgängige Verrohrung durch den notwendigen Einsatz von Etagenverteilern nicht möglich ist und es die räumlichen 
Bedingungen in diesen Verteilern erfordern, wird der Faser-Typ G.657.A2 mit einem minimalen Biegeradius von lediglich 7,5 mm empfohlen.

Die vorgelagerten LWL-Access-Netze arbeiten durchwegs mit Single-Mode-Fasern des Typs ITU-T G.652.D, welche mit G.657.A 
voll kompatibel sind und somit direkt verbunden werden können. 

##### 8 Fasern

Obwohl die Norm DIN EN 50700 lediglich zumindest 2 Fasern pro ENE vorsieht und in der Praxis bisher häufig 4-faserige Kabel 
verwendet werden, wird aus den folgenden Gründen empfohlen, Kabel mit 8 Fasern zu verwenden:

- Die Kostenunterschiede zwischen LWL-Kabeln mit 4 und solchen mit 8 Fasern sind bezogen auf das Gesamtprojekt minimal. Auch der Verlegeaufwand unterscheidet sich in der Regel nicht, wenn keine Spleiße innerhalb der IHV durchgeführt werden müssen (Etagenverteiler). 
- Röhrchen der Dimension 3/2.1 mm sind uneingeschränkt auch für 8-fasrige Kabel mit einem Kabeldurchmesser bis 1.4 mm geeignet.
- Durch die Verfügbarkeit ausreichender (Reserve-)Fasern kann bei späterem Bedarf auf teure WDM-Lösungen verzichtet werden.
- Ein späteres Austauschen der Inhauskabel bei höherem Faserbedarf ist zwar möglich, erfordert jedoch erheblichen zusätzlichen Aufwand und ein neuerliches Betreten der Nutzereinheiten.
- Die Fasern müssen am DP nicht vorab aufgelegt werden. Dies kann im notwendigen Ausmaß anlassbezogen bzw. nach praktischer Notwendigkeit durch das oder die vorgelagerte/n Netz/e bzw. internen Telekommunikationsdienste erfolgen.
- Sollte ausnahmsweise mehr als ein vorgelagertes LWL-Access-Netz (eventuell auch zu einem späteren Zeitpunkt) Zugang zu den Endkunden des MPO begehren, ist für jedes Netz eine eigene dedizierte Faser vorhanden und ein Umpatchen bei künftigem Wechsel des Internet-Anbieters nicht erforderlich.
- Es sollten jedenfalls ausreichend Fasern für zukünftige Anwendungen abseits der Access-Netze zur Verfügung stehen (beispielhafte Aufzählung):
- SAT-Verkabelung: Nach dem Stand der Technik ist die Verkabelung einer Haus-Satellitenanlage mit LWL anstelle von Koax problemlos sowie kostengünstig und wird in jüngerer Zeit mehr und mehr zum Standard. Dabei sollte aus Wirtschaftlichkeitsgründen für jede Satellitenposition eine separate Faser zum Endkunden zur Verfügung stehen (z.B. Astra und Eutelsat). In diesem Fall empfiehlt sich eine separate Verrohrung samt höherfaserigem LWL-Kabel vom DP zu der/den Satellitenantenne/n.
- RFoG: Wenn auch die Zukunft des kabelgestützten Fernsehens wohl dem IPTV gehört, gibt es noch zahlreiche DOCSIS-Netzwerke, welche jedoch mehr und mehr von Koax auf Glasfaser umstellen.
- Smart-Building: Das Internet der Dinge bringt in Zukunft nach dem Modell des digitalen Zwillings zahlreiche Anwendungen zur Echtzeit-Überwachung und -steuerung von Gebäuden und Liegenschaften, welche neben Funkschnittstellen (LoRaWAN, 5G/6G-Slice) in vielen Fällen auch Festnetzanbindungen über LWL nutzen werden.
- Sensorikfasern: Mittels dedizierter Glasfaser sind stromunabhängige Alarmierungen und andere OTDR-basierte Dienste möglich, welche die einzelne Faser als Sensor nutzen.
- Quanteninternet: In etwas fernerer Zukunft wird auch das in Österreich weltweit führend entwickelte Quanteninternet neue Anwendungen der sicheren Datenübertragung ermöglichen. Dabei ist jedoch eine dedizierte durchgängige Faser (P2P, nicht P2MP!) bis zum Endnutzer erforderlich.

Ausdrücklich wird darauf hingewiesen, dass der Einsatz von 8 Fasern nach obiger Begründung als absolut zukunftstauglich 
bei maximal eingesetzten möglichen Anwendungen gesehen wird. Dies wird in der Praxis nur selten der Fall sein. Der Einsatz 
von 4-faserigen Kabeln wird daher in der überwiegenden Anzahl der Fälle jedenfalls auch mittel- bis langfristig ausreichend sein.

##### Brandschutzklasse E~ca~ oder besser

Obwohl die OIB-Richtlinie 2 in der aktuellen Ausgabe vom Mai 2023 in Z. 3.4.6 für Einzelleitungen von Messeinrichtungen bzw. 
Kommunikationskabeln (z.B. Internet, Kabelfernsehen) keine brandschutztechnischen Anforderungen mehr stellt, sollte das 
verwendete Kabel in Anlehnung an Tabelle 1a Z 2.5 besagter Richtlinie zumindest der Brandschutzklasse E~ca~ der europäischen 
Bauproduktenverordnung oder besser entsprechen. Dabei besteht die Möglichkeit für die Hersteller, Rohre und Kabel als System 
in die entsprechende Klasse prüfen zu lassen.

##### OTO vorkonfektioniert

Die Vorkonfektionierung auf Seite des Endkunden durch die Montage des OTO ermöglicht das Einziehen bzw. Einschieben/Einblasen 
des Kabels von der Endnutzereinheit bis zum DP ohne das Erfordernis, Spleißarbeiten durchzuführen. Viele Elektriker sind 
aktuell noch nicht auf solche vorbereitet und müssten diese Tätigkeiten auf spezialisierte Subunternehmen auslagern. 
Außerdem ist die Vorkonfektionierung aufgrund automatisierter industrieller Abläufe deutlich schneller und günstiger möglich 
als die Konfektionierung des OTO durch den verlegenden Handwerker vor Ort.


##### Empfehlung von Pigtails für Access-Netze am DP

Ist der ausführende Elektriker auf Spleißarbeiten ausgerichtet, empfiehlt sich am DP die Anbringung von Pigtails des Typs 
LC/APC für jede Faser, welche an ein vorgelagertes Access-Netz angeschlossen werden soll, um einen klaren Verantwortungsübergang 
und eine Prüfschnittstelle zu gewährleisten.

##### Alternativ: Konfektionierung am DP durch PIP

Andernfalls erfolgt auf der Seite des DP die Spleißverbindung durch Fachpersonal des jeweils die Faser nutzenden vorgelagerten 
LWL-Netzes. Dieses hat selbst zu entscheiden, ob die Verbindung durchgespleißt (kostengünstig), oder ob mittels Pigtail 
eine patchbare Verbindung hergestellt werden soll, welche auch die jederzeitige isolierte Prüfung der Inhausfaser von 
Seiten des DP ermöglicht. Diese Vorgangsweise wird auch für alle internen LWL-Dienste empfohlen.

##### Grundsätzlich keine patchbare Verbindung am DP nötig

Die grundsätzliche Herstellung von patchbaren Verbindungen durch das MPO auf Seiten des DP für alle Fasern würde einen 
erheblichen Zusatzaufwand erfordern, der nur in den seltensten Fällen notwendig sein wird. In den meisten Fällen ist 
aufgrund der jedenfalls ausreichend vorhandenen Fasern in der IHV ein Durchspleißen zu vorgelagerten LWL-Netzen für eine 
dauerhafte exklusive Nutzung der betroffenen Faser die günstigste und praktikabelste Lösung. Ein späteres „Umpatchen“ ist 
jedenfalls nicht erforderlich.

##### Überlängen

Am DP sind mindestens 2 Meter Überlängen vorzusehen und auf den dafür vorgesehenen Kassetten je Endnutzereinheit zu 
versorgen (Überlängenspeicher).

##### Fasernutzung

Mit einem festgelegten Farbkonzept wird zumindest pro MPO sichergestellt, dass die Nutzung der einzelnen Fasern der ENE 
stets nach dem gleichen Muster erfolgt. 

Da in den Kabeln der diversen Hersteller teils unterschiedliche Faserfarben verwendet werden, wird hier lediglich die 
Nummerierung angeführt:

Faser 1: Vorgelagertes LWL-Access-Netz 1 

Faser 2: Vorgelagertes LWL-Access-Netz 2 

Faser 3: Vorgelagertes LWL-Access-Netz 3 / RFoG / Reserve 

Faser 4: SAT-Anlage Pos. 1 

Faser 5: SAT-Anlage Pos. 2 

Faser 6: SAT-Anlage Pos. 3 / Reserve

Faser 7: Smart-Building/Smart-Home 

Faser 8: Sensorik

Bei Bedarf kann davon natürlich abgewichen werden. Dies sollte aber am DP dokumentiert sein. Weiterführende Informationen 
zur Installation der Verkabelung sind der ÖVE EN 50174-2 zu entnehmen.


### Endkundenschnittstelle

##### LC/APC

Analog zur Norm DIN EN 50700 sollen die aufgelegten Fasern in der OTO mit LC/APC-Steckern zugänglich sein, welche durch 
den Schrägschliff eine hervorragende Rückflussdämpfung von mindestens -60 dB aufweisen. Dies ist eine der meistverbreiteten 
Steckernormen und bietet aufgrund des geringeren Platzbedarfs gegenüber den gleichwertigen SC/APC-Steckern im OTO für 8 
Anschlüsse eine ausreichend hohe Packungsdichte. Grundsätzlich können auch SC/APC-Stecker verwendet werden. Deren höherer 
Platzbedarf verhindert jedoch im Regelfall die Nutzung von mehr als vier Fasern im OTO.

Geschützte E2000-Stecker sind erheblich teurer und aufgrund der niedrigen Laserleistung (Laserklasse 1M gem. EN-60825-1) 
an dieser Stelle nicht erforderlich.

Im OTO müssen zumindest all jene Fasern, welche am DP eine Steckverbindung aufweisen oder auf ein vorgelagertes Access-Netz 
bzw. einen (geplanten) internen Dienst direkt gespleißt werden, eine (idealerweise vorkonfektionierte) Steckverbindung 
aufweisen. Für die übrigen Fasern sind entsprechende Überlängenspeicher vorzusehen.

##### Wohnungsverteiler

Der OTO soll im oder in der Nähe des Wohnungsverteiler/s untergebracht werden. Dort terminiert auch in der Regel die strukturierte 
Wohnungsverkabelung. An diesem Punkt endet auch die Inhausverrohrung.

### Messung

##### Dämpfungsmessung bei zwei Steckern

Zur Messung/Prüfung der Fasern soll nach dem Einziehen des Kabels von Seiten der Endnutzereinheit auf allen Steckern des 
OTO, deren Fasern auch am DP über einen Stecker verfügen, eine Dämpfungsmessung mittels Lichtquelle und Dämpfungsmessgerät 
durchgeführt werden.

##### Laser-Rotlicht-Messung am OTO

Zur Messung/Prüfung jener Fasern, welche nur im OTO über einen Stecker verfügen, kann zumindest eine Laser-Rotlichtmessung 
durchgeführt werden. Diese zeigt die grundsätzliche Lichtdurchgängigkeit der Faser, nicht jedoch die konkreten Dämpfungswerte. 

##### OTDR-Messung

Empfohlen wird aus Gewährleistungsgründen (Vermeidung eines versteckten Baumangels mit der ausdrücklich zugesicherten 
Eigenschaft der materialüblichen Dämpfungswerte) vor allem bei der Verwendung von Etagenverteilern eine OTDR-Messung. Das 
Messprotokoll ist dem Auftraggeber bei Gewerkübergabe auszuhändigen. Die Messung kann ggf. auch durch ein anderes Unternehmen 
durchgeführt werden als jenes, welches die Installation zu verantworten hat.


### OAID

##### Kostenlose OAIDs

Die Open-Access-ID wird von der OFAA entwickelt und verwaltet. Sie bezeichnet als 8-stellige Zahlen- und Ziffernkombination 
eindeutig den Endpunkt (Endnutzerschnittstelle) einer Glasfaserleitung und dient dem einfacheren Handling aller kundenbezogenen 
Prozesse für die involvierten Akteure (PIP, ANO, ISP, Entstördienst, etc.). Sie wird im Regelfall auf der OTO-Dose sichtbar 
aufgeklebt, um bei Kundenkontakten sofort verfügbar zu sein. Die OAID wird auf Lebenszeit des Objektes und der Leitungen 
vergeben und ändert sich nie, auch wenn sich z.B. die Adresse einer Liegenschaft ändern würde oder ein anderer Kunde die 
Nutzungseinheit bezieht.

Ergänzt wird die OAID durch die OLID, welche mittels Suffixes die einzelnen Fasern des jeweiligen Endkundenanschlusses nummeriert.

Da die IHV in der Regel unabhängig von vorgelagerten LWL-Netzen errichtet wird und ggf. auch mehreren von diesen zur Verfügung 
steht, ist es erforderlich, die OAID bereits im Zuge der Errichtung der IHV zuzuordnen. Nur so kann sie in allen späteren 
Prozessen (Zusammenschluss einzelner Fasern mit vorgelagerten Netzen, Bestellung von Internetdiensten, Entstörung) als 
eindeutige Kennung der betroffenen ENE dienen.

Da diese OAIDs damit aber nicht aus dem Portfolio eines einzelnen vorgelagerten PIP stammen können, ist es erforderlich, 
diese im Zuge der Errichtung der IHV direkt von der OFAA zu beziehen und eine spätere Fremdzuordnung von OAIDs in den 
Softwaresystemen der PIPs zu ermöglichen.

Die Vergabe der OAIDs für ein MPO, das mit IHV ausgestattet wird, sollte mittels online-Portal kostenlos (ansonsten wird 
die Akzeptanz mangels rechtlicher Verpflichtung nicht erreicht) direkt über die OFAA erfolgen. Der diesbezügliche Prozess 
ist noch zu definieren.

### Betrieb

##### IHV-Netzbetrieb und Entstörung

Für den laufenden Betrieb, die Servicierung und die anlassbezogene Entstörung der IHV empfiehlt sich die Beauftragung eines 
einschlägigen Unternehmens. Dies kann der errichtende Hauselektriker oder ein spezialisiertes regionales Unternehmen sein. 
Dieser Dienstleister muss jedoch in der Lage sein, LWL-Fasern per OTDR zu messen und Glasfasern zu spleißen, um im Schadensfall 
Störungen beseitigen zu können. Dazu empfiehlt sich, über die Hausverwaltung ein passendes SLA einzugehen, das auf den 
jeweiligen Bedarf (private oder wirtschaftliche Nutzung, maximal zulässige Entstörzeiten) abstellt und über die Betriebskosten 
abgerechnet wird. Da Störungen der IHV erfahrungsgemäß äußerst selten auftreten, sollte dieser Kostenfaktor keine große 
Rolle spielen.




