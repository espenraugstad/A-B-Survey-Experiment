# A-B-Survey-Experiment
This repository contains all the code used in the A/B-Survey experiment.

## Content
### Frontend
This folder contains all the HTML, CSS, and JavaScript for the two versions of the survey. This was deployed to AWS Amplify.

### Backend
This contains one file which is was deployed on AWS Lambda. It receives information from AWS API Gateway containing results from the survey, process them, and put them in a Dynamo DB.

### Data Processing
The results from the Dynamo DB was downloaded as a csv-file. The information in this was processed using Python in two versions. One version creates a more managable csv-file, while the other version plots the results in a grouped bar chart.

## Further reading
For more information, take a look at the project description at Decade 21 (link will be available soon).