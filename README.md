# Arbeitsagentur Coachingangebote API

Eine der größten Datenbanken zu Coaching-/Aktivierungsangeboten Deutschlands durchsuchen.

## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Client Credentials sind folgende:

**ClientID:** ee971dcb-96fa-47b3-b2be-00863e4fc88b

**ClientSecret:** 1050e0b7-6db8-49e8-aff9-0e58e556681f

```bash
curl \
-H 'Host: rest.arbeitsagentur.de' \
-H 'Accept: */*' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' \
-H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' \
-H 'User-Agent:  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0' \
--data-binary "client_id=ee971dcb-96fa-47b3-b2be-00863e4fc88b&client_secret=1050e0b7-6db8-49e8-aff9-0e58e556681f&grant_type=client_credentials" \
--compressed 'https://rest.arbeitsagentur.de/oauth/gettoken_cc'
```

Der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/avgs/avgs/pc/v1/aktivierungsangebote im header als 'OAuthAccessToken' inkludiert werden.

**URL:** https://rest.arbeitsagentur.de/infosysbub/avgs/avgs/pc/v1/aktivierungsangebote


## Coaching-/Aktivierungsangebote


**URL:** https://rest.arbeitsagentur.de/infosysbub/avgs/avgs/pc/v1/aktivierungsangebote

Die Suche nach Coaching-/Aktivierungsangeboten ermöglicht verfügbare Weiterbildungsangebote mit verschiedenen GET-Parametern zu filtern.


### Filter

**Parameter:** *mz*  (Optional)

- SA%2001
- SA%2004
- SA%2005

Maßnahmenziel: SA%2001 = Heranführung an den Ausbildungs- und Arbeitsmarkt sowie Feststellung, Verringerung und Beseitigung von Vermittlungshemmnissen; SA%2004 = Heranführung an eine selbständige Arbeit; SA%2005 = Stabilisierung einer Beschäftigungsaufnahme.


**Parameter:** *sw*  (Optional)

Suchwort (z.B. Vermittlungshemmnisse)


**Parameter:** *ort*  (Optional)

Ortsangabe nebst Postleitzahl und Koordinaten (z.B. Feucht_90537_11.224918_49.376701)


**Parameter:** *page* (Optional)

Ergebnissseite (beginnend mit 0)


**Parameter:** *re*  (Optional)
- BW
- BY
- BE
- BB
- HB
- HH
- HE
- MV
- NI
- NW
- RP
- SL
- SN
- ST
- SH
- TH

Region/Bundesland: BW=Bade-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen. Mehrere Komma-getrennte Angaben möglich (z.B. re=TH,BW).


**Parameter:** *ban* (Optional)
Bildungsanbieter-ID (z.B. 229563). 


**Parameter:** *uk* (Optional)
- Bundesweit
- 25
- 50
- 100
- 150
- 200

Umkreis: Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.


**Parameter:** *mna* (Optional)
- 0
- 1

Maßnahmenart: 0=Einzelmaßnahme; 1=Gruppenmaßnahme. Komma-separierte Angaben möglich.


**Parameter:** *deufoev* (Optional)
- true
- false

DEUFOEV: true = (nur) Anbieter berufsbezogener Sprachförderung Deutsch (DeuFöV) anzeigen.


### Beispiel:

```bash
co=$(curl -m 60 -H "Host: rest.arbeitsagentur.de" \
-H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0" \
-H "Accept: application/json, text/plain, */*" \
-H "Accept-Language: de,en-US;q=0.7,en;q=0.3" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Origin: https://web.arbeitsagentur.de" \
-H "DNT: 1" \
-H "Connection: keep-alive" \
-H "Pragma: no-cache" \
-H "Cache-Control: no-cache" \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/infosysbub/avgs/pc/v1/aktivierungsangebote?mz=SA%2001&uk=Bundesweit&deufoev=false&page=1')
```


