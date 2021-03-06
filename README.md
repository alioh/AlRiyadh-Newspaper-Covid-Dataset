# Riyadh Newspaper Coverage of COVID-19


## About the Data:
This dataset is part of a research that we will share soon. It is a dataset of Arabic newspapers
articles addressing COVID-19 related events. The data origin is [Alriyadh][Alriyadh] newspaper.
It contains all news articles until **1 February 2021** that have the following words:

| Arabic | English Translation |
| :--: | :--: |
| كورونا | Corona |
| كوفيد-19 | Covid-19 |
| كوفيد المستجد | New Covid |
| حظر التجول | Curfew |
| منع التجول | Curfew |

## Purpose of the Data:
We shared this brief EDA about the data in-order to give
you an insight on how the data looks like. Please share with us your
results if you worked on the data.

## Value of the Data:
- Alriyadh COVID News is the first, largest dataset that contains newspaper articles ranging from national and international news to opinion columns published to address topics related to COVID-19. 
- The dataset can help to accurately generate events timeline that can be used to interpret trends in COVID related data.  
- It can be also useful for pretraining and fine-tuning deep learning pre-trained language models on downstream Arabic NLP.


## Data origin:
The data were scraped / collected from [Alriyadh](https://www.alriyadh.com/) newspaper.

## Data Size:
Each word have different size:

| Word | # of News / Articles |
| :--: | :------------------: |
| كورونا | 21961 |
| كوفيد-19 | 1266 |
| كوفيد المستجد | 3044 |
| حظر التجول | 1087 |
| منع التجول | 1255 |


The total size of the dataset after deleting news articles that have more of one
word in our selection of words is: **24084 rows**

## Data Elements:
The following table explains each column the dataset:


| Column | Description | Datatype | Example |
| :--: | :--: | :--: | :--: |
| ID * | News article ID | Integer | `1867288` |
| Category | Which category in the newspaper the news article were published | String | `مقالات اليوم` / `أخبار المناطق` |
| Source | Source of the news article. Can be news source or the auther name | String | `الرياض - واس` or `خالد بن علي المطرفي` |
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
| FullText | Title + Subtitle + Text | String | `أمير الجوف يشدّد على تطبيق الإجراءات الاحترازية\\n ورصد المخالفات رأس اجتماع ... في تحقيقها ولله الحمد` |
| FullTextCleaned | FullText column after cleaning and removing unwanted characters (English words, numbers, new line character '\\n | String | `أمير الجوف يشدّد على تطبيق الإجراءات الاحترازية ورصد المخالفات رأس اجتماع ... في تحقيقها ولله الحمد` |
| FullTextWords | FullTextCleaned text split into words | List | `['أمير', 'الجوف', 'يشدّد', 'على', 'تطبيق', 'الإجراءات', ... 'الحمد']` |
| WordsCounts | Counts of how many words in a news article after cleaning | Integer | `201` |

\* For this column, to view the content, add `alriyadh.com/` before it followed by the value.

## Exploratory Data Analysis:
[Streamlit][streamlit]

## Download the data:
[GitHub Page Link][github], [Github Link][download]
##### The file is zipped because it is big ( +360 MB )


## License and Citation::
### License
The data is being made freely available for download under a [Creative Commons Attribution 3.0 International license](https://creativecommons.org/licenses/by-nc/3.0/).
### Citing the dataset:
Najwa Alghamdi and Ali Alohali, Saudi journalism in the age of COVID (2021). Submitted to Data in Brief. [Science Direct](https://www.sciencedirect.com/).

## Team:
The team behind this project:
- [Ali Alohali][ali]
- [Dr. Najwa AlGhamdi][najwa]



[najwa]: https://www.linkedin.com/in/dr-najwa-alghamdi-a77aa93/
[ali]: https://www.alioh.com/
[download]: https://github.com/alioh/AlRiyadh-Newspaper-Covid-Dataset/raw/master/Alriyadh_News_Dataset.zip
[CCAI]: https://creativecommons.org/licenses/by/4.0/
[SD]: https://www.sciencedirect.com/
[streamlit]: https://share.streamlit.io/alioh/alriyadh-newspaper-covid-dataset/dashboard.py
[Alriyadh]: https://www.alriyadh.com/
[github]: https://github.com/alioh/AlRiyadh-Newspaper-Covid-Dataset/