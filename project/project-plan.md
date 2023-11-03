# Project Plan

## Main Question
<!-- Describe your data science project in max. 5 sentences. -->

Is there a correlation between Education level and Economic Freedom and what features of each of them are the root of this. 

## Description
<!-- Outline the impact of the analysis, e.g. which pains it solves. -->

 Education quality and growing new generations that have a higher cognitive skill are considered as a one of the key features of the success of a country in term of economical computation and freedom in the world. By the help of these two datasets, we can compare their correlation to test the hypothesis and addition to that, we can analyze how this correlation is changed in time since our datasets are measured the performance on both categories for a considerably long period of time.

       
## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Economic Freedom Rankings
* Metadata URL:
  * https://www.fraserinstitute.org/economic-freedom/dataset?geozone=world&page=dataset&min-year=2&max-year=0&filter=0&year=2021
* Data URL:
  * https://www.fraserinstitute.org/sites/all/modules/custom/ftw_maps_pages/files/efotw-2023-master-index-data-for-researchers-iso.xlsx
* Data Format: xlsx

Dataset includes entire economic freedom dataset, including sub-indicators from 1975 to 2021 for every country that included into the research.

### Datasource2: Educational level score 
* Metadata URL: 
    * [https://pisadataexplorer.oecd.org/ide/idepisa/dataset.aspx](https://pisadataexplorer.oecd.org/ide/idepisa/report.aspx?p=1-RMS-1-20183,20153,20123,20093,20063,20033,20003-PVREAD-TOTAL-IN2,IN3,AUS,AUT,BEL,CAN,CHL,COL,CZE,DNK,EST,FIN,FRA,DEU,GRC,HUN,ISL,IRL,ISR,ITA,JPN,KOR,LVA,LTU,LUX,MEX,NLD,NZL,NOR,POL,PRT,SVK,SVN,ESP,SWE,CHE,TUR,GBR,USA-MN_MN-Y_J-0-0-37&Lang=1033)
* Data URL:
    * link to download the dataset
* Data Format: xls


Subject, Age: Reading, Mathematics and Science, 15 years
Jurisdictions: Selected countries and jurisdictions, International Average (OECD), Australia, Austria, Belgium, Canada, Chile, Colombia, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Israel, Italy, Japan, Korea, Latvia, Lithuania, Luxembourg, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, Slovak Republic, Slovenia, Spain, Sweden, Switzerland, Turkey, United Kingdom, United States
Measures: PISA Reading Scale: Overall Reading, PISA Mathematics Scale: Overall Mathematics, PISA Science Scale: Overall Science
Variables: All students, Student (Standardized) Gender
Years/Studies: 2018, 2015, 2012, 2009, 2006, 2003, 2000



## Work Packages
<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Explore Datasources 
2. Build an Automated Data Pipeline 
3. Add Automated Tests 
4. Explore and Analyze Resulting Data 
5. Add Continuous Integration 
6. Improve Data Pipeline 
7. Report Findings 
8. Refine Datasources Notebook 
9. Make Repository Submission-Ready 
