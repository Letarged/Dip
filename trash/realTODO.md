
- zaviesť "parser error" - chyba ktorá nastala v parseru - nech uživateľ vie že je jeho chyba, že ten extra parser naprogramoval na hovno


PARSERY NIE SU HOTOVE !!! tie patterns !!

Ponúknuť nmap "-A" buď na tie porty, kde nie je známy názov služby, alebo na všetky ktoré sú otvorené

Masscaan občas vráti prázdny output a vtedy to je problém

Ešte zjednodušiť pridávanie user-modulov. Aby uživateľ nemusel hrabať v kóde (napr teraz by musel zasahovat do scanCoordination a tiez do scanCoordinationAssisant, čo je nepriatelne). Takže všetko cez ďalšie config subory, mapovacie subory a tak. Aby jedine, čo uživateľ musel pridať je záznam v nejakom mapovacom súbore a potom úplne nové python súbory (ako parser a assist a tak.. tieto sa len jednoducho namapuju). JEden z takych mapovacich suborov bude možno:
    - 
    - služba: http
    - assist: /xyz/craft
    - ja nevieeeeem už, som unaveny

Vypísanie potencionálnych cieľov (možno scoring?)

Pridat moznost -A na objavene porty (napriklad s číslom 800+)

Pridat SSLSCAN a PTWEBDISCOVER a FTP anon?

Spraviť inštalačný súbor

Ošetrenie nevalidných vstupov (do nejakej miery)

Vložiť možnosti proxy 

