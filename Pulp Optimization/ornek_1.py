"""
Python pulp kütüphanesi ile lineer optimizasyon çözümü.

Maksimize Z = 5x1 + 3x2 LP'ni çözelim.

x1 + x2 <= 5 (Toplam yatırım 2.7 mliyar)
-x1 + 2x2 <=4 (En az iki tane sağlık ocağı)

2x1 - 2x2 <=3 (Yönetici sayısı 19'u geçmemeli)

x1, x2 >=0 ve tamsayı
"""
import pulp as p






Lp_problem = p.LpProblem("Problem", p.LpMaximize)

x = p.LpVariable("x", lowBound= 0, cat='Integer')
y = p.LpVariable("y", lowBound= 0, cat='Integer')



Lp_problem += 3*x + 3*y#Amaç fonksiyonu

Lp_problem += x + y <= 5#Kısıtlar
Lp_problem += -1*x - 2*y <=4#Kısıtlar
Lp_problem += 2*x - 2*y <=3#Kısıtlar


print(Lp_problem)#Problemi yazdırıp bir görelim doğru mu değil mi



cozum = Lp_problem.solve()
print(p.LpStatus[cozum])

print("x : ", p.value(x), "y : ", p.value(y), "z : ", p.value(Lp_problem.objective))









