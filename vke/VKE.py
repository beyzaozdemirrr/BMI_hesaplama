# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:06:45 2024

@author: beyza
"""

def hesapla(boy, kilo):
    
    return kilo/(boy**2)


def degerler(deger):
    
    if deger < 18.5:
        return "Zayıf"
    elif 18.5 <= deger < 24.9:
        return "Normal"
    elif 25 <= deger < 29.9:
        return "Fazla Kilolu"
    else:
        return "Obez"

kilo=float(input('kilonuzu giriniz'))
boy=float(input('boyunuzu metre cinsinden giriniz'))

deger = hesapla(boy, kilo)
kategori = degerler(deger)


print(f"\nVücut Kitle İndeksiniz (BMI): {deger:.2f}")
print(f"Kategori: {kategori}")