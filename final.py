# -*- coding: utf-8 -*
__author__ = 'wsf'
import os
import re
import random
#import Image
def automaticExtract(dirname,result,mapingfile):
    '''
    本函数假定数据集内的每个子文件夹代表一类，然后根据这个假定生成用于caffe训练的文本文件
    :param dirname: 数据集地址
    :param result: 结果存放地址,只存放相对路径，便于后续修改
    :param mapingfile: 给每类的label mapping结果
    :return:无
    '''
    f_result=open(result,'wb')
    f_mapingfile=open(mapingfile,'wb')
    temp=re.sub(dirname.split(os.sep)[-1],'',dirname)
    i=0
    for root,dirs,files in os.walk(dirname):
        if len(files) !=0:
          f_mapingfile.write(root.split(os.sep)[-1]+" %d"%i+' '+str(len(files))+'\n')

          for _file in files:
              f_result.write(root.replace(temp,'')+os.sep+_file+' '+str(i)+'\n')
             # print root
             # print re.sub(ospath,"",root)
          i=i+1
    f_result.close()
    f_mapingfile.close()


def splitAndSample(infile,trainoutfile,testout,pro):
    '''

    :param infile: 输入的文件地址
    :param outfile: 结果保存的地址
    :param pro: 训练数据占总数据的比例,必须在0-1之间
    :return:
    '''
    f_in=open(infile,'r')
    f_train_out=open(trainoutfile,'wb')
    f_test_out=open(testout,'wb')
    lines=f_in.readlines()
    trainlines=random.sample(lines,int(pro*len(lines)))
    testlines=list(set(lines)-set(trainlines))
    f_train_out.writelines(trainlines)
    f_test_out.writelines(testlines)
    f_in.close()

    f_train_out.close()
    f_test_out.close()



#dirname='E:\Data\Scene\SUN397'
#result='E:\se_train.txt'
#mapingfile='E:\se_mapping.txt'
#automaticExtract(dirname,result,mapingfile)
#splitAndSample('E:\selected.txt','E:\se_train_sample.txt','E:\se_test.txt',0.7)
#automaticExtract('E:\Data\CUB_200_2011\images','E:\\bird.txt','E:\\birdmap.txt')
splitAndSample('E:\\bird.txt','E:\\bird_train.txt','E:\\bird_test.txt',0.7)