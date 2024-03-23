# -*encoding:gbk
import matplotlib.pyplot as plt
import numpy as np
delta_p=[i*50 for i in range(1,6)]
N=[4.5,9.0,13.2,17.8,22.2]
# 拟合数据
coeffs = np.polyfit(delta_p, N, 1)
print(coeffs)
fit_func = np.poly1d(coeffs)

# 生成拟合线的y值
fit_y = fit_func(delta_p)
plt.scatter(delta_p,N)
plt.plot(delta_p, fit_y, 'r')
plt.xlabel('delta_p')
plt.ylabel('N',rotation=0)
plt.show()