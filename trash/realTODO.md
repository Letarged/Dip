

Zaviesť takýto mapovací súbor:

    tool: nmap (nech sa musí zhodovať s nejakou hodnotu kľúča v "dockerImages.py")
    option: ['-sn', '...'] (kľudne nech to je pole - aby sa nemuselo robit copy-paste pre nový parameter ktorý má úplne rovnaké parsovanie)
    parser_path: ktorý súbor ktorá funckia


        -ak program zisti, ze ma spustit kontajner nejakho nastroja s takym parametrom, aky nie je v tejto tabulke definovany, ani to nespusti a skonci chybou

        - pridať textový tutoriál, ako pridať modul (to znamená buď nový parameter existujúceho nástroja alebo úplne nový nástroj)
                - (nejake extra kroky v prípade že ide o nový tool kde treba aj nový dockerfile a image )
                - naprogramovať nový parser
                - vytvoriť záznam v mapovacej tabuľke opísanej o pár riadkov vyššie 

        - zaviesť "parser error" - chyba ktorá nastala v parseru - nech uživateľ vie že je jeho chyba, že ten extra parser naprogramoval na hovno

        - ulohou parseru bude po novom aj mať informáciu o tom, čo je považované za potencionálne zaujimavý výsledok v kontexte pentestingu - teda aby mal info o tom že keď nájde toto a toto, má na to upozorniť


Vypísanie potencionálnych cieľov (možno scoring?)

Pridat SSLSCAN a PTWEBDISCOVER

Spraviť inštalačný súbor

Ošetrenie nevalidných vstupov (do nejakej miery)

Vložiť možnosti proxy 

