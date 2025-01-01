import qrcode

png = qrcode.make('https://www.youtube.com/watch?v=6ZB2A0050O0&list=RDxZF8PSFUZ8g&index=15&ab_channel=PipeCalderon')
png.save('codigo.png')