from datetime import datetime
from astropy.time import Time

# Python'un varsayılan pakei datetime'dan şimdi zamanını (local) al
print(datetime.now())
# Python'un varsayılan pakei datetime'dan şimdi zamanını (utc) al
print(datetime.utcnow())

# Python'un varsayılan pakei datetime ile string veriyi zaman objesine dönüştür
py_zaman = datetime.strptime('2020-12-07 17:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
# Python zaman objesini kullanarak astropy zaman objesi oluştur
zaman = Time('2020-12-07T17:00:00.000')
print(zaman.jd)
