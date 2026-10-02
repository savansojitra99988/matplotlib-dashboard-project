import pandas as pd
import mplcursors
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
data=pd.read_csv('data.csv')
ytdata=pd.read_csv('ytdata.csv')


age=data['Age']
dev_sal=data["All_Devs"]
py_sal=data['Python']
js_sal=data['JavaScript']
print(data.head())
print(data.info())
print(ytdata.head())
dev_sal=pd.to_numeric(data['All_Devs'],errors='coerce').fillna(0)
py_sal=pd.to_numeric(data['Python'],errors='coerce').fillna(0)
js_sal=pd.to_numeric(data['JavaScript'],errors='coerce').fillna(0)



view_count=pd.to_numeric(ytdata['view_count'],errors='coerce').fillna(0)
likes=pd.to_numeric(ytdata['likes'],errors='coerce').fillna(0)
ratio=pd.to_numeric(ytdata['ratio'],errors='coerce').fillna(0)


fig,ax=plt.subplots(2,2,figsize=(14,10))
fig.suptitle("Tech Trends & Media Insights Dashboard",fontsize=46)
ax1=ax[0,0]
ax1.plot(age,dev_sal,linestyle='--',label='All Devs')
ax1.plot(age,py_sal,label='Python')
ax1.plot(age,js_sal,label='JavaScript')
ax1.fill_between(age, py_sal, dev_sal,
                 where=(py_sal > dev_sal),
                 interpolate=True, alpha=0.25, color='green',
                 label='Python > All Devs')
ax1.fill_between(age, py_sal, dev_sal,
                 where=(py_sal <= dev_sal),
                 interpolate=True, alpha=0.25, color='red',
                 label='Python <= All Devs')

ax1.set_title("Median Salary by Age")
ax1.set_xlabel("Age")
ax1.set_ylabel("Salary (USD)")
ax1.legend()

ax2=ax[0,1]
sc=ax2.scatter(view_count, likes, s=100, edgecolor='black', c=ratio, cmap='summer',alpha=0.75)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_title("YouTube Videos view VS likes count")
ax2.set_xlabel("View Count")
ax2.set_ylabel("Likes")

cbar=fig.colorbar(sc,ax=ax2)
cbar.set_label("Like/Dislike Ratio")

mplcursors.cursor(sc, hover=True)


ax3 = ax[1,0]
ax3.hist(age, bins=10, edgecolor='black')
ax3.axvline(age.mean(), color='red', linestyle='--', label='Mean Age')

ax3.set_title("Distribution of Developer Ages")
ax3.set_xlabel("Age")
ax3.set_ylabel("Frequency")
ax3.legend()
fig.tight_layout()

ax4=ax[1,1]
languages = ['Python', 'JavaScript', 'Java', 'C++']
usage=[40,30,20,10,]
explode=[0.1,0,0,0]

ax4.pie(usage,labels=languages,autopct='%1.1f%%',startangle=90,explode=explode,shadow=True)
ax4.set_title("Programming Language Usage")


plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig('dashboard.png')
plt.show()
