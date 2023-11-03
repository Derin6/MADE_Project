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
    * https://pisadataexplorer.oecd.org/ide/idepisa/dataset.aspx
* Data URL:
    * link to download the dataset
* Data Format: xlsx


Subject, Age: Global Competence, 15 years
Jurisdictions: Selected countries and jurisdictions, International Average (OECD), Canada, Chile, Colombia, Greece, Israel, Korea, Latvia, Lithuania, Slovak Republic, Spain, Albania, Brunei Darussalam, Chinese Taipei, Costa Rica, Croatia, Hong Kong (China), Indonesia, Kazakhstan, Malta, Morocco, Panama, Philippines, Russia, Serbia, Singapore, Thailand, Russian Federation: Moscow region, Russian Federation: Republic of Tatarstan, Spain: Andalusia, Spain: Aragon, Spain: Asturias, Spain: Balearic Islands, Spain: Basque Country, Spain: Canary Islands, Spain: Cantabria, Spain: Castile and Leon, Spain: Castile-La Mancha, Spain: Catalonia, Spain: Comunidad Valenciana, Spain: Extremadura, Spain: Galicia, Spain: La Rioja, Spain: Madrid, Spain: Murcia, Spain: Navarre, United Kingdom: Scotland
Measures: PISA Reading Scale: Overall Reading, PISA Mathematics Scale: Overall Mathematics, PISA Science Scale: Overall Science, PISA Global Competence Scale
Variables: All students, Student (Standardized) Gender, ISCED designation, ISCED level, ISCED orientation, Have you ever repeated a [grade]? At [ISCED 1], Have you ever repeated a [grade]? At [ISCED 2], Have you ever repeated a [grade]? At [ISCED 3], Grade Repetition, Number of school changes, How old were you when you started [ISCED 0]? Years, Highest Education of parents - alternate definition (ISCED), Index hs Education - alternate definition (ISCED)



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
