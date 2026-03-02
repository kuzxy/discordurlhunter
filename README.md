# Kuzey Sniper 2.0 - Vanity URL Hunter DISCORD @Z6VB

## English Description

### Project Overview
This tool is designed to monitor 2-character vanity URLs on Discord. It constantly scans combinations and attempts to claim available URLs for a specific server automatically.

### Important Warnings
- Self-Bot Risk: This tool operates as a self-bot. Using self-bots is against Discord's Terms of Service and may result in account suspension. Use at your own risk.
- Level 3 Requirement: The target server must have Level 3 Boost status to successfully assign a vanity URL.
- Token Security: Never use your primary account token. It is highly recommended to use an alternative (alt) account for this process.

### Installation and Usage
1. Ensure Python is installed on your system.
2. Install required libraries: pip install requests urllib3
3. Open the script and enter your alt account token in the TOKEN field.
4. Enter your target server ID in the MY_SERVER_ID field.
5. Run the script: python sniper.py

### Technical Notes
- VDS Usage: The script requires a constant internet connection. For 24/7 operation, running the script on a Virtual Private Server (VDS) is recommended.
- Banned URLs: Many 2-character URLs are blacklisted by Discord. The script is designed to skip these and continue scanning.

---

## Turkce Aciklama

### Proje Ozeti
Bu arac, Discord uzerindeki 2 haneli ozel URL'leri izlemek icin tasarlanmistir. Kombinasyonlari surekli tarar ve bosta buldugu URL'leri belirttiginiz sunucuya otomatik olarak cekmeye calisir.

### Onemli Uyarilar
- Self-Bot Riski: Bu arac bir self-bot mantigiyla calisir. Self-bot kullanimi Discord hizmet kosullarina aykiridir ve hesabin kapatilmasina neden olabilir. Kullanim sorumlulugu tamamen kullaniciya aittir.
- Level 3 Sarti: URL'yi kendi sunucunuza cekebilmeniz icin hedef sunucunun Level 3 Boost seviyesinde olmasi sarttir.
- Token Guvenligi: Asla ana hesabiniza ait tokeni kullanmayin. Bu islem icin her zaman bir yan hesap (alt account) tercih edilmelidir.

### Kurulum ve Kullanim
1. Sisteminizde Python yuklu oldugundan emin olun.
2. Gerekli kutuphaneleri kurun: pip install requests urllib3
3. Kod dosyasini acin ve TOKEN kismina yan hesabiniza ait tokeni yapistirin.
4. MY_SERVER_ID kismina URL'nin tanimlanacagi sunucu ID'sini yazin.
5. Kodu calistirin: python sniper.py

### Teknik Notlar
- VDS Kullanimi: Bilgisayariniz kapandiginda kod durur. 7/24 kesintisiz calisma icin bir VDS (Sanal Sunucu) uzerinde calistirilmasi onerilir.
- Yasakli URL'ler: 2 haneli URL'lerin bircogu Discord tarafindan kara listeye alinmistir. Kod bu durumlari atlayip taramaya devam edecek sekilde yapilandirilmistir.
