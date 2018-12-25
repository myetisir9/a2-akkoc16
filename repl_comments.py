from hashlib import sha256

def create_hash(password):
    #Function taken from: https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

password_hash = '51447d39ee4c9a8b7f54b58d8d4dd3eab587969dc3229eb51191fa3a4eaaa1df'
CommentList=[]
k=0
while True:
    x=input('Enter your comment:')
    y=input('Enter your password:')
    password_hash2 = create_hash(y)

    if password_hash == password_hash2:
        CommentList.append(x)
        print('Previous comments:')
        k+=1
        for j in range(k):
            print(str(j+1)+'.'+CommentList[j])
    else :
        print('Wrong password.')
