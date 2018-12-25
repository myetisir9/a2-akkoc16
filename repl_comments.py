CommentList=[]
k=0
while True:
    x=input('Enter your comment:')
    CommentList.append(x)
    k+=1
    print('Previous comments:')
    for j in range(k):
        print(str(j+1)+'.'+CommentList[j])