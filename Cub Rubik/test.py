from ursina import *
app = Ursina(title='3D Rubik')
cube_pieces = []

LEFT = {Vec3(-1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
BOTTOM = {Vec3(x, -1, z) for x in range(-1, 2) for z in range(-1, 2)}
FACE = {Vec3(x, y, -1) for x in range(-1, 2) for y in range(-1, 2)}
BACK = {Vec3(x, y, 1) for x in range(-1, 2) for y in range(-1, 2)}
RIGHT = {Vec3(1, y, z) for y in range(-1, 2) for z in range(-1, 2)}
TOP = {Vec3(x, 1, z) for x in range(-1, 2) for z in range(-1, 2)}
SIDE_POSITIONS = LEFT | BOTTOM | FACE | BACK | RIGHT | TOP

cubes_side_positons = {'LEFT': LEFT, 'BOTTOM': BOTTOM, 'RIGHT': RIGHT, 'FACE': FACE, 'BACK': BACK, 'TOP': TOP}
rotation_axes = {'LEFT': 'x', 'RIGHT': 'x', 'TOP': 'y', 'BOTTOM': 'y', 'FACE': 'z', 'BACK': 'z'}

cube_pieces = [Entity(model='models/custom_cube', texture='textures/combined_image', position=pos) for pos in SIDE_POSITIONS]
centru = Entity(model='models/custom_cube', texture='textures/rubik_texture2', position=(0,0,0))

camera = EditorCamera()
camera.position = (0, 0, 0)
camera.rotation = (20, -45, 0)

def reaxed():
    global cube_pieces
    global centru
    for cube in cube_pieces:
        if cube.parent == centru:
            world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
            cube.parent = scene
            cube.position, cube.rotation = world_pos, world_rot
    centru.rotation=0

animation_time = 0.5
action_trigger = True

def toggle_animation_trigger():
    global action_trigger
    action_trigger = not action_trigger

def rotate_side(side_name,increment):
    global action_trigger
    global animation_time
    global centru
    global cube_pieces
    if not action_trigger:
        return 
    action_trigger = False
    cube_positions = cubes_side_positons[side_name]
    rotation_axis = rotation_axes[side_name]
    reaxed()
    for cube in cube_pieces:
        if cube.position in cube_positions:
            cube.parent = centru
            eval(f'centru.animate_rotation_{rotation_axis}({increment}, duration={animation_time})')
    invoke(toggle_animation_trigger,delay=animation_time+0.05)

culoare_butoane='#000000'

update_b = Button(scale=0.04,x=-0.85, y=.46, color=color.clear, text='', text_color=color.clear,tooltip=Tooltip('<scale:1><white>' + 'Update'),icon="textures by positions\\button textures\\refr2.png")
reset_b = Button(scale=0.04,x=-0.80, y=.46, color=color.clear, text='', text_color=color.hex(culoare_butoane),tooltip=Tooltip('<scale:1><white>' + 'Reset 3D cube'),icon="textures by positions\\button textures\\reset2.png")
camera_b = Button(scale=0.04,x=-0.75, y=.46, color=color.clear, text='', text_color=color.hex(culoare_butoane),tooltip=Tooltip('<scale:1><white>' + 'Reset view'),icon="textures by positions\\button textures\camera_reset.png")
next_b = Button(scale=0.058,x=0.055, y=-.46, color=color.clear, text='U', text_color=color.white,tooltip=Tooltip('<scale:1><white>' + 'Next'),icon="textures by positions\\button textures\\right.png")
prev_b = Button(scale=0.058,x=-0.055, y=-.46, color=color.clear, text='P', text_color=color.white,tooltip=Tooltip('<scale:1><white>' + 'Previous'),icon="textures by positions\\button textures\left.png")
play_b = Button(scale=0.04,x=0, y=-.46, color=color.clear, text='', text_color=color.white,tooltip=Tooltip('<scale:1><white>' + 'Play Animation'),icon="textures by positions\\button textures\play-buttton.png")

b = Button(scale=0.04,x=-0.85,y=-.46, color=color.gray, text='F', text_size=1, text_color=color.hex(culoare_butoane))
b2 = Button(scale=0.04,x=-0.80, y=-.46, color=color.gray, text='F\'', text_size=1, text_color=color.hex(culoare_butoane))
b3 = Button(scale=0.04,x=-0.75, y=-.46, color=color.gray, text='R', text_size=1, text_color=color.hex(culoare_butoane))
b4 = Button(scale=0.04,x=-0.70, y=-.46, color=color.gray, text='R\'', text_size=1, text_color=color.hex(culoare_butoane))
b5 = Button(scale=0.04,x=-0.65,y=-.46, color=color.gray, text='L', text_size=1, text_color=color.hex(culoare_butoane))
b6 = Button(scale=0.04,x=-0.60, y=-.46, color=color.gray, text='L\'', text_size=1, text_color=color.hex(culoare_butoane))
b7 = Button(scale=0.04,x=-0.55, y=-.46, color=color.gray, text='B', text_size=1, text_color=color.hex(culoare_butoane))
b8 = Button(scale=0.04,x=-0.50, y=-.46, color=color.gray, text='B\'', text_size=1, text_color=color.hex(culoare_butoane))
b9 = Button(scale=0.04,x=-0.45, y=-.46, color=color.gray, text='U', text_size=1, text_color=color.hex(culoare_butoane))
b10 = Button(scale=0.04,x=-0.40, y=-.46, color=color.gray, text='U\'', text_size=1,text_color=color.hex(culoare_butoane))
mutari_text = Text(x=-0.87, y=-.403,text='Mutări:',text_color=color.hex('#ccd0d0'))
start = False

f2 = open("3d window closed.txt", "w")
def quit_app():
    f2.write('1')
    quit()
def input(key):
    f2.write('1')
    if key == 'escape':
        quit()
contor_update=0

def refreshed_id():
    global mutare
    global mutare_r
    global solved
    global total
    global play_b_cnt

    play_b_cnt=-1
    mutare=-1
    mutare_r=mutare
    f1 = open("solved.txt", "r")
    solved=f1.read()
    solved=solved.split('\n')
    for i in range(len(solved)):
        solved[i]=[char for char in solved[i].split(' ') if char]
    total = []
    [total.append(solved[i][j]) for i in range(len(solved)) for j in range(len(solved[i]))]
    f1.close()

start_moves=False

def update_texture():
    global contor_update
    global start_moves
    global play_b_cnt
    play_b_cnt=-1
    start_moves=True
    refreshed_id()
    contor_update+=1
    f4=open('textures by positions\cntr.txt','w')
    f4.write(str(contor_update))
    f4.close()
    global cube_pieces
    f13 = open("textures by positions\colturi_inter_ids.txt", "r")
    s=f13.read()
    if not s:
        return
    subprocess.run(['python', 'textures by positions\id_to_texture.py'])
    cube_pieces[0].texture=f'textures by positions\combined_image.png'
    cube_pieces[1].texture=f'textures by positions\\all\\{contor_update}combined_image17.png'
    cube_pieces[2].texture=f'textures by positions\\all\\{contor_update}combined_image4.png'
    cube_pieces[3].texture=f'textures by positions\\all\\{contor_update}combined_image10.png'
    cube_pieces[4].texture=f'textures by positions\\all\\{contor_update}combined_image19.png'
    cube_pieces[5].texture=f'textures by positions\\all\\{contor_update}combined_image0.png'
    cube_pieces[6].texture=f'textures by positions\\all\\{contor_update}combined_image9.png'
    cube_pieces[7].texture=f'textures by positions\\all\\{contor_update}combined_image15.png' 
    cube_pieces[8].texture=f'textures by positions\\all\\{contor_update}combined_image2.png' 
    cube_pieces[9].texture=f'textures by positions\combined_image.png'
    cube_pieces[10].texture=f'textures by positions\combined_image.png'
    cube_pieces[11].texture=f'textures by positions\combined_image.png'
    cube_pieces[12].texture=f'textures by positions\\all\\{contor_update}combined_image8.png' 
    cube_pieces[13].texture=f'textures by positions\\all\\{contor_update}combined_image12.png' 
    cube_pieces[14].texture=f'textures by positions\\all\\{contor_update}combined_image6.png' 
    cube_pieces[15].texture=f'textures by positions\\all\\{contor_update}combined_image13.png' 
    cube_pieces[16].texture=f'textures by positions\\all\\{contor_update}combined_image14.png' 
    cube_pieces[17].texture=f'textures by positions\\all\\{contor_update}combined_image5.png' 
    cube_pieces[18].texture=f'textures by positions\\all\\{contor_update}combined_image16.png' 
    cube_pieces[19].texture=f'textures by positions\combined_image.png'
    cube_pieces[20].texture=f'textures by positions\\all\\{contor_update}combined_image1.png'
    cube_pieces[21].texture=f'textures by positions\\all\\{contor_update}combined_image18.png'
    cube_pieces[22].texture=f'textures by positions\combined_image.png'
    cube_pieces[23].texture=f'textures by positions\\all\\{contor_update}combined_image3.png'
    cube_pieces[24].texture=f'textures by positions\\all\\{contor_update}combined_image11.png'
    cube_pieces[25].texture=f'textures by positions\\all\\{contor_update}combined_image7.png'
    arata_mutari()

def reset_colors():
    global cube_pieces
    global start_moves
    global mutari_disponibile
    global pasi_text_box
    global play_b
    play_b.icon="textures by positions\\button textures\play-buttton.png"
    if mutari_disponibile:
        [destroy(mutari_disponibile[i]) for i in range(len(mutari_disponibile))]
        mutari_disponibile.clear()
    if pasi_text_box:
        destroy(pasi_text_box)
    start_moves=False
    i=-1
    for cube in cube_pieces:
        destroy(cube)
    cube_pieces.clear()
    cube_pieces = [Entity(model='models/custom_cube', texture='textures/combined_image', position=pos) for pos in SIDE_POSITIONS]
    refreshed_id()

def reset_camera_view():
    global camera
    camera.position = (0, 0, 0)
    camera.rotation = (20, -45, 0)

b.on_click = Func(rotate_side,'FACE',90)
b2.on_click = Func(rotate_side,'FACE',-90)
b3.on_click = Func(rotate_side,'RIGHT',90)
b4.on_click = Func(rotate_side,'RIGHT',-90)
b5.on_click = Func(rotate_side,'LEFT',-90)
b6.on_click = Func(rotate_side,'LEFT',90)
b7.on_click = Func(rotate_side,'BACK',-90)
b8.on_click = Func(rotate_side,'BACK',90)
b9.on_click = Func(rotate_side,'TOP',90)
b10.on_click = Func(rotate_side,'TOP',-90)
camera_b.on_click = Func(reset_camera_view)
update_b.on_click = Func(update_texture)
reset_b.on_click = Func(reset_colors)

def on_destroy():
    f2.write('1')
    Func(quit,'escape')
app.on_destroy = on_destroy

pasi=['Pasul 1: ','Pasul 2: ','Pasul 3: ','Pasul 4: ','Pasul 5: ','Pasul 6: ','Pasul 7: ']
pasi_text_box = Text(x=0.2, y=-.45,text='',text_color=color.hex('#ccd0d0'))
refreshed_id()

mutari_disponibile=[]
mutare_disponibila_1 =Text(x=0.31, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_1)
mutare_disponibila_2 =Text(x=0.35, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_2)
mutare_disponibila_3 =Text(x=0.39, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_3)
mutare_disponibila_4 =Text(x=0.43, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_4)
mutare_disponibila_5 =Text(x=0.47, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_5)
mutare_disponibila_6 =Text(x=0.51, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_6)
mutare_disponibila_7 =Text(x=0.55, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_7)
mutare_disponibila_8 =Text(x=0.59, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_8)
mutare_disponibila_9 =Text(x=0.63, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_9)
mutare_disponibila_10 =Text(x=0.67, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_10)
mutare_disponibila_11 =Text(x=0.71, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_11)
mutare_disponibila_12 =Text(x=0.75, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_12)
mutare_disponibila_13 =Text(x=0.79, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_13)

def arata_mutari():
    global solved
    global pasi_text_box 
    mutare_locala=mutare
    global mutari_disponibile
    if mutare==len(total)-1:
        if pasi_text_box:
            [destroy(mutari_disponibile[i]) for i in range(len(mutari_disponibile))]
            destroy(pasi_text_box)
            pasi_text_box = Text(x=0.2, y=-.45,text='Rezolvare completă!',text_color=color.hex('#ccd0d0'))
        return 
    j=0
    while j<6 and mutare_locala>=len(solved[j]):
        mutare_locala-=len(solved[j])
        j+=1
    if pasi_text_box:
        destroy(pasi_text_box)
    pasi_text_box = Text(x=0.2, y=-.45,text=pasi[j],text_color=color.hex('#ccd0d0'))
    
    if mutari_disponibile:
        [destroy(mutari_disponibile[i]) for i in range(len(mutari_disponibile))]
        mutari_disponibile.clear()
    mutari_disponibile=[]
    mutare_disponibila_1 =Text(x=0.31, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_1)
    mutare_disponibila_2 =Text(x=0.35, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_2)
    mutare_disponibila_3 =Text(x=0.39, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_3)
    mutare_disponibila_4 =Text(x=0.43, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_4)
    mutare_disponibila_5 =Text(x=0.47, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_5)
    mutare_disponibila_6 =Text(x=0.51, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_6)
    mutare_disponibila_7 =Text(x=0.55, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_7)
    mutare_disponibila_8 =Text(x=0.59, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_8)
    mutare_disponibila_9 =Text(x=0.63, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_9)
    mutare_disponibila_10 =Text(x=0.67, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_10)
    mutare_disponibila_11 =Text(x=0.71, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_11)
    mutare_disponibila_12 =Text(x=0.75, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_12)
    mutare_disponibila_13 =Text(x=0.79, y=-.45,text='',text_color=color.hex('#ccd0d0'));mutari_disponibile.append(mutare_disponibila_13)
    
    zona=mutare_locala//12
    if zona==-1:
        zona=0
    if zona ==0:
        k=12*zona-1
    else :
        k=12*zona
    for i in range(len((mutari_disponibile))):
        if not solved[j]:
            return
        k+=1
        if k<=len(solved[j])-1:
            mutari_disponibile[i].text=solved[j][k]
            if k == mutare_locala:
                mutari_disponibile[i].color=color.gold

def next_b_function():
    global mutare
    global mutare_r
    global total
    if not start_moves:
        return
    if not action_trigger:
        return 
    mutare+=1
    if mutare>len(total)-1:
        return
    mutare_r=mutare
    if total[mutare]=='F':
        rotate_side('FACE',90)
    elif total[mutare]=="F\'":
        rotate_side('FACE',-90)
    elif total[mutare]=='R':
        rotate_side('RIGHT',90)
    elif total[mutare]=="R\'":
        rotate_side('RIGHT',-90)
    elif total[mutare]=='L':
        rotate_side('LEFT',-90)
    elif total[mutare]=="L\'":
        rotate_side('LEFT',90)
    elif total[mutare]=='B':
        rotate_side('BACK',-90)
    elif total[mutare]=="B\'":
        rotate_side('BACK',90)
    elif total[mutare]=='U':
        rotate_side('TOP',90)
    elif total[mutare]=="U\'":
        rotate_side('TOP',-90)
    arata_mutari()

def prev_b_function():
    global mutare_r
    global mutare
    global total
    if not start_moves:
        return
    if not action_trigger:
        return 
    if mutare_r<0:
        return
    if total[mutare_r]=='F':
        rotate_side('FACE',-90)
    elif total[mutare_r]=="F\'":
        rotate_side('FACE',90)
    elif total[mutare_r]=='R':
        rotate_side('RIGHT',-90)
    elif total[mutare_r]=="R\'":
        rotate_side('RIGHT',90)
    elif total[mutare_r]=='L':
        rotate_side('LEFT',90)
    elif total[mutare_r]=="L\'":
        rotate_side('LEFT',-90)
    elif total[mutare_r]=='B':
        rotate_side('BACK',90)
    elif total[mutare_r]=="B\'":
        rotate_side('BACK',-90)
    elif total[mutare_r]=='U':
        rotate_side('TOP',-90)
    elif total[mutare_r]=="U\'":
        rotate_side('TOP',90)
    mutare_r-=1
    mutare-=1
    arata_mutari()

def play_b_function():
    global play_b
    global play_b_cnt
    play_b_cnt+=1
    #play_b_start = Button(scale=0.04,x=0, y=-.46, color=color.clear)
    #play_b_stop = Button(scale=0.04,x=0, y=-.46, color=color.clear)
    if not start_moves:
        return
    if play_b_cnt%2:
        play_b.icon="textures by positions\\button textures\play-buttton.png"
    else:
        k=-1
        for i in range(mutare,len(total)):
            k+=1
            invoke(next_b_function,delay=3/2*k*(animation_time+0.09))

        play_b.icon="textures by positions\\button textures\pause.png"

next_b.on_click = Func(next_b_function)
prev_b.on_click = Func(prev_b_function)
play_b.on_click = Func(play_b_function)

app.run()
