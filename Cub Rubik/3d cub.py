

'''import bpy
import math
pi = math.pi
start_frame = 0
end_frame = 0
ind = 2

def U():
    global end_frame
    collection_name = 'fata galbena'
    end_frame += 50
    
    collection = bpy.data.collections.get(collection_name)

    for obj in collection.objects:   
        
        initial_z_rotation = obj.rotation_euler.z
        final_z_rotation = initial_z_rotation - pi/2 

        obj.rotation_euler.z = initial_z_rotation
        obj.keyframe_insert(data_path="rotation_euler", index=ind, frame=start_frame)
        obj.rotation_euler.z = final_z_rotation
        obj.keyframe_insert(data_path="rotation_euler", index=ind, frame=end_frame)

def F():
    global end_frame
    global start_frame
    collection_name = 'mijloc'
    end_frame += 50
    start_frame+=50
    collection = bpy.data.collections.get(collection_name)

    for obj in collection.objects:   
        
        initial_x_rotation = obj.rotation_euler.x
        final_x_rotation = initial_x_rotation + pi/2

        obj.rotation_euler.x = initial_x_rotation
        obj.keyframe_insert(data_path="rotation_euler", index=ind, frame=start_frame)
        obj.rotation_euler.x = final_x_rotation
        obj.keyframe_insert(data_path="rotation_euler", index=ind, frame=end_frame)
U()

F()
'''

f = open("id.txt", "r")
id_culori=[char for char in f.read()]
i=0
while(len(id_culori)>54):
    if id_culori[i] in ['0','1','2','3','4','5']:
        print()
    else:
        id_culori.pop(i)
        i-=1
    i+=1
    if i==len(id_culori):
        i=0

print(id_culori)
