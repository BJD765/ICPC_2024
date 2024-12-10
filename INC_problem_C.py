# Problem C: Double chunks

N = int(input())
A = list(map(int, input().split()))


last = {}                                   # menyimpan index terakhir suatu double chunk muncul
dc = {}                                     # dictionary (max amount of peanuts, jumlah kemunculan)
max = 0                                     # jumlah kemunculan maksimum

# last[S] berarti index terakhir dimana jumlah S muncul. berarti S muncul di index last[S] dan last[S] +1
 
 
for i in range(N - 1):
    S = A[i] + A[i + 1]
    if S not in last or last[S] + 1 < i:      # penjelasan di(1)  
        dc[S] = dc.get(S, 0) + 1              # cari apakah double chunk dengan jumlah peanut S sudah muncul sebelumnya, jika sudah, kemunculannya ditambah satu. jika belum maka 0+1 = 1.
        last[S] = i                           # catat index terakhir munculnya double chunk dengan jumlah peanut S. 
        if dc[S] > max:                       # jika jumlah kemunculan double chunk dengan jumlah peanut S lebih banyak dari jumlah kemunculan double chunk yang sebelumnya (misal dengan jumlah peanut y) maka ganti nilai max dengan jumlah kemunculan double chunk dengan jumlah peanut S. 
            max = dc[S]

print(max)                                     # print kemunculan yang paling banyak dari double chunks jumlah peanuts tertentu                              


#(1)
# S not in last untuk mengecek apakah S belum pernah muncul sebelumnya.     
# last[S] + 1 < i untuk mengecek supaya tidak ada index yang tumpang tindih.
# misal index 2 dan 3 sudah terhitung sebagai suatu double chunk dengan jumlah peanuts S, maka index 3 dan 4 tidak bisa dianggap sebagai double chunk dengan jumlah peanuts S. minimal harus index 4 dan 5, jadi tidak ada index yang tumpang tindih.