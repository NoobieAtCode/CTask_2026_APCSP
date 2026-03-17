### WORK ON THIS (the parser for the base-n to base-n operation)

base_n1 = 2
base_n2 = 10
test_input_base_n = 10010101

def convert_bases(basen1: int, basen2: int, inputbase_n):
    # Convert both inputs to Array[string]
    # Invert both lists 
    inputbase_n1_list_inv = invertlist(list(str(inputbase_n)))
    return inputbase_n1_list_inv

def invertlist(listinput: list):
    # The output of the program is added to this
    output = []

    for i in range(len(listinput)-1, -1, -1):
        output.append(listinput[i])

    return output

print(convert_bases(base_n1, base_n2, test_input_base_n))
#print(invertlist([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
#[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z] base 2 - base 36; cbase 37 - cbase 62