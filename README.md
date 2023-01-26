# Project H.A.R.N.
H.A.R.N. (Hydro-farming with Autonomous Regulation of Nutrients) is a plant nutrient deficiency classification system which can detect whether a rice plant is healthy or has any of N, P or K deficiency when provided with an image of a rice leaf. Deployed webapp ([link](https://faryar251-harn-predictions-eqt4lv.streamlit.app/)).

# <a name="toc">Table of Contents</a>
1. [Introduction](#intro)
2. [Dataset](#ds)
3. [Installation Guide](#install)
4. [Screenshots](#ss)

# 1. <a name="intro">Introduction</a>
###### [Back to Table of Contents](#toc)
There are various methods for identifying nutrient deficiency in plants such as rapid testing & plant analysis. Also, the existing Hydroponic systems usually have automated system which is just relying on the external paraments of the plant such as temperature, humidity, etc.. Plants require nutrients to germinate, grow, fight off diseases and pests and to reproduce. A plant that lacks an essential nutrient cannot complete its life cycle. However, having too much of a nutrient can harm and even kill plants. This is why, the purpose of project H.A.R.N. is to provide a better and fast solution for identifying plant nutrient deficiency using Image Processing techniques and Convolutional Neural Networks (CNN). This project is made to identify nutrient deficiency in rice and spinach plants. The nutrients that will be identified by this project are Macronutrients viz (Nitrogen (N), Potassium (K), and Phosphorous (P)). Various CNN models was tested and the model with the best fit is deployed using StreamLit as a webapp [here.](https://faryar251-harn-predictions-eqt4lv.streamlit.app/)

The paper referred provides a detailed process: [Using Deep Convolutional Neural Networks for Image-Based Diagnosis of Nutrient Deficiencies in Rice](https://www.hindawi.com/journals/cin/2020/7307252/) by Zhe Xu, Xi Guo, Anfan Zhu, Xiaolin He, Xiaomin Zhao, Yi Han and Roshan Subedi.

# 2. <a name="ds">Dataset</a>
###### [Back to Table of Contents](#toc)
Dataset is labeled and available here: [Google Drive](https://drive.google.com/drive/folders/1kfX8iL_A2MK-XbGqOowDwzDv0PWAO7Y6?usp=sharing)

# 3. <a name="install">Installation Guide</a>
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

# 4. <a name="ss">Screenshorts</a>
###### [Back to Table of Contents](#toc)

### 4.1. Home page
![ss1](https://user-images.githubusercontent.com/72343934/214845647-6f7a53e4-015f-474c-9d9a-372348203d0e.png)

### 4.2. K Deficiency detection
![ss2](https://user-images.githubusercontent.com/72343934/214845702-d4062640-e4e8-433a-8e43-ad2a9087940d.png)

### 4.3. N Deficiency detection
![ss3](https://user-images.githubusercontent.com/72343934/214845732-5ec18963-2b15-4351-a869-d8114478a0a2.png)

### 4.4. P Deficiency detection
![ss4](https://user-images.githubusercontent.com/72343934/214845750-92f04ff7-9c08-42bc-91fd-74840ec7870a.png)

### 4.5. Healthy Rice leaf detection
![ss5](https://user-images.githubusercontent.com/72343934/214845762-67d87804-ed32-45ca-8eba-5fb4fe80ba27.png)
