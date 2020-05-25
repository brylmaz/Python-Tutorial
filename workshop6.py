
x = [[1,5,7],[6,8,7],[3,5,1]]
y = [[9,6,1],[7,2,6],[4,7,5]]
sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j]+y[i][j]

print(sonuc)

