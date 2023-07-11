import qrcode

# Токен вашего бота
bot_token = "6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk"

# Создание объекта QR-кода
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Формирование данных для QR-кода (ссылка на бота)
bot_link = "https://www.singulart.com/en/artist/aram-simonyan-34860?campaign_id=1717&fbclid=IwAR0VcUvFJaKW4D_lS6hxInCS_NKM5FJRdp4Ft7ZddlPB3dKrvTd361xxtC0_aem_Ae0L5ItDEv86OcGwGB_e-Ueiu1XReQib6_zX1xdESaux7RYLBmz2rxMQNAFNkjpAmII"
qr.add_data(bot_link)
qr.make(fit=True)

# Генерация изображения QR-кода
qr_image = qr.make_image(fill="black", back_color="white")

# Сохранение QR-кода в файл
qr_image.save("bot_qr_code.png")