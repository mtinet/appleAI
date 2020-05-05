# appleAI

## 멀쩡한 사과와 상한 사과를 구별하는 visionAI 모델을 만들고 테스트 하기  
### 아래의 python 파일, 사전학습모델파일, 감지 모델파일, 데이터셋을 모두 다운로드 한다.  
### 트레이닝 파일과 테스트 파일에 있는 로드 부분은 실제 해당 파일이나 폴더의 path를 정확하게 맞춰줘야 한다.  
- trainingApple.py : 데이터셋을 이용한 학습을 하는 파일  
- testNormalApple.py : 학습한 모델을 이용해 추론하는 파일(일반 사과 파일을 불러옴)  
- testDefactedApple.py : 학습한 모델을 이용해 추론하는 파일(결함 사과 파일을 불러옴)  
- [pretrained-yolov3.h5 다운로드](https://drive.google.com/file/d/1G7WNC9is3J-qcp16lNap4PzT_bubdadp/view?usp=sharing)  
- [detection_model-ex-028--loss-8.723.h5 다운로드](https://drive.google.com/file/d/1rDqf4I94dVMcUnlZVytutMAd1SfPrkH5/view?usp=sharing)  
- [apple dataset 다운로드](https://drive.google.com/file/d/1eNgPrxJxu_s-79OIVgSgv_VifQ9YZeEd/view?usp=sharing)  


## 개요
### 데스크탑 버전  
* 이 레파지토리를 다운로드 받아서 사용함, image 폴더 안의 이미지들은 결과를 보여주기 위한 캡쳐파일이므로, 프로그램의 구동과는 관계가 없음  

* 최초의 apple_dataset 폴더 안에는 학습을 위한 train(annotations, images)폴더와 평가를 위한 validation(annotations, images)폴더만 있다.  
 - train-annotations(이미지 정보를 지도학습으로 지도하기 위한 정보가 들어있는 xml 파일들을 포함함)  
 - train-images(이미지 파일들을 포함함, annotations 파일과 파일명이 같음, 일반사과 294장, 결함사과 269장)  
 - validation-annotations(이미지 정보를 지도학습으로 지도하기 위한 정보가 들어있는 xml 파일들을 포함함)  
 - validation-images(이미지 파일들을 포함함, annotations 파일과 파일명이 같음, 일반사과 75장, 결함사과 75장)  

* traingApple.py 파일은 apple_dataset폴더의 데이터셋을 이용해 pretrained-yolov3.h5파일로 학습을 하며 사용한 데이터셋 폴더 안에 cache, json, logs, models폴더를 만들고, json폴더 안에는 detection_config.json 파일이 만들어진다.  
![](https://github.com/mtinet/appleAI/blob/master/images/folder1.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/folder2.png?raw=true)  

* testApple.py파일은 detection_model-ex-028--loss-8.723.h5파일과 training 단계에서 만들어진 detection_config.json 파일을 이용해 image_apple.jpg 파일을 불러와 추론하고 결과값을 출력하고 image-new.jpg 파일을 저장한다.  
![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop.png?raw=true)  

* testNormalApple.py파일과 testDefactedApple.py 파일은 detection_model-ex-028--loss-8.723.h5파일과 training 단계에서 만들어진 detection_config.json 파일을 이용해 각각 image_apple.jpg와 defactedApple.jpg파일을 불러와 추론하고 image-new.jpg, image-new1.jpg 파일을 저장 한 다음 결과값과 결과 이미지를 보여준다.  

![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop1.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop2.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop3.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop4.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/resultDesktop5.png?raw=true)  

* 



### 코랩 버전  
* [참조 사이트 링크](https://medium.com/deepquestai/ai-in-agriculture-detecting-defects-in-apples-b246799b329c)  

* [코랩 실행 예제 링크](https://colab.research.google.com/drive/1vfISFuOlMtpS06XdkuUFr81w5EtCBfoO)  

* 이 예제를 코랩으로 실행할 때는 구글 드라이브를 연계해야 코랩이 끊어져도 데이터를 유지할 수 있음(예제의 첫부분이 구글 드라이브와 연계하는 부분)  
![](https://github.com/mtinet/appleAI/blob/master/images/connectGDrive.png?raw=true)  

* 코랩을 사용해도 epoch당 15분 정도가 걸리므로 총 50회의 epoch를 돌리기 위해서는 12시간이 넘게 걸리게 되고, 컴퓨터를 켜놓고 잔다고 해도 자동으로 연결이 끊어지므로, 2~5번 정도의 epoch만 돌려볼 것을 권장함, 5번 정도 돌리면 loss가 많이 줄어 있음   
![](https://github.com/mtinet/appleAI/blob/master/images/colab1.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/colab2.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/colab3.png?raw=true)  

* 이 예제를 데스크탑(xeon 3123, GTX750)으로 구동하면 코랩보다 훨씬 오래 걸림  
![](https://github.com/mtinet/appleAI/blob/master/images/desktop.png?raw=true)  

* traningApple.py 파일을 이용해 학습을 시키고 나면, 불러온 데이터셋이 있는 폴더(여기서는 apple_dataset)안에 json폴더가 생기고, 그 안에 detection_config.json 파일이 만들어짐. testApple.py 파일은 이 json파일과 detection_model-ex-028--loss-8.723.h5을 불러와서 내가 확인하고 싶은 이미지의 사과의 결함여부를 확인하게 됨  
![](https://github.com/mtinet/appleAI/blob/master/images/json.png?raw=true)  

* 학습이 끝나면 마지막에서 두번째 코드와 마지막 코드를 통해 실제 사과를 분석할 수 있는데, 이 때 사용할 사과의 이미지는 사용자가 선택해서 사용하면 되고, path만 정확하게 맞춰주면 됨  

* 내가 사용한 멀쩡한 사과 이미지  
![](https://github.com/mtinet/appleAI/blob/master/images/image_apple.jpg?raw=true)  

* 내가 사용한 결함이 있는 사과 이미지  
![](https://github.com/mtinet/appleAI/blob/master/images/defactedApple.jpg?raw=true)  

* 결과(이미지를 보여주지 않는 결과, 파일은 코랩에 저장되도록 되어 있음)  
![](https://github.com/mtinet/appleAI/blob/master/images/result.png?raw=true)  

* 결과(이미지를 보여주는 결과, cv2를 이용해 결과 이미지를 보여주도록 코드를 수정함, 파일은 코랩에 저장되도록 되어 있음)  
![](https://github.com/mtinet/appleAI/blob/master/images/result1.png?raw=true)  
![](https://github.com/mtinet/appleAI/blob/master/images/result2.png?raw=true)  

