import qrcode

# Токен вашего бота
bot_token = "6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk"

# Создание объекта QR-кода
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Формирование данных для QR-кода (ссылка на бота)
bot_link = f"https://t.me/{bot_token}"
qr.add_data(bot_link)
qr.make(fit=True)

# Генерация изображения QR-кода
qr_image = qr.make_image(fill="black", back_color="white")

# Сохранение QR-кода в файл
qr_image.save("bot_qr_code.png")