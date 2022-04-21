"""
Python pulp kütüphanesi ile lineer optimizasyon çözümü.

Maksimize Z = 20x1 + 10x2 + 15x3 LP'ni çözelim.

3x1 + 2x2 + 5x3 <= 55

2x1 + x2 + x3 <= 26

5x1 + 2x2 + 4x3 <= 57

x1, x2 ve x3 >=0 ve tamsayı
"""
import pulp as p

Lp_problem = p.LpProblem("Problem", p.LpMaximize)

x = p.LpVariable("x", lowBound=0, cat="Continuous")
y = p.LpVariable("y", lowBound=0, cat="Continuous")
z = p.LpVariable("z", lowBound=0, cat="Continuous")




#Amaç Fonk
Lp_problem += 20*x + 10*y + 15*z

#Sınırlar
Lp_problem += 3*x + 2*y + 5*z <= 55
Lp_problem += 2*x + y + z <= 26
Lp_problem += 5*x + 2*y + 4*z <= 57

print(Lp_problem)#Problemi yazdırıp bir görelim doğru mu değil mi

cozum = Lp_problem.solve()

print(p.LpStatus[cozum])

print("x : ", p.value(x), "y : ", p.value(y), "z : ", p.value(Lp_problem.objective))





