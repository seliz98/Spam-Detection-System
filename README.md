The aim of this assignment is to design and develop a simple and rudimentary spam detection 
system using the following technologies:  
• Cloud Infrastructure using AWS, GCP or other industry-standard public cloud  
• Hadoop  
• MapReduce  
• Hive  
• Pig 

I have used an amazon reviews dataset for this assignment. The dataset is acquired from Kaggle (https://www.kaggle.com/datasets/naveedhn/amazon-product-review-spam-and-nonspam) and the used dataset is Cell_Phones_and_Accessories.json. Since this dataset is in json format I converted it into a csv file saved as amazon_review.csv, choosing only required columns i.e, reviewerID, reviewText, category and class using pandas. The file in which this 
work is done is in Spam-Detection-System.ipynb in the git repo. After converting into csv the file size is of 1.1GB. I have converted the reviewtext column into lowercase string before converting it into csv file. 
