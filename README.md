# Telegram Kalkulyator Bot

Ushbu Telegram kalkulyator bot matematik amallarni yechish va foydalanuvchilarga statistik ma'lumotlarni taqdim etish uchun mo'ljallangan. 

## Asosiy xususiyatlar

- Matematik amallar: qo'shish, ayirish, ko'paytirish, bo'lish va ildiz olish.
- Foydalanuvchilar sonini ko'rsatish uchun statistikani taqdim etish.
- Admin panel orqali foydalanuvchilarga xabar va rasm yuborish imkoniyati.

## O'rnatish

1. **Python va kerakli kutubxonalarni o'rnating**:
   - Python o'rnatilganligini tekshiring. Agar o'rnatilmagan bo'lsa, [Python rasmiy saytidan](https://www.python.org/downloads/) o'rnating.
   - Kerakli kutubxonalarni o'rnating:
     ```bash
     pip install python-telegram-bot
     ```

2. **Bot tokenini olish**:
   - Telegramda [@BotFather](https://t.me/botfather) botini toping va yangi bot yarating. Bot yaratganingizda sizga token beriladi, ushbu tokenni saqlang.

3. **Koddagi tokenni o'zgartirish**:
   - `main.py` faylini oching va quyidagi qatorni toping:
     ```python
     BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
     ```
   - `"YOUR_BOT_TOKEN_HERE"` ni olingan tokeningiz bilan almashtiring.

4. **Botni ishga tushirish**:
   - Terminal yoki buyruq qatorini oching va quyidagi buyruqni bajarish orqali botni ishga tushiring:
     ```bash
     python main.py
     ```

## Admin funksiyalari

Admin panelida quyidagi funksiyalar mavjud:
- Foydalanuvchilarga rasm va xabar yuborish.
- Foydalanuvchilar sonini ko'rsatish.

## Dasturchi

Dasturchi: [@DragonOwner](https://t.me/DragonOwner)

## Mualliflik Huquqlari

© 2024 Telegram Kalkulyator Bot. Barcha huquqlar himoyalangan.
