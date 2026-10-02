# ========== REAL-TIME CRICKET DASHBOARD PROJECT ==========
import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.animation import FuncAnimation

print("="*60)
print("REAL-TIME CRICKET DASHBOARD - Learning Journey + Final Project")
print("="*60)

# ---------------------------------------------------------
# 1. Basic Line Plot (Runs per Over)
# ---------------------------------------------------------
overs = np.arange(1, 6)
runs_per_over = np.array([8, 12, 10, 15, 9])
plt.plot(overs, runs_per_over, marker='o')
plt.title("Basic Line Plot - Runs per Over")
plt.xlabel("Overs"); plt.ylabel("Runs")
plt.grid()
plt.savefig("1_basic_line.png", dpi=300, bbox_inches="tight")
plt.show(); plt.clf()

# ---------------------------------------------------------
# 2. Bar Chart (Player Runs)
# ---------------------------------------------------------
players = ['Player A', 'Player B', 'Player C', 'Player D']
runs = np.array([45, 38, 52, 41])
bars = plt.bar(players, runs, color=['blue','green','orange','red'])
for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2., h, str(h), ha='center', va='bottom', fontweight='bold')
plt.title("Bar Chart - Player Runs")
plt.savefig("2_bar_chart.png", dpi=300, bbox_inches="tight")
plt.show(); plt.clf()

# ---------------------------------------------------------
# 3. Horizontal Bar Chart (Wickets)
# ---------------------------------------------------------
wickets = np.array([2, 3, 1, 4])
plt.barh(players, wickets, color='purple', alpha=0.7, edgecolor='black')
for i, v in enumerate(wickets):
    plt.text(v+0.1, i, str(v), va='center', fontweight='bold')
plt.title("Horizontal Bar - Wickets Taken")
plt.savefig("3_horizontal_bar.png", dpi=300, bbox_inches="tight")
plt.show(); plt.clf()

# ---------------------------------------------------------
# 4. Scatter Plot (Runs vs Wickets)
# ---------------------------------------------------------
plt.scatter(runs, wickets, s=200, c=wickets, cmap='viridis', edgecolors='black')
for i, p in enumerate(players):
    plt.annotate(p, (runs[i]+0.5, wickets[i]+0.2), ha='center', va='bottom', fontweight='bold')
plt.title("Scatter Plot - Runs vs Wickets")
plt.xlabel("Runs"); plt.ylabel("Wickets")
plt.colorbar(label="Wickets")
plt.savefig("4_scatter_plot.png", dpi=300, bbox_inches="tight")
plt.show(); plt.clf()

# ---------------------------------------------------------
# 5. Pie Chart (Team Contribution)
# ---------------------------------------------------------
plt.pie(runs, labels=players, autopct='%1.1f%%', explode=[0.1,0,0,0], shadow=True)
plt.title("Pie Chart - Contribution to Team Runs")
plt.savefig("5_pie_chart.png", dpi=300, bbox_inches="tight")
plt.show(); plt.clf()

# ---------------------------------------------------------
# 6. Animated Line Plot (Live Score Progression)
# ---------------------------------------------------------
timestamps = [datetime.datetime(2026, 10, 2, 10, 0) + datetime.timedelta(minutes=i) for i in range(30)]
ball_scores = np.random.randint(0, 7, size=30)
fig, ax = plt.subplots()
x_vals, y_vals = [], []

def animate(i):
    x_vals.append(timestamps[i])
    y_vals.append(sum(ball_scores[:i+1]))
    ax.cla()
    ax.plot(x_vals, y_vals, marker='o', color='red')
    ax.set_title("Live Score Progression")
    ax.set_xlabel("Ball Time"); ax.set_ylabel("Total Runs")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, alpha=0.3)

ani = FuncAnimation(fig, animate, frames=len(ball_scores), interval=500, repeat=False)
plt.show()

# ---------------------------------------------------------
# 7. FINAL PROJECT: REAL-TIME CRICKET DASHBOARD
# ---------------------------------------------------------
players = ['Player A', 'Player B', 'Player C', 'Player D']
runs = np.array([450, 380, 520, 410])
wickets = np.array([12, 18, 7, 15])
strike_rate = np.array([135, 128, 142, 130])

team_runs = runs.sum()
timestamps = [datetime.datetime(2026, 10, 2, 10, 0) + datetime.timedelta(minutes=i) for i in range(120)]
ball_scores = np.random.randint(0, 7, size=120)

fig = plt.figure(figsize=(16, 10))

# Plot 1: Runs Comparison
ax1 = plt.subplot(2, 3, 1)
bars = ax1.bar(players, runs, color=['#1f77b4','#ff7f0e','#2ca02c','#d62728'], alpha=0.8)
for bar in bars:
    h = bar.get_height()
    ax1.text(bar.get_x()+bar.get_width()/2., h, str(h), ha='center', va='bottom', fontweight='bold')
ax1.set_title("Runs Scored by Players"); ax1.set_ylabel("Runs"); ax1.grid(axis='y', alpha=0.3)

# Plot 2: Wickets Comparison
ax2 = plt.subplot(2, 3, 2)
ax2.barh(players, wickets, color='purple', alpha=0.7, edgecolor='black')
for i, v in enumerate(wickets):
    ax2.text(v+0.5, i, str(v), va='center', fontweight='bold')
ax2.set_title("Wickets Taken"); ax2.set_xlabel("Wickets"); ax2.grid(axis='x', alpha=0.3)

# Plot 3: Strike Rate
ax3 = plt.subplot(2, 3, 3)
ax3.plot(players, strike_rate, marker='o', markersize=10, linewidth=2.5, color='green')
ax3.set_title("Strike Rate Comparison"); ax3.set_ylabel("Strike Rate"); ax3.grid(True, alpha=0.3)

# Plot 4: Runs vs Wickets
ax4 = plt.subplot(2, 3, 4)
sc = ax4.scatter(runs, wickets, s=300, c=strike_rate, cmap='viridis', alpha=0.7, edgecolors='black', linewidths=2)
for i, p in enumerate(players):
    ax4.annotate(p, (runs[i]+0.5, wickets[i]+0.5), ha='center', va='bottom', fontweight='bold')
ax4.set_title("Runs vs Wickets"); ax4.set_xlabel("Runs"); ax4.set_ylabel("Wickets")
plt.colorbar(sc, ax=ax4, label="Strike Rate")

# Plot 5: Team Contribution
ax5 = plt.subplot(2, 3, 5)
ax5.pie(runs, labels=players, autopct='%1.1f%%', shadow=True, explode=[0.1,0,0,0])
ax5.set_title("Contribution to Team Runs")

# Plot 6: Real-Time Match Score
ax6 = plt.subplot(2, 3, 6)
x_vals, y_vals = [], []
def animate_final(i):
    x_vals.append(timestamps[i])
    y_vals.append(sum(ball_scores[:i+1]))
    ax6.cla()
    ax6.plot(x_vals, y_vals, marker='o', color='red', linewidth=2)
    ax6.set_title("Live Match Score"); ax6.set_xlabel("Ball Time"); ax6.set_ylabel("Total Runs")
    ax6.tick_params(axis='x', rotation=45); ax6.grid(True, alpha=0.3)

ani = FuncAnimation(fig, animate_final, frames=len(ball_scores), interval=1000, repeat=False)

plt.suptitle("REAL-TIME CRICKET PERFORMANCE DASHBOARD", fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout(rect=[0,0,1,0.97])
plt.show()

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------
print("="*60)
print("SUMMARY - FILES CREATED")
print("="*60)
print("""
1_basic_line.png
2_bar_chart.png
3_horizontal_bar.png
4_scatter_plot.png
5_pie_chart.png
(Animated plots shown live, not saved)
Final Dashboard displayed live
""")
