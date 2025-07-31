
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定中文字體以避免亂碼

# 假設初始投入金額
initial_amount = 100  # USDT

# 協議利率（年化）
borrow_rate = 0.053  # A 協議借款利率
deposit_rate = 0.0945  # B 協議存款利率

# 時間軸（以天為單位，最多一年）
days = np.arange(1, 366)  # 從第1天到第365天
years = days / 365  # 換算成年

# 計算每日的收益（複利假設）
borrow_cost = initial_amount * ((1 + borrow_rate) ** years - 1)
deposit_gain = initial_amount * ((1 + deposit_rate) ** years - 1)
net_profit = deposit_gain - borrow_cost

# 繪圖
plt.figure(figsize=(10, 6))
plt.plot(days, net_profit, label='Net Profit (USDT)', color='green')
plt.axhline(0, color='gray', linestyle='--')
plt.title('循環借貸套利收益曲線')
plt.xlabel('到期日（天）')
plt.ylabel('收益（USDT）')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()