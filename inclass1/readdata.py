import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv', index_col=0, low_memory = False)
print('Read in file')

dsNames=[x for x in df.columns if x.split('_')[0]=='DS']
normNames = [x for x in df.columns if x.split('-')[0] == 'Normal']
print('Split ds and norm samples')

dsMeans = df[dsNames].T.describe().loc['mean']
normMeans = df[normNames].T.describe().loc['mean']
print('Get mean if ds and norm samples')

print('Draw scatter plot')
plt.scatter(dsMeans,normMeans)
plt.title("Chr21 Gene Expression in Trisomy 21 Individuals vs. Normal")
plt.show()

print('Draw line graph')
sort_dsMean=np.sort(dsMeans)
plt.plot(sort_dsMean)
plt.show()
 
print('Draw Bar plot')
index = np.arange(len(normMeans))
plt.bar(index, normMeans)
plt.show()


print('Draw Box plot')
ds = np.asarray([ h for h in dsMeans if not np.isnan(h) ])
norm = np.asarray([ h for h in normMeans if not np.isnan(h) ])
plt.boxplot([ds,norm])
plt.show()



print('Done!')


