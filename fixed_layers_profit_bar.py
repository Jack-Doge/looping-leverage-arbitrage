import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Arial']  # 設定中文字體以避免亂碼

# 基本參數
initial_investment = 2000  # 初始自有資金
ltv = 0.9  # loan-to-value 比例
borrow_rate = 0.053
deposit_rate = 0.0945
days = 90
years = days / 365

# 用來儲存每輪循環的收益
profit = 0
profits = []
layers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 循環層數

# 循環借貸計算
equity = initial_investment
for i in layers:
    # 每一輪借出資金
    loan_amount = equity * ltv ** i
    # 存入總額為上一輪 equity + 新借的資金
    deposit_amount = loan_amount
    # 計算收益（複利）
    gain = deposit_amount * ((1 + deposit_rate) ** years - 1)
    cost = loan_amount * ((1 + borrow_rate) ** years - 1) + 8
    print(f'第 {i} 輪借款金額: {loan_amount:.2f} USDT, 存入金額: {deposit_amount:.2f} USDT, 收益: {gain:.2f} USDT, 成本: {cost:.2f} USDT')

    profit += gain - cost
    profits.append(profit)
    # 將新借來的資金疊加進 equity 用於下一輪
    # equity += loan_amount

# 繪製 bar chart
plt.figure(figsize=(10, 6))
plt.bar([f'{i} round' for i in layers], profits, color='skyblue')
plt.title(f'initial capital {initial_investment} USDT')
plt.xlabel('round')
plt.ylabel('profit (USDT)')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(f'arbitrage_profit_bar_chart{initial_investment}.png', dpi=300)
plt.show()
