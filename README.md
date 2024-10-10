# 🇹🇷 Midasbuy Hesap Kontrolcüsü | 🇬🇧 Midasbuy Account Checker

🇹🇷 Bu proje, Selenium WebDriver kullanarak Midasbuy hesaplarına otomatik giriş yapmayı sağlar. `midasbuy.txt` dosyasından e-posta ve şifre bilgilerini okur ve giriş denemeleri yapar. Başarılı ve başarısız girişleri ayrı dosyalara kaydeder.

🇬🇧 This project automates logging into Midasbuy accounts using Selenium WebDriver. It reads email and password pairs from the `midasbuy.txt` file and attempts to log in. Successful and unsuccessful login attempts are logged in separate files.

## 🇹🇷 Özellikler | 🇬🇧 Features
- 🇹🇷 Midasbuy sitesine otomatik giriş yapar.  
  🇬🇧 Automatically logs into the Midasbuy website.
  
- 🇹🇷 Başarılı ve başarısız girişleri ayırır: `live.txt` (başarılı), `offkanka.txt` (başarısız).  
  🇬🇧 Separates successful and unsuccessful logins: `live.txt` (successful), `offkanka.txt` (unsuccessful).

- 🇹🇷 Giriş yapılırken oluşabilecek hataları yakalar ve `dec.txt` dosyasına kaydeder.  
  🇬🇧 Catches errors during login attempts and logs them in `dec.txt`.

## 🇹🇷 Gereksinimler | 🇬🇧 Requirements
- 🇹🇷 Python 3.x  
  🇬🇧 Python 3.x

- 🇹🇷 Gerekli Python kütüphaneleri:
  - `selenium`
  - `webdriver-manager`  
  🇬🇧 Required Python libraries:
  - `selenium`
  - `webdriver-manager`

Kurulum için şu komutları kullanabilirsiniz:  
You can install the required libraries using the following commands:

```bash
pip install selenium webdriver-manager
