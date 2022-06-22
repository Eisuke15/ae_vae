import torch
from torchvision import transforms
import os


def device(device_num = 0):
    return torch.device(f"cuda:{device_num}" if torch.cuda.is_available() else "cpu")


def mkdir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def net_path(epoch, nz=20, vae=False, numbers=None):
    if numbers is None: # multiple class
        mkdir_if_not_exists('./trained_net/multi')
        return f"./trained_net/multi/{'v' if vae else ''}ae_z{nz:03d}_e{epoch+1:04d}.pth"
    else:  # single class
        dir_name = '-'.join(str(n) for n in sorted(numbers))
        mkdir_if_not_exists(f'./trained_net/single/{dir_name}')
        return f"./trained_net/single/{dir_name}/{'v' if vae else ''}ae_z{nz:03d}_e{epoch+1:04d}.pth"
