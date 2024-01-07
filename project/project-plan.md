# Project Plan

## Main Question
<!-- Describe your data science project in max. 5 sentences. -->

Is there a correlation between Human DEvelopment Index and Crime Rates ( In two type of categories: Offences or Envireonmental Crimes) on Country level ?

## Description
<!-- Outline the impact of the analysis, e.g. which pains it solves. -->

 United Nations providing each contry a score from 0 to 1 depend on several factor such as education duration for each citizen and economical parameters. Addition to that, United Nations also collects crime rates for each Country that provides the data publicly accessable for several categories. During this work, it is aimed to compare different crime scores with different factors of development index to be able to see if is there any significant relation that can can be found to investigate deeper. 

       
## Datasources
<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Human Development Report
* Metadata URL:
  * https://hdr.undp.org/content/human-development-report-2021-22
* Data URL:
  *https://github.com/Derin6/MADE_Project/blob/77927c42c204107353521835a03242dcc45f1f66/project/efotw-2023-master-index-data-for-researchers-iso.xlsx](https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Table.xlsx
* Data Format: xlsx

Dataset includes entire uman Development Index  dataset, including sub-indicators from 2021 to 2021 for every country that included into the research. Data Fetaures are listed below:
"Human Development Index (HDI) ,		Life expectancy at birth	,	Expected years of schooling	,	Mean years of schooling	,	Gross national income (GNI) per capita	,	GNI per capita rank minus HDI rank	,	HDI rank"


### Datasource2: Corruption & Economic Crime 
* Metadata URL: 
    * https://dataunodc.un.org/dp-crime-corruption-offences
* Data URL:
    * https://dataunodc.un.org/sites/dataunodc.un.org/files/data_cts_corruption_and_economic_crime.xlsx
* Data Format: xlsx


Dataset includes Crime rates in each country for several sub-categories from 2003 to 2021 with two measurement option: Counts or rate per 100,000 population.  Data Fetaures are listed below:
"Iso3_code, Country,	Region,	Subregion,	Indicator,	Dimension,	Category,	Sex,	Age,	Year,	Unit of measurement,	VALUE,	Source"


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
