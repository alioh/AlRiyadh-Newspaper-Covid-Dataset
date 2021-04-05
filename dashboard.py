import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown('# Saudi journalism in the age of COVID')

# -------------- #

st.markdown('''##### Make sure to view this app using light theme. ([Click here to learn how to change the theme](https://raw.githubusercontent.com/alioh/AlRiyadh-Newspaper-Covid-Dataset/master/ThemeSettings.png))''')

# -------------- #

st.markdown('## About the Data:')
st.markdown('''This dataset is part of a research that we will share soon. It is a dataset of Arabic newspapers
 articles addressing COVID-19 related events. The data origin is [Alriyadh](https://www.alriyadh.com/) newspaper.
 It contains all news articles until **1 February 2021** that have the following words:

| Arabic | English Translation |
| :--: | :--: |
| كورونا | Corona |
| كوفيد-19 | Covid-19 |
| كوفيد المستجد | New Covid |
| حظر التجول | Curfew |
| منع التجول | Curfew |''')

# -------------- #

st.markdown('## Purpose of the Data:')
st.markdown('''We shared this brief EDA about the data in-order to give
you an insight on how the data looks like. Please share with us your
results if you worked on the data.''')

# -------------- #

st.markdown('## Value of the Data:')
st.markdown('''- Alriyadh COVID News is the first, largest dataset that contains newspaper articles ranging from national and international news to opinion columns published to address topics related to COVID-19. 
- The dataset can help to accurately generate events timeline that can be used to interpret trends in COVID related data.  
- It can be also useful for pretraining and fine-tuning deep learning pre-trained language models on downstream Arabic NLP.''')

# -------------- #

st.markdown('## Data origin:')
st.markdown('''The data were scraped / collected from [Alriyadh](https://www.alriyadh.com/) newspaper.''')

# -------------- #

st.markdown('## Data Size:')
st.markdown('''Each word have different size:

| Word | # of News / Articles |
| :--: | :------------------: |
| كورونا | 21961 |
| كوفيد-19 | 1266 |
| كوفيد المستجد | 3044 |
| حظر التجول | 1087 |
| منع التجول | 1255 |''')

st.text('')
st.markdown('''The total size of the dataset after deleting news articles that have more of one
word in our selection of words is: **24084 rows**''')

# -------------- #

st.markdown('## Data Dictionary:')
st.markdown('''The following table explains each column the dataset:

| Column | Description | Datatype | Example |
| :--: | :--: | :--: | :--: |
| ID * | News article ID | Integer | `1867288` |
| Category | Which category in the newspaper the news article were published | String | `مقالات اليوم` / `أخبار المناطق` |
| Source | Source of the news article. Can be news source or the author name | String | `الرياض - واس` or `خالد بن علي المطرفي` |
| Date | Date | Date | `2020-03-27` |
| Time | If null means the news article didn't have time entry | String | `12:05:51` |
| Title | News article title | String | `أمير الجوف يشدّد على تطبيق الإجراءات الاحترازيه` |
| Subtitle | News article subtitle, not always filled | String | `رأس اجتماع غرفة العمليات المشتركة` |
| Text | News article text | String | `شدّد صاحب السمو الملكي الأمير فيصل بن نواف بن عبدالعزيز...` |
| Image * | If the news article have one image, the image source will be added here | String | `/media/thumb/af/1d/1000_5b1f4e7dc6.jpg` |
| Caption | If the news article have one image, it caption will be added here | String | `اليابان تخزن المزيد من النفط السعودي محققة انتعاشاً للطلب` |
| Images * | If the news article have more than one image, the images source will be added here | List | `['/media/thumb/08/d7/1000_a4964ed6ad.jpg', '/media/thumb/04/14/1000_127ad97cda.jpg']` | 
| Captions | If the news article have more than one image, the captions will be added here | List | `['مواعيد إلكترونية لاستقبال المراجعين', 'تطبيق مواعيد الدخول في المحاكم']` |
| URL | Direct link to the news article | String | `http://www.alriyadh.com/1867288` |
| Terms | Terms used in the news article from the previous 5 mentioned in __About the Data__ | List | `['كورونا', 'حظر التجول']` |
| FullText | Title + Subtitle + Text | String | `أمير الجوف يشدّد على تطبيق الإجراءات الاحترازية\\n ورصد المخالفات رأس اجتماع ... في تحقيقها ولله الحمد`  |
| FullTextCleaned | FullText column after cleaning and removing unwanted characters (English words, numbers, new line character '\\n') | String | `أمير الجوف يشدّد على تطبيق الإجراءات الاحترازية ورصد المخالفات رأس اجتماع ... في تحقيقها ولله الحمد` |
| FullTextWords | FullTextCleaned text split into words | List | `['أمير', 'الجوف', 'يشدّد', 'على', 'تطبيق', 'الإجراءات', ... 'الحمد']` |
| WordsCounts | Counts of how many words in a news article after cleaning | Integer | `201` |
''')

st.text('')
st.markdown('''\* For this column, to view the content, add `alriyadh.com` before it followed by the value.''')

# -------------- #

st.markdown('## Exploratory Data Analysis:')
st.markdown('''In this section, we will give a brief insight about the data:''')

# -- Chart #1 -- #

NewsOverTime = pd.read_csv('EDA/NewsOverTime.csv', index_col=[0])
st.markdown('''### New articles over time:''') 
st.markdown('''News articles published after July 2019.''')
st.markdown('''##### Double right click to reset graph.''')
NewsOverTimeFig = px.line(NewsOverTime[NewsOverTime['Date'] > '2019-07-01'], x="Date", y="Total")
st.plotly_chart(NewsOverTimeFig, use_container_width=True)


# -- Chart #2 -- #

DaysNews = pd.read_csv('EDA/DaysNews.csv', index_col=[0])
st.markdown('''### News articles by day:''')
DaysNewsfig = px.bar(DaysNews[['Day', 'Total']], x="Day", y="Total", text="Total")
st.plotly_chart(DaysNewsfig, use_container_width=True)

# -- Chart #3 -- #

NewsByCategory = pd.read_csv('EDA/NewsCategoryByMonthEN.csv', index_col=[0])
st.markdown('''### News articles by category:''')
st.markdown('''News articles published > 2020. Translation for categories in this dataset:''')
st.markdown('''
**Arabic**|**English**|**Total News Articles**|
:-----:|:-----:|:-----:|
الأخبار المصورة|News in Photos|29
مقالات اليوم|Today's Articles|1112
متابعات|Follow-ups|845
المنوعات|Miscellaneous|295
المحليات|Local News|5178
دنيا الرياضة|Sport World|2347
الدولية|International|5339
الاقتصاد|Economy|2658
الأولـــى|First Page|192
الأخــيــرة|Last Page|674
الرأي|Opinions|522
كلمة الرياض|Riyadh Message|80
طــب|Medicine|8
أخبار المناطق|Regions News|859
خزامى الصحارى|Deserts lavender|24
سينما|Cinema|3
صورة اليوم|Today's Photo|10
فن|Art|101
قول على قول|Words on Words|7
محطات متحركة|Moving Stations|3
فيديو الرياض|Riyadh Video|1
ثقافة اليوم|Today's Culture|235
تقارير دولية|World Reports|4
تقارير رسومية|Graphical Reports|14
الأخبار الهامة|Important News|3
المجتمع الدولي|The International Community|1
أدب الجمعة|Friday Literature|1
الكاريكاتير|Caricature|1
تحقيقات وتقارير|Investigations and reports|2
ثقافة السبت|Saturday Education|2
اخر الثقافة|Latest news on culture|19
آخر الأخبار|Latest News|1
نجوم الأمس الرياضي|Yesterdays Sports Starts|1''')

NewsByCategoryfig = px.treemap(NewsByCategory.reset_index(), path=[px.Constant('Year'), 'Month', 'CategoryEn'], values='Total',
                  color='Total', hover_data=['CategoryAR', 'Total'])
st.plotly_chart(NewsByCategoryfig, use_container_width=True)

# -- Chart #4 -- #

NewsByCategoryHisto = NewsByCategory.groupby('CategoryEn')['Total'].sum().reset_index()
NewsByCategoryHistofig = px.histogram(NewsByCategoryHisto, x="CategoryEn", y="Total")
st.plotly_chart(NewsByCategoryHistofig, use_container_width=True)

# -- Chart #5 -- #

NewsByCategoryPiefig = px.pie(NewsByCategoryHisto, values='Total', names='CategoryEn')
st.plotly_chart(NewsByCategoryPiefig, use_container_width=True)

# -------------- #

st.markdown('## Download the data:')
st.markdown('''[GitHub Page Link](https://github.com/alioh/AlRiyadh-Newspaper-Covid-Dataset/), [Download Link](https://github.com/alioh/AlRiyadh-Newspaper-Covid-Dataset/raw/master/Alriyadh_News_Dataset.zip)''')
st.markdown('''##### The file is zipped because it is big ( +360 MB )''')

# -------------- #

st.markdown('## License and Citation:')
st.markdown('''### License:''')
st.markdown('''The data is being made freely available for download under a
[Creative Commons Attribution 3.0 International license](https://creativecommons.org/licenses/by-nc/3.0/).''')
st.markdown('''### Citing the dataset:''')
st.markdown('''Najwa Alghamdi and Ali Alohali, Saudi journalism in the age of COVID (2021).Submitted to Data in Brief.''')
st.markdown('''We would like to thank Alriyadh Newspaper for making their articles archive publicly available.''')


# -------------- #

st.markdown('## Team:')
st.markdown('''The team behind this project:
- [Dr. Najwa AlGhamdi](https://www.linkedin.com/in/dr-najwa-alghamdi-a77aa93/)
- [Ali Alohali](https://www.alioh.com/)''')
