# Project H.A.R.N.
H.A.R.N. (Hydro-farming with Autonomous Regulation of Nutrients) is a plant nutrient deficiency classification system which can detect whether a rice plant is healthy or has any of N, P or K deficiency when provided with an image of a rice leaf. Deployed webapp ([link](https://harnpredict.streamlit.app/)).

# <a name="toc">Table of Contents</a>
1. [Introduction](#intro)
2. [Dataset](#ds)
3. [Technologies Used](#tech)
4. [Installation Guide](#install)
5. [Screenshots](#ss)

# 1. <a name="intro">Introduction</a>
###### [Back to Table of Contents](#toc)
There are various methods for identifying nutrient deficiency in plants such as rapid testing & plant analysis. Also, the existing Hydroponic systems usually have automated system which is just relying on the external paraments of the plant such as temperature, humidity, etc.. Plants require nutrients to germinate, grow, fight off diseases and pests and to reproduce. A plant that lacks an essential nutrient cannot complete its life cycle. However, having too much of a nutrient can harm and even kill plants. This is why, the purpose of project H.A.R.N. is to provide a better and fast solution for identifying plant nutrient deficiency using Image Processing techniques and Convolutional Neural Networks (CNN). This project is made to identify nutrient deficiency in rice and spinach plants. The nutrients that will be identified by this project are Macronutrients viz (Nitrogen (N), Potassium (K), and Phosphorous (P)). Various CNN models was tested and the model with the best fit is deployed using StreamLit as a webapp [here.](https://harnpredict.streamlit.app/)

The paper referred provides a detailed process: [Using Deep Convolutional Neural Networks for Image-Based Diagnosis of Nutrient Deficiencies in Rice](https://www.hindawi.com/journals/cin/2020/7307252/) by Zhe Xu, Xi Guo, Anfan Zhu, Xiaolin He, Xiaomin Zhao, Yi Han and Roshan Subedi.

# 2. <a name="ds">Dataset</a>
###### [Back to Table of Contents](#toc)
Dataset is labeled and available here: [Google Drive](https://drive.google.com/drive/folders/1kfX8iL_A2MK-XbGqOowDwzDv0PWAO7Y6?usp=sharing)

# 3. <a name="tech">Technologies Used</a>
###### [Back to Table of Contents](#toc)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 
# 4. <a name="install">Installation Guide</a>
###### [Back to Table of Contents](#toc)
> Note: I have used Git Bash for the project and provided the code for the same.
- Create a folder in your local machine.
- Create a virtual environment.
```
pip install virtualenv
```
Open Git Bash and navigate to your project folder OR open project folder, right click and then click 'Get Bash Here'
```
python -m virtualenv {whatever_virtual_env_name_you_want_to_give}
```
- Activate the virtual environment.
```
source {whatever_virtual_env_name_you_want_to_give}/scripts/activate
```
- Fork and clone this repository to your local machine's project folder.
- Install all the necessary dependencies and modules inside the virtual environment:
```
pip install -r requirements.txt
```

# 5. <a name="ss">Screenshorts</a>
###### [Back to Table of Contents](#toc)

### 5.1. Home page
![ss1](https://user-images.githubusercontent.com/72343934/214845647-6f7a53e4-015f-474c-9d9a-372348203d0e.png)

### 5.2. K Deficiency detection
![ss2](https://user-images.githubusercontent.com/72343934/214845702-d4062640-e4e8-433a-8e43-ad2a9087940d.png)

### 5.3. N Deficiency detection
![ss3](https://user-images.githubusercontent.com/72343934/214845732-5ec18963-2b15-4351-a869-d8114478a0a2.png)

### 5.4. P Deficiency detection
![ss4](https://user-images.githubusercontent.com/72343934/214845750-92f04ff7-9c08-42bc-91fd-74840ec7870a.png)

### 5.5. Healthy Rice leaf detection
![ss5](https://user-images.githubusercontent.com/72343934/214845762-67d87804-ed32-45ca-8eba-5fb4fe80ba27.png)
