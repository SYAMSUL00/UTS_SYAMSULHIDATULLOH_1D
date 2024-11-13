while True: 
    
    jumbarang = int(input("masukan jumlah barang :"))
    for i in range (1,jumbarang + 1):
        harga_barang = float(input(f"masukan harga barang ke {i} :"))


    total_harga_barang = harga_barang + harga_barang
    print(f"jadi semua nya adalah RP. {total_harga_barang}")