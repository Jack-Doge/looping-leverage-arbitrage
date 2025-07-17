import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定中文字體以避免亂碼
plt.rcParams['axes.unicode_minus'] = False  # 正確顯示負號

# 固定參數
ltv = 0.9  # loan-to-value 比例
borrow_rate = 0.053
deposit_rate = 0.0945
days = 60
years = days / 365
compound_year = 90 / 365

# 不同初始資金（1000~20000, step=100）
initial_investments = list(range(1000, 100001, 1000))
final_profits = []
layer_counts = []  # 記錄每個初始資金的實際循環層數
leverage_multipliers = []  # 記錄每個初始資金的槓桿乘數
apys = []  # 記錄每個初始資金的年化APY
liquidate_percents = []  # 記錄每個初始資金的清算浮動百分比

for initial_investment in initial_investments:
    profit = 0
    equity = initial_investment
    layer = 1
    total_loan = 0
    while True:
        loan_amount = equity * ltv
        deposit_amount = loan_amount
        gain = deposit_amount * ((1 + deposit_rate) ** years - 1)
        cost = loan_amount * ((1 + borrow_rate) ** years - 1) + 20
        round_profit = gain - cost
        print(f"本金: {initial_investment}, 層: {layer}, gain: {gain:.8f}, cost: {cost:.8f}, round_profit: {round_profit:.8f}")
        if round_profit <= 0:
            break
        profit += round_profit
        total_loan += loan_amount
        equity = loan_amount
        layer += 1
    final_profits.append(profit)
    layer_counts.append(layer - 1)
    # 槓桿乘數 = (初始資金 + 所有借來的資金) / 初始資金
    final_asset = initial_investment + total_loan
    leverage_multiplier = final_asset / initial_investment
    leverage_multipliers.append(leverage_multiplier)
    # 年化APY = 總收益 / 初始資金 / (天數/365)
    apy = (profit / initial_investment) / compound_year if initial_investment > 0 else 0
    apys.append(apy)
    liquidate_percent = (1 / leverage_multiplier) * 100
    liquidate_percents.append(liquidate_percent)

# print出每個初始資金的循環輪數
for inv, layers in zip(initial_investments, layer_counts):
    print(f'初始資金 {inv} USDT，循環輪數：{layers}')

# 畫圖：兩個窗格
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# 上方：年化APY折線圖
ax1.plot(initial_investments, apys, color='green', label='Estimated APY')
ax1.set_title('Estimated Annualized APY vs Initial Investment (Dynamic Layers)')
ax1.set_ylabel('Estimated APY')
ax1.grid(axis='y')
ax1.legend()

# 下方：根據leverage multiplier計算的liquidation amount百分比
ax2.plot(initial_investments, liquidate_percents, color='red', label='Liquidation Threshold (%)')
ax2.set_title('Collateral Price Drop to Liquidation (%) vs Initial Investment')
ax2.set_xlabel('Initial Investment (USDT)')
ax2.set_ylabel('Collateral Price Drop to Liquidation (%)')
ax2.grid(axis='y')
ax2.legend()

plt.tight_layout()
plt.savefig('arbitrage_apy_vs_investment.png', dpi=300)
plt.show() 