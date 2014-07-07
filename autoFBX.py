import bpy
import os
from bpy.app.handlers import persistent

bl_info = {"name": "autoFBX", "category": "Import-Export"}

@persistent
def save_fbx(scene):
	#Edit filename to end in .fbx
	newpath = os.path.splitext(bpy.data.filepath)[0] + '.fbx'

	print('AutoFBX::Exporting to FBX in current directory...')
	bpy.ops.export_scene.fbx(check_existing=False, filepath=newpath, filter_glob="*.fbx", 
		version='BIN7400', use_selection=False, axis_forward='X', axis_up='Z')
	print('AutoFBX::Done!')

def register():
	bpy.app.handlers.save_post.append(save_fbx)
    
def unregister():
    print("AutoFBX Disabled")

