import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # For a quick cost histogram

# Parameters (tweak these for sensitivity tests)
num_simulations = 10000
ar_prob = 0.3  # AR event probability (30% by 2040)
beset_prob_given_ar = 0.5  # Besetting given AR (50% post-fog)
salvage_cost = 10_000_000  # $10M per incident
demurrage_daily = 500_000  # $500K/day
avg_delay_days = 4  # Average fog/besetting duration

# Simulate transits
np.random.seed(42)  # For reproducibility
ar_events = np.random.binomial(1, ar_prob, num_simulations)
beset_events = np.random.binomial(1, beset_prob_given_ar, num_simulations) * ar_events
overall_beset_prob = np.mean(beset_events)

direct_cost = beset_events * salvage_cost
delay_cost = beset_events * (demurrage_daily * avg_delay_days)
total_cost_per_transit = direct_cost + delay_cost

# Summary stats
mean_total_cost = np.mean(total_cost_per_transit)
std_total_cost = np.std(total_cost_per_transit)
ci_low, ci_high = np.percentile(total_cost_per_transit, [2.5, 97.5])

summary = pd.DataFrame({
    'Metric': ['Overall Beset Prob', 'Mean Total Cost/Transit', 'Std Dev Cost', 
               '95% CI Low', '95% CI High', 'AR Events (Count)', 'Beset Events (Count)'],
    'Value': [f'{overall_beset_prob:.1%}', f'${mean_total_cost:,.0f}', f'${std_total_cost:,.0f}', 
              f'${ci_low:,.0f}', f'${ci_high:,.0f}', np.sum(ar_events), np.sum(beset_events)]
})
print(summary.to_string(index=False))

# Bonus: Plot cost distribution (saves as PNG for your article)
plt.figure(figsize=(8, 5))
plt.hist(total_cost_per_transit, bins=50, alpha=0.7, color='navy', edgecolor='white')
plt.axvline(mean_total_cost, color='red', linestyle='--', label=f'Mean: ${mean_total_cost:,.0f}')
plt.xlabel('Total Cost per Transit ($)')
plt.ylabel('Frequency')
plt.title('NSR Besetting Cost Distribution (10K Sims)')
plt.legend()
plt.savefig('besetting_cost_hist.png', dpi=300, bbox_inches='tight')  # High-res for doc
plt.show()  # Pops up if in interactive mode