![ofaa_logo](https://user-images.githubusercontent.com/7644657/160231882-45ef6059-f580-414f-abf6-f6326c0a1f1c.jpg)

# Open Fiber Standards

[![CC BY NC ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

Ziel von [OFAA](https://ofaa.at) ist der Ausbau von offenen Glasfaser-Netzen in Österreich. Zur Unterstützung dieses 
Ziels erarbeiten die [Mitglieder von OFAA](https://www.ofaa.at/organisation/) Empfehlungen und Standards im 
Zusammenhang mit Planung, Errichtung und Nutzung der Netze.

Die Empfehlungen und Standards werden als sogenannte Fiber Enhancement Proposals (FEP) diskutiert und öffentlich zur 
Verfügung gestellt. Die FEPs sollen die involvierten Parteien in 3-LOM Netzen durch Wissen und Praxis unterstützen.

Weitere Details zu dieser Vorgangsweise finden sich in der Definition des FEP selbst.

# License

[![CC BY NC ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by-nc-nd].

[cc-by-nc-nd]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png

[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY%20NC%20ND%204.0-lightgrey.svg

## Development

Um die Dokumentation lokal zu erstellen und zu betrachten, ist es möglich via Docker einen Webserver zu starten,
welcher die aktuellen Änderungen stets rendert und darbietet (Hot Reload).

Zum Starten einer solchen Instanz kann das beigelegte Docker Compose File (*docker-compose.yml*) genutzt werden. Die
Dokumentation kann dann mithilfe auf dem eigenen Rechner unter [http://localhost:8081](http://localhost:8081) 
aufgerufen werden.

### Kommandozeile

Zum Starten über die Kommandozeile navigieren sie mit dem Terminal ihrer Wahl in das Projektverzeichnis. Dort können
sie mit dem nachfolgenden Befehl die Dokumentation lokal starten.

```shell
docker-compose up development 
```

Sobald sie nun im Projektverzeichnis eine Datei bearbeiten, wird der Webserver versuchen die Dokumentation neu zu 
erstellen und die Änderungen sind auf [ihrem Rechner](http://localhost:8081) verfügbar.

