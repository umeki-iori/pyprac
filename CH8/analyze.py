import os

target_path = r'C:\Windows\System32'



total_size = 0
for filename in os.listdir(target_path):
    total_size += os.path.getsize(os.path.join(target_path))

print(total_size)