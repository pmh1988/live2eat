# Project Overview: Live2Eat
<p align="center">
  <img src="/readme_images/project_overview.png" alt="Alt text" width="600" height="300">
</p>
Live2Eat is an innovative calorie-tracking application that uses food image detection to automate the process of logging meals. The app is designed to be seamlessly integrated with a user's social media content, allowing them to easily track their food intake throughout the day. One of the key features of Live2Eat is its ability to detect local dishes, making it an ideal tool for travelers and foodies who want to keep track of their diet while exploring new cuisines.

The project was developed by a team of three members during a two-week program at Le Wagon Institute. Our team was inspired to create Live2Eat in response to the common pain points that hinder health and wellness programs from becoming permanent lifestyle changes. We recognized that traditional calorie-tracking methods can be time-consuming and cumbersome, making it difficult for people to stay on track with their goals.

Our solution was to develop an app that simplifies the process of calorie tracking by using advanced image recognition technology to identify and log meals automatically. This approach reduces the time and effort required to track food intake, making it more accessible and manageable for users. By integrating Live2Eat with social media, we hope to make calorie tracking a seamless and effortless part of daily life, helping users to stay on track with their health and wellness goals.

Overall, Live2Eat represents a significant innovation in the field of calorie tracking and has the potential to make a real impact on people's lives. Our team is proud of the work we have accomplished and excited about the potential of Live2Eat to help people make lasting, positive changes to their health and wellness habits.


# Data Sources
<p align="center">
  <img src="/readme_images/Sources.png" alt="Alt text" width="600" height="300">
</p>
The images used in Live2Eat were sourced from a variety of locations, including local food blogs such as DanielFooddairy. Due to the unique nature of local delicacies, we found that images of these foods were not readily available in large quantities online. To address this issue, we leveraged a variety of techniques to generate a diverse set of food images for our dataset.

Firstly, we used Canva, a graphic design platform, to create multiple variations of the same image. This approach allowed us to create a more comprehensive and diverse dataset by generating different angles, lighting, and colors for each image.

Additionally, we used the Keras image data generator to further augment the images in our dataset. This allowed us to apply a range of transformations to the images, including rotation, shearing, and zooming, to increase the diversity of our dataset and improve the performance of our image recognition model.

Overall, the use of local food blogs, Canva, and the Keras image data generator allowed us to create a robust and comprehensive dataset for Live2Eat. Our team is confident that this diverse and well-curated dataset will help to ensure accurate and reliable food image recognition within the app.

# Methods and Techniques
<p align="center">
  <img src="/readme_images/Tech_Stack.png" alt="Alt text" width="600" height="300">
</p>

Preprocessing: The team preprocessed the dataset by splitting it into train and test sets. They used techniques such as data augmentation and normalization to improve the performance of the model.

Convolutional Neural Networks: The team used convolutional neural networks (CNNs) to train the image classification model. They focused on using a simple architecture that consisted of convolution layers with 3x3 filters, a stride of 1, and same padding. They also used maxpool layers with 2x2 filters and a stride of 2. This helped to reduce the number of hyperparameters and made the model easier to train.

Transfer Learning: To create the base model, the team used a pre-trained VGG16 model, which is a CNN that has been trained on a large dataset of images. Since the VGG16 model was already trained on a similar domain and task, the team could use its pre-trained network to improve the performance of their model.

Google Video Intelligence API: The team used the Google Video Intelligence API to capture images based on the model and store the files in the respective folder. They also used the API to deduplicate the captured images.

Input Calorie Calculator: The team created an input calorie calculator to display the user's total calorie intake based on the images captured by the model. This helped users to track their calorie intake and make healthier choices.

Deployment: Finally, the team deployed the model and input calorie calculator on Streamlit, a web application framework that allows users to interact with the model and input calorie calculator through a user-friendly interface. This made it easier for users to use the model and track their calorie intake.

# Results
<p align="center">
  <img src="/readme_images/result.jpg" alt="Alt text" width="500" height="400">
</p>

The team achieved an accuracy of 85% in image classification. However, the team acknowledged that this result was a shortfall because the model was only trained on a limited number of local cuisine due to time constraints. Therefore, the model may not be able to accurately classify all types of food images.

To improve the accuracy of the model, the team could consider training it on a larger dataset that includes more local cuisine. They could also consider using more advanced techniques such as fine-tuning the pre-trained VGG16 model or using other pre-trained models that are better suited for the specific task of food image classification.

Despite the shortfall in accuracy, the team's live2eat project is a promising proof-of-concept that demonstrates the potential of using image classification and calorie tracking to help users make healthier choices. With further refinement and improvement, this technology could help people around the world to improve their health and wellness.

# Code Organization

An overview of the project's file structure and any important code files, including how to run the code and any dependencies.
```bash
##   e.g. if group is "{group}" and project_name is "live2eat"
git remote add origin git@github.com:{group}/live2eat.git
git push -u origin master
git push -u origin --tags
```

# Acknowledgments

A section to acknowledge any contributors, data sources, or other individuals or organizations that contributed to the project.

# Future Work

Suggestions for future work and improvements that could be made to the project.

# Contact Information

A way for people to contact the project owner or contributors if they have questions or feedback.
Check for live2eat in github.com/{group}. If your project is not set please add it:
