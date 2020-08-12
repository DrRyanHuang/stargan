'''
@Author: RyanHuang
@Github: DrRyanHuang
@Brife : 
    下载给定的数据集 `zip` 文件
    若预下载过, 请注释 `wget.download(url, zip_file_str)` 
@Notice:
    原程序是个 `shell` 脚本, 不能直接在 `windows` 运行, 笔者改为了 `Py` 文件
    以下为原 `shell` 脚本
'''

'''
FILE=$1

if [ $FILE == "celeba" ]; then

    # CelebA images and attribute labels
    URL=https://www.dropbox.com/s/d1kjpkqklf0uw77/celeba.zip?dl=0
    ZIP_FILE=./data/celeba.zip
    mkdir -p ./data/
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./data/
    rm $ZIP_FILE


elif [ $FILE == 'pretrained-celeba-128x128' ]; then

    # StarGAN trained on CelebA (Black_Hair, Blond_Hair, Brown_Hair, Male, Young), 128x128 resolution
    URL=https://www.dropbox.com/s/7e966qq0nlxwte4/celeba-128x128-5attrs.zip?dl=0
    ZIP_FILE=./stargan_celeba_128/models/celeba-128x128-5attrs.zip
    mkdir -p ./stargan_celeba_128/models/
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./stargan_celeba_128/models/
    rm $ZIP_FILE

elif [ $FILE == 'pretrained-celeba-256x256' ]; then

    # StarGAN trained on CelebA (Black_Hair, Blond_Hair, Brown_Hair, Male, Young), 256x256 resolution
    URL=https://www.dropbox.com/s/zdq6roqf63m0v5f/celeba-256x256-5attrs.zip?dl=0
    ZIP_FILE=./stargan_celeba_256/models/celeba-256x256-5attrs.zip
    mkdir -p ./stargan_celeba_256/models/
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./stargan_celeba_256/models/
    rm $ZIP_FILE

else
    echo "Available arguments are celeba, pretrained-celeba-128x128, pretrained-celeba-256x256."
    exit 1
fi
'''
import os
import wget
import argparse

# 用于解析命令行传回来的参数
def param_parse():

    # 创建一个参数解析对象
    parser = argparse.ArgumentParser()
    # 添加需要解析的参数
    parser.add_argument("-ds", 
                        "--dataset", 
                        help="请选择 `dataset` ",
                        type=str)
    
    # 参数解析
    args = parser.parse_args()    
    return vars(args)


def download_data(url):
    
    wget.download

if __name__ == '__main__':

    x = param_parse()
    print(x)

    dataset_list = ["celeba", 'pretrained-celeba-128x128', 'pretrained-celeba-256x256']
    
    data_url = 'https://www.dropbox.com/s/d1kjpkqklf0uw77/celeba.zip?dl=0'
    pretrain_128x128 = 'https://www.dropbox.com/s/7e966qq0nlxwte4/celeba-128x128-5attrs.zip?dl=0'
    pretrain_256x256 = 'https://www.dropbox.com/s/zdq6roqf63m0v5f/celeba-256x256-5attrs.zip?dl=0'
    url_list = [data_url, pretrain_128x128, pretrain_256x256]
    
    data_url_dict = {k:v for k, v in zip(dataset_list, url_list)}

    zip_file = './data/celeba.zip'
    
    os.makedirs('./data/')
    
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./data/
    rm $ZIP_FILE
    
    









