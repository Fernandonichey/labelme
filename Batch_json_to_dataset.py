import os

def batch_json_to_dataset(path,  Envs = 'Labelme'):
    json_file = os.listdir(path)
    os.system("conda activate Labelme")
    for file in json_file:
        os.system("labelme_json_to_dataset.exe %s"%(path + '/' + file))

if __name__ =='__main__':
    path = R'C:\Users\ren5szh\Desktop\AI\LabelMe\json'
    batch_json_to_dataset(path)