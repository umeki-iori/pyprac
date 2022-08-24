import os


# print(os.path.isabs(r'C:\Users\i-umeki\AppData\Roaming\Blender Foundation\Blender\3.2'))

# print(os.path.dirname(r'C:\Users\i-umeki\AppData\Roaming\Blender Foundation\Blender\3.2'))
# print(os.path.basename(r'C:\Users\i-umeki\AppData\Roaming\Blender Foundation\Blender\3.2'))
# print(os.path.split(r'C:\Users\i-umeki\AppData\Roaming\Blender Foundation\Blender\3.2'))


testpath = r'C:\Users\i-umeki\AppData\Roaming\Blender Foundation\Blender\3.2'

print(os.sep)
print(testpath.split(os.sep))