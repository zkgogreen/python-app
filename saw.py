def transfor(arr):
    result = []
    for i in range(len(arr[0])):
        sementara = []
        for j in range(len(arr)):
            sementara.append(arr[j][i])
        result.append(sementara)
    return result

def sums(arr):
    hasil = []
    for i in arr:
        hasil.append(sum(i))
    return hasil
        

def saw(kriteria,alternatif):
    tralternatif = transfor(alternatif)
    pembagi = []
    for i in range(len(kriteria[0])):
        sementara = []
        if kriteria[0][i] == 'benefit':
            maxnumber = max(tralternatif[i])
            for j in tralternatif[i]:
                sementara.append((j/maxnumber)*kriteria[1][i])
        else:
            minnumber = min(tralternatif[i])
            for j in tralternatif[i]:
                sementara.append((minnumber/j)*kriteria[1][i])
        pembagi.append(sementara)
        hasil = transfor(pembagi)
    return sums(hasil)

kriteria = [
    ['cost','benefit','benefit','benefit','benefit','benefit'],
    [.2,.2,.25,.15,.1,.1]
]
alternatif = [
    [3500000,1,3,1,55,2],
    [3000000,3,2,2,55,2],
    [2500000,5,5,5,50,5],
    [750000,5,5,5,57,4]
]

result = saw(kriteria,alternatif)
print(result)
