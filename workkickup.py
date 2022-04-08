"""Junção"""

import os
import shutil
import numpy as np
import argparse
import cv2
import glob
import re
import sys
import torch
from torch._C import NoneType
import time
import wget
import pickle



url = sys.argv[1]

if(os.path.exists('myyolov3/embaixadinha2.mp4')):
      os.remove('myyolov3/embaixadinha2.mp4')
      print('embaixadinha.mp4 removido')

#url = 'https://video.ftjl2-1.fna.fbcdn.net/v/t39.25447-2/277761056_651071029315651_4578569319050896963_n.mp4?_nc_cat=106&vs=e4248c5c26c7c1ca&_nc_vs=HBksFQAYJEdDQk1qaEJEQ0cxSkpWQUNBRVBtaDVHSldJby1ibWRqQUFBRhUAAsgBABUAGCRHQm40anhBbEVXc0JjSWNDQUt0WmU2Z2tucnNhYnJGcUFBQUYVAgLIAQBLBogScHJvZ3Jlc3NpdmVfcmVjaXBlATENc3Vic2FtcGxlX2ZwcwAQdm1hZl9lbmFibGVfbnN1YgAgbWVhc3VyZV9vcmlnaW5hbF9yZXNvbHV0aW9uX3NzaW0AKGNvbXB1dGVfc3NpbV9vbmx5X2F0X29yaWdpbmFsX3Jlc29sdXRpb24AEWRpc2FibGVfcG9zdF9wdnFzABUAJQAcAAAmqOCAjLnApgsVAigCQzMYC3Z0c19wcmV2aWV3HBdAPXaHKwIMShgZZGFzaF9vZXBfaHEyX2ZyYWdfMl92aWRlbxIAGBh2aWRlb3MudnRzLmNhbGxiYWNrLnByb2Q4ElZJREVPX1ZJRVdfUkVRVUVTVBsJiBVvZW1fdGFyZ2V0X2VuY29kZV90YWcGb2VwX2hkE29lbV9yZXF1ZXN0X3RpbWVfbXMBMAxvZW1fY2ZnX3J1bGUHdW5tdXRlZBNvZW1fcm9pX3JlYWNoX2NvdW50BDM4MzERb2VtX2lzX2V4cGVyaW1lbnQADG9lbV92aWRlb19pZA8zNzEyNjg2NjgyNjI5NzESb2VtX3ZpZGVvX2Fzc2V0X2lkEDEzNTg3MTUzMTQ1OTQzNTQVb2VtX3ZpZGVvX3Jlc291cmNlX2lkEDMxODA4OTQ4MDIxNTU1NDAcb2VtX3NvdXJjZV92aWRlb19lbmNvZGluZ19pZA81MjgwMTMzMTUzNDk1ODclAhwAJcQBGweIAXMENTUyNgJjZAoyMDIyLTA0LTAyA3JjYgQzODAwA2FwcBRGYWNlYm9vayBmb3IgQW5kcm9pZAJjdBlDT05UQUlORURfUE9TVF9BVFRBQ0hNRU5UE29yaWdpbmFsX2R1cmF0aW9uX3MGMjkuNTg2AnRzFXByb2dyZXNzaXZlX2VuY29kaW5ncwA%3D&ccb=1-5&_nc_sid=5e2f14&efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ohc=d5FMM759QfkAX8FG16P&tn=SIjHU8LBZWe664y-&_nc_ht=video.ftjl2-1.fna&oh=00_AT9wiW7HE7IoeBS69LYtuVgEr0b1OVX-bCpthTKdK-ctEA&oe=62534835&_nc_rid=192074815240389'
width =''
height = ''

wget.download(url,'embaixadinha2.mp4')
print('time before start')
time.sleep(10.0)

width =''
height = ''
def frameNumber(title):
  
  sizeTitle = len(title)
  titleCut = title[sizeTitle-7:sizeTitle-4]
  finalCut = ''
  #print(title[sizeTitle-7:sizeTitle-4])
  number = 0
  if(titleCut.find('-')!=-1):
    #print(titleCut)
    #print('tem o -')
    if(titleCut[0].find('-')!=-1):
      #print("primeira posição")
      finalCut = titleCut[1:3]
    if(titleCut[1].find('-')!=-1):
      #print("segunda posição")
      finalCut = titleCut[2]
  else:
    finalCut = titleCut
    

  #print("finalCut: "+finalCut)
  return finalCut

def numericalSort(value):
      parts = numbers.split(value)
      parts[1::2] = map(int, parts[1::2])
      return parts

def text_update(frame_):
  
  global qtd
  embaixada = qtd
  getFrame = str(frame_)
  if(listFrames != ''):
        for fr in listFrames:
          #print(str(frame_)+ " " + fr)
          if(int(getFrame) == int(fr)):
            qtd+=1
            embaixada = qtd

  print("qtd: " + str(qtd))    
  return str(embaixada)


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def main():

    # parse all args
    #parser = argparse.ArgumentParser()
    #parser.add_argument('source', type=str, help='Path to source video')
    #parser.add_argument('dest_folder', type=str, help='Path to destination folder')
    #args = parser.parse_args()

    # get file path for desired video and where to save frames locally
    # trocar o nome do video
    pathIn = 'data/images'

    if(os.path.exists('data/images/bus.jpg')):
      os.remove('data/images/bus.jpg')
      
    if(os.path.exists('data/images/zidane.jpg')):
      os.remove('data/images/zidane.jpg')

    if(os.path.exists('runs/detect')):
      shutil.rmtree('runs/detect')

    isExist = os.path.exists(pathIn)

    print("exists? "+ str(isExist))
    
    if not os.path.exists('imgSave'):
      os.makedirs('imgSave')
      print('imgSaveCreated')

  
    if not isExist:
      os.makedirs(pathIn)
      print('directory created')

    cap = cv2.VideoCapture("embaixadinha2.mp4") 
    path_to_save = os.path.abspath(pathIn)
    
    current_frame = 1

    if (cap.isOpened() == False):
        print('Cap is not open')

    
    width = cap. get(cv2. CAP_PROP_FRAME_WIDTH )
    height = cap. get(cv2. CAP_PROP_FRAME_HEIGHT )
    print("width " + str(width))
    print("height " + str(height))

    with open('sizes.txt', 'w') as f:
      f.write(str(width)+ " "+str(height))

    # cap opened successfully
    while(cap.isOpened()):

        # capture each frame
        ret, frame = cap.read()
        if(ret == True):

            # Save frame as a jpg file
            #trocar o prefixo do nome do frame
            name = 'emb3-' + str(current_frame) + '.jpg' 
            print(f'Creating: {name}')
            cv2.imwrite(os.path.join(path_to_save, name), frame)

            # keep track of how many images you end up with
            current_frame += 1
        
        else:
            break

    # release capture 
    cap.release()
    
    cv2.destroyAllWindows()
    print('done')

    ### Como rodar incode

if __name__ == '__main__':
  main()

print("pausa1")
#time.sleep(10.0)

#sys.argv= ['main', '--weights yolov3.pt', '--img 640', '--conf 0.25', '--yolov3\data\images\\', '--save-txt', '--classes 0 32']


#!python detect.py --weights yolov3.pt --img 640 --conf 0.25 --source data/images --save-txt --save-conf --classes 0 32

os.system('python detect.py --weights yolov3.pt --img 640 --conf 0.25 --source data/images --save-conf    --save-txt --classes 0 32')




'''
      leitura dimensões do video
    '''

sizes = ''
with open('sizes.txt', 'r') as f:
  sizes = f.readline()
listSizes = sizes.split(' ')
    
alist = []
folder_path = 'runs/detect/exp/labels/'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
      with open(filename, 'r') as f:
        text = f.read()
        alist.append(filename)
        #print (filename)
        #print (len(text))
        #print(text)



alist.sort(key=natural_keys)
#print(alist)
maiorValor = 0.0;
controleSubida = 0.0;
embaixada = 0
erros = 0
descida = True
naoTemBola = True
unicaPessoa = True
continuarContando = True
bolasDuplicadas = 0
pessoasDuplicadas = 0
centroPessoa = 1.0
larguraPessoa = 1.0
alturaPessoa = 1.0
alturaAtualPessoa = 1.0

textoEmbaixadas = ''
gapFrame = 0.1

for title in alist:
      f = open(title, "r")

      naoTemBola = True
      frameN = frameNumber(title)
      print("frameN: "+frameN)
      for line in f:
        line = line.strip()
        words = line.split(' ')
        #print("linha: ")
        #print(words)

        #print(words[2])
        #print("maior valor: "+str(maiorValor))
        ##print("embaixada" + str(embaixada))

        #print(words[0])
        tipo = int(words[0])
        altura = float(words[2])

        #sizeTitle = len(title)
        #print(title[sizeTitle-7:sizeTitle-4])
        
        #print("titulo: "+title)
        #print(len(title))

        if(continuarContando):
          print("continuar True")

          if(tipo == 0):
            if(float(words[5]) < 0.80):
              print("pessoa com ident baixa")
              break
            if(unicaPessoa == False):
              pessoasDuplicadas +=1
            alturaPessoa = float(listSizes[1]) * float(words[4])
            #print("altura Pessoa: "+ str(alturaPessoa))
            #print("altura atual Pessoa: " + str(alturaAtualPessoa))
            if(alturaPessoa < alturaAtualPessoa * 0.7):
              print("pessoa com tamnho muito abaixo da media")
              break
            else:
              alturaAtualPessoa = ((alturaAtualPessoa + alturaPessoa)/2)
              print("nova altura PEssoa: "+ str(alturaAtualPessoa))  
            unicaPessoa = False
            centroPessoa = float(words[1])
            larguraPessoa = float(words[3])
            
            #print("larguraPessoa: " + str(larguraPessoa))
            #print("centroPessoa: " + str(centroPessoa))


          if(tipo == 32):

            if(naoTemBola == False):
              bolasDuplicadas+=1
            naoTemBola = False

            larguraRealPessoa = larguraPessoa * float(listSizes[0])
            cantosLarguraPessoa = (larguraRealPessoa/2)/float(listSizes[0])
            larguraRealBola = float(words[3]) * float(listSizes[0])
            print("largura bola: " + str(larguraRealBola))
            cantosLarguraBola = ((larguraRealBola/2) / float(listSizes[0]))
            print("canto: " + str(cantosLarguraBola))
            print("centro Bola: "+ words[1])
            print("centro pessoa "+ str(centroPessoa))
            print("canto Pessoa: "+ str(cantosLarguraPessoa))

            if(embaixada == 1):
              gapFrame = 0.01
              

            if(abs(maiorValor - altura) < gapFrame):
              print("abs")
              break
            
            
            if(descida):
              if(altura > maiorValor):
                maiorValor = altura
                print("entrou if")
              else:
                
                print("entrou else")
                #if(float(words[1]) - cantosLarguraBola > (centroPessoa +cantosLarguraPessoa+0.0276041)):
                if(float(words[1]) - cantosLarguraBola > (centroPessoa + cantosLarguraPessoa + 0.2)):
                  print("maior que canto direito")
                  
                  print("pingou fora direito")
                  print("centro Bola: "+ words[1])
                  print("canto pessoa  "+str(centroPessoa +cantosLarguraPessoa))
                  continuarContando = False
                  break
                #if(float(words[1]) + cantosLarguraBola < (centroPessoa - cantosLarguraPessoa - 0.0276041)):
                if(float(words[1]) + cantosLarguraBola < (centroPessoa - cantosLarguraPessoa - 0.2)):
                  print("menor que canto esquerdo")
                  continuarContando = False
                  print("pingou fora esquerdo")
                  break
                if(float(words[5]) < 0.75):
                  print("(float(words[5]) < 0.75)")
                  break
                descida = False
                controleSubida = altura
                textoEmbaixadas = textoEmbaixadas + frameN + " "
                embaixada +=1
                
            else:
              if(controleSubida > altura):
                controleSubida = altura
              else:
                controleSubida = 0.0
                maiorValor = 0.0
                descida = True
          
        


        #cv2.putText(frame, on_video_text, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        unicaPessoa = True  
        #print("Não tem bola: "+ str(naoTemBola))
        if(naoTemBola):
          erros +=1


        
      f.close()
printed = "Embaixadas: " + str(embaixada)
print("Erros: " + str(erros))
print("Bolas duplicadas: " + str(bolasDuplicadas))
print("Pessoas duplicadas: " + str(pessoasDuplicadas))
print(printed)
print("texto embaixadas"+ textoEmbaixadas)

with open('outputEmbaixadas.txt', 'w') as f:
        f.write("Erros "+ str(erros))
        f.write("\nBolas duplicadas " + str(bolasDuplicadas))
        f.write("\nPessoas duplicadas " + str(pessoasDuplicadas))
        f.write("\nEmbaixadas "+ str(embaixada))
if(embaixada == 0):
  textoEmbaixadas = '0'
with open('outputFrames.txt', 'w') as f:
        f.write(textoEmbaixadas)

arquivo = open("finalcount.bin", "wb")
lista = [str(embaixada)]
pickle.dump(lista, arquivo)
arquivo.close()



print("pausa2")
#time.sleep(10.0)

'''primeiro video
'''
img_array = []
numbers = re.compile(r'(\d+)')


for filename in sorted(glob.glob('runs/detect/exp/*.jpg') , key=numericalSort):
      img = cv2.imread(filename)
      height, width, layers = img.shape
      size = (width,height)
      img_array.append(img)

out = cv2.VideoWriter('vboundBox3.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 15, size)

for i in range(len(img_array)):
      out.write(img_array[i])
      
out.release()


print("pausa3")
#time.sleep(10.0)

'''

    escrever textos
'''

tree_video = cv2.VideoCapture('vboundBox3.mp4')
path_to_save = os.path.abspath("imgSave/")


frame_width  = tree_video.get(cv2.CAP_PROP_FRAME_WIDTH )
frame_height = tree_video.get(cv2.CAP_PROP_FRAME_HEIGHT )

img = cv2.imread('logo_vertical2.png')
if(frame_height == 720.0):
  img = cv2.imread('logo_vertical720.png')

# Get Image dimensions
img_height, img_width, _ = img.shape
print(str(img_height) +" "+str(img_width))

fps = tree_video.get(cv2.CAP_PROP_FPS)
print(fps)
lines = ''

frame_ = 0
qtd = 0
with open('outputFrames.txt', 'r') as f:
  lines = f.readline()

lenLines = len(lines)
lines = lines[0: lenLines-1]
listFrames = lines.split(' ')

length = int(tree_video.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )





print(str(frame_height) +" "+str(frame_width))
while(True):
  
  ret, frame = tree_video.read()
  font = cv2.FONT_HERSHEY_SIMPLEX


  on_video_text = text_update(frame_)
  
  alpha = 0.2
  beta = (1.0)
  if(frame_ < length):
    dst = cv2.addWeighted(img, alpha, frame, beta, 0.0)
    #overlay_image_alpha(frame, img, 150, 350, alpha_mask=0.1)

    
  cv2.putText(dst, on_video_text, (150, 150), font, 3, (0, 255, 255), 6, cv2.LINE_4)
  print("qtd: " + str(qtd))
  

  name = 'saveVid-' + str(frame_ + 1) + '.jpg'
  if(frame_ < length):
    cv2.imwrite(os.path.join(path_to_save, name), dst)
  else:
    break
  frame_ = frame_ + 1

  #cv2_imshow(frame)

    # Save frame as a jpg file
  #trocar o prefixo do nome do frame
  name = 'saveVid-' + str(frame_) + '.jpg' 
  print(f'Creating: {name}')

  #cv2.imwrite(os.path.join(path_to_save, name), frame_)



  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

tree_video.release()
cv2.destroyAllWindows()

print("pausa4")
#time.sleep(10.0)


img_array = []
numbers = re.compile(r'(\d+)')

for filename in sorted(glob.glob('imgSave/*.jpg') , key=numericalSort):
  img = cv2.imread(filename)
  height, width, layers = img.shape
  size = (width,height)
  img_array.append(img)



out = cv2.VideoWriter('finalvideo.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 15, size)

#out = cv2.VideoWriter('./yolov3/Bound_and_Count3.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, size)

for i in range(len(img_array)):
  out.write(img_array[i])
  
out.release()
print('finished')
