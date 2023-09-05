# estmation of values - crowd computing

from statistics import mean
from scipy import stats
Estimates=[1000,26,98,102,146,923,814,669,694,556]
Estimates.sort()
#statistics
print(mean(Estimates))
#scipy used
m=stats.trim_mean(Estimates,0.1)
print(m)
#manual
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    print(Estimates[i]) #removing first and last 10% values
print(mean(Estimates))

