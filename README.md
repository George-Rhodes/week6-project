# week6-project of an exercise routine 
### Usefull links
- [Trello Board](https://trello.com/b/Isjf9yth/qa-project)
- [website](http://35.246.99.81:5000/)
## contents

















## Brief

### Requirements

The minimum viable product(MVP) was to create an application that uses CRUD (Create, Read, Update, Delete) functions and using tools and methodologies learned during training so far.
* Using a kanban style board tech such as trello board that has user stories use cases and tasks needed to complete the project, including a detailed risk assesment.
* A relational database with at least 2 tables and one relation to store data for the project.
* A function CRUD application using python and flask while following best practices and designs.
* A functioning front-end website and integrated API's, using Flask
* Fully designed test suites for the application, as well as automated tests for validation of the application. Providing high test coverage in the backend and provide consistent reports and evidence to support a TDD approach.

### my approach
To fulfill these requirements i decided to make an aplication made for everyone, from gym sharks, to people who just want to lose weight which allows them to:

* Create a routine that stores:
  * A title for their routine.
  * Author.
  * Description.
* Create an exercise taht stores:
  * the exercise name.
  * the type of resistance such as Kilos and reesistance level.
  * store how long/many they shoudl do.
* View and update both routines and exercises. 
* delete exercises indervidually or all in one got when the perant routine is delted. 



### Stretch goal
* Implement log ins and accounts so only the person who created them can delete.
* Allow comments for other users to comment on routines that have been posted.
* split cardio and strength into their seportate tables.

## Architecture


### Database
This is the Entity Relationship Diagram (ERD). this is the current structure of the data base for teh the current build of teh application, it is a one to many relation shipe and stores all required information.

![Imgur](https://i.imgur.com/tO9B8Cs.png)

### CI Pipeline
The image below represents my continuous integration pipeline with the associated frameworks and services related to them. It is a breakdown of the services and tools used to develop and deploy a well-tested, functioning program. The services I have chosen within the pipeline provide the most efficient method of rapid development to be automated and tested.

![Imgur](https://i.imgur.com/WhYD2i2.png)



## Project Tracking
using teh methodologies i have learnt and also using my own experince i decide to use Trello as my kanban board to visually show and track my progress of my project and sho show my workflow in completion of the current build of the application. below is a screen shot of my Trello board.

![Imgur](https://i.imgur.com/k619atK.png) ![Imgur](https://i.imgur.com/XuSQSVZ.png)

## Risk Assessment
Below is a screen shot of my risk assessment outlining potential risks giving them an impact value and detailing a proposed response to them.

![Imgur](https://i.imgur.com/jbyrM4M.png)

## Testing
Testing was done by using Pytest for unit testing in which i test tested most of my functions acheiveing an 80% as shown below the parts that was missed was updataing routines and Exercises though when doing practical tests these passed.
![Imgur](https://i.imgur.com/ldkKVAv.png)

i also carried out intergration testing and this passed sucesffully scoring 100%, though i dont have a screen shot at this current moment.

## Front-End Design
my front end design of my application is very basic and minimal but fully satisfys the CRUD functionality making it a working prototype meeting the MVP requirements.
below is a screen shot of the index page
![Imgur](https://i.imgur.com/UJ9rujk.png)
 below is the current state of adding a routine, and lookes very similar to updating a routine, it gives teh option of allowing teh user to view the whole description in teh text box.
![Imgur](https://i.imgur.com/4o9QhIc.png)
Below is an empty routine with no exercises stored inside.
![Imgur](https://i.imgur.com/LnnYu4g.png)
below is adding a singular exercise to the routine, alo update looks very similer to this.
![Imgur](https://i.imgur.com/DLfEvYH.png)
below is a populated Routine with a list exercises stored inside.
![Imgur](https://i.imgur.com/3EpOTis.png)

## Current evaluation

How i see teh current application is it is very basic using the core functions of CRUD, though this may be sucessefull in fulfilling the MVP requirments, there is much that could be improved upon. for isnatcne not allowing everyone to eddit any routine they line and having cardipn and strength training combined into one table.


## Future improvements
For the nect itiratiopn of this app here are teh proposed improvemnt:
* log in system, that only allows you to eddit teh routines associated with that account.
* split teh excersises into 2 different tables for cardio and strength.
* add a filter for intensities.
* allow users to search for other users routines using a search bar.
* allow commenting / notifications for users to interact with one and other.

## Author
George Rhodes
