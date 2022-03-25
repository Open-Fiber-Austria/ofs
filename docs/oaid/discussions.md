# FAQ

#### Ist die OAID DSGVO konform?

In der bisherigen Praxis werden Adressdaten und Personendaten zwischen den Systemen bzw. Ebenen eines 3-LOM Netzes ausgetauscht. Mit einer stringenten Verwendung der Open Access ID ist der Austausch personenbezogener Daten nicht oder nur mehr sehr eingeschränkt notwendig. Die OAID unterstützt somit das _Minimum Prinzip_ der DSGVO (ein System ist so zu gestalten, dass ein Minimum an Daten ausreicht).

#### Hat die OAID eine Prüfsumme?

Eine Prüfsumme ergibt sich durch eine Berechnung auf den ursprünglichen Code, das Ergebnis (im Allgemeinen ein oder zwei Stellen) wird als Teil des Codes dargestellt. Die Prüfsommer erlaubt die dezentrale Formalprüfung der Eingabe.

Ein Beispiel für den Einsatz einer Prüfsumme ist die International Bank Account Number (IBAN). Die IBAN hat in Österreich zwanzig Stellen bestehend aus `AT` + 2 Prüfziffern + 16 Ziffern. Dadurch kann bereits bei der Eingabe und ohne unmittelbare Rückfrage bei einem Server (Offline VerifikationN) die formale Korrektheit, nicht aber die tatsächliche Existenz, geprüft werden. Der Vorteil dieser Methode wird dann klar, wenn man die Menge der Zahlungsvorgänge betrachtet. Die Prüfsumme dient der Entlastung der zentralen Systeme.

Die Anzahl der Geschäftsfälle in der Kommunikation mit dem Kunden zur OAID ist demgegenüber deutlich geringer, beschränkt sich zumeist auf An- und Ummeldung von ISP Verträgen oder Störungen. Dazu kommt, dass weder bei der mündlichen Entgegennahme noch in papierform eine unmittelbare Verifizierung stattfinden kann.

Technisch ist die Ergänzung einer Prüfsummer möglich, jedoch derzeit nicht geplant. Eine einfache Formalprüfung auf den verwendeten Code-Raum sowie nachfolgende Online Verifikation erscheinen vorerst ausreichend.

#### Gilt die OAID für ein Gebäude?

Die OAID identifiziert den kundenseitigen Glasfaseranschluss. Im Allgemeinen versorgt ein solcher Anschluss eine (Gebäude-)Nutzeinheit. Ein Gebäude oder ein Grundstück mit mehreren Nutzeinheiten und individuellen Glasfaser-Anschlüssen erhält daher mehrere OAIDs.

Ein Einfamilienhaus erhält in der Regel eine OAID. In einem Mehrparteienhaus werden mehrere OAIDs vergeben udn den einzelnen Nutzeinheiten (Wohnungen) zugeteilt. Dadurch ist es den (späteren) Besitzern bzw. Mietern möglich, einen Internet-Dienstevertrag für ihre Nutzeinheit zu bestellen.

![Multi-Dwelling Building](/assets/real_multi-dwelling.png){ align=center, loading=lazy }

Bild zeigt Standorte eines Mehrparteienhauses mit zugehörigem Planungspunkt. Die Standorte sind entsprechend der Stiegenhäuser abgebildet - die geografische Platzierung in Kreisform dient zur besseren Visualisierung, es ist im Allgemeinen nicht notwendig (und auch nicht bekannt), die OAID exakt zu positionieren. 

!!! warning ""
    Die OAID ist die letzte Möglichkeit, ohne aufwändige Interaktion mit dem Kunden, Anfragen auf unbekannten oder auch identischen Adressen zu unterscheiden. 
<!---
Je unterscheidbarer die OAID, desto zuverlässiger kann genau der richtige Abschluss (FTU) identifiziert werden. Von einer OAID für Gebäude mit potenziell mehreren Nutzeinheiten ist also eher abzuraten. 
-->

#### Ist die OAID öffentlich?

Die OAID ist die eindeutige, adressunabhängige Identifikation des Glasfaser-Anschlusses und wird bei Geschäftsprozesses zu diesem Anschluss verwendet. Die OAID ist den beteiligten P und kein geheimes Kennwort.

#### Warum 8 Stellen?

Die Kommunikation mit dem Endkunden kann über verschiedenste und nicht immer ausschließlich digitale Kanäle erfolgen. Ein kurzer Identifikationsschlüssel erleichtert vor allem die direkte (analoge) Kommunikation. Bei der Gestaltung der OAID wurde daher ein Kompromiss aus Absicherung der ID versus Länge des Codes getroffen.

Die Anzahl der erlaubten Kombinationen bei einer Länge von acht Stellen ist > 1000 Milliarden.
