import seaborn as sns
from scipy.stats import poisson
data_poisson=poisson.rvs(mu=3, size=1000)
data_poisson
ax=sns.displot(data_poisson)
ax.set(xlabel='poisson distribution',ylabel='Frequency')
from scipy.stats import norm
data_normal=norm.rvs(size=1000,loc=0,scale=1)
data_normal
ax=sns.displot(data_normal),
   bins=100,
   kde=True
ax.set(xlabel='normal distribution',ylabel='frequency')
