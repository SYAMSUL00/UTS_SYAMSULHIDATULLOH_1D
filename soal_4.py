beratbadan = int(input("Masukan Berat Badan : "))
tinggibadan = float(input("Masukan Tinggi Badan : "))
bmi = beratbadan / tinggibadan
print(f"Berat Badan :{beratbadan}Kg")
print(f"Tinggi Badan : {tinggibadan}M")
print(f"Nilai BMI anda : {bmi}")
if bmi < 18.5 :
    print("Berat Badan kurang")
elif 18.5 <= bmi < 24.9:
    print("Berat Badan kurang")
elif 25 <= bmi < 29.9:
    print("Kelebihan Berat Badan")
elif bmi / 30:
    print("Obesitas")
else : 
    print("berat badan normal")