Lab 6


Oppgave 1:
I det følgende kan vi starte med å presisere at denne løsningen har basert seg på 
resultatet vi har fått fra hjelpeverktøyet Wireshark. Wireshark er en “nettverks-sniffer”. 
Målet med laben er å finne ut av hvordan nettverksprotokoller fungerer I praksis.

I oppgave én og to er det viktig å kunne hvordan man tommer cache, 
 hvordan man starter en “capture”. Følgende instruksjon er vedlagt om “capture”:

“Å starte en "capture" (det norske begrepet "fangst" er også forholdsvis beskrivende) 
betyr å starte en ny prosess (et dataprogram) som fanger opp alle meldingene som går gjennom 
det spesifiserte nettverksgrensesnittet (for eksempel et ethernet-kort) på den aktuelle datamaskinen. 
Den beste måten å starte en capture på er å gå på: Capture-> Interfaces. 
Der ser du alle nettverksenhetene på maskinen. Trykk start på den enheten som du vil fange opp trafikk i fra. 
Det er som regel det eneste kortet som har trafikk når du sjekker.” (Tatt fra oppgave-instruksjon.


a) 
For å løse oppgave 1 a startet jeg først med å tømme cache I nettleseren jeg skulle bruke. 
Deretter gikk jeg inn på Wireshar igjen. Jeg måtte finne ut av hvilken ip-adresse som var 
aktiv for så å starte en live capture.  Etter å ha startet capture gikk jeg inn på nettleseren 
og lastet opp følgende side: http://www-net.cs.umass.edu. 
Etter at innlastningen var ferdig, stoppet jeg capture. 
Jeg la fort merke til at det var flere meldinger/pakker som ble fremstilt. I
denne oppgaven er det HTTP-meldingene som skal etterforskes. For å slippe å lete gjennom listen, 
er det viktig å kunne hvordan man sorterer seg fram til det man leter etter. 
I Wireshark sorterer man på følgende måte: Oppe I venste hjørne ser man en søkemotor, 
etterfulgt av en knapp som kalles for “expression”. Man kan enten trykke på expression, 
og deretter søke seg gjennom field name-listen. Det du skal lete etter er 
“http – Hypertext Transfer Protocol” (tips: hold inne ctrl+f og søk etter http). 
Den andre metoden innebærer at du søker etter “http” I søkemotoren, og deretter trykker på “apply”. 
Trykk så på “protocol” for å sortere innholdet alfabetisk etter protocol-type. 

Hvor lang tid tok det da fra “http GET” - meldingen ble sendt til “http OK”-meldingen ble mottatt?

HTTP Get meldingen ble sendt ut etter 3.171428000 sekunder, 
og vi mottok HTTP Get Ok etter 3.189186000 sekunder. Det vil si at det tok 0.017758 
sekunder fra da HTTP Get meldingen ble sendt ut til vi mottok HTTP GET Ok meldingen.

(Følgende resultater ble hentet fra en annen medstudents resulater:
Http GET falt på 0.9973890000 sekunder, mens http OK falt på 1.1229400000 sekunder. 
Differansen er da 0,125551 sekunder. Det vil si at fra “http GET”- meldingen ble sendt 
tok det 0,125551 sekunder til “http OK” -meldingen ble mottatt.)

Hva kan denne verdien brukes til ?
Hypertext Transfer Protocol er en tekst-basert førespørsel-svar-klient-server protkoll. 
En http-klient (Mozilla Firefox) foretar en http-forespøsel til en http-server(Apache server), 
som vil utstede en http-respons. Så verdien brukes til å regne ut hvor lang tid get 
tar fra http-klienten utsteder en forespørsel til en http-server og får en http-respons. 


Kilder, lastet ned 16.03.2015: 
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11 w3.org
https://ask.wireshark.org/questions/13384/display-http-header wireshark.org
https://wiki.wireshark.org/Hyper_Text_Transfer_Protocol wireshark.org
https://www.youtube.com/watch?v=NHLTa29iovU Youtube.com


b)
Get = Den ber om en represtasjon av en spesefik resurs. 
Forspørselen som bruker GET skal bare motta data, og ikke ha noen andre effekter.
Connection = Den konverterer forsespørselen om tilkobling til en 
åpenbar/gjennomsiktig TCP/IP tunnel. 
Målet med dette er for å legge til rette for SSL kryptert 
kommunkasjon(HTTPS) gjennom en ukrypter HTTP server.

Host = Det er siden vi henter informasjon fra eller den siden 
vi er på i dette tilfelle er det http://www-net.cs.umass.edu/.

Accept = Accept førespørselen brukes til å spesifisere hvilke 
mediatyper som er akseptable for responsen fra hosten. 
Accept forespørselen kan også inneholde parametere som setter 
en standard for kvaliteten på innholdet.

Origin = Denne headeren kommer fra brukersiden, og beskriver hvilke 
sikkherhetskontekster som gjorde at brukeren startet en http forespørsel. 
Serversiden kan bruke origin headeren for å forsikre seg om 
at brukerens nettleser kan stoles på.

Accept Encoding = Accept Encoding forespørsel-header feltet er lik som Accept, 
men begrenser innholdet i koden som er akseptert for en tilbakemelding.
Når en server tester om koden er akseptabel i forhold til Accept Encoding 
bruker man følgene regler : 1. Hvis koden er listet i Accept Encoding feltet er 
dette akseptabelt, men hvis qvalue = 0 er dette ikke akseptabelt. 2. Symbolet «*» 
i et Accept Encoding felt matcher alle tilgjengelige koder og må ikke være listet 
i header feltet. 3. Hvis flere koder er akseptable, blir den koden som har høyest 
verdi fra qvalue 1+ valgt. 4. «Identity» innholds koden er alltid akseptabel, 
hvis den ikke spesifikt inneholder «identity;q=0», eller fordi feltet inkluderer «*q=0». 
Hvis Accept Encoding feltets verdi er tom er bare selve «identity» akseptabel. 
Accept Language = Accept Language forespørsel-header feltet er lik som Accept,
 men begrenser språkene som er foretrukket som en respons av forespørselen. 
=======

a) HTTP Get meldingen ble sendt ut etter 3.171428000 sekunder, og vi mottok 
HTTP Get Ok etter 3.189186000 sekunder.
Det vil si at det tok 0.017758 sekunder fra da HTTP Get meldingen 
ble sendt ut til vi mottok HTTP GET Ok meldingen.

b)
Get = Den ber om en represtasjon av en spesefik resurs. Forspørselen som bruker GET 
skal bare motta data, og ikke ha noen andre
effekter.

Post = Det er en forsspørsels metode som brukes når du vil sende 
data til en web server, f eks når du sender inn en ett utfyllt HTML skjema 

Connection = Den konverterer forsespørselen om tilkobling til en 
åpenbar/gjennomsiktig TCP/IP tunnel.
Målet med dette er for å legge til rette for SSL kryptert kommunkasjon
(HTTPS) gjennom en ukrypter HTTP server.

Host = Det er siden vi henter informasjon fra eller den siden vi er på
 i dette tilfelle er det http://www-net.cs.umass.edu/

Accept = Accept førespørselen brukes til å spesifisere hvilke mediatyper 
som er akseptable for responsen fra hosten.
Accept forespørselen kan også inneholde parametere som setter 
en standard for kvaliteten på innholdet.

Origin = Denne headeren kommer fra brukersiden, og beskriver 
hvilke sikkherhetskontekster som gjorde at brukeren startet en 
http forespørsel. Serversiden kan bruke origin headeren for å forsikre 
seg om at brukerens nettleser kan stoles på.

Accept Encoding = Accept Encoding forespørsel-header feltet er lik 
som Accept, men begrenser innholdet i koden som er akseptert
for en tilbakemelding.  Når en server tester om koden er akseptabel i 
forhold til Accept Encoding bruker man følgene regler : 
1. Hvis koden er listet i Accept Encoding feltet er dette akseptabelt, 
men hvis qvalue = 0 er dette ikke akseptabelt.
2. Symbolet «*» i et Accept Encoding felt matcher alle tilgjengelige 
koder og må ikke være listet i header feltet.
3. Hvis flere koder er akseptable, blir den koden som har høyest 
verdi fra qvalue 1+ valgt.
4. «Identity» innholds koden er alltid akseptabel, hvis den ikke 
spesifikt inneholder «identity;q=0», eller fordi 
feltet inkluderer «*q=0». Hvis Accept Encoding feltets verdi er 
tom er bare selve «identity» akseptabel. 

Accept Language = Accept Language forespørsel-header feltet er lik som 
Accept, men begrenser språkene som er foretrukket som en respons av forespørselen.



Oppgave 2

a) Det er siden jeg ikke har vært på siden før. nettleseren vil skjekke om 
siden er mellomragret/cachet for å se om vi har vært der før og siden jeg 
ikke har vært der så blir ikke IF-MODIFIED-SINCE sendt med forsesøpsel.

b) Jeg fikk den filen jeg var ute etter. Serveren svarte med et HTTP 
koden var 200 som vil si at den var OK.

c) Grunnen til at jeg får IF-MODIFIED-SINCE er på grunn av at jeg at 
jeg har vært på siden, og at det er i minnet. Det gjør som at den vet 
at jeg har vært på siden, og vi er da ute etter siste forandring bare. 
Det er ikke noe vits å laste ned hele siden på nytt pga DATA megnde osv.

d) Det innformasjon vi får av HTTP server koden er 304. Det betyr at siden 
jeg prøver eller vil besøke ikke er oppdatert siden sist jeg var der. 
Det er altså lagret i mellomlagret/cache i nettleser.
>>>>>>> 34b5bac39f7ff251be150036e5eaf945409ff001
 
