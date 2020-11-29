import pandas as pd
import json
import sys
import os 
import plotly.express as px
import plotly

try:
    dataset = sys.argv[1]
except:
    print("execute using - python3 plot_district_map.py <dataset-name>\n\nmake sure dataset and the geojson are in the same directory as the script")
    sys.exit()

list_dir = os.listdir('.')

if dataset not in list_dir:
    print("the dataset mentoined - {} does not exist in current directory".format(dataset))
    sys.exit()


df = pd.read_csv(dataset)
df["id"] = (df["state"]+df["district"])
df["id"] = df["id"].apply(lambda x: x.replace(" ",""))

df['district'] = df['district'].replace(['korea'],'koriya')
df['district'] = df['district'].replace(['gautam buddha naga'],'gautam buddha nagar')
df['district'] = df['district'].replace(['jyotiba phule naga'],'jyotiba phule nagar')
df['district'] = df['district'].replace(['dakshin bastar dant'],'dakshin bastar dantewada')
df['district'] = df['district'].replace(['leh'],'leh (ladakh)')
df['district'] = df['district'].replace(['north twenty four '],'north 24 parganas')
df['district'] = df['district'].replace(['south twenty four '],'south 24 parganas')
df['district'] = df['district'].replace(['paschim medinipur'],'pashchim medinipur')
df['district'] = df['district'].replace(['pashchimi singhbhu'],'pashchimi singhbhum')
df['district'] = df['district'].replace(['ribhoi'],'ri bhoi')
df['district'] = df['district'].replace(['sahibzada ajit sin'],'sahibzada ajit singh nagar')
df['district'] = df['district'].replace(['sabarkantha'],'sabar kantha')
df['district'] = df['district'].replace(['shahid bhagat sing'],'shahid bhagat singh nagar')
df['district'] = df['district'].replace(['sri potti sriramulu'],'sri potti sriramulu nellore')
df['district'] = df['district'].replace(['north  district'],'north district')

cols = list(df.columns)
cols = cols[2:-1]
print("The columns which can be used to plot the maps are :")

for i in range(0,len(cols)):
    print("{}. {}".format(i+1,cols[i]))
#print("\n")
choice_no = input("enter the corresponding number of the column of your choice : ")
choice_no = int(choice_no.strip())
choice = cols[choice_no-1]

print("processing......")

data = df.nlargest(5,[choice])
fig = px.bar(data, x=choice, y="district", color='state', orientation='h',
             height=400,range_x=[0,100],
             title=choice,text=choice)

dataset = dataset.split(".")[0]
fig.write_html("barplot-{}-{}.html".format(dataset,choice))
print("\nthe output html has been written to the current directory\nopen barplot-{}-{}.html in a browser to view your output".format(dataset,choice))

