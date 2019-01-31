import os
import time
import subprocess

# Get default editor
EDITOR = os.getenv('EDITOR', None)
if EDITOR is None:
    EDITOR = subprocess.check_output(['which', 'editor']).decode().split()[0]
# Here the notes will be stored
NOTES_PATH = os.path.join(os.path.expanduser('~'), '.notas')
# Create path if not exists
if not os.path.exists(NOTES_PATH):
    os.makedirs(NOTES_PATH)


def new(args):
    """Open default editor or custom editor with name"""
    editor = EDITOR
    if args.editor:
        editor = args.editor
    cmd = [editor, os.path.join(NOTES_PATH, args.name)]
    subprocess.call(cmd)


def _ls(path):
    """Returns a list with files in path order by getmtime"""
    files = sorted([os.path.join(path, f) for f in os.listdir(path)],
                   key=os.path.getmtime, reverse=True)
    return files


def cat():
    pass


def rm(args):
    to_remove = os.path.join(NOTES_PATH, args.name)
    if os.path.exists(to_remove):
        ret = input("Remove '{}'? [y/N]: ".format(to_remove))
        if ret in 'yY':
            os.remove(to_remove)
    else:
        print("Note '{}' doesn't exists :/".format(to_remove))


def get_basename(filename):
    """Returns the basename of filename"""
    return os.path.basename(filename)


def ls(args):
    """Prints all notes"""
    headers = '{:<5} {:<40} {:<40}'.format('#', 'NAME', 'UPDATED')
    print(headers, end='\n\n')
    for count, filename in enumerate(_ls(NOTES_PATH)):
        name = get_basename(filename)
        if len(name) > 35:
            name = '...' + name[-35:]
        updated = time.ctime(os.path.getmtime(filename))
        print('{:<5} {:<40} {:<40}'.format(count, name, updated))
    print()
