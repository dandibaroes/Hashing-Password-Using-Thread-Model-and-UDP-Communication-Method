# import library socket karena akan menggunakan IPC socket
import socket
from hashlib import md5
import os
import sys
import multiprocessing
import time
import threading
import logging
import hashlib               
 
# definisikan alamat IP binding  yang akan digunakan 
ip = "192.168.1.5" 

# definisikan port number binding  yang akan digunakan
port = 1234               
 
# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         
print ("Socket berhasil dibuat")

# lakukan bind
s.bind((ip, port))
pesan = "socket bind ke alamat " + ip + " dan port " + str(port)
print (pesan)
 
data = s.recv(1024).decode()
print("Pesan diterima : ",data)


global _Finish
_Finish = False
################################################################################
def getListPassword():
    # counter = 0
    password_file = "dict.txt"#raw_input("Enter a dictionary file: ")

    try:
        password_file = open(password_file, "r")
    except:
        print("\n File Not Found")
        quit()

    list_password = []
    for password in password_file:
        # counter += 1
        pswrd = password.strip()
        list_password.append(pswrd)

    return list_password
################################################################################
def splitIntoFive(list_password):
    part1 = len(list_password)//5
    part2 = part1*2
    part3 = part1*3
    part4 = part1*4
    part5 = len(list_password)

    return part1, part2, part3, part4, part5
################################################################################
def crackPassword(password_hash, list_password, part):
    global _Finish
    if _Finish == False:
        if ((part/(len(list_password)//5)) == 1):
            for index in range(0, part):
                check_md5 = md5((list_password[index]).encode('utf-8')).hexdigest()
                if password_hash == check_md5:
                    print("\n Match Found! Password is " +list_password[index])
                    _Finish = True
                    break
            else: 
                print("\n No Match Found!")


        else:
            for index in range((part-(len(list_password)//5))+1, part):
                check_md5 = md5((list_password[index]).encode('utf-8')).hexdigest()
                if password_hash == check_md5:
                    print("\n Match Found! Password is " +list_password[index])
                    _Finish = True
                    break
            else: 
                print("\n No Match Found!")

################################################################################            
if __name__ == '__main__':  
    print("=========================================")
    print("   HASHING PASSWORD USING THREAD MODEL   ")
    print("=========================================")
    password      = data
    hash_object   = hashlib.md5(str(password).encode('utf-8'))
    password_hash = hash_object.hexdigest()
    print("     Hash : " +password_hash)
   
    list_password = getListPassword()
    a, b, c, d, e = splitIntoFive(list_password)
    numofthreads  = 5
    threadList    = []
    start=time.time()
    
    print("\n----------------------------------------")
    print("  STARTING SEARCHING.....\n")
    for i in range(numofthreads):
        if _Finish == False:
            t1 = threading.Thread(target=crackPassword, args=(password_hash, list_password, a))
            t2 = threading.Thread(target=crackPassword, args=(password_hash, list_password, b))
            t3 = threading.Thread(target=crackPassword, args=(password_hash, list_password, c))
            t4 = threading.Thread(target=crackPassword, args=(password_hash, list_password, d))
            t5 = threading.Thread(target=crackPassword, args=(password_hash, list_password, e))
        else:
            time.sleep(0)


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    threadList.append(t1)
    threadList.append(t2)
    threadList.append(t3)
    threadList.append(t4)
    threadList.append(t5)
    end=time.time()
    print("\n\nExecution Time : ", end-start)
