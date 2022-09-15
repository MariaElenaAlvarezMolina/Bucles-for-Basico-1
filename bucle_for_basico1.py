#1. Básico
for a in range(151):
    print(a)

print('--------')

#2. Múltiplos de cinco
for b in range(5, 1001):
    if(b % 5==0):
        print(b)

print('--------')

#3. Contar, a la manera del Dojo
for c in range(1, 101):
    if(c % 10==0):
        print("Coding Dojo")
    elif(c % 5==0):
        print("Coding")
    else:
        print(c)

print('--------')

#4. Whoa. Es un gran idiota
sum = 0
for d in range(500001):
    if(d % 2==1):
        sum += d
print(sum)

print('--------')

#5. Cuenta regresiva de a 4
count = 0
for e in range(2018, 0, -4):
    print(e)

print('--------')

#6. Contador flexible
lowNum = 1
highNum = 20
mult = 4
for f in range(lowNum, highNum+1):
    if(f % mult==0):
        print(f)