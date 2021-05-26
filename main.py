__author__="kvda"

class myClass():
    def myFunc(self):
        print("Program penjumlahan/pengurangan dua buah Matriks")
        print("---")
        barisInp = input("Masukkan jumlah baris : ")
        kolomInp = input("Masukkan jumlah kolom : ")
        operasi = input("Operasi yang diinginkan (Pengurangan/Penjumlahan) : ")
        print("")

        matriks1 = []
        matriks2 = []

        offset = 0
        
        print("Matriks pertama")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks1.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("Matriks pertama : ")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks1[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        print("")
        
        
        offset = 0
        print("Matriks kedua")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks2.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("Matriks kedua : ")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks2[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        print("")
        
        if(operasi=="Penjumlahan" or operasi=="penjumlahan"):
            print("Hasil dari penjumlahan matriks anda : ")
            print("---")
            print(" ")
            offset = 0
            offsetMatriks = 0
            while offset<int(barisInp):
                offset2 = 0
                while offset2<int(kolomInp):
                    print(int(matriks1[offsetMatriks])+int(matriks2[offsetMatriks]),end=" ")
                    offsetMatriks+=1
                    offset2+=1
                print(" ")
                offset+=1
        elif(operasi=="Pengurangan" or operasi=="pengurangan"):
            print("Hasil dari penjumlahan matriks anda : ")
            print(" ")
            offset = 0
            offsetMatriks = 0
            while offset<int(barisInp):
                offset2 = 0
                while offset2<int(kolomInp):
                    print(int(matriks1[offsetMatriks])-int(matriks2[offsetMatriks]),end=" ")
                    offsetMatriks+=1
                    offset2+=1
                print(" ")
                offset+=1
         
if __name__ == '__main__':
    myClass().myFunc()