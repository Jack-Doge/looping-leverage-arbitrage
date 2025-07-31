import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定中文字體以避免亂碼

# 固定參數
ltv = 0.9  # loan-to-value 比例
borrow_rate = 0.053
deposit_rate = 0.0945
days = 90
years = days / 365

# 不同初始資金（1000~10000, step=100）
initial_investments = list(range(1000, 10001, 100))
final_profits = []
layer_counts = []  # 記錄每個初始資金的實際循環層數
leverage_multipliers = []  # 記錄每個初始資金的槓桿乘數

for initial_investment in initial_investments:
    profit = 0
    equity = initial_investment
    layer = 1
    total_loan = 0
    while True:
        loan_amount = equity * ltv
        deposit_amount = loan_amount
        gain = deposit_amount * ((1 + deposit_rate) ** years - 1)
        cost = loan_amount * ((1 + borrow_rate) ** years - 1) + 8
        round_profit = gain - cost
        print(f'初始資金 {initial_investment} USDT，第 {layer} 輪：gain={gain:.2f}, cost={cost:.2f}, round_profit={round_profit:.2f}')
        if round_profit < 0:
            break  # 當前這輪收益為負，停止循環
        profit += round_profit
        total_loan += loan_amount
        equity = loan_amount  # 下一輪的投入只用本輪借來的資金
        layer += 1
    final_profits.append(profit)
    layer_counts.append(layer - 1)
    # 槓桿乘數 = (初始資金 + 所有借來的資金) / 初始資金
    final_asset = initial_investment + total_loan
    leverage_multiplier = final_asset / initial_investment
    leverage_multipliers.append(leverage_multiplier)

# print出每個初始資金的循環輪數
for inv, layers in zip(initial_investments, layer_counts):
    print(f'初始資金 {inv} USDT，循環輪數：{layers}')

# 畫圖：兩個窗格
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# 上方：收益折線圖
ax1.plot(initial_investments, final_profits, color='skyblue', label='Profit')
# 只標註部分點避免重疊
for idx in range(0, len(initial_investments), 5):
    x = initial_investments[idx]
    y = final_profits[idx]
    n = layer_counts[idx]
ax1.set_title('Profit vs Initial Investment (Dynamic Layers)')
ax1.set_ylabel('Profit (USDT)')
ax1.grid(axis='y')
ax1.legend()

# 下方：槓桿乘數折線圖
ax2.plot(initial_investments, leverage_multipliers, color='orange', label='Leverage Multiplier')
ax2.set_title('Leverage Multiplier vs Initial Investment')
ax2.set_xlabel('Initial Investment (USDT)')
ax2.set_ylabel('Leverage Multiplier')
ax2.grid(axis='y')
ax2.legend()

plt.tight_layout()
plt.savefig('arbitrage_profit_vs_investment.png', dpi=300)
plt.show()
