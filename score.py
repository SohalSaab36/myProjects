import footballScorePredictor as fc
t1,s1,t2,s2 = fc.getInfo()
for g in range(100):
    fc.predictScore(t1,s1,t2,s2)