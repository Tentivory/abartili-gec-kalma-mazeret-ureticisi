#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Geç Kalma Mazeret Üreticisi
Çünkü bazen "trafik vardı" yetmez, evrenin kendisi seni durdurmalıdır.
"""

import random
import time

def dramatik_bekleme(mesaj):
    print(mesaj)
    for i in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print()

def mazeret_uret(siddet=3):
    baslangic = [
        "Vallahi şu oldu:",
        "Yemin ederim anlatmasam inanmazsın:",
        "Tam kapıdan çıkarken evren bana şunu dedi:",
        "Annem bile inanmadı ama gerçek şu:"
    ]
    
    olaylar = [
        "kedi kapının önünde oturup bana 'bugün gitme' diye baktı",
        "asansör kendi kendine şiir okumaya başladı ve bitirmesini bekledim",
        "sokaktaki bir karga bana 'bugün önemli bir gün değil' diye bağırdı",
        "ayakkabılarım aniden felsefi bir kriz geçirdi ve yürümeyi reddetti",
        "trafik ışığı kırmızıyken yeşil, yeşilken kırmızı olmaya karar verdi",
        "gökyüzünden bir çay bardağı düştü ve onu yakalamak için 47 dakika koştum"
    ]
    
    sonuclar = [
        "ve bu yüzden tam {dakika} dakika geciktim. Özür dilerim ama bu benim kontrolüm dışında.",
        "sonuç olarak evrenin planını bozmamak için bekledim. Şimdi buradayım.",
        "bu yüzden geldiğimde biraz geçtim ama ruhen tam zamanındayım."
    ]
    
    dakika = random.randint(5, 45) * siddet
    
    mazeret = f"{random.choice(baslangic)} {random.choice(olaylar)} {random.choice(sonuclar).format(dakika=dakika)}"
    return mazeret

def main():
    print("=" * 50)
    print("   ABARTILI GEÇ KALMA MAZERET ÜRETİCİSİ v1.0")
    print("   (Gerçekten çalışır, gerçekten saçmadır)")
    print("=" * 50)
    
    dramatik_bekleme("Mazeret üretmek için evreni sorguluyorum")
    
    for i in range(1, 4):
        print(f"\n--- Seviye {i} Mazeret ---")
        print(mazeret_uret(siddet=i))
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("Not: Bu mazeretlerin hiçbiri gerçek değildir. Ama olabilirdi.")
    print("=" * 50)
    
    # Gizli not: bazen sistemin kendisi gecikmenin sebebidir
    # (sadece kodun içinde duruyor, kimse görmez)

if __name__ == "__main__":
    main()

# Damga: Kayyum Grok | 13 Kasım 2026 | Ciddiyetle ama değil
# İmza: Bu kod gerçekten çalışır. Denemeden inanma.
