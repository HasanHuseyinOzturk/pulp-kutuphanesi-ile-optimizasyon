"""
Python pulp kütüphanesi ile lineer optimizasyon çözümü.

Maksimize Z = 1200x1 + 2000x2 LP'ni çözelim.

2x1 + 6x2 <= 27 (Toplam yatırım 2.7 mliyar)

x2 >=2 (En az iki tane sağlık ocağı)

3x1 + x2 <=19 (Yönetici sayısı 19'u geçmemeli)

x1, x2 >= 0 ve tamsayı
"""
import pulp as p







#Problemi tanımlayalım 
Lp_problem = p.LpProblem("Problem", p.LpMaximize)




#X1 ve X2 yi x ve y olarak tanımlayalım.
x = p.LpVariable("x", lowBound = 0, cat='Integer')#x değerimizi 0 dan büyük ve Integer olarak tanımladık.
y = p.LpVariable("y", lowBound = 0, cat='Integer')#y değerimizi 0 dan büyük ve Integer olarak tanımladık.




#Amaç fonksiyonumuzu tanımlamak için Lp_problem += 1200*x1 + 2000*x2 yazmamız gerekir
Lp_problem += 1200*x + 2000*y#Burada amaç fonk artık tanımladık



#Sınırlarımızı da burada tanımlıyoruz
Lp_problem += 2*x + 6*y <=27
Lp_problem += y >=2
Lp_problem += 3*x + y <=19


print(Lp_problem)#Problemi yazdırıp bir görelim doğru mu değil mi


cozum = Lp_problem.solve()#Problemimizi çöz dedik ve cozum değişkenine atadık.
print(p.LpStatus[cozum])

print("x = ", p.value(x))
print("y = ", p.value(y))
print("z = ", p.value(Lp_problem.objective))




































