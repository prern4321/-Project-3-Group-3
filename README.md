<h1 align="center">Group 3 – Project 3:</h1>
 
 
![image](https://user-images.githubusercontent.com/111789352/211095843-ddb20a61-4b6f-4cd4-8f86-bb700448cd16.png)
![hospitalporter](https://user-images.githubusercontent.com/111789352/211096550-e8240e64-0387-4f24-9062-15ba766e94fb.jpeg)




# Contributors:

- Prerna Dutt
-	Rahmi Rahmiev
-	Jacob Page
-	Salma Abdirahman
-	Razvan Radu



# Description of Project:

##	Why did we choose the project?

The COVID-19 pandemic has brought to the forefront the numerous challenges faced by the healthcare industry, including increased demand and resource constraints. In light of these issues, we were motivated to investigate the availability and quality of healthcare, specifically in the National Health Service (NHS). Our goal was to select a topic that aligned with this focus.

##	What were our aims/objectives?

The primary objective of our project was to utilise the selected dataset to create a dashboard that visualises the locations of hospitals within England. We also aimed to include information on both non-independent (NHS) and independent (private) hospitals in the database, allowing for comparison between the two types.

Our summarised objectives included:

-	Developing a dashboard containing visualisations derived from the dataset.
-	Creating an interactive map visualisation illustrating the locations of public and private hospitals in England.
-	Developing visualisations comparing the number of public and private hospitals in England.



# Data Set:

After conducting a thorough review of available data sets, we have identified and selected the following three datasets for further analysis:

1.	NHS public data from the UK Government: https://www.data.gov.uk/dataset/73740ffe-cecb-4cba-afb9-51ea996187a1/nhs-england-nhs-choices-hospitals-patient-comments-and-ratings   
2.	NHS Public Data from the UK Government: https://digital.nhs.uk/data-and-information/publications/statistical/hospital-admitted-patient-care-activity/2020-21#resources    
3.	Hospital Data in England from Kaggle: https://www.kaggle.com/datasets/manchunhui/uk-hospitals

Following our selection process, we have chosen to utilise the geospatial data of the UK NHS Hospital Database available on Kaggle. The dataset was downloaded in CSV format and subsequently cleaned and pre-processed for analytical and visualisation purposes.

The Kaggle dataset was selected due to its relevance to the aims of our project, specifically the requirement for geospatial data to create interactive visualisations, such as a map displaying the locations of hospitals in England. The dataset closely fits these requirements and was therefore deemed the most suitable option.

## Preview of Dataset

[![Datasetpreview](https://user-images.githubusercontent.com/111789352/211102761-1359c402-7280-46a2-989f-ddffca7f219d.png)](https://www.kaggle.com/datasets/manchunhui/uk-hospitals)


While the dataset includes a large amount of information, our focus was on the hospital ID/name, location, and type (NHS/non-independent sector or Private/independent sector). These specific details were necessary for the purposes of our analysis.

Aim of the project :
To be able to locate the hospitals on the map , hospitals with the county and their type (private/nhs) across the counties. Our focus was primarily to  build our knowledge on getting the different technologies to work together to create interactive visualizations.



# Technology used:

-	**Python Flask API:** Utilised to automatically fetch data from the SQL database and render the template.
-	**JavaScript:** Used to plot the interactive charts.
-	**SQL with Flask:** Utilised to import data from a CSV file obtained from Kaggle and store it in a newly created database.
-	**HTML and CSS:** Utilised to create the web application, with HTML providing the structure and layout and CSS enhancing the appearance.
-	**Bootstrap:** Utilised alongside HTML and CSS for navigation bars and buttons.
-	**Pandas:** Used to clean, prepare, and transform the data for analysis by removing unnecessary columns and data.



# JS Library

After conducting a review of various JavaScript libraries, we evaluated both HighCharts and CanvasJS.


[![CanvasJS](https://user-images.githubusercontent.com/111789352/211121281-98d49e56-54fa-4259-8517-f14abe7f9472.png)](https://canvasjs.com/) </a> [![HighCharts](https://user-images.githubusercontent.com/111789352/211123880-60ea752f-ead2-4daf-9f8e-13258d774589.png)](https://www.highcharts.com/)


After testing, we ultimately chose to proceed with CanvasJS as it effectively met the requirements of our project. Mainly for its ability to create rich interactive and easily animated dashboards. Also, for its portability across devices and ability to be supported by major browsers.



# Coding logic 

Please note the code was witten in chunks so it is easier to run and debug
### Index Page
![image](https://user-images.githubusercontent.com/112128775/210757658-3cdc641f-4afd-4026-bcf0-568ec07dacd7.png)

### County Plot Visualization
![image](https://user-images.githubusercontent.com/112128775/210757793-0ea7b9ec-c86e-4a33-b5f9-21383ebf2fdd.png)

### Sector Chart Visualization
![image](https://user-images.githubusercontent.com/112128775/210757844-1e5d7efe-b605-4b85-bb4c-8ed9163b778d.png)

### Map Plot Visualizaton 
![image](https://user-images.githubusercontent.com/112128775/211083897-27a9a467-0eb3-47b6-b508-be7227c0c877.png)



## Visualizations created  :

1) Interactive map of Public and Private hospital locations
![image](https://user-images.githubusercontent.com/112128775/211114964-6bde59a7-1972-4868-bbe5-54a3e49a62cb.png)

2) Localised visualizaton of hospitals within a county and their location details using canvas.js
![image](https://user-images.githubusercontent.com/112128775/211115030-0921b687-4113-44fa-b2b4-c39325f8abc6.png)

3) Pie chart visualization of the spread of independant/private vs non independant/nhs hospitals within a county.
![image](https://user-images.githubusercontent.com/112128775/211115050-a20f3a1f-4255-4173-889c-c0f5c5c2037d.png)



# Contribution:
## Prerna Dutt
(Insert individual contribution)



## Jacob Page
(Insert individual contribution)



## Rahmi Rahmiev
(Insert individual contribution)



## Razvan Radu
(Insert individual contribution)



## Salma Abdirahman

After selecting the dataset as a team, we established the project timeline and I created a shared document to track progress. I contributed my JavaScript knowledge and researched various JS libraries for use in the project, initially focusing on HighCharts for visualisation. However, due to issues with code reliability, time constraints, and the ability of CanvasJS to create similar or superior visualisations, we decided to abandon the use of HighCharts and proceed with CanvasJS instead.

We collaborated effectively as a team on various aspects of the project, including the presentation. I created a skeleton presentation and uploaded it as a shared document, allowing other team members to edit and contribute to various sections. In addition, I assisted in the finalisation of the README, ensuring that it met the necessary requirements and was presented in a professional manner.
