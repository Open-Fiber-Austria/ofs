# Glossar (Version 1)

## Ebene: Technische Infrastruktur 

### Potential Premise

- **Definition:** Netzdimensionierungszahl, die das maximal mögliche Ausbaupotenzial darstellt.
- **Erläuterung/Beispiel:** Z. B. bei Mehrparteienhäusern (MPH) können zusätzliche Premises entstehen. Nicht ausgebauter Dachboden, Greenfields/Bauerwartungsland, Bauvorhabens-Meldung, etc.


### Premise Planned (Geplante Anschlüsse)

- **Definition:** Premises, die konkret für den Ausbau geplant sind.
- **Erläuterung/Beispiel:** Es ist bekannt, wie viele Premises errichtet werden sollen. Wichtige Zahl für Vorvermarktung/im Rollout, bevor gebaut wird

### Premise Passed (Versorgbare Anschlüsse)

- **Definition:** Premises, bei denen innerhalb von 4-6 Wochen und zu einem „üblichen“ Herstellungsentgelt ein Anschluss bereitgestellt werden könnte, *(gemäß GIA)*.
- **Erläuterung/Beispiel:** 
    - Droprohr vor oder am Grundstück. Kann sich während der Tiefbautätigkeiten täglich verändern; Erreichbarkeit über Feeder ist Voraussetzung.
    - Wenn das Gebäude angeschlossen ist, gelten alle Premises in diesem Gebäude als Passed gemäß BEREC und EK

### *Premise Prepared / Premise Passed +*

- **Definition:** *Premises, die bis zum HAK/BEP verbunden sind, aber möglicherweise (noch) keine Glasfaser bis zur Wohnung/Premise haben.*
- **Erläuterung/Beispiel:** *Z. B. Glasfaser im Keller, aber in Wohnungen nur Kupferleitungen. Oder Glasfaser im Keller (eines MPH) und nicht jede Wohnung wurde angeschlossen – ist die nicht angeschlossene Wohnung dann Premise Prepared?*

    !!! warning 
  
        In Deutschland ist **Premise Passed +** anders besetzt.

### Premise Connected

- **Definition:** Premises, die tatsächlich an das Glasfasernetz angeschlossen sind. ONT ist **noch nicht** vorhanden.
- **Erläuterung/Beispiel:** Kann sich durch Herstellung von Premises Passed ergeben. Fiber to the Home – die Glasfaser muss bis in die Räumlichkeiten verlegt sein, in der sich der Netzabschlusspunkt

### *Premise Connected +*

- **Definition:** *Premise Connected mit ONT*
- **Erläuterung/Beispiel:** *„Bereit für Dienst“ innerhalb von Minuten/Stunden*

### Premise Activated
- **Definition:** Premises, die aktiv im Glasfasernetz surfen
- **Erläuterung/Beispiel:** Nur eine Premise Connected kann zu einer Premise Activated werden (Trichter)


<figure markdown="span">
  ![Trennung_Trichter](/assets/glossar_bsp.png){ width="85%"}
  <figcaption>Hier ist ein Beispielbild</figcaption>
</figure>



## Take Rates

### Aktivierungsrate
- **Berechnung:** Premises Activated / Premises Connected + oder Connected

### Take-up Rate
- **Berechnung:** Premises Activated / Premises Passed
- **Beschreibung:** Nachfrage durch Angebot

### Anschlussrate
- **Berechnung:** Premises Connected / Premises Passed
- **Beschreibung:** Technisch

### Versorgungsrate
- **Berechnung:** Premises Passed / Premises Potential
- **Beschreibung:** Passed gemessen an alles möglichen Anschlüssen, Versorgungsrate, Angebot durch Potential

### Vorvermarktungsrate
- **Berechnung:** Eine interne Kennzahl



## Ebene: Vertrieb/Vermarktung

### L1 Planned
- **Definition:** Premise wird realisiert z.B. L1 Vertrag mit Endkunden gültig
- **Erläuterung/Beispiel:** L1 Planned immer einer Teilmenge von Potential Premise

### L1 Planned +
- **Definition:** Premise wird realisiert z.B. L1 Vertrag mit L3 Verpflichtung mit Endkunden gültig

### L1 Scheduled
- **Definition:** Premise mit geplantem Realisierungs-Datum

### L1 Ready
- **Definition:** An der Premise ist ein oder mehrere Faserlinks verwendbar
- **Erläuterung/Beispiel:** = Premise Connected / Connected +

