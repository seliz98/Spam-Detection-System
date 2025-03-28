import pandas as pd;
import glob;

folderPath = "tfidfResults";

allFiles = glob.glob(folderPath + "/*.txt");

for FilePath in allFiles:
    filename = FilePath.split('tfidfResults/')[1];
    print(filename.split('.')[0]+' Reviewer ID\n');
    df = pd.read_csv(FilePath, sep="\t",header=None,names=["word","tfidf_score"]);
    df["word"] = df["word"].str.split(" ",n=1,expand=True);
    result = df.sort_values(by = ["tfidf_score"], ascending=False).head(10);
    print(result);
   #print('\n\n');