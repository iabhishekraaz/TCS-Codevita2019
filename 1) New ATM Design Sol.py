#===================CODE BY==============
#===================ABHISHEK RAJ==============
#      Codevita 1
n=int(input())
total=int(input())
hun=int(input())
thun=int(input())
fhun=int(input())
thou=int(input())
max=0
for i in range(thou+1):
#     print("i=",i)
    for j in range(fhun+1):
#         print("j=",j)
        for k in range(thun+1):
#             print("k=",k)
            for l in range(hun+1):
#                 print("l=",l)
#                 print("i+j+k+l=",i+j+k+l)
#                 print("i*1000+j*500+k*200+l*100=",i*1000+j*500+k*200+l*100)
                if ((i+j+k+l)<=n and (i*1000+j*500+k*200+l*100)==total):
                    c=i+j+k+l
                    if max<c:
                        max=c
print(max)

                
