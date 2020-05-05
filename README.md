# appleAI

## 멀쩡한 사과와 상한 사과를 구별하는 visionAI 모델을 만들고 테스트 하기  
### 아래의 python 파일, 사전학습모델파일, 감지 모델파일, 데이터셋을 모두 다운로드 한다.  
### 트레이닝 파일과 테스트 파일에 있는 로드 부분은 실제 해당 파일이나 폴더의 path를 정확하게 맞춰줘야 한다.  
- traningApple.py : 데이터셋을 이용한 학습을 하는 파일  
- testApple.py : 학습한 모델을 이용해 추론하는 파일  
- [pretrained-yolov3.h5 다운로드](https://drive.google.com/file/d/1G7WNC9is3J-qcp16lNap4PzT_bubdadp/view?usp=sharing)  
- [detection_model-ex-028--loss-8.723.h5 다운로드](https://drive.google.com/file/d/1rDqf4I94dVMcUnlZVytutMAd1SfPrkH5/view?usp=sharing)  
- [apple dataset 다운로드](https://drive.google.com/file/d/1eNgPrxJxu_s-79OIVgSgv_VifQ9YZeEd/view?usp=sharing)  


## 개요
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

* 학습이 끝나면 마지막에서 두번째 코드와 마지막 코드를 통해 실제 사과를 분석할 수 있는데, 이 때 사용할 사과의 이미지는 사용자가 선택해서 사용하면 되고, path만 정확하게 맞춰주면 됨  

* 내가 사용한 멀쩡한 사과 이미지  
![](https://github.com/mtinet/appleAI/blob/master/images/image_apple.jpg?raw=true)  

* 내가 사용한 결함이 있는 사과 이미지  
![](https://github.com/mtinet/appleAI/blob/master/images/image_defactedApple.jpg?raw=true)  

* 결과  
![](https://github.com/mtinet/appleAI/blob/master/images/result.png?raw=true)  
