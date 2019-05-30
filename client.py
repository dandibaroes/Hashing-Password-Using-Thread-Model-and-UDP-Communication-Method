# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
UDP_IP = "192.168.1.5"

# definisikan target port number server yang akan dituju
UDP_PORT = 1234

print ("target IP:", UDP_IP)
print ("target port:", UDP_PORT)
#print ("pesan:", PESAN)

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#input password yang mau diuji
pesan = input("password yang mau diuji : ")
print("Mengirim password: " + pesan)
#kirim password ke server
sock.sendto(pesan.encode(), (UDP_IP, UDP_PORT))
print("Password terkirim\n")

# menutup socket
print("Menutup Socket")
sock.close()