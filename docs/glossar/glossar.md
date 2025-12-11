# Glossar

*Klarheit für alle – Einheitliche Definitionen und Maßstäbe für transparente Glasfasernetze.*

Mit dem OFAA-Glossar schaffen wir eine gemeinsame Grundlage für zentrale Begriffe und Definitionen im Glasfaserausbau. 
Ziel ist es, Klarheit, Einheitlichkeit und Transparenz zu gewährleisten – damit alle Beteiligten in Glasfaserprojekten 
dieselbe Sprache sprechen: von der technischen Planung über die Förderabwicklung bis hin zum Netzbetrieb.

Das Glossar orientiert sich an bestehenden Vorgaben der EU, des Bundes sowie an relevanten Branchenstandards. Damit leisten 
wir einen Beitrag zur Harmonisierung der Terminologie und stellen sicher, dass einheitliche Begriffe in allen Prozessen 
Anwendung finden. Zugleich möchten wir das Bewusstsein für die Vielschichtigkeit der Begriffswelt innerhalb der Glasfaserbranche 
schärfen und eine konsolidierte Wissensbasis für unsere Mitglieder und Partner bereitstellen.

Ein zentrales Beispiel für die Notwendigkeit klarer Definitionen ist die bisher uneinheitliche Verwendung von Begriffen 
wie *„Homes Passed“* oder *„Haushalte“*. Während der Begriff *„Haushalt“* (laut Statistik Austria: Personen mit Hauptwohnsitz 
an einer Adresse) eine soziale Einheit beschreibt, eignet er sich für technische Planungen, Monitoring oder Förderlogiken 
nicht – da Haushaltsdaten weder geokodiert noch adressscharf öffentlich verfügbar sind. Aus diesem Grund wurde der Begriff 
*„Premise“* eingeführt, der eine eindeutig abgegrenzte technische Nutzungseinheit bezeichnet und direkt auf das BEV-Register 
verweist. Die *Premise* bildet damit die Grundlage für alle Ausbaustufen und Kennzahlen – von der potenziellen Erschließung 
bis zur aktivierten Nutzung.

Das OFAA-Glossar ist das Ergebnis gemeinsamer Arbeit des Teams OFAA-Glossar. Es stellt ein strukturiertes Begriffssystem 
entlang der technischen Schichten des Netzbetriebs bereit und wird auf [www.ofaa.at](https://ofaa.at) veröffentlicht. Alle 
Mitglieder der OFAA sind aufgerufen, die darin enthaltenen Definitionen anzuwenden – als verbindlichen Referenzrahmen für 
den österreichischen Glasfaserausbau.


## Grundsätzliches Überlegungen

- Begriffsdschungel vereinheitlichen, Homes Passed sagt jeder, aber jeder meint was anderes damit 


<figure markdown="span">
  ![Grundsätzliches Überlegungen](/assets/fttx_wolke.png){ width="80%"}
</figure>


- Haushalte und Homes sind nicht das Gleiche


    !!! info "Haushalt vs. Home"
    
        Ein **Haushalt** beschreibt eine soziale Einheit, d. h. Personen mit Hauptwohnsitz an einer Adresse (laut Statistik Austria). 
        Da Haushalte statistisch erfasst, aber nicht geokodiert oder adressgenau (öffentlich zugänglich) verfügbar sind, 
        **eignen sie sich nicht** zur Planung, Messung oder Bewertung von Ausbauzielen.

        **Home** ist ein technischer Begriff, der sich im Glasfaserausbau etabliert hat - insbesondere in den Formulierungen FTTH (Fiber to the Home) oder Homes Passed. <br>
        Anders als der sozialstatistische „Haushalt“ bezieht sich „Home“ in der technischen Planung auf eine adressierbare physische Nutzungseinheit, die potenziell an das Netz angeschlossen werden kann.
        Je nach Kontext kann „Home“ also eine oder mehrere Wohnungen, Geschäftseinheiten oder Einfamilienhäuser bezeichnen - unabhängig davon, ob dort aktuell ein Haushalt lebt.



- Breitbandverfügbarkeitsmeldungen (ZIB, RTR) sollen umgestellt werden auf BEV-Register (objektgenaue Meldung) →
sinnvollerweise passen die Definitionen auch mit den Elementen aus dem Register zusammen


    !!! info "BEV-Register"
        Mit dem [BEV-Register](https://www.bev.gv.at/Services/Downloads/Produktbezogene-Downloads/Unentgeltliche-Produkte/Adressregister.html)[^1] sind die **öffentlich zugänglichen** und im 6-Monatszyklus veröffentlichen **AGWR-Daten** gemeint


    - Eine Adresse hat ein oder mehrere Objekte. Ein Objekt hat eine oder mehrere Nutzungseinheiten (siehe Abbildung AGWR-Kennziffern[^2])
    - Glasfaser geht bei FTTH bis in die Nutzungseinheit, also sollte die Definition auf dieser Ebene ansetzen 
    - Erster Übersetzungsversuch von Nutzungseinheit: Premise (statt Home; Home wird schnell mit Haushalt verknüpft → problematisch)


<figure markdown="span">
  ![OBJNR-NTZLNR](/assets/objnr_ntznr.png){ width="80%"}
  <small>Quelle: [Statistik Austria: Kennziffern der Adressen](https://www.statistik.at/fileadmin/pages/489/AGWR_Allgemeines_Adressen.pdf)[^2]</small>
</figure>



[^1]: https://www.bev.gv.at/Services/Downloads/Produktbezogene-Downloads/Unentgeltliche-Produkte/Adressregister.html
[^2]: https://www.statistik.at/fileadmin/pages/489/AGWR_Allgemeines_Adressen.pdf


## Premises

**Warum überhaupt der Begriff „Premise“?**

Premise angelehnt an [“Guidelines on State aid for broadband network” der Europäischen Kommission, Chapter 2.2., Nr. 19l](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52023XC0131(01))[^3]:

: *(l) __‘premises passed’__ means __end users’ premises__ to which, upon request from end users and within 4 weeks from the
date of the request, an operator can provide broadband services (regardless of whether those premises are already
connected to the network or not). The price charged by the operator for providing such broadband services at end
users’ premises in this case must not exceed normal connection fees. This means that it must not include any
additional or exceptional cost as compared to the standard commercial practice and, in any case, must not
exceed the usual price in the Member State concerned. That price must be determined by the competent national
authority;*



Wird [in der deutschen Fassung](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:52023XC0131(01))[^4] mit „Räumlichkeiten“ übersetzt, inhaltlich sehr nahe an **„Nutzungseinheiten“**

: *(l) __„erschlossene Räumlichkeiten“__ Räumlichkeiten von Endnutzern, in denen ein Betreiber auf Antrag von Endnutzern
innerhalb von vier Wochen ab dem Datum des Antrags Breitbanddienste anbieten kann (unabhängig davon, ob die
betreffenden Räumlichkeiten bereits an das Netz angeschlossen sind oder nicht). Der vom Betreiber für die
Bereitstellung solcher Breitbanddienste in den Räumlichkeiten der Endnutzer berechnete Preis darf in diesem Fall
nicht höher sein als die normale Anschlussgebühr. Er darf also im Vergleich zur üblichen Geschäftspraxis keine
Zusatz- oder Sonderkosten beinhalten und in keinem Fall den in dem betreffenden Mitgliedstaat üblichen Preis
übersteigen. Dieser Preis muss von der zuständigen einzelstaatlichen Behörde festgelegt werden;*


`Definition` 

- Eine Premise ist eine Nutzungseinheit eines Objekts aus dem BEV-Register 
- Gibt es noch kein Objekt mit Nutzungseinheiten im BEV-Register, kann man in einer ersten Annäherung über
Katastralgemeindenummer + Grundstücksnummer gehen (KG+GNR) => für Identifikation und Verschlüsselung; Verortung ist
NICHT (exakt) möglich


`Erläuterungen` 

- Premise = Nutzungseinheit 
- Premise ist die kleinste Einheit 
- Wir brauchen die Ebene der Nutzungseinheit in den öffentlich zugänglichen Daten als eigenes Datenbank-Objekt.
Technologie entscheidet; FTTP/H => **Fiber** to the Premise, wir zählen Premises nur, solange Glasfaser vorhanden, Fiber to the
*Building* reicht nicht 
- Erfahrungswerte: FTTP ist gleichzusetzen mit FTTH und ist ein besserer Begriff, weil Home nicht alles abdeckt, FTTP als Faser bis
zur Endkundeneinheit/Nutzungseinheit 
- Premises-Definition verlaufen im **Trichter**: Premises Potential ⊇ Premises Planned ⊇ Premises Passed ⊇
Premises Connected ⊇ Premise Connected Service-ready ⊇ Premises Activated



!!! info "Hinweis zur Abgrenzung: Premises ≠ Haushalte"
  
    Im Glasfaserausbau sind Premises die maßgebliche technische Einheit – nicht Haushalte. Eine **Premise** ist eine räumlich eindeutig identifizierbare Adresse (z. B. Wohnung, Einfamilienhaus, Geschäftslokal) mit eigener ID im BEV-Register. Ein **Haushalt** hingegen beschreibt eine soziale Einheit, d. h. Personen mit Hauptwohnsitz an einer Adresse (laut Statistik Austria).

    Da Haushalte statistisch erfasst, aber nicht geokodiert oder adressscharf (öffentlich zugänglich) verfügbar sind, eignen sie sich nicht zur Planung, Messung oder Bewertung von Ausbauzielen. Premises hingegen bilden die Grundlage für die technische Erschließung und die Definition von Kennzahlen wie Passed, Connected oder Activated.

    **Fazit:** Für Ausbauplanung, Monitoring und Zieldefinitionen muss immer die Einheit "Premise" verwendet werden.


<figure markdown="span">
  ![Trennung_Trichter](/assets/trichter_v5.png){ width="100%"}
</figure>



[^3]: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52023XC0131(01)
[^4]: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:52023XC0131(01)




### Technische Ebene: Layer 1 (FTTP)

#### Premise Potential (PPO)

`Definition` 

: Netzdimensionierungszahl, die das maximal mögliche Ausbaupotenzial darstellt.


`Erläuterung/Beispiele` 

- Z. B. bei Mehrparteienhäusern (MPH) können zusätzliche Premises entstehen. Nicht ausgebauter Dachboden, Greenfields/Bauerwartungsland, Bauvorhabens-Meldung, etc.
- Alle Anschlüsse, die eine Objekt-ID + ID/Laufnummer der Nutzungseinheit haben oder ohne ID auf ein Grundstück verortet werden können.


`Deutsche Bezeichnung` 

: Potenzielle anschließbare Nutzungseinheiten



#### Premise Planned (PPL)

`Definition` 

: Premises, die konkret für den Ausbau geplant sind.


`Erläuterung/Beispiele` 

- Es ist bekannt, wie viele Premises errichtet werden sollen. Wichtige Zahl für Vorvermarktung/im Rollout, bevor gebaut wird.
- Nicht alle Nutzungseinheiten sind anschlussfähig/-geeignet (z.B. Carport)


`Deutsche Bezeichnung` 

: Geplante anschließbare Nutzungseinheiten



#### Premise Passed (PP)

`Definition` 

: Premises, bei denen innerhalb von 4-6 Wochen und zu einem „üblichen“ Herstellungsentgelt ein Anschluss bereitgestellt werden könnte, (gemäß GIA).


`Erläuterung/Beispiele` 

: Droprohr vor oder am Grundstück. Kann sich während der Tiefbautätigkeiten täglich verändern; Erreichbarkeit über Feeder ist Voraussetzung.


`Deutsche Bezeichnung` 

: Versorgbare Nutzungseinheiten, Erschlossene Nutzungseinheiten



#### Premise Connected (PC)

`Definition` 

: Premises, die tatsächlich an das Glasfasernetz angeschlossen sind (Fiber Termination Unit/FTU vorhanden)


`Erläuterung/Beispiele` 

: Kann sich durch Herstellung von Premises Passed ergeben. *Fiber to the Home* – die Glasfaser muss bis in die Nutzungseinheit verlegt sein, in der sich der Netzabschlusspunkt befindet


`Deutsche Bezeichnung` 

: Hergestellte Nutzungseinheiten




### Technische Ebene: Layer 2 (FTTP)


#### Premise Connected Service-ready (PCS)

`Definition` 

: Premise Connected mit installiertem ONT oder optisch aktiver Anschluss ohne ONT; Netzabschluss aktiv, Dienstbereitstellung in sehr kurzer Zeit möglich.


`Erläuterung/Beispiele` 

: Die Premise ist physisch vollständig erschlossen (Glasfaser bis zum Netzabschlusspunkt), das ONT (oder ein vergleichbares Demarcation Device) ist installiert oder der Anschluss ist optisch aktiv. Ein Dienst kann innerhalb von Minuten oder Stunden aufgeschaltet werden.


`Deutsche Bezeichnung` 

: Betriebsbereite Nutzungseinheiten, Aktivierungsfähige Nutzungseinheiten



### Technische Ebene: Layer 3 (FTTP)

#### Premise Activated (PA)

`Definition` 

: Premises, die aktiv im Glasfasernetz surfen


`Erläuterung/Beispiele` 

: Nur eine Premise Connected kann zu einer Premise Activated werden (Trichter)


`Deutsche Bezeichnung` 

: Aktivierte Nutzungseinheiten




### Technische Ebenen an einem Schaubild erläutert

Ein Gebäude, bestehend aus:

- 1 Geschäftsfläche
- 5 Wohnungen
- 1 nicht ausgebauter Dachstuhl, potentiell eine weitere Wohnung

ist an ein Open Access Glasfasernetz angeschlossen.

- Die Geschäftsfläche sowie Wohnungen 1, 3 und 4 sind direkt an das Glasfasernetz angeschlossen, Wohnung 2 und Wohnung 5 sowie der Dachstuhl nicht.
- Wohnung 2 und 5 wurden in der Planung des Netzes berücksichtig, der unausgebaute Dachstuhl jedoch nicht. Somit sind bis zum HAK Kapazitäten für diese Wohnungen abgelegt, nicht aber für den Dachstuhl.
- Die Geschäftsfläche und Wohnung 1 beziehen bereits bei einem ISP einen Dienst.
- In Wohnung 3 ist sowohl das FTU als auch das ONT montiert.
- In Wohnung 4 ist nur das FTU montiert.

Wenn das Gebäude das gesamte Glasfasernetz darstellt, hat es also:

- 7 PPO 
- 6 PPL 
- 6 PP 
- 4 PC
- (3 PCS – eingeklammert, weil noch offen, ob eine Unterscheidung hier notwendig ist)
- 2 PA


<figure markdown="span">
  ![Schaubild](/assets/schaubild_v1.jpg){ width="100%"}
</figure>



### Kaufmännische Ebene: Vertrieb/Vermarktung

#### L1 Offered \[Premise Offered] (L1O)

`Definition`

: L1 Angebot für Premise ist an Kunden versendet


`Erläuterung/Beispiele` 

: L1 Offered immer einer Teilmenge von Premise Potential


`Deutsche Bezeichnung` 

: (Glasfaser-) Anschluss angeboten



#### L1 Sold \[Premise Sold] (L1S)

`Definition` 

: L1 Vertrag für Premise ist vorhanden


`Erläuterung/Beispiele` 

- Der Kunde bestätigt die Bestellung und erhält einen gültigen Vertrag mit AGB, ggf. OAID, etc., Verkaufte Premise
- Premise Sold wird nach Roll-out idR zu Premise Connected

`Deutsche Bezeichnung` 

: (Glasfaser-) Anschluss verkauft



## Take Rates


#### Aktivierungsrate

`Berechnung` 

- Premises Activated / Premises Connected
- **= PA/PC**


`Beschreibung` 

: L3 Take-up Rate



#### Anschlussrate (Take-up Rate) 

`Berechnung` 

- Premises Activated / Premises Passed
- **= PA/PP**


`Beschreibung` 

: Technische Versorgung L1 Take-up Rate



#### Ausbaurate

`Berechnung` 

- Premises Passed / Premises Planned
- **=PP/PPL**


`Beschreibung` 

- Idealerweise sollen alle PPL zu PP werden 
- Sinnvoll erst nach Roll out



#### Versorgungsrate

`Berechnung` 

- Premises Passed / Premises Potential
- **=PP/PPO**


`Beschreibung` 

: Passed gemessen an alles potenziellen Anschlüssen, Versorgungsrate, Angebot durch Potential



#### Bestellrate

`Berechnung` 

- L1 Sold \[Premise Sold] / Premises Planned
- **=L1S/PPL**


`Beschreibung` 

: Alle bestellten Dosen durch alle Premises Planned



#### Vorvermarktungsrate

`Berechnung` 

: Sehr individuell je Betreiber, kann nicht einheitlich definiert werden


`Beschreibung` 

: Eine interne Kennzahl, relevant in der Vorvermarktung, wird oft bei min. 40% angesetzt




## Take Rates am Schaubild erläutert:

Bezieht man sich wieder auf das Schaubild so ergeben sich für das theoretische Open Access Glasfasernetz bestehend aus
diesem einen Gebäude:

- Aktivierungsrate: 50,00% (2 PA zu 4 PC)
- Anschlussrate /Take-up Rate: 33,33% (2 PA zu 6 PP)
- Ausbaurate: 100,00% (6 PC zu 6 PPL)
- Versorgungsrate: 85,71% (6 PP zu 7 PPO)

Zur Kaufmännischen Ebene und zu Bestellraten muss noch ein eigenes Schaubild erstellt werden.

??? info "Schaubild"

    <figure markdown="span">
      ![Schaubild](/assets/schaubild_v1.jpg){ width="100%"}
    </figure>