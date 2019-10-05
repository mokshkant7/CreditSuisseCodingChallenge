inputs=[4,1,1,2,2,3,1,5,1]
time_freq=inputs[1:]
X=[time_freq[1]]

for i,freq in enumerate(time_freq[2:]):
    flag=0
    if not i%2==0:
        for j,x in enumerate(X):
            if x==freq or x + time_freq[i-1]>=freq and x-time_freq[i-1]<=freq:
                X[j]=freq
                flag=1
        if flag == 0:
            X.append(freq)

output=len(X)
print(output)
