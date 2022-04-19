# DC-Movies App

### Author

Mohammed Azim

#### Video Presentation

https://drive.google.com/file/d/1WfJiPwNrMzjmYSYfupsRJMzl6aL97Z9T/view?usp=sharing

#### Notes

This is my documentation in the form of a READ.md for my project as part of QA Ltd MarEnable22 training team. The project is part of the DevOps pathway.

## Contents

* [App Description](#app-descripton)
* [Brief](#brief)
  * [Project requirements](#project-requirements)
  * [My Approach](#my-approach)
* [Architecture](#architecture)
  * [Database Structure](#database-structure)
  * [Front-end Structure](#front-end-structure)
  * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
  * [Risk Assessment](#risk-assessment)
* [Testing](#testing)
*[Future improvements](#possible-improvements)

## App Description

This CRUD applicaiton is for users to view a DC movies database with each movie showing its release date accompanied with their critics score. The app will also allow the user to add their own review of any movie along with the option to edit or delete thereafter.

## Brief

The creation of a CRUD application using the skills and tools taught by our respective trainers; Ryan, Victoria, Harry and Luke. The acronym CRUD stand for Create, Read, Update, Delete.

### Project Requirements

* A Trello board with full expansion on user stories. This can also provide also provide a record of any issue/issues or risks that was faced during the creation of the project.

* A relational database used to store data for the project, this database needs to have minimum at least 2 tables in it. Also be required to model a relationship to demestrate understanding.

* Clear Documentation from a design phase describing the architecture used for the CRUD app project as well as a detailed Risk Assessment.

* A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board.

* Fully designed test suites for the application as well as a automated test for validation of the application. Must be able to provide high test coverage for the backend and provide consistent reports and evidence to support a TDD approach.

* A functioning front-end website and integrated API's, using Flask.

* Code must fully integrated into a VCS (Version Control System) using the Feature-Branch model which will then be built through a CI server and deployed to a cloud-based virtual machine.

### My Approach

My project follows the requirements listed above and the design of app is a follows:

* Implement a read functionality DC movie database showing list of 14 DC movies.

* Have a create functionality for user so that they can  add review for any movie in the database.

* Implement a update functionality so that the user can change their review for the movie.

* Implement a delete functionality so that the user is able to delete a review they no longer hold of the movie.

## Architecture

### Database Structure

#### ERD - Entity Realtionship Diagram

![DC-Movie-ERD](./crud_app/Images/DC%20Movies%20CRUD%20App.png)

Above is my ERD this highlights the base structure of my CRUD application. It shows that it is a one to many realtionship app with each movie within the database having multiple reviews.

### Front-end Structure

homepage:

![DC-Movie-app-homepage](./crud_app/Images/App%20front%20end%201.png)

![DC-Movie-app-homepage](./crud_app/Images/App%20front%20end%202.png)

This is the homepage for my CRUD application. The database shows 14 DC movies each with their critics score and release year. Each movie also has a add and view review button so that a user can apply their own respective critique of any movie they choose.

![DC-Movie-app-add-review](./crud_app/Images/front%20end%20Add%20review.png)

![DC-Movie-app-add-review-2](./crud_app/Images/front%20end%20add%20review%202.png)

When Pressing the add review button you will be taken to this page where the user will be directed to fill in their first and last names along with their own critic score and review of the film.

![DC-Movie-app-view-review](./crud_app/Images/view%20review.png)

This is the view review page where the user can see the implentation of their review for the movie of their choice. On this page the add and view review buttons and replaced with edit and delete buttons

![DC-Movie-app-edit-review](./crud_app/Images/edit%20review.png)

If the user chooses to they can edit the review the functions edits change in the original review and not create a second review from the same user.

![DC-Movie-app-delete-review](./crud_app/Images/delete%20review.png)

As shown once the delte button pressed clicking on view reviews will show nothing as the review is now gone

### CI Pipeline

![CI-Pipeline](./crud_app/Images/CI%20Pipeline.png)

The CI pipeline above lists all associated frameworks of the project used and shows rapid development to development as it automates the integration process and push to github with minimal effort. This procress is handled by Jenkins via a webhook. Testing is the main focus of the automation process. Any code pushed to GitHub will then automatically be pushed to Jenkins.

## Project Tracking

### Trello Board

![DC-Movie-Trello](./crud_app/Images/DC%20Movie%20trello%20board.png)

Link to trello board: <https://trello.com/b/uV5mmSkY/dc-movie-app-board>

I created this trello board to record my app progression and efficiently work through towards my end goal for the CRUD app. I created user stories which for each process this allowed maximum progression in each step of the app stage.

### Risk Assessment

![DC_movie-Risk-assessment](./crud_app/Images/Risk%20assessment.png)

Above is my risk assessment detailing possible issues that can occur with the application pre and post completion.

## Testing

This is my Jenkins automatic testing for my CRUD application:

![Console-output](./crud_app/Images/Console%20output.png)

Above is the jenkins console ouput which shows the tests ran my CRUD app

![Coverge-report](./crud_app/Images/Coverage%20report.png)

Above is the kenkins coverge report which shows the overall testing percentage my app recieved based on the unit testing ran.

## Future Improvements

* Main improvement I would like to make for this CRUD app is the aesthetics of the html broswer. It is very basic and raw and improveing the aesthics and making it more presentable will go a long way in increasing visters.

* Making a registration page where users can register and have their own accountm so that they can keep track of their own activeies and refer back to their reviews if they ever want to edit or delete them.

* Adding a comments section under a users reviews so that other users can offer their opinion on the users own review
