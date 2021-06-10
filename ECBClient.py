import socket

#input plainteks dan nim
plainteks = input('Plainteks : ')
key = '67' 

#convert plainteks to binner
plainteksBiner = list(
    map(
        lambda huruf: bin(huruf)[2:].zfill(8),
        bytearray(plainteks.encode())
    )
)

#convert key to binner
keyBiner = ''.join(
    map(
        lambda angka: bin(int(angka))[2:].zfill(4),
        list(key)
    )
)

#print plainteks dan key binnernya
print('Plainteks Binner: ', ' '.join(plainteksBiner))
print('Kunci/Key Binner: ', keyBiner)

#Enkripsi , dixor dengan kunci binnernya
#setiap elemen plainteksBinner(), dixor dengan kunci (nimBinner)
enkripsi = list(
    map(
        lambda huruf: bin(
        (int(huruf, 2) ^ int(keyBiner, 2)) << 1
        )[2:].zfill(8),
        plainteksBiner
    )
)

#Print Hasil Enkripsi
print('Chiperteks: ', ' '.join(enkripsi))

#koneksi ke server
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Koneeksi ke Server')
clientSocket.connect(('127.0.0.1', serverPort))

print('Mengirim ke Server')

#Mengirim hasil enkripsi ke server
clientSocket.send(''.join(enkripsi).encode())

#koneksi ditutup
clientSocket.close()