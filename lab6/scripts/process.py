# 实验六(模电实验二)
import numpy as np
import matplotlib.pyplot as plt
import random

# 定义颜色列表
colors = ['g', 'r', 'c', 'm']
color_random = random.choice(colors)  # 随机选择一个颜色


# 定义方波函数
def square_wave(A, T, t, duty_cycle):
    return A * (t % T < T * duty_cycle) * 2 - A


# 数据，要改，定义电压频率和峰值
f = 403.6  # 电压频率为403.6Hz
A = 23.6 / 2  # 电压峰值为23.6V
duty_cycle = 0.5  # 占空比为50%

# 定义方波周期
T = 1 / f

# 定义时间范围
t = np.linspace(0, 3 * T, 512) # 3倍方波周期

# 绘制方波

plt.figure(figsize=(10, 6))
plt.title('Square Wave (Rf = 10kΩ)')
# 标记方波频率、幅值、占空比，位置处于空白处
plt.text(0.1, 0.8, 'Frequency: {:.2f}Hz'.format(f), fontsize=12, color='black', transform=plt.gca().transAxes)
plt.text(0.1, 0.75, 'Amplitude:± {:.2f}V'.format(A), fontsize=12, color='black', transform=plt.gca().transAxes)
plt.text(0.1, 0.7, 'Duty Cycle: {:.2f}'.format(duty_cycle), fontsize=12, color='black', transform=plt.gca().transAxes)

plt.plot(1000 * t, square_wave(A, T, t, duty_cycle), label='Square Wave', color=color_random)
plt.xlabel('Time / ms')
plt.ylabel('Voltage / V')
# 自定义y轴刻度
yticks = np.arange(-int(A+2)*10/10, int(A+2)*10/10, 2)  # 生成从-30到30的刻度，步长为4
plt.yticks(yticks)

plt.grid()
plt.legend()

# 保存图片
plt.savefig('Square Wave.png')
plt.show()

#  ×掉上一个窗口，绘制另外一个方波发生器，和三角波发生器，绘制在同一张图上
# 另外一个方波发生器，和三角波发生器，绘制在同一张图上
# 方波发生器
# 已知方波频率、幅值、占空比、周期时间，绘制方波波形
# 三角波发生器
# 已知三角波频率、幅值、周期时间，绘制三角波波形

# 数据需要改
T1 = 1 / 1000  # 方波周期为1ms,记录了可修改
A1 = 12.8 / 2  # 方波幅值为12.8V
duty_cycle1 = 0.5  # 方波占空比为47.37%
f2 = 1000  # 三角波频率为1000Hz
A2 = 4 / 2  # 三角波幅值为4V

# 三角波周期
T2 = 1 / f2

# 时间范围
t = np.linspace(0, 3 * T1, 512)  # 3倍方波周期


# 定义三角波函数
def triangle_wave(A, T, t):
    return 4 * A / T * np.abs(t % T - T / 2) - A


# 绘制方波和三角波
plt.figure(figsize=(10, 6))

plt.title('Square Wave and Triangle Wave')
# 图中标记方波占空比、幅值，三角波幅值、频率，位置处于空白处
plt.text(0.1, 0.8, 'Duty Cycle: {:.2f}'.format(duty_cycle1), fontsize=12, color='black', transform=plt.gca().transAxes)
plt.text(0.1, 0.75, 'Square Wave Amplitude:± {:.2f}V'.format(A1), fontsize=12, color='black',
         transform=plt.gca().transAxes)
plt.text(0.1, 0.7, 'Triangle Wave Amplitude:± {:.2f}V'.format(A2), fontsize=12, color='black',
         transform=plt.gca().transAxes)
plt.text(0.1, 0.65, 'Triangle Wave Frequency: {:.2f}Hz'.format(f2), fontsize=12, color='black',
         transform=plt.gca().transAxes)

plt.plot(1000 * t, square_wave(A1, T1, t, duty_cycle1), label='Square Wave', color=color_random)
plt.plot(1000 * t, triangle_wave(A2, T2, t), label='Triangle Wave', color='orange')
plt.xlabel('Time / ms')
plt.ylabel('Voltage / V')
# 自定义y轴刻度
yticks = np.arange(-8, 8.1, 1)  # 生成从-8到8的刻度，步长为1
plt.yticks(yticks)
plt.grid()
plt.legend()
# 保存图片
plt.savefig('Square Wave and Triangle Wave.png')
plt.show()
