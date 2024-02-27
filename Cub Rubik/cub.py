import tkinter as tk
from tkinter import ttk
from copy import deepcopy
faces=tk.Tk()
faces.title('Rubik')
colors=["white", "blue", "red", "green", "orange", "yellow"]

block = [] #matrice culori
for i in range(8):
    r = []
    for j in range(11):
        r.append(None)
    block.append(r)

id1=[[0,0,0],[0,0,0],[0,0,0]]#white
id2=[[0,0,0],[0,1,0],[0,0,0]]#blue
id3=[[0,0,0],[0,2,0],[0,0,0]]#red
id4=[[0,0,0],[0,3,0],[0,0,0]]#green
id5=[[0,0,0],[0,4,0],[0,0,0]]#orange
id6=[[0,0,0],[0,5,0],[0,0,0]]#yellow 
id=[id1,id2,id3,id4,id5,id6]#id cullori

incepe_rezolvarea = False

id1c=[[0,0,0],[0,0,0],[0,0,0]]#white
id2c=[[1,1,1],[1,1,1],[1,1,1]]#blue
id3c=[[2,2,2],[2,2,2],[2,2,2]]#red
id4c=[[3,3,3],[3,3,3],[3,3,3]]#green
id5c=[[4,4,4],[4,4,4],[4,4,4]]#orange
id6c=[[5,5,5],[5,5,5],[5,5,5]]#yellow 
id_complet=[id1c,id2c,id3c,id4c,id5c,id6c]#id cullori cub complet

def reset():
    id1r=[[0,0,0],[0,0,0],[0,0,0]]#white
    id2r=[[0,0,0],[0,1,0],[0,0,0]]#blue
    id3r=[[0,0,0],[0,2,0],[0,0,0]]#red
    id4r=[[0,0,0],[0,3,0],[0,0,0]]#green
    id5r=[[0,0,0],[0,4,0],[0,0,0]]#orange
    id6r=[[0,0,0],[0,5,0],[0,0,0]]#yellow 
    id_reset=[id1r,id2r,id3r,id4r,id5r,id6r]#id culori
    global id
    id=id_reset

def verify():
    ok=0
    global id
    for i in range(len(id)):
        s=0
        for j in range(len(id[i])):
            for k in range(len(id[i][j])):
                if id[i][j][k] == i:
                    s+=1
        if s==9:
            ok+=1
    if ok == 6:
        if message_label:
            destroy()
        message("Solutie completa!")
        return True
    return False

message_label=tk.Label()
def message(m):
    global message_label
    message_label = tk.Label(faces, text='\n'+m+'\n', font=("Areal", 12))
    message_label.grid(column=0, columnspan=11)

colt=[]
inter=[]
colt_complet=[]
inter_complet=[]
colt_cub=[]
inter_cub=[]
inter_cub_copy=[]
colt_cub_copy=[]
r_buton=False
def transform_id_in_pieces(id):
    global colt
    colt=[[id[0][0][0],id[1][2][0],id[4][2][2]],[id[0][0][2],id[1][2][2],id[2][2][0]],
          [id[0][2][2],id[2][2][2],id[3][2][0]],[id[0][2][0],id[3][2][2],id[4][2][0]],
          [id[5][2][0],id[1][0][0],id[4][0][2]],[id[5][2][2],id[1][0][2],id[2][0][0]],
          [id[5][0][2],id[2][0][2],id[3][0][0]],[id[5][0][0],id[4][0][0],id[3][0][2]]]
    global inter
    inter = [[id[0][0][1],id[1][2][1]],[id[0][1][2],id[2][2][1]],
            [id[0][2][1],id[3][2][1]],[id[0][1][0],id[4][2][1]],
            [id[5][2][1],id[1][0][1]],[id[5][1][2],id[2][0][1]],
            [id[5][0][1],id[3][0][1]],[id[5][1][0],id[4][0][1]],
            [id[1][1][0],id[4][1][2]],[id[1][1][2],id[2][1][0]],
            [id[3][1][0],id[2][1][2]],[id[3][1][2],id[4][1][0]]]
    
def verify_cub_complet():
    global id
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet

    transform_id_in_pieces(id_complet)
    colt_complet=colt
    inter_complet=inter
    transform_id_in_pieces(id)
    colt_cub=colt
    inter_cub=inter
    local_copy_id_inter=deepcopy(inter_cub)
    local_copy_id_complet_inter=deepcopy(inter_complet)
    
    for i in range(3):
        colt_complet.sort()
        colt_cub.sort()
        for j in range(8):
            colt_complet[j].sort()
            colt_cub[j].sort()

    for i in range(8):
        if colt_cub[i] != colt_complet[i]:
            message("Introduce o forma valida! Pentru a edita: ⬅️")
            return 
    for i in range(2):
        inter_complet.sort()
        inter_cub.sort()
        for j in range(12):
            inter_complet[j].sort()
            inter_cub[j].sort()
    for i in range(12):
        if inter_complet[i] != inter_cub[i]:
            message("Introduce o forma valida! Pentru a edita: ⬅️")
            return 
    for i in range(3):
        steaua_alba()
    
    print('\n\n')

    for i in range(3):
        colturi_alb()
    
    print('\n\n')
    
    for i in range(8):
        layer2()
        print('\n')
    f_galbena()
    
    print('\n')
    
    f_galbena_pt2()
    f_galbena_pt2()
    f_galbena_pt2()
    
    print('\n')
    layer3()

    print('\n')
    final()
    print('\n')
    print(id)
    


def buton_send_func():
    global buton_retry
    buton_retry.config(bg='white')

    global incepe_rezolvarea
    incepe_rezolvarea = True
    global r_buton
    if r_buton == True:
        return
    if message_label:
        destroy()
    verify()
    verify_cub_complet()
    r_buton = True

def destroy():
    message_label.destroy()
    
def buton_reset_func():
    global buton_retry
    buton_retry.config(bg='white')
    global incepe_rezolvarea
    global r_buton
    r_buton = False
    if message_label:
        destroy()
    if incepe_rezolvarea is True:
        destroy()
    incepe_rezolvarea = False
    global id
    reset()
    for i in range(7):
        for j in range(11):
            if i!=3 and j!=3 and i!=3 and j!=7:
                if i==1 and j==1 :
                    b=tk.Canvas(faces,width=70,height=70,bg='white',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)  
                elif i==1 and j==5 :
                    b=tk.Canvas(faces,width=70,height=70,bg='blue',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)  
                elif i==1 and j==9:
                    b=tk.Canvas(faces,width=70,height=70,bg='red',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)  
                elif i==5 and j==1:
                    b=tk.Canvas(faces,width=70,height=70,bg='green',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)  
                elif i==5 and j==5:
                    b=tk.Canvas(faces,width=70,height=70,bg='orange',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)  
                elif i==5 and j==9:
                    b=tk.Canvas(faces,width=70,height=70,bg='yellow',borderwidth=2,relief="solid")
                    b.grid(row=i,column=j)       
                else:
                    b=tk.Canvas(faces,width=70,height=70,bg='white',borderwidth=2,relief="solid",)
                    b.grid(row=i,column=j)
                    b.bind("<Button-1>",lambda event, ii=i, jj=j : schimbare_culori(ii,jj))
                    b.bind("<Button-3>",lambda event, ii=i, jj=j : schimbare_culori2(ii,jj))
                    block[i][j]=b
            else:
                b=tk.Canvas(faces,width=70,height=70,borderwidth=0,relief="solid")
                b.grid(row=i,column=j)
                block[i][j]=b

def schimbare_culori(ii,jj):
    global incepe_rezolvarea
    global block
    if incepe_rezolvarea is True:
        return
    ok=0
    index_i,index_j=0,0
    if ii<3:
        if jj <3:
            ok=0
            index_i=ii
            index_j=jj
        elif jj>3 and jj<7:
            ok=1
            index_i=ii
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=2
            index_i=ii
            index_j=abs(8-jj)
    else:
        if jj <3:
            ok=3
            index_i=abs(4-ii)
            index_j=jj
        elif jj>3 and jj<7:
            ok=4
            index_i=abs(4-ii)
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=5
            index_i=abs(4-ii)
            index_j=abs(8-jj)
    
    c_c = id[ok][index_i][index_j]
    
    if c_c+1 >= len(colors):
        c_c=0
    else:
        c_c+=1
    id[ok][index_i][index_j]=c_c;
    block[ii][jj].config(bg=colors[id[ok][index_i][index_j]])
    
def schimbare_culori2(ii,jj):
    global incepe_rezolvarea
    global block
    if incepe_rezolvarea is True:
        return
    ok=0
    index_i,index_j=0,0
    if ii<3:
        if jj <3:
            ok=0
            index_i=ii
            index_j=jj
        elif jj>3 and jj<7:
            ok=1
            index_i=ii
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=2
            index_i=ii
            index_j=abs(8-jj)
    else:
        if jj <3:
            ok=3
            index_i=abs(4-ii)
            index_j=jj
        elif jj>3 and jj<7:
            ok=4
            index_i=abs(4-ii)
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=5
            index_i=abs(4-ii)
            index_j=abs(8-jj)
    c_c = ok
    id[ok][index_i][index_j]=c_c;
    block[ii][jj].config(bg=colors[id[ok][index_i][index_j]])

def schimbare_culori3(ii,jj):
    global incepe_rezolvarea
    global block
    if incepe_rezolvarea is True:
        return
    ok=0
    index_i,index_j=0,0
    if ii<3:
        if jj <3:
            ok=0
            index_i=ii
            index_j=jj
        elif jj>3 and jj<7:
            ok=1
            index_i=ii
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=2
            index_i=ii
            index_j=abs(8-jj)
    else:
        if jj <3:
            ok=3
            index_i=abs(4-ii)
            index_j=jj
        elif jj>3 and jj<7:
            ok=4
            index_i=abs(4-ii)
            index_j=abs(4-jj)
        elif jj>7 and jj<11:
            ok=5
            index_i=abs(4-ii)
            index_j=abs(8-jj)
    if index_i==index_j and index_i==1:
        return
    else:
        c_c = ok
        id[ok][index_i][index_j]=c_c;
        block[ii][jj].config(bg=colors[id[ok][index_i][index_j]])

for i in range(7):
    for j in range(11):
        if i!=3 and j!=3 and i!=3 and j!=7:
            if i==1 and j==1 :
                b=tk.Canvas(faces,width=70,height=70,bg='white',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)  
            elif i==1 and j==5 :
                b=tk.Canvas(faces,width=70,height=70,bg='blue',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)  
            elif i==1 and j==9:
                b=tk.Canvas(faces,width=70,height=70,bg='red',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)  
            elif i==5 and j==1:
                b=tk.Canvas(faces,width=70,height=70,bg='green',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)  
            elif i==5 and j==5:
                b=tk.Canvas(faces,width=70,height=70,bg='orange',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)  
            elif i==5 and j==9:
                b=tk.Canvas(faces,width=70,height=70,bg='yellow',borderwidth=2,relief="solid")
                b.grid(row=i,column=j)       
            else:
                b=tk.Canvas(faces,width=70,height=70,bg='white',borderwidth=2,relief="solid",)
                b.grid(row=i,column=j)
                b.bind("<Button-1>",lambda event, ii=i, jj=j : schimbare_culori(ii,jj))
                b.bind("<Button-3>",lambda event, ii=i, jj=j : schimbare_culori2(ii,jj))
                block[i][j]=b
        else:
            b=tk.Canvas(faces,width=70,height=70,borderwidth=0,relief="solid")
            b.grid(row=i,column=j)
            block[i][j]=b

f_count = False
f_count1 = False
u_count = False
u_count1 = False

def F(face):
    global id
    id1=deepcopy(id)
    local_id=deepcopy(id)
    global f_count
    global f_count1
    global colt_cub
    global inter_cub
    global inter_cub_copy
    global colt_cub_copy

    id1[face][0][2]=local_id[face][0][0]
    id1[face][2][2]=local_id[face][0][2]
    id1[face][2][0]=local_id[face][2][2]
    id1[face][0][0]=local_id[face][2][0]

    id1[face][0][1]=local_id[face][1][0]
    id1[face][1][2]=local_id[face][0][1]
    id1[face][2][1]=local_id[face][1][2]
    id1[face][1][0]=local_id[face][2][1]
    
    if face == 1:
        st=4
        dr=2
        if f_count == True and f_count1 == True:
            print("F'",end=' ')
            f_count = False
            f_count1=False
        elif f_count == False:
            print("F",end=' ')
        id1[st][0][2]=local_id[0][0][0]
        id1[st][1][2]=local_id[0][0][1]
        id1[st][2][2]=local_id[0][0][2]

        id1[0][0][0]=local_id[dr][2][0]
        id1[0][0][1]=local_id[dr][1][0]
        id1[0][0][2]=local_id[dr][0][0]

        id1[5][2][0]=local_id[st][2][2]
        id1[5][2][1]=local_id[st][1][2]
        id1[5][2][2]=local_id[st][0][2]

        id1[dr][0][0]=local_id[5][2][0]
        id1[dr][1][0]=local_id[5][2][1]
        id1[dr][2][0]=local_id[5][2][2];
    elif face == 2:
        st=1
        dr=3
        if f_count == True and f_count1 == True:
            print("R'",end=' ')
            f_count = False
            f_count1=False
        elif f_count == False:
            print("R",end=' ')

        id1[0][0][2]=local_id[dr][2][0]
        id1[0][1][2]=local_id[dr][1][0]
        id1[0][2][2]=local_id[dr][0][0]

        id1[5][2][2]=local_id[st][2][2]
        id1[5][1][2]=local_id[st][1][2]
        id1[5][0][2]=local_id[st][0][2]

        id1[st][0][2]=local_id[0][0][2]
        id1[st][1][2]=local_id[0][1][2]
        id1[st][2][2]=local_id[0][2][2]

        id1[dr][0][0]=local_id[5][2][2]
        id1[dr][1][0]=local_id[5][1][2]
        id1[dr][2][0]=local_id[5][0][2]  
    elif face == 3:
        st=2
        dr=4
        if f_count == True and f_count1 == True:
            print("B'",end=' ')
            f_count = False
            f_count1=False
        elif f_count == False:
            print("B",end=' ')

        id1[0][2][0]=local_id[dr][0][0]
        id1[0][2][1]=local_id[dr][1][0]
        id1[0][2][2]=local_id[dr][2][0]

        id1[5][0][0]=local_id[st][0][2]
        id1[5][0][1]=local_id[st][1][2]
        id1[5][0][2]=local_id[st][2][2]

        id1[st][0][2]=local_id[0][2][2]
        id1[st][1][2]=local_id[0][2][1]
        id1[st][2][2]=local_id[0][2][0]

        id1[dr][0][0]=local_id[5][0][2]
        id1[dr][1][0]=local_id[5][0][1]
        id1[dr][2][0]=local_id[5][0][0]  
    elif face == 4:
        st=3
        dr=1
        if f_count == True and f_count1 == True:
            print("L'",end=' ')
            f_count = False
            f_count1=False
        elif f_count == False:
            print("L",end=' ')

        id1[0][2][0]=local_id[dr][2][0]
        id1[0][1][0]=local_id[dr][1][0]
        id1[0][0][0]=local_id[dr][0][0]

        id1[5][2][0]=local_id[st][0][2]
        id1[5][1][0]=local_id[st][1][2]
        id1[5][0][0]=local_id[st][2][2]

        id1[st][0][2]=local_id[0][2][0]
        id1[st][1][2]=local_id[0][1][0]
        id1[st][2][2]=local_id[0][0][0]

        id1[dr][0][0]=local_id[5][0][0]
        id1[dr][1][0]=local_id[5][1][0]
        id1[dr][2][0]=local_id[5][2][0]
    id=deepcopy(id1)
    transform_id_in_pieces(id)
    inter_cub=deepcopy(inter)
    colt_cub=deepcopy(colt)
    inter_cub_copy=deepcopy(inter_cub)
    colt_cub_copy=deepcopy(colt_cub)
 
def F_(face):
    global f_count
    global f_count1
    f_count = True
    F(face)
    F(face)
    f_count1 = True 
    F(face)
    
def d_F(face):
    F(face)
    F(face)

def U():
    global id
    id1=deepcopy(id)
    local_id=deepcopy(id)
    global u_count
    global u_count1
    global colt_cub
    global inter_cub
    global inter_cub_copy
    global colt_cub_copy
    if u_count == True and u_count1 == True:
        print("U'",end=' ')
        u_count = False
        u_count1=False
    elif u_count == False:
        print("U",end=' ')

    id1[5][0][2]=local_id[5][0][0]
    id1[5][2][2]=local_id[5][0][2]
    id1[5][2][0]=local_id[5][2][2]
    id1[5][0][0]=local_id[5][2][0]

    id1[5][0][1]=local_id[5][1][0]
    id1[5][1][2]=local_id[5][0][1]
    id1[5][2][1]=local_id[5][1][2]
    id1[5][1][0]=local_id[5][2][1]

    id1[1][0][0]=local_id[2][0][0]
    id1[1][0][1]=local_id[2][0][1]
    id1[1][0][2]=local_id[2][0][2]

    id1[3][0][0]=local_id[4][0][0]
    id1[3][0][1]=local_id[4][0][1]
    id1[3][0][2]=local_id[4][0][2]

    id1[4][0][0]=local_id[1][0][0]
    id1[4][0][1]=local_id[1][0][1]
    id1[4][0][2]=local_id[1][0][2]

    id1[2][0][0]=local_id[3][0][0]
    id1[2][0][1]=local_id[3][0][1]
    id1[2][0][2]=local_id[3][0][2]
    id=deepcopy(id1)
    transform_id_in_pieces(id)
    inter_cub=deepcopy(inter)
    colt_cub=deepcopy(colt)
    inter_cub_copy=deepcopy(inter_cub)
    colt_cub_copy=deepcopy(colt_cub)

def U_():
    global u_count
    global u_count1
    u_count = True
    U()
    U()
    u_count1 = True
    U()
    
def d_U():
    U()
    U()

def steaua_alba():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)

    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)
    for i in range(4):
        if 0 in inter_cub[i]:
            if inter_cub[i][0] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x!=i:
                    if x==0:
                        if i==1:
                            d_F(2);U();d_F(1)
                        elif i==2:
                            d_F(3);d_U();d_F(1)
                        elif i==3:
                            d_F(4);U_();d_F(1)
                    elif x==1:
                        if i==0:
                            d_F(1);U_();d_F(2)
                        elif i==2:
                            d_F(3);U();d_F(2)
                        elif i==3:
                            d_F(4);d_U();d_F(2)
                    elif x==2:
                        if i==0:
                            d_F(1);d_U();d_F(3)
                        elif i==1:
                            d_F(2);U_();d_F(3)
                        elif i==3:
                            d_F(4);U();d_F(3)
                    elif x==3:
                        if i==0:
                            d_F(1);U();d_F(4)
                        elif i==1:
                            d_F(2);d_U();d_F(4)
                        elif i==2:
                            d_F(3);U_();d_F(4)
            elif inter_cub[i][1] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x==0:
                    if i==1:
                        F(2);F(1)
                    elif i==2:
                        F(3);F_(2);U();d_F(1);F(2)
                    elif i==3:
                        F_(4);F_(1)
                    elif i==0:
                        F_(1);F(2);U();F_(2);d_F(1)
                elif x==1:
                    if i==0:
                        F_(1);F_(2)
                    elif i==2:
                        F(3);F(2)
                    elif i==3:
                        d_F(4);U_();F(1);F_(2);F_(1)
                    elif i==1:
                        F_(2);F(3);U();F_(3);d_F(2)
                elif x==2:
                    if i==0:
                        d_F(1);U();F_(4);F(3);F(4)
                    elif i==1:
                        F_(2);F_(3)
                    elif i==3:
                        F(4);F(3)
                    elif i==2:
                        F_(3);F(4);U();F_(4);d_F(3)
                elif x==3:
                    if i==0:
                        F(1);F(4)
                    elif i==1:
                        d_F(2);U();F_(1);F(4);F(1)
                    elif i==2:
                        F_(3);F_(4)
                    elif i==3:
                        F_(4);F(1);U();F_(1);d_F(4)
    
    for i in range(8,12,1):
        if 0 in inter_cub[i]:
            if inter_cub[i][0] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x==0:
                    if i==8:
                        F_(4);U_();F(4);d_F(1)
                    elif i==9:
                        F(2);U();F_(2);d_F(1)
                    elif i==10:
                        F_(2);U();F(2);d_F(1)
                    elif i==11:
                        F(4);U_();F_(4);d_F(1)
                elif x==1:
                    if i==8:
                        F_(4);d_U();F(4);d_F(2)
                    elif i==9:
                        F_(2)
                    elif i==10:
                        F(2)
                    elif i==11:
                        d_F(3);F(2);d_F(3)
                elif x==2:
                    if i==8:
                        F_(4);U();F(4);d_F(3)
                    elif i==9:
                        F(2);U_();F_(2);d_F(3)
                    elif i==10:
                        F_(2);U_();F(2);d_F(3)
                    elif i==11:
                        F(4);U();F_(4);d_F(3)
                elif x==3:
                    if i==8:
                        F(4)
                    elif i==9:
                        d_F(1);F(4);d_F(1)
                    elif i==10:
                        d_F(3);F_(4);d_F(3)
                    elif i==11:
                        F_(4)
            elif inter_cub[i][1] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x==0:
                    if i==8:
                        F_(1)
                    elif i==9:
                        F(1)
                    elif i==10:
                        d_F(2);F(1);d_F(2)
                    elif i==11:
                        d_F(4);F_(1);d_F(4)
                elif x==1:
                    if i==8:
                        F(1);U_();F_(1);d_F(2)
                    elif i==9:
                        F_(1);U_();F(1);d_F(2)
                    elif i==10:
                        F(3);U();F_(3);d_F(2)
                    elif i==11:
                        F(4);U();F_(3);F(2);F(3)
                elif x==2:
                    if i==8:
                        d_F(4);F(3);d_F(4)
                    elif i==9:
                        d_F(2);F_(3);d_F(2)
                    elif i==10:
                        F_(3)
                    elif i==11:
                        F(3)
                elif x==3:
                    if i==8:
                        F(1);U();F_(1);d_F(4)
                    elif i==9:
                        F_(1);U();F(1);d_F(4)
                    elif i==10:
                        F(3);U_();F_(3);d_F(4)
                    elif i==11:
                        F_(3);U_();F(3);d_F(4)

    for i in range(4,8,1):
        if 0 in inter_cub[i]:
            if inter_cub[i][0] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x==0:
                    if i==4:
                        d_F(1)
                    elif i==5:
                        U();d_F(1)
                    elif i==6:
                        d_U();d_F(1)
                    elif i==7:
                        U_();d_F(1)
                elif x==1:
                    if i==4:
                        U_();d_F(2)
                    elif i==5:
                        d_F(2)
                    elif i==6:
                       U();d_F(2)
                    elif i==7:
                        d_U();d_F(2)
                elif x==2:
                    if i==4:
                        d_U();d_F(3)
                    elif i==5:
                        U_();d_F(3)
                    elif i==6:
                        d_F(3)
                    elif i==7:
                        U();d_F(3)
                elif x==3:
                    if i==4:
                        U();d_F(4)
                    elif i==5:
                        d_U();d_F(4)
                    elif i==6:
                        U_();d_F(4)
                    elif i==7:
                        d_F(4)
            elif inter_cub[i][1] == 0:
                inter_cub_copy[i].sort()
                x=list.index(inter_complet,inter_cub_copy[i])
                if x==0:
                    if i==4:
                        F(2);U_();F_(2);F(1)
                    elif i==5:
                        F_(2);F(1);F(2)
                    elif i==6:
                        U();F_(2);F(1);F(2)
                    elif i==7:
                        F(4);F_(1);F_(4)
                elif x==1:
                    if i==4:
                        F(1);F_(2);F_(1)
                    elif i==5:
                        F(3);U_();F_(3);F(2)
                    elif i==6:
                        F_(3);F(2);F(3)
                    elif i==7:
                        U();F_(3);F(2);F(3)
                elif x==2:
                    if i==4:
                        U_();F(2);F_(3);F_(2)
                    elif i==5:
                        F(2);F_(3);F_(2)
                    elif i==6:
                        U();F(2);F_(3);F_(2)
                    elif i==7:
                        d_U();F(2);F_(3);F_(2)
                elif x==3:
                    if i==4:
                        F_(1);F(4);F(1)
                    elif i==5:
                        U();F_(1);F(4);F(1)
                    elif i==6:
                        d_U();F_(1);F(4);F(1)
                    elif i==7:
                        U_();F_(1);F(4);F(1)

def colturi_alb():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    colt_cub_copy=deepcopy(colt_cub)

    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)  
    
    for i in range(4):
        if 0 in colt_cub[i]:
            if colt_cub[i][0] == 0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==1:
                        F(2);U();F_(2);U();F(1);U_();F_(1)
                    elif i==2:
                        F_(2);d_U();F(2);U_();F_(4);U();F(4) 
                    elif i==3:
                        F(4);U();F_(4);U_();F(1);U_();F_(1)
                elif x==1:
                    if i==0:
                        F_(4);U_();F(4);F(2);U();F_(2)
                    elif i==2:
                        F_(2);d_U();F(2);U_();F(2);U();F_(2)
                    elif i==3:
                        F(4);U_();F_(4);d_U();F(2);U();F_(2)
                elif x==2:
                    if i==0:
                        F_(4);U_();F(4);U_();F(3);U();F_(3)
                    elif i==1:
                        F(2);U();F_(2);U_();F(3);U_();F_(3)
                    elif i==3:
                        F(4);d_U();F_(4);F(3);U_();F_(3)
                elif x==3:
                    if i==0:
                        F(1);d_U();F_(1);F(4);U_();F_(4)
                    elif i==1:
                        F(2);U();F_(2);d_U();F(4);U_();F_(4)
                    elif i==2:
                        F(3);U();F_(3);F(4);d_U();F_(4)
            elif colt_cub[i][1]==0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==0:
                        F(1);U();F_(1);U_();F(1);U();F_(1)
                    elif i==1:
                        F_(1);U_();d_F(1);d_U();F_(1)
                    elif i==2:
                        F_(2);U_();F(2);F(1);U_();F_(1)
                    elif i==3:
                        F_(3);F(1);U_();F_(1);F(3)
                elif x==1:
                    if i==0:
                        F(1);U();F_(1);F(2);d_U();F_(2)
                    elif i==1:
                        F_(1);U_();F(1);d_U();F(2);U_();F_(2)
                    elif i==2:
                        F_(2);U_();d_F(2);d_U();F_(2)
                    elif i==3:
                        F_(3);U();F(3);F(2);U();F_(2)
                elif x==2:
                    if i==0:
                        F(1);U();F_(1);F_(2);U();F(2)
                    elif i==1:
                        F_(1);F(3);U_();F(1);F_(3)
                    elif i==2:
                        F_(2);U_();F(2);d_U();F(3);U_();F_(3)
                    elif i==3:
                        F_(3);U_();d_F(3);d_U();F_(3)
                elif x==3:
                    if i==0:
                        F(1);F_(3);U();F(3);F_(1)
                    elif i==1:
                        F_(1);U_();F(1);F(4);U_();F_(4)
                    elif i==2:
                        F_(2);F(4);U_();F_(4);F(2)
                    elif i==3:
                        F_(3);U_();F(3);d_U();F(4);U_();F_(4)
            elif colt_cub[i][2]==0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==0:
                        F_(4);U_();F(4);d_U();F(1);U_();F_(1)
                    elif i==1:
                        F(2);F_(4);U();F(4);F_(2)
                    elif i==2:
                        F(3);U();F_(3);F_(4);U();F(4)
                    elif i==3:
                        F(4);U();d_F(4);d_U();F(4)
                elif x==1:
                    if i==0:
                        F_(4);F(2);U_();F(4);F_(2)
                    elif i==1:
                        F(2);U();F_(2);U_();F(2);U();F_(2)
                    elif i==2:
                        F_(1);F(3);U();F(1);F_(3)
                    elif i==3:
                        F(4);U();F_(4);F_(1);U();F(1)
                elif x==2:
                    if i==0:
                        F_(4);U_();F(4);F(3);U_();F_(3)
                    elif i==1:
                        F(2);U();d_F(2);d_U();F(2)
                    elif i==2:
                        F(3);U();F_(3);d_U();F_(2);U();F(2)
                    elif i==3:
                        F(4);F_(2);U();F_(4);F(2)
                elif x==3:
                    if i==0:
                        F_(4);d_U();d_F(4);U_();F_(4)
                    elif i==1:
                        F(2);U();F_(2);F_(3);U();F(3)
                    elif i==2:
                        F(3);U();d_F(3);d_U();F(3)
                    elif i==3:
                        F(4);U();F_(4);U_();F(4);U();F_(4)
    
    for i in range(4,8,1):
        if 0 in colt_cub[i]:
            if colt_cub[i][0] == 0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==4:
                        F(1);d_U();F_(1);d_U();F_(4);U();F(4)
                    elif i==5:
                        U();F(1);d_U();F_(1);d_U();F_(4);U();F(4)
                    elif i==6:
                        d_U();F(1);d_U();F_(1);d_U();F_(4);U();F(4)
                    elif i==7:
                        U_();F(1);d_U();F_(1);d_U();F_(4);U();F(4)
                elif x==1:
                    if i==4:
                        U_();F(2);d_U();F_(2);d_U();F_(1);U();F(1)
                    elif i==5:
                        F(2);d_U();F_(2);d_U();F_(1);U();F(1)
                    elif i==6:
                        U();F(2);d_U();F_(2);d_U();F_(1);U();F(1)
                    elif i==7:
                        d_U();F(2);d_U();F_(2);d_U();F_(1);U();F(1)
                elif x==2:
                    if i==4:
                        d_U();F(3);d_U();F_(3);U_();F(3);U();F_(3)
                    elif i==5:
                        U_();F(3);d_U();F_(3);U_();F(3);U();F_(3)
                    elif i==6:
                        F(3);d_U();F_(3);U_();F(3);U();F_(3)
                    elif i==7:
                        U();F(3);d_U();F_(3);U_();F(3);U();F_(3)
                elif x==3:
                    if i==4:
                        U();F(4);d_U();F_(4);U_();F(4);U();F_(4)
                    elif i==5:
                        d_U();F(4);d_U();F_(4);U_();F(4);U();F_(4)
                    elif i==6:
                        U_();F(4);d_U();F_(4);U_();F(4);U();F_(4)
                    elif i==7:
                        F(4);d_U();F_(4);U_();F(4);U();F_(4)
            elif colt_cub[i][1]==0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==4:
                        U_();F_(4);U();F(4)
                    elif i==5:
                        d_U();F(1);U_();F_(1)
                    elif i==6:
                        F(1);d_U();F_(1)
                    elif i==7:
                        U_();F(1);U();F_(1)
                elif x==1:
                    if i==4:
                        U_();F(2);U();F_(2)
                    elif i==5:
                        U();F(2);U_();F_(2)
                    elif i==6:
                        d_U();F(2);U_();F_(2)
                    elif i==7:
                        d_U();F(2);U();F_(2)
                elif x==2:
                    if i==4:
                        F_(2);d_U();F(2)
                    elif i==5:
                        F(3);U_();F_(3)
                    elif i==6:
                        U();F(3);U_();F_(3)
                    elif i==7:
                        F_(2);U();F(2)
                elif x==3:
                    if i==4:
                        F_(3);U();F(3)
                    elif i==5:
                        F(4);d_U();F_(4)
                    elif i==6:
                        F(4);U_();F_(4)
                    elif i==7:
                        F(4);U();F_(4)
            elif colt_cub[i][2]==0:
                colt_cub_copy[i].sort()
                x=list.index(colt_complet,colt_cub_copy[i])
                if x==0:
                    if i==4:
                        U();F(1);U_();F_(1)
                    elif i==5:
                        F_(4);U();F(4)
                    elif i==6:
                        U();F_(4);U();F(4)
                    elif i==7:
                        F(1);U_();F_(1)
                elif x==1:
                    if i==4:
                        F(2);U_();F_(2)
                    elif i==5:
                        F(2);U();F_(2)
                    elif i==6:
                        U();F(2);U();F_(2)
                    elif i==7:
                        F(2);d_U();F_(2)
                elif x==2:
                    if i==4:
                        F(3);d_U();F_(3)
                    elif i==5:
                        U_();F(3);U();F_(3)
                    elif i==6:
                        F(3);U();F_(3)
                    elif i==7:
                        d_U();F(3);U_();F_(3)
                elif x==3:
                    if i==4:
                        d_U();F(4);U_();F_(4)
                    elif i==5:
                        F_(3);d_U();F(3)
                    elif i==6:
                        U();F_(3);d_U();F(3)
                    elif i==7:
                        U();F(4);U_();F_(4)

def layer2():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)

    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)

    for i in range(4,8,1):
        if bool(5 in inter_cub[i]) == False:
            if inter_cub[i][1] == 1:
                if i==5:
                    U()
                elif i==6:
                    d_U()
                elif i==7:
                    U_()
                if inter_cub[i][0] == 2:
                    U();F(2);U_();F_(2);U_();F_(1);U();F(1)
                elif inter_cub[i][0] == 4:
                    U_();F_(4);U();F(4);U();F(1);U_();F_(1)
            elif inter_cub[i][1] ==2:
                if i==4:
                    U_()
                elif i==6:
                    U()
                elif i==7:
                    d_U()
                if inter_cub[i][0] ==1:
                    U_();F_(1);U();F(1);U();F(2);U_();F_(2)
                elif inter_cub[i][0]==3:
                    U();F(3);U_();F_(3);U_();F_(2);U();F(2)
            elif inter_cub[i][1]==3:
                if i==4:
                    d_U()
                elif i==5:
                    U_()
                elif i==7:
                    U()
                if inter_cub[i][0]==2:
                    U_();F_(2);U();F(2);U();F(3);U_();F_(3)
                elif inter_cub[i][0]==4:
                    U();F(4);U_();F_(4);U_();F_(3);U();F(3)
            elif inter_cub[i][1]==4:
                if i==4:
                    U()
                elif i==5:
                    d_U()
                elif i==6:
                    U_()
                if inter_cub[i][0]==3:
                    U_();F_(3);U();F(3);U();F(4);U_();F_(4)
                elif inter_cub[i][0]==1:
                    U();F(1);U_();F_(1);U_();F_(4);U();F(4)
    
    for i in range(8,12,1):
        if bool(5 in inter_cub[i]) == False:
            if inter_cub[8]!=[1,4]:
                F(1);U_();F_(1);U_();F_(4);U();F(4)
                return
            elif inter_cub[9]!=[1,2]:
                F(2);U_();F_(2);U_();F_(1);U();F(1)
                return 
            elif inter_cub[10]!=[3,2]:
                F(3);U_();F_(3);U_();F_(2);U();F(2)
                return
            elif inter_cub[11]!=[3,4]:
                F(4);U_();F_(4);U_();F_(3);U();F(3)
                return 
def f_galbena():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)

    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)

    
    if (id[5][0][1]==5 and id[5][1][0]==5 and id[5][1][1]==5 and id[5][1][2]==5 and id[5][2][1]==5):
        return
    elif (id[5][0][1]==5 and id[5][1][1]==5 and id[5][2][1]==5):
        U();F(1);F(2);U();F_(2);U_();F_(1)
    elif (id[5][1][0]==5 and id[5][1][1]==5 and id[5][1][2]==5):
        F(1);F(2);U();F_(2);U_();F_(1)
    elif (id[5][0][1]==5 and id[5][1][0]==5 and id[5][1][1]==5):
        F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    elif (id[5][0][1]==5 and id[5][1][1]==5 and id[5][1][2]==5):
        U_();F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    elif (id[5][1][1]==5 and id[5][1][2]==5 and id[5][2][1]==5):
        d_U();F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    elif (id[5][1][0]==5 and id[5][1][1]==5 and id[5][2][1]==5):
        U();F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    else:
        F(1);F(2);U();F_(2);U_();F_(1);d_U();F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)

def f_galbena_pt2():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)
    
    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)
    
    if (id[1][0][0]==5 and id[1][0][2]==5 and id[3][0][0]==5 and id[3][0][2]==5):#algo1
        F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    elif (id[2][0][0]==5 and id[2][0][2]==5 and id[4][0][0]==5 and id[4][0][2]==5):#algo1pt2
        U();F(1);F(2);U();F_(2);U_();F(2);U();F_(2);U_();F(2);U();F_(2);U_();F_(1)
    elif (id[5][2][0]==5 and id[1][0][2]==5 and id[2][0][2]==5 and id[3][0][2]==5):#algo2
        F(2);U();F_(2);U();F(2);d_U();F_(2)
    elif (id[5][2][2]==5 and id[2][0][2]==5 and id[3][0][2]==5 and id[4][0][2]==5):#algo2pt2
        U();F(2);U();F_(2);U();F(2);d_U();F_(2)
    elif (id[5][0][2]==5 and id[3][0][2]==5 and id[4][0][2]==5 and id[1][0][2]==5):#algo2pt3
        d_U();F(2);U();F_(2);U();F(2);d_U();F_(2)
    elif (id[5][0][0]==5 and id[4][0][2]==5 and id[1][0][2]==5 and id[2][0][2]==5):#algo2pt4
        U_();F(2);U();F_(2);U();F(2);d_U();F_(2)
    elif (id[5][2][0]==5 and id[2][0][0]==5 and id[3][0][0]==5 and id[4][0][0]==5):#algo3
        U_();F_(4);U_();F(4);U_();F_(4);d_U();F(4)
    elif (id[5][2][2]==5 and id[3][0][0]==5 and id[4][0][0]==5 and id[1][0][0]==5):#algo3pt2
        U();U_();F_(4);U_();F(4);U_();F_(4);d_U();F(4)
    elif (id[5][0][2]==5 and id[4][0][0]==5 and id[1][0][0]==5 and id[2][0][0]==5):#algo3pt3
        d_U();U_();F_(4);U_();F(4);U_();F_(4);d_U();F(4)
    elif (id[5][0][0]==5 and id[1][0][0]==5 and id[2][0][0]==5 and id[3][0][0]==5):#algo3pt4
        U_();U_();F_(4);U_();F(4);U_();F_(4);d_U();F(4)
    elif (id[5][0][0]==5 and id[5][0][2]==5 and id[2][0][0]==5):#algo4
        F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2)
    elif (id[5][0][0]==5 and id[5][2][0]==5 and id[3][0][0]==5):#algo4pt2
        U();F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2)
    elif (id[5][2][2]==5 and id[5][2][0]==5 and id[4][0][0]==5):#algo4pt3
        d_U();F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2)
    elif (id[5][2][2]==5 and id[5][0][2]==5 and id[1][0][0]==5):#algo4pt4
        U_();F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2)
    elif (id[5][0][2]==5 and id[5][2][0]==5 and id[2][0][0]==5):#algo5
        F(2);F_(3);F_(2);F(1);F(2);F(3);F_(2);F_(1)
    elif (id[5][0][0]==5 and id[5][2][2]==5 and id[3][0][0]==5):#algo5pt2
        U();F(2);F_(3);F_(2);F(1);F(2);F(3);F_(2);F_(1)
    elif (id[5][2][0]==5 and id[5][0][2]==5 and id[4][0][0]==5):#algo5pt3
        d_U();F(2);F_(3);F_(2);F(1);F(2);F(3);F_(2);F_(1)
    elif (id[5][0][0]==5 and id[5][2][2]==5 and id[1][0][0]==5):#algo5pt4
        U_();F(2);F_(3);F_(2);F(1);F(2);F(3);F_(2);F_(1)    
    elif id[5]!=id_complet[5]:
         F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2) #algoexit

def layer3():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)
    
    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)
    if verify():
        return
    if id[1][0][0]==id[1][0][2] or id[2][0][0]==id[2][0][2] or id[3][0][0]==id[3][0][2] or id[4][0][0]==id[4][0][2] :
        if id[1][0][0]==id[1][0][2] and id[3][0][0]!=id[3][0][2]:
            F(3);d_U();F_(3);U_();F(3);d_U();F_(1);U();F_(3);U_();F(1) 
        elif id[2][0][0]==id[2][0][2] and id[4][0][0]!=id[4][0][2]: 
            F(4);d_U();F_(4);U_();F(4);d_U();F_(2);U();F_(4);U_();F(2) 
        elif id[3][0][0]==id[3][0][2] and id[1][0][0]!=id[1][0][2]:
            F(1);d_U();F_(1);U_();F(1);d_U();F_(3);U();F_(1);U_();F(3)
        elif id[4][0][0]==id[4][0][2] and id[2][0][0]!=id[2][0][2]:
            F(2);d_U();F_(2);U_();F(2);d_U();F_(4);U();F_(2);U_();F(4)
    else:
        F(3);d_U();F_(3);U_();F(3);d_U();F_(1);U();F_(3);U_();F(1)  
        if verify():
            return
        if id[1][0][0]==id[1][0][2] or id[2][0][0]==id[2][0][2] or id[3][0][0]==id[3][0][2] or id[4][0][0]==id[4][0][2] :
            if id[1][0][0]==id[1][0][2] and id[3][0][0]!=id[3][0][2]:
                F(3);d_U();F_(3);U_();F(3);d_U();F_(1);U();F_(3);U_();F(1) 
            elif id[2][0][0]==id[2][0][2] and id[4][0][0]!=id[4][0][2]: 
                F(4);d_U();F_(4);U_();F(4);d_U();F_(2);U();F_(4);U_();F(2) 
            elif id[3][0][0]==id[3][0][2] and id[1][0][0]!=id[1][0][2]:
                F(1);d_U();F_(1);U_();F(1);d_U();F_(3);U();F_(1);U_();F(3)
            elif id[4][0][0]==id[4][0][2] and id[2][0][0]!=id[2][0][2]:
                F(2);d_U();F_(2);U_();F(2);d_U();F_(4);U();F_(2);U_();F(4)

def final():
    global colt
    global inter
    global colt_cub
    global inter_cub
    global colt_complet
    global inter_complet
    global inter_cub_copy
    global colt_cub_copy

    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)
    
    transform_id_in_pieces(id_complet)
    colt_complet=deepcopy(colt)
    inter_complet=deepcopy(inter)
    x=0
    j=0
    for i in range(1,5,1):
        if id[i][0][0]==id[i][0][1] and id[i][0][2]==id[i][0][1]:
            x=id[i][0][0]
            j=i
    if x==1:
        if j==1:
            if id[4][0][1]==2:
                d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
            if id[2][0][1]==4:
                F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
        elif j==2:
            U();
            if id[4][0][1]==2:
                d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
            if id[2][0][1]==4:
                F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
        elif j==3:
            d_U()
            if id[4][0][1]==2:
                d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
            if id[2][0][1]==4:
                F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
        elif j==4:
            U_()
            if id[4][0][1]==2:
                d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
            if id[2][0][1]==4:
                F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
    elif x==2:
        if j==1:
            U_()
            if id[1][0][1]==3:
                d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
            if id[3][0][1]==1:
                F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
        elif j==2:
            if id[1][0][1]==3:
                d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
            if id[3][0][1]==1:
                F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
        elif j==3:
            U()
            if id[1][0][1]==3:
                d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
            if id[3][0][1]==1:
                F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
        elif j==4:
            d_U()
            if id[1][0][1]==3:
                d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
            if id[3][0][1]==1:
                F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
    elif x==3:
        if j==1:
            d_U()
            if id[2][0][1]==4:
                d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
            if id[4][0][1]==2:
                F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
        elif j==2:
            U_()
            if id[2][0][1]==4:
                d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
            if id[4][0][1]==2:
                F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
        elif j==3:
            if id[2][0][1]==4:
                d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
            if id[4][0][1]==2:
                F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
        elif j==4:
            U()
            if id[2][0][1]==4:
                d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
            if id[4][0][1]==2:
                F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
    elif x==4:
        if j==1:
            U()
            if id[3][0][1]==1:
                d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
            if id[1][0][1]==3:
                F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
        elif j==2:
            d_U()
            if id[3][0][1]==1:
                d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
            if id[1][0][1]==3:
                F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
        elif j==3:
            U_()
            if id[3][0][1]==1:
                d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
            if id[1][0][1]==3:
                F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
        elif j==4:
            if id[3][0][1]==1:
                d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
            if id[1][0][1]==3:
                F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
    elif x==0:
        d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
        layer3()
        for i in range(1,5,1):
            if id[i][0][0]==id[i][0][1] and id[i][0][2]==id[i][0][1]:
                x=id[i][0][0]
                j=i
        if x==1:
            if j==1:
                if id[4][0][1]==2:
                    d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
                if id[2][0][1]==4:
                    F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
            elif j==2:
                U();
                if id[4][0][1]==2:
                    d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
                if id[2][0][1]==4:
                    F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
            elif j==3:
                d_U()
                if id[4][0][1]==2:
                    d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
                if id[2][0][1]==4:
                    F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
            elif j==4:
                U_()
                if id[4][0][1]==2:
                    d_F(2);U_();F_(2);U_();F(2);U();F(2);U();F(2);U_();F(2)
                if id[2][0][1]==4:
                    F_(2);U();F_(2);U_();F_(2);U_();F_(2);U();F(2);U();d_F(2)
        elif x==2:
            if j==1:
                U_()
                if id[1][0][1]==3:
                    d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
                if id[3][0][1]==1:
                    F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
            elif j==2:
                if id[1][0][1]==3:
                    d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
                if id[3][0][1]==1:
                    F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
            elif j==3:
                U()
                if id[1][0][1]==3:
                    d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
                if id[3][0][1]==1:
                    F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
            elif j==4:
                d_U()
                if id[1][0][1]==3:
                    d_F(3);U_();F_(3);U_();F(3);U();F(3);U();F(3);U_();F(3)
                if id[3][0][1]==1:
                    F_(3);U();F_(3);U_();F_(3);U_();F_(3);U();F(3);U();d_F(3)
        elif x==3:
            if j==1:
                d_U()
                if id[2][0][1]==4:
                    d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
                if id[4][0][1]==2:
                    F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
            elif j==2:
                U_()
                if id[2][0][1]==4:
                    d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
                if id[4][0][1]==2:
                    F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
            elif j==3:
                if id[2][0][1]==4:
                    d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
                if id[4][0][1]==2:
                    F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
            elif j==4:
                U()
                if id[2][0][1]==4:
                    d_F(4);U_();F_(4);U_();F(4);U();F(4);U();F(4);U_();F(4)
                if id[4][0][1]==2:
                    F_(4);U();F_(4);U_();F_(4);U_();F_(4);U();F(4);U();d_F(4)
        elif x==4:
            if j==1:
                U()
                if id[3][0][1]==1:
                    d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
                if id[1][0][1]==3:
                    F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
            elif j==2:
                d_U()
                if id[3][0][1]==1:
                    d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
                if id[1][0][1]==3:
                    F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
            elif j==3:
                U_()
                if id[3][0][1]==1:
                    d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
                if id[1][0][1]==3:
                    F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
            elif j==4:
                if id[3][0][1]==1:
                    d_F(1);U_();F_(1);U_();F(1);U();F(1);U();F(1);U_();F(1)
                if id[1][0][1]==3:
                    F_(1);U();F_(1);U_();F_(1);U_();F_(1);U();F(1);U();d_F(1)
        
def buton_complet_func():
    global id
    id=deepcopy(id_complet)
    for i in range(7):
        for j in range(11):
            if i!=3:
                if j!=3:
                    if j!=7:
                        if j!=11:
                            schimbare_culori3(i,j)

def buton_info_func():
    if message_label:
        destroy()
        message('1.Ține cubul cu fața albă spre tine, iar cu fața albastră in sus.\n 2. Completează fetele in ordinea: alb,albastru,rosu,verde,portocaliu. \n 3. Pentru fața galbenă (în sus): ține cubul cu partea albastră spre tine\n 4.Fiecare față se completează de sus în jos, de la dreapta spre stanga\n5.Alege culoarea apăsând click stânga pe pătrațica dorită pentru a derula prin acestea,\n iar click dreapta pentru a completa pătrațica cu culoarea feții curente \n6. Apasă butonul ➡️ pentru a trimite rezolvarea,\n pe 🔁 pentru a reseta fețele, iar pe 💯 pentru a face cubul complet\n7. Dupa ce ai trimis rezolvarea, poți modifica fețele apăsând pe ⬅️')

for j in range(11):
    b=tk.Canvas(faces,width=70,height=70,borderwidth=0,relief="solid")
    b.grid(row=7,column=j)
    block[7][j]=b

def buton_retry_func():
    global buton_retry
    buton_retry.config(bg='lightblue')
    global incepe_rezolvarea
    incepe_rezolvarea = False
    global r_buton
    r_buton=False

buton_send = tk.Button(faces, text="➡️",relief="solid",font="Areal",borderwidth=1,command=buton_send_func,activebackground='#423f3b',activeforeground='white')
buton_send.grid(row=8,column=0, columnspan=7, sticky=tk.W+tk.E)

buton_complet = tk.Button(faces, text="💯",relief="solid",font="Areal",borderwidth=1,command=buton_complet_func,activebackground='#423f3b',activeforeground='white')
buton_complet.grid(row=8,column=9, columnspan=1, sticky=tk.W+tk.E)

buton_reset = tk.Button(faces, text="🔁",relief="solid",font="Areal",borderwidth=1,command=buton_reset_func,activebackground='#423f3b',activeforeground='white')
buton_reset.grid(row=8,column=10, columnspan=1, sticky=tk.W+tk.E)

buton_info = tk.Button(faces, text="ℹ️",relief="solid",font="Areal",borderwidth=1,command=buton_info_func,activebackground='#423f3b',activeforeground='white')
buton_info.grid(row=8,column=8, columnspan=1, sticky=tk.W+tk.E)

buton_retry = tk.Button(faces, text="⬅️",relief="solid",font="Areal",borderwidth=1,command=buton_retry_func,activebackground='Lightblue',activeforeground='black')
buton_retry.grid(row=8,column=7, columnspan=1, sticky=tk.W+tk.E)

faces.mainloop()
