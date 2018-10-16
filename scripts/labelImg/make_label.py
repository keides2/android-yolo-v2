
backup_dir = './model'

def cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout, stderr = p.communicate()
    return stdout.rstrip()

dirs = cmd("ls "+"./image_data")
labels = dirs.splitlines()

if os.path.exists(backup_dir):
    cmd("rm  -rf "+backup_dir)

# make directories
os.makedirs(backup_dir)
labelsTxt_backup = open(backup_dir + '/labels.txt','w')
classNo=0
for label in labels:
    labelsTxt_backup.write(label.decode('utf-8')+"\n")
    classNo += 1

NUM_CLASSES = classNo
print("class number=" + str(NUM_CLASSES))
labelsTxt_backup.close()

# ラベルの確認
# !cat ./model/labels.txt