import os

def check_dataset():
    paths = [
        'data/images/train',
        'data/images/val',
        'data/labels/train',
        'data/labels/val'
    ]

    for p in paths:
        if os.path.exists(p):
            print(f'{p} -> OK')
        else:
            print(f'{p} -> MISSING')