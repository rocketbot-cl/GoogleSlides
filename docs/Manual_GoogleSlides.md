



# Google Slides
  
This module allows you to create, write and update Google Slides. You can add or remove slides and text on them; download the presentation in various formats; and more.  

  
![banner](imgs/BannerGoogleSlides.jpg)


## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

Before using this module, you must register your app into Google Cloud Portal.

1. Sign in with a google account and get into the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form to create a new proyect and then press "Create".
3. Within the Navigation Menu (Left), get into API and Services.
4. Go to the upper section and press "+ ENABLE API AND SERVICES".
5. Search for "Google Slides API", select it and then press "ENABLE". Same with "Google Drive API".
6. Go back to the Navigation Menu, go to API and Services and then get into Credentials.
7. Press Create Credentials and select OAuth Client ID. Then select Application Type: Desktop App, give it a name and press Create.
8. Download the credentials JSON file.
9. Finally, go back to the Navigation Menu, go to Consent Screen and add your user in the "Test Users" section (even if it is the same that is creating the app).

Note: When the first connection is made, a .pickle 
file will be created in the Rocketbot root folder, to connect to the same service with another account you must give each session a name. If credentials expire you must delete the .pickle file and create and download a new credentials (JSON) file.


## Description of the commands

### Setup G-Suite credentials
  
Get permissions to handle Google Slides with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Path||C:/path/to/credentials.json|
|Session||session|
|Variable where the result will be saved||Variable|

### New Presentation
  
Create a new Google Slides presentation with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Title of presentation||Title|
|Variable where the ID will be saved||Variable|
|Session||session|

### Add blank slide
  
Add a new slide to your Google Slides presentation
|Parameters|Description|example|
| --- | --- | --- |
|ID of presentation||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variable where the result will be saved||Variable|

### Add layout slide
  
Add a new slide with title and body to your Google Slides presentation
|Parameters|Description|example|
| --- | --- | --- |
|ID of presentation||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Variable where the result will be saved||Variable|

### Delete Presentation
  
Delete a selected Google Presentation
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Session||session|
|Variable where the result will be saved||Variable|

### Delete Slide
  
Delete a slide from a selected Google Presentation
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Slide ID||SLIDES_API1476047835_0|
|Session||session|
|Variable where the result will be saved||Variable|

### Add Text
  
Insert a new Text in Google Slides presentation with Rocketbot. This command is used for blank slides.
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Slide ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Text||Text to insert|
|Font size|Font size that the written text will have.|12|
|Align|Align that the written text will have.|Left|
|Text color|Color that the written text will have|Black|
|Bold|Select whether the text will be bold.|True|
|Italic|Select whether the text will be italic.|True|
|Underline|Select whether the text will be underlined.|False|
|Variable where the ID will be saved||Variable|
|Text Identifier||MyText1|
|Session||session|

### Insert Text
  
Insert text into an element already created on a specific slide of Google Slides.
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Slide ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Text||Text to insert|
|Font size|Font size that the written text will have.|12|
|Align|Align that the written text will have.|Left|
|Text color|Color that the written text will have|Black|
|Bold|Select whether the text will be bold.|True|
|Italic|Select whether the text will be italic.|True|
|Underline|Select whether the text will be underlined.|False|
|Variable where the ID will be saved||Variable|
|ID of the Element to which the Text will be inserted||MyBoxText|
|Session||session|

### Delete Text
  
Remove text from an element in a Google Slides presentation with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Slide ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|Element ID of the TextBox||MyText1|
|Variable where the ID will be saved||Variable|
|Session||session|

### Download Slides
  
Download a Google Slides presentation in PP or PDF format with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||1M1YsqIRAaQnjWcSYjinLiaChD_Jv_zcKohLMs0G_0sE|
|File format (Slides)||---- Select format ----|
|Path where to save file||C:\users\usuario\Downloads|
|Variable where the result will be saved||Variable|
|Session||session|

### Get Info
  
Gets the name of the presentation and the elements of the indicated slide
|Parameters|Description|example|
| --- | --- | --- |
|Presentation ID||14olZxHX8sQUzUg33h72b-uK32jxC1u3uwsKlw0gEgM0|
|Index of the slide to obtain||0|
|Session||session|
|Variable where the result will be saved||Variable|
