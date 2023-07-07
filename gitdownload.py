import os
import git
import shutil
import tempfile

if os.path.exists('main.py'):
    os.remove("main.py")
# Create temporary dir
t = tempfile.mkdtemp()
# Clone into temporary dir
git.Repo.clone_from('https://github.com/sajjin/Reward_points.git', t, branch='master', depth=1)
# Copy desired file from temporary dir
shutil.move( f"{t}/main.py", '/home/rewards/Documents/Reward_points-master/main.py')
shutil.move( f"{t}/requirements.txt", '/home/rewards/Documents/Reward_points-master/requirements.txt')
# Remove temporary dir
os.system("pip3 install -r requirements.txt")
os.system("python3 main.py")
os.system('rmdir /S /Q "{}"'.format(t))
os.remove("main.py")