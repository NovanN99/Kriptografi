import socket #socket
from textwrap import wrap #Fungsi wrap(), yang diterima dari client
#Memecah string yang panjang menjadi kelompok yang panjangnya 8 bit

#key
key = '67'

nimBiner = ''.join(
    map(
        lambda angka: bin(int(angka))[2:].zfill(4),
        list(key)
    )
)

#print nim dan nim yang sudah berbentuk biner
print('Key: ', nimBiner)

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1) #setting agar server dapat menerima koneksi dari client
print('Server TCP dimuulai, menunggu koneksi')

connectionSocket, addr = serverSocket.accept() #Menunggu Koneksi
print('Koneksi diterima, Menerima Data')

#Menerima data dari client
data = connectionSocket.recv(1024)

#Diprint
print('Data diterima, Data: ', data.decode())

dekripsi = list(
    map(
        lambda huruf : bin(
        (int(huruf, 2) >> 1) ^ int(nimBiner, 2))[2:].zfill(8),wrap(data.decode(), 8)
    )
)

#print hasilnya
#join(), dekripsi tipe datanya list
#' '.join(dekripsi): setiap elemen dalam dekripsi akan dijoin
#['0000', '0001'] = '0000, 0001'
print('Message biner: ', ''.join(dekripsi))

#chr(): mengubah integer menjadi karakter
plainteks = ''.join(
    map(
        lambda huruf: chr(int(huruf,2)),
        dekripsi
    )
)

#print
print('Message Plainteks : ', plainteks)