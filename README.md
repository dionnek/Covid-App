# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

Use Markdown to write your readme.md file.  Here is a [cheatsheet](https://www.markdownguide.org/cheat-sheet/).

The final dashboard is deployed on Heroku [here](https://ma705bostonuniversities.herokuapp.com).

## Dashboard Description

Brief description of dashboard's purpose.

This dashboard This dashboard provides an interactive visualization of the progress of the Covid-19 Vaccine since its deployment in December 2020.
Users residing in the U.S. will gain a better understanding of how their state compares to others as well as how the U.S. compares to other countries from this dashboard.
Users can interact with information including:
- The total amount of vaccines deployed since January 2021 by state
- The reported amount of fully vaccinated individuals in each state since the deployment
- The total amount of vaccines deployed in various countries since January 2021
- The breakdown in the types of vaccines received by individuals in the different countries over time
- How reported Covid-19 cases and related deaths have changed since the deployment of the vaccine

### Data Sources

Brief description of where/how you got the data and how it was processed.

-Vaccination by state data: https://www.kaggle.com/paultimothymooney/usa-covid19-vaccinations
This dataset contains information from https://ourworldindata.org/us-states-vaccinations#licence and is updated regularly. The data was cleaned by removing dates with null values and U.S. territories for consistency purposes. This dataset is linked to the first two graphs showing vaccination progress by state.

-World vaccine data: https://www.kaggle.com/gpreda/covid-world-vaccination-progress
This dataset contains information from https://ourworldindata.org/coronavirus and is updated regularly. The data was cleaned by removing null date values. This dataset is linked to the pie chart and following graph showing vaccine progress in various countries and the breakdown of the type of vaccine being administered. 

-World Covid cases data: https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths
This dataset comes from the World Health Organization. Countries that were not seen in the World Vaccine dataset and dates prior to December 24th, 2020 were removed from this one for consistency purposes. This dataset is linked to the last two graphs showing Covid-19 cases and related deaths since the deploment of the vaccine. 

### Other Comments


