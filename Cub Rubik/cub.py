#pip install ursina
import tkinter as tk
from copy import deepcopy
from ursina import *
import random
import subprocess

faces=tk.Tk()
icon_image = tk.PhotoImage(file='img.png')
faces.title('Rubik')
colors=["white", "blue", "red", "green", "orange", "yellow"]
faces.iconphoto(True, icon_image)
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
f10=open('textures by positions\colturi_inter_ids.txt','w')
id1c=[[0,0,0],[0,0,0],[0,0,0]]#white
id2c=[[1,1,1],[1,1,1],[1,1,1]]#blue
id3c=[[2,2,2],[2,2,2],[2,2,2]]#red
id4c=[[3,3,3],[3,3,3],[3,3,3]]#green
id5c=[[4,4,4],[4,4,4],[4,4,4]]#orange
id6c=[[5,5,5],[5,5,5],[5,5,5]]#yellow 
id_complet=[id1c,id2c,id3c,id4c,id5c,id6c]#id cullori cub complet
file1 = open("id_update.txt", "w")
file1.close()
file1 = open("id_update.txt", "a")
id_scrambled=[]
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
        transform_id_in_pieces(id_complet)
        f10=open('textures by positions\colturi_inter_ids.txt','w')
        f10.write(str(colt))
        f10.write('\n')
        f10.write(str(inter))
        f10.close()
        message("Solutie completa!")
        f1 = open("solved.txt", "w")
        f1.write(solved)
        f1.close()
        f = open("id.txt", "w")
        f.write(str(id))
        return True
    return False
""""""
message_label=tk.Label()
def message(m):
    global message_label
    message_label = tk.Label(faces, text='\n'+m+'\n', font=("Areal", 12))
    message_label.grid(row=9,column=0, columnspan=11)
solved=''
mm='\n'
def message2(m):
    global nr_mutari
    global mm
    global message_label
    if message_label:
        destroy()
    if m:
        if nr_mutari>=34:
            mm+="           \n           "
            nr_mutari=0
            mm+=m
        else:
            mm+=m
        message_label = tk.Label(faces, text=mm, font=("Areal", 12))
        message_label.grid(row=0,rowspan=10,column=18, columnspan=25)
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
    global nr_mutari
    transform_id_in_pieces(id_complet)
    colt_complet=colt
    inter_complet=inter
    transform_id_in_pieces(id)
    colt_cub=colt
    inter_cub=inter
    local_copy_id_colt=deepcopy(colt)
    local_copy_id_inter=deepcopy(inter)
    
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
    if verify():
        return 
    f10=open('textures by positions\colturi_inter_ids.txt','w')
    f10.write(str(local_copy_id_colt))
    f10.write('\n')
    f10.write(str(local_copy_id_inter))
    f10.close()
    nr_mutari=0
    global random_scramble
    f = open("id.txt", "w")
    f.write(str(id))
    global file1
    if file1:
        file1.close()
    file1 = open("id_update.txt", "w")
    file1.close()
    file1 = open("id_update.txt", "a")
    global solved
    if random_scramble:
        message2("Amestecare random:\n           "+random_scramble+'           \n\n\n')
    message2("           \nPartea 1. Steaua albă:\n           ")
    for i in range(3):
        steaua_alba()
    nr_mutari=0
    print('\n\n')
    solved+='\n'
    message2("           \n\nPartea 2. Colțurile albe:\n           ")

    for i in range(3):
        colturi_alb()
    solved+='\n'
    print('\n\n')
    nr_mutari=0
    message2("           \n\nPartea 3. Layer 2:\n           ")
    for i in range(8):
        layer2()
        print('\n')
    solved+='\n'
    nr_mutari=0
    message2("           \n\nPartea 4. Steaua galbenă:           \n")
    f_galbena()
    solved+='\n'
    print('\n')
    nr_mutari=0
    message2("\n\n           Partea 5. Partea galbenă completă:           \n")
    i=0
    print('step1')
    while id[5]!=id_complet[5]:
        i+=1
        f_galbena_pt2()
        if i>10:
            break
    if i>10:
        f1 = open("solved.txt", "w")
        f1.write(solved)
        f1.close()
        destroy()
        message('*Error 404*\n\nInvalid solve')
        return 
    print('next step1')
    nr_mutari=0
    message2("           \n\nPartea 6. Rearanjare :\n           ")
    print('\n')
    solved+='\n'
    layer3()
    nr_mutari=0
    message2("           \n\nPartea 7. Algoritm Final :\n           ")
    print('\n')
    solved+='\n'
    final()
    print('\n')
    
    message2('           \n')
    f1 = open("solved.txt", "w")
    f1.write(solved)
    print(id)
    print(solved)
    f1.close()
    file1.close()
    
def buton_send_func():
    global nr_mutari
    nr_mutari=0
    global buton_retry
    global mm
    global b_random
    global random_scramble
    b_random=False
    global file1
    if file1:
        file1.close()
    file1 = open("id_update.txt", "w")
    file1.close()
    file1 = open("id_update.txt", "a")
    mm='\n'
    buton_retry.config(bg='white',foreground='black')
    global solved
    solved=''
    global incepe_rezolvarea
    incepe_rezolvarea = True
    global r_buton
    if r_buton == True:
        return
    if message_label:
        destroy()
    verify()
    global id
    global id_scrambled
    id_scrambled=deepcopy(id)
    verify_cub_complet()
    random_scramble=''
    r_buton = True
    id=deepcopy(id_scrambled)

def destroy():
    message_label.destroy()
    
def buton_reset_func():
    global file1
    if file1:
        file1.close()
    file1 = open("id_update.txt", "w")
    file1.close()
    file1 = open("id_update.txt", "a")
    global mm
    global nr_mutari
    nr_mutari=0
    mm='\n'
    global b_random
    global random_scramble
    b_random=False
    random_scramble=''
    global buton_retry
    buton_retry.config(bg='white',foreground='black')
    global incepe_rezolvarea
    global r_buton
    global solved
    solved=''
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

def schimbare_culori4(ii,jj):
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
                b=tk.Canvas(faces,width=70,height=70,bg='white',borderwidth=2,relief="solid")
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
nr_mutari=0

def F(face):
    global id,f_count,f_count1,colt_cub,inter_cub,inter_cub_copy,colt_cub_copy,nr_mutari,b_random,random_scramble,solved,file1
    id1=deepcopy(id)
    local_id=deepcopy(id)
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
        if b_random:
            if f_count == True and f_count1 == True:
                random_scramble+="F' "
                f_count = False
                f_count1=False
            elif f_count == False:
                random_scramble+="F "
        else:
            if f_count == True and f_count1 == True:
                print("F'",end=' ')
                message2("F' ")
                solved+="F' "
                f_count = False
                f_count1=False
                nr_mutari+=1
            elif f_count == False:
                print("F",end=' ')
                message2("F ")
                solved+="F "
                nr_mutari+=1
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
        if b_random:
            if f_count == True and f_count1 == True:
                random_scramble+="R' "
                f_count = False
                f_count1=False
            elif f_count == False:
                random_scramble+="R "
        else:
            if f_count == True and f_count1 == True:
                print("R'",end=' ')
                message2("R' ")
                solved+="R' "
                f_count = False
                f_count1=False
                nr_mutari+=1
            elif f_count == False:
                print("R",end=' ')
                message2("R ")
                solved+="R "
                nr_mutari+=1

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
        if b_random:
            if f_count == True and f_count1 == True:
                random_scramble+="B' "
                f_count = False
                f_count1=False
            elif f_count == False:
                random_scramble+="B "
        else:
            if f_count == True and f_count1 == True:
                print("B'",end=' ')
                message2("B' ")
                solved+="B' "
                f_count = False
                f_count1=False
                nr_mutari+=1
            elif f_count == False:
                print("B",end=' ')
                message2("B ")
                solved+="B "
                nr_mutari+=1

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
        if b_random:
            if f_count == True and f_count1 == True:
                random_scramble+="L' "
                f_count = False
                f_count1=False
            elif f_count == False:
                random_scramble+="L "
        else:
            if f_count == True and f_count1 == True:
                print("L'",end=' ')
                message2("L' ")
                solved+="L' "
                f_count = False
                f_count1=False
                nr_mutari+=1
            elif f_count == False:
                print("L",end=' ')
                message2("L ")
                solved+="L "
                nr_mutari+=1

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
    file1.write(str(id))
    file1.write('\n')
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
    global id, u_count, u_count1, colt_cub, inter_cub, inter_cub_copy, colt_cub_copy, nr_mutari, b_random, random_scramble, solved, file1
    id1=deepcopy(id)
    local_id=deepcopy(id)
    if b_random:
            if u_count == True and u_count1 == True:
                random_scramble+="U' "
                u_count = False
                u_count1=False
            elif u_count == False:
                random_scramble+="U "
    else:
        if u_count == True and u_count1 == True:
            print("U'",end=' ')
            message2("U' ")
            solved+="U' "
            u_count = False
            u_count1=False
            nr_mutari+=1
        elif u_count == False:
            print("U",end=' ')
            message2("U ")
            solved+="U "
            nr_mutari+=1

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
    file1.write(str(id))
    file1.write('\n')
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
        if inter_cub[i][0]!=5 and inter_cub[i][1]!=5:
            if inter_cub[i][1] == 1:
                if i==5:
                    if inter_cub[i][0] == 2:
                        U();U();F(2);U_();F_(2);U_();F_(1);U();F(1)
                        return
                    elif inter_cub[i][0] == 4:
                        U();U_();F_(4);U();F(4);U();F(1);U_();F_(1)
                        return
                elif i==6:
                    if inter_cub[i][0] == 2:
                        d_U();U();F(2);U_();F_(2);U_();F_(1);U();F(1)
                        return
                    elif inter_cub[i][0] == 4:
                        d_U();U_();F_(4);U();F(4);U();F(1);U_();F_(1)
                        return
                elif i==7:
                    if inter_cub[i][0] == 2:
                        U_();U();F(2);U_();F_(2);U_();F_(1);U();F(1)
                        return
                    elif inter_cub[i][0] == 4:
                        U_();U_();F_(4);U();F(4);U();F(1);U_();F_(1)
                        return
                if inter_cub[i][0] == 2:
                    U();F(2);U_();F_(2);U_();F_(1);U();F(1)
                    return
                elif inter_cub[i][0] == 4:
                    U_();F_(4);U();F(4);U();F(1);U_();F_(1)
                    return
            elif inter_cub[i][1] ==2:
                if i==4:
                    if inter_cub[i][0] ==1:
                        U_();U_();F_(1);U();F(1);U();F(2);U_();F_(2)
                        return
                    elif inter_cub[i][0]==3:
                        U_();U();F(3);U_();F_(3);U_();F_(2);U();F(2)
                        return
                elif i==6:
                    if inter_cub[i][0] ==1:
                        U();U_();F_(1);U();F(1);U();F(2);U_();F_(2)
                        return
                    elif inter_cub[i][0]==3:
                        U();U();F(3);U_();F_(3);U_();F_(2);U();F(2)
                        return
                elif i==7:
                    if inter_cub[i][0] ==1:
                        d_U();U_();F_(1);U();F(1);U();F(2);U_();F_(2)
                        return
                    elif inter_cub[i][0]==3:
                        d_U();U();F(3);U_();F_(3);U_();F_(2);U();F(2)
                        return
                if inter_cub[i][0] ==1:
                    U_();F_(1);U();F(1);U();F(2);U_();F_(2)
                    return
                elif inter_cub[i][0]==3:
                    U();F(3);U_();F_(3);U_();F_(2);U();F(2)
                    return
            elif inter_cub[i][1]==3:
                if i==4:
                    if inter_cub[i][0]==2:
                        d_U();U_();F_(2);U();F(2);U();F(3);U_();F_(3)
                        return
                    elif inter_cub[i][0]==4:
                        d_U();U();F(4);U_();F_(4);U_();F_(3);U();F(3)
                        return
                elif i==5:
                    if inter_cub[i][0]==2:
                        U_();U_();F_(2);U();F(2);U();F(3);U_();F_(3)
                        return
                    elif inter_cub[i][0]==4:
                        U_();U();F(4);U_();F_(4);U_();F_(3);U();F(3)
                        return
                elif i==7:
                    if inter_cub[i][0]==2:
                        U();U_();F_(2);U();F(2);U();F(3);U_();F_(3)
                        return
                    elif inter_cub[i][0]==4:
                        U();U();F(4);U_();F_(4);U_();F_(3);U();F(3)
                        return
                if inter_cub[i][0]==2:
                    U_();F_(2);U();F(2);U();F(3);U_();F_(3)
                    return
                elif inter_cub[i][0]==4:
                    U();F(4);U_();F_(4);U_();F_(3);U();F(3)
                    return
            elif inter_cub[i][1]==4:
                if i==4:
                    if inter_cub[i][0]==3:
                        U();U_();F_(3);U();F(3);U();F(4);U_();F_(4)
                        return
                    elif inter_cub[i][0]==1:
                        U();U();F(1);U_();F_(1);U_();F_(4);U();F(4)
                        return
                elif i==5:
                    if inter_cub[i][0]==3:
                        d_U();U_();F_(3);U();F(3);U();F(4);U_();F_(4)
                        return
                    elif inter_cub[i][0]==1:
                        d_U();U();F(1);U_();F_(1);U_();F_(4);U();F(4)
                        return
                elif i==6:
                    if inter_cub[i][0]==3:
                        U_();U_();F_(3);U();F(3);U();F(4);U_();F_(4)
                        return
                    elif inter_cub[i][0]==1:
                        F(1);U_();F_(1);U_();F_(4);U();F(4)
                        return
                if inter_cub[i][0]==3:
                    U_();F_(3);U();F(3);U();F(4);U_();F_(4)
                    return
                elif inter_cub[i][0]==1:
                    U();F(1);U_();F_(1);U_();F_(4);U();F(4)
                    return
    print("falty")
    transform_id_in_pieces(id)
    colt_cub=deepcopy(colt)
    inter_cub=deepcopy(inter)
    inter_cub_copy=deepcopy(inter_cub)
    if inter_cub[8]!=[1,4]:
        if inter_cub[8]==[4,1]:
            F(1);U_();F_(1);U();F_(4);d_U();F(4);d_U();F_(4);U();F(4)
            return
        elif inter_cub[8][0]==1 and inter_cub[9][0]==1 and inter_cub[8][0]!=5 and inter_cub[9][0]!=5 :
            d_F(1);d_U();d_F(1);d_U();d_F(1);U()
            return 
        if 5 not in inter_cub[8]:
            F(1);U_();F_(1);U_();F_(4);U();F(4)
            return
    elif inter_cub[9]!=[1,2]:
        if inter_cub[9]==[2,1]:
            F(2);U_();F_(2);U();F_(1);d_U();F(1);d_U();F_(1);U();F(1)
            return 
        elif inter_cub[9][1]==2 and inter_cub[10][1]==2 and inter_cub[9][0]!=5 and inter_cub[10][0]!=5:
            d_F(1);d_U();d_F(1);d_U();d_F(1);U()
            return 
        if 5 not in inter_cub[9]:
            F(2);U_();F_(2);U_();F_(1);U();F(1)
            return 
    elif inter_cub[10]!=[3,2]:
        if inter_cub[10]==[2,3]:
            F(3);U_();F_(3);U();F_(2);d_U();F(2);d_U();F_(2);U();F(2)
            return 
        elif inter_cub[10][0]==3 and inter_cub[11][0]==3 and inter_cub[10][1]!=5 and inter_cub[11][0]==5:
            d_F(3);d_U();d_F(3);d_U();d_F(3);U()
            return
        if 5 not in inter_cub[10]:
            F(3);U_();F_(3);U_();F_(2);U();F(2)
            return
    elif inter_cub[11]!=[3,4]:
        if inter_cub[11]==[4,3]:
            F(4);U_();F_(4);U();F_(3);d_U();F(3);d_U();F_(3);U();F(3)
            return 
        elif inter_cub[11][1]==4 and inter_cub[8][1]==4 and inter_cub[11][0]!=5 and inter_cub[8][0]!=5:
            d_F(3);d_U();d_F(3);d_U();d_F(3);U()
            return
        if 5 not in inter_cub[11]:
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
         U();F(1);F(2);F_(3);F_(2);F_(1);F(2);F(3);F_(2) #algoexit

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
    if message_label:
        destroy()
    id=deepcopy(id_complet)
    for i in range(7):
        for j in range(11):
            if i!=3:
                if j!=3:
                    if j!=7:
                        if j!=11:
                            schimbare_culori3(i,j)

show_info = 0

def close_callback():
    pass
x=0
def info_window_copy(i):
    global x
    x=i
def buton_info_func():
    global buton_info
    global show_info
    show_info+=1
    if show_info%2:
        info_window=tk.Tk()
        info_window.title("Informații pentru a folosi programul")
        info_window_copy(info_window)
        buton_info.config(bg='#525266',foreground='white')
        m='Pentru a inchide această fereastră, reapasă pe ℹ️ \n\n                 1.Ține cubul cu fața albă spre tine, iar cu fața albastră in sus.                 \n 2. Completează fetele in ordinea: alb,albastru,rosu,verde,portocaliu. \n 3. Pentru fața galbenă (în sus): ține cubul cu partea albastră spre tine\n 4.Fiecare față se completează de la stânga spre dreapta, de sus în jos\n                 5.Alege culoarea apăsând click stânga pe pătrațica dorită pentru a derula prin acestea,                 \n iar click dreapta pentru a completa pătrațica cu culoarea feții curente \n6. Apasă butonul ➡️ pentru a trimite rezolvarea,\n pe 🔁 pentru a reseta fețele, iar pe 💯 pentru a face cubul complet\n7. Dupa ce ai trimis rezolvarea, poți modifica fețele apăsând pe ⬅️\n8. Pe tot parcursul rezolvării, ține fața cu centrul albastru spre tine,\niar fața cu centrul alb in jos\n\nMutări:\n\n*cele care nu au \' se mută în sensul acelor de ceasornic relativ feței respective,\n iar cele care au \' se mută în sensul invers acelor de ceasornic relativ feței respective*\n\n F : front , F\' : front prim \n  R : right , R\' : right prim \n  L : Left , L\' : Left prim \n  B : back , B\' : back prim \n  U : up , U\' : up prim\n\nDeschide 3D View (🧊) pentru a vizualiza comenzile'
        
        message_label2 = tk.Label(info_window,text='\n'+m+'\n', font=("Areal", 12))
        message_label2.pack()
    
        info_window.protocol("WM_DELETE_WINDOW", close_callback)
    else:
        info_window=x
        info_window.destroy()
        buton_info.config(bg='white',foreground='black')

for j in range(11):
    b=tk.Canvas(faces,width=35,height=35,borderwidth=0,relief="solid")
    b.grid(row=7,column=j)
    block[7][j]=b

def buton_retry_func():
    global buton_retry
    buton_retry.config(bg='#525266',foreground='white')
    global incepe_rezolvarea
    incepe_rezolvarea = False
    global r_buton
    
    block[7][j]=b
    r_buton=False

for i in range(9):
    b=tk.Canvas(faces,width=0,height=0,borderwidth=0,relief="solid")
    b.grid(row=i,column=12)

b_random=False
b_cnt=0
random_scramble=''
def buton_random_func():
    f10=open('textures by positions\colturi_inter_ids.txt','w')
    global file1
    if file1:
        file1.close()
    file1 = open("id_update.txt", "w")
    file1.close()
    file1 = open("id_update.txt", "a")
    global id, id_complet, b_random, random_scramble, b_cnt, incepe_rezolvarea, r_buton, solved
    incepe_rezolvarea=False
    solved=''
    r_buton=False
    b_random=True
    b_cnt+=1
    if b_cnt%2==0:
        destroy()
        random_scramble=''

    if message_label:
        destroy()
    id=deepcopy(id_complet)
    moves=random.randint(15,20)
    mutare_precedenta=random.randint(1,4)
    range_=4
    range_precedent=0
    while moves:
        mutare = random.randint(1, 15)
        
        if mutare != mutare_precedenta:
            mutare_precedenta = mutare
            range_precedent = range_
            moves -= 1
            if mutare <= 4:
                range_ = 0
                F(mutare)
            elif 5 <= mutare <= 8:
                indice = mutare - 4
                range_ = 1
                d_F(indice)
            elif 9 <= mutare <= 12:
                indice = mutare - 8
                range_ = 2
                F_(indice)
            elif 13<=mutare<=15:
                range_ = 3
                if mutare == 13:
                    U()
                elif mutare == 14:
                    d_U()
                elif mutare == 15:
                    U_()
    
    message(random_scramble)
    print(id)
    for i in range(7):
        for j in range(11):
            if i!=3:
                if j!=3:
                    if j!=7:
                        if j!=11:
                            schimbare_culori4(i,j)

def buton_3dview_func2():
    f5 = open("3d window closed.txt", "r")
    x=f5.read()
    if not x:
        if message_label:
            destroy()
        message('3D View already opened')
        return 
    if message_label=='3D View already opened':
        destroy()
    subprocess.Popen(['python', 'test.py'], shell=True)

f20=open("3d window closed.txt",'w')
f20.write('1')
f20.close()

def test():
    for i in range(200):
        buton_random_func()
        buton_send_func()
        
buton_send = tk.Button(faces, text="➡️",relief="solid",font="Areal",borderwidth=1,command=buton_send_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_send.grid(row=8,column=0, columnspan=5, sticky=tk.W+tk.E)

buton_complet = tk.Button(faces, text="💯",relief="solid",font="Areal",borderwidth=1,command=buton_complet_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_complet.grid(row=8,column=9, columnspan=1, sticky=tk.W+tk.E)

buton_reset = tk.Button(faces, text="🔁",relief="solid",font="Areal",borderwidth=1,command=buton_reset_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_reset.grid(row=8,column=10, columnspan=1, sticky=tk.W+tk.E)

buton_info = tk.Button(faces, text="ℹ️",relief="solid",font="Areal",borderwidth=1,command=buton_info_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_info.grid(row=8,column=8, columnspan=1, sticky=tk.W+tk.E)

buton_retry = tk.Button(faces, text="⬅️",relief="solid",font="Areal",borderwidth=1,command=buton_retry_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_retry.grid(row=8,column=5, columnspan=1, sticky=tk.W+tk.E)


buton_3dview = tk.Button(faces, text="🧊",relief="solid",font="Areal",borderwidth=1,command=buton_3dview_func2,activebackground='#423f3b',activeforeground='white',bg='white')
buton_3dview.grid(row=8,column=6, columnspan=1, sticky=tk.W+tk.E)

buton_random = tk.Button(faces, text="🎰",relief="solid",font="Areal",borderwidth=1,command=buton_random_func,activebackground='#423f3b',activeforeground='white',bg='white')
buton_random.grid(row=8,column=7, columnspan=1, sticky=tk.W+tk.E,)

#buton_random = tk.Button(faces, text="test",relief="solid",font="Areal",borderwidth=1,command=test,activebackground='#423f3b',activeforeground='white',bg='white')
#buton_random.grid(row=8,column=4, columnspan=1, sticky=tk.W+tk.E,)

faces.mainloop()
