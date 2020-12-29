
def rgb2gray(r,g,b):
    # 0.3R+0.6G+0.1B
    return 0.3*r+0.6*g+0.1*b

flag = True
n=0
m=0
gray=[]
while flag:
    try:
        row = input().split()
        n = len(row)
        m+=1
        gray_row=0
        for i in range(n):
            b,g,r = map(int, row[i].split(','))
            gray_row +=rgb2gray(r,g,b)
        gray.append(gray_row/n)
    except:
        flag=False
print('day' if sum(gray)/m>100 else 'night')
