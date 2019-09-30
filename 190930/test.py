data = """Kim Byungchul bcking92@gmail.com
Jinhong Park mpcato37@gmail.com
Minji Kim aestas822@gmail.com
Yunyoung Chung double.y.0525@gmail.com
Hyunbin Lee lhb4196@gmail.com
Yang ChanWoo oizys18@gmail.com
Daeseung Bang dsbang02@gmail.com
Oh Jeasuk jeasuk93@gmail.com
Jaehyun Kim didwjd169@gmail.com
Haneol Lee haru5442@gmail.com
Kuhnhee Lee sheva0902@gmail.com
Wooseop IM wooseopim93@gmail.com
"""

arr = data.split('\n')
names = []
emails = []

for a in arr:
    if not a: continue

    tmp = a.split('\xa0')
    
    names.append(tmp[0])
    emails.append(tmp[1])

print(', '.join(names),', '.join(emails))