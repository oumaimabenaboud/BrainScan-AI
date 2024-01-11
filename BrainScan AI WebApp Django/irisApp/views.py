from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
import tensorflow as tf
import numpy as np

from PIL import Image
import cv2

tf_session = tf.compat.v1.Session()
model=tf.keras.models.load_model('./savedModels/our_model_BT.h5')

def index (request):
    return render(request,'home.html',{})

def predictimage(request):
    print(request)
    print(request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    print(testimage)
    img=Image.open(testimage, mode='r')
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(opencvImage,(150,150))
    img = img.reshape(1,150,150,3)
    p = model.predict(img)
    p = np.argmax(p,axis=1)[0]

    if p==0:
        p='Tumeur du gliome'
        description="Les tumeurs gliales sont des tumeurs qui se développent dans les cellules gliales du cerveau et de la moelle épinière. Les cellules gliales soutiennent et protègent les neurones. Il existe plusieurs types de tumeurs gliales, notamment les astrocytomes, les oligodendrogliomes et les méningiomes. Ces tumeurs peuvent être bénignes ou malignes et peuvent causer des symptômes tels que des maux de tête, des nausées et des vomissements, des convulsions et des troubles de la vision. Le traitement dépend de la nature de la tumeur et de son emplacement. Il peut inclure la chirurgie, la radiothérapie et la chimiothérapie."
    elif p==1:
        p='Aucune tumeur détectée'
        description="Cela signifie que le modèle de prédiction a analysé l'image IRM d'entrée et a déterminé qu'il n'y a pas de signes ou d'indications d'une tumeur cérébrale présente dans l'image. Cela indique que le modèle n'est pas en mesure d'en identifier une dans l'image fournie. Il est important de noter que cette prédiction doit être interprétée par un radiologue ou un médecin, car le modèle peut avoir un faux négatif ou manquer une petite tumeur. De même, le modèle peut être précis mais le patient peut avoir une tumeur dans une autre zone du cerveau qui n'est pas prise en compte par l'image."
    elif p==2:
        p='Tumeur du méningiome'
        description="Un méningiome est une tumeur bénigne qui se développe à partir des membranes qui entourent le cerveau et la moelle épinière. Il est le plus souvent localisé dans la région de la boîte crânienne, tels que les cavités qui entourent le cerveau (cavité crânienne) et la colonne vertébrale (canal spinal). Les symptômes dépendent de l'emplacement de la tumeur et peuvent inclure des maux de tête, des troubles de la vision, des troubles de la coordination et de la marche, des troubles de la mémoire et de la concentration, et des crises d'épilepsie. Le traitement peut inclure la chirurgie, la radiothérapie et la surveillance."
    else:
        p='Tumeur hypophysaire'
        description="Les tumeurs hypophysaires sont des tumeurs qui se développent à partir de la glande hypophyse, qui est située à la base du cerveau. La glande hypophyse est responsable de la production de nombreux hormones importantes qui régulent de nombreuses fonctions corporelles, telles que la croissance, la reproduction et la régulation de la métabolisme. Les tumeurs hypophysaires peuvent être bénignes ou malignes. Les tumeurs bénignes, comme l'adenome hypophysaire, sont généralement plus courantes, tandis que les tumeurs malignes, comme le carcinome hypophysaire, sont plus rares. Les symptômes courants des tumeurs hypophysaires comprennent des troubles de l'humeur, des perturbations de la vision, des troubles de la croissance, des troubles de la reproduction, des troubles de la thyroïde et des troubles de la métabolisme. Le traitement peut inclure la chirurgie, la radiothérapie et la thérapie hormonale."

    # if p!=1:
    #     print(f'The Model predicts that it is a {p}')
    context={'filePathName': filePathName, 'description':description, 'prediction':p}
    return render(request,'home.html',context)