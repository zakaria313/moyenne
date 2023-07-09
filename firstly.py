print("First one : ch generale")
emd1 = float(input("please enter your note of emd1: "))
emd2 = float(input("please enter your note of emd2: "))
td = float(input("please enter your note of td: "))
tp = float(input("please enter your note of tp: "))

a1 = ((emd1+emd2)+((td+tp)/2))/3
print("")
print(a1)
print("")

print("2/ ch organique")
emd01 = float(input("please enter your note of emd1: "))
emd02 = float(input("please enter your note of emd2: "))
td1 = float(input("please enter your note of td: "))
tp1 = float(input("please enter your note of tp: "))

a2 = ((emd01+emd02)+((td1+tp1)/2))/3
print("")
print(a2)
print("")

print("3/ bio cell")
emd11 = float(input("please enter your note of emd1: "))
emd12 = float(input("please enter your note of emd2: "))
emd13 = float(input("please enter your note of emd3: "))
tp11 = float(input("please enter your note of tp: "))

a3 = (emd11+emd12+emd13+tp11)/4
print("")
print(a3)
print("")

print("4/ biostat")
emd111 = float(input("please enter your note of emd1: "))
emd112 = float(input("please enter your note of emd2: "))
td111 = float(input("please enter your note of td: "))

a4 = ((emd111+emd112)+td111)/3
print("")
print(a4)
print("")

print("5/ bio vegetale")
emd1111 = float(input("please enter your note of emd1: "))
emd1112 = float(input("please enter your note of emd2: "))
tp1111 = float(input("please enter your note of tp: "))

a5 = ((emd1111+emd1112)+(tp1111))/3
print("")
print(a5)
print("")

print("6/ physio")
emd11111 = float(input("please enter your note of emd: "))
td11111 = float(input("please enter your note of td: "))

a6 = ((emd11111*2)+(td11111))/3
print("")
print(a6)
print("")

print("7/ physique")
emd00 = float(input("please enter your note of emd1: "))
emd000 = float(input("please enter your note of emd2: "))
td00 = float(input("please enter your note of td: "))

a7 = ((emd00+emd000)+td00)/3
print("")
print(a7)
print("")

print("8/ anato")
a8 = float(input("please enter your note of emd: "))
print("")
print(a8)
print("")

print("9/ francais")
a9 = float(input("please enter your note of emd: "))
print("")
print(a9)
print("")

print("10/ histoire")
a10 = float(input("please enter your note of emd: "))
print("")
print(a10)

print("")
print("")

result = str(((a1*3)+(a2*3)+(a3*3)+(a4*3)+(a5*2)+(a6*2)+(a7*2)+(a8*2)+(a9*1)+(a10*1))/22)

print("--> the result is: "+result)

if float(result) >= 10:
    print("congratulation, from it to the top !")
elif float(result) < 10:
    print("rabi ywf9k, you can do'it , mzl kyn rattrapage , rak(i) reb7(a) ")
input("please press enter to exit")
import time
time.sleep(2)  # Delay of 2 seconds


























