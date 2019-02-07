# Cast Agency Web App 

A web application that manages models and companies for a casting agency with an admin panel. This project made for 
Software Engineering Course in ITU for using **Agile** methodologies in a **Software Development Process**. As an application
it built on **Python**,**Flask Framework** and **Sqlite** database. Also application has the capability of serving models as an **API** to companies which are signed up.

## Required Libraries For Venv 

1. You can download libraries by using 
   - pip install libraryName
   
2. Libraries
   - [Flask](http://flask.pocoo.org)
   - [Flask-Admin](http://flask.pocoo.org)
   - [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)
   - [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
   - [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
   - [Flask-Mail](https://flask-mail.readthedocs.io/en/latest/)
   - [Flask-RESTFul](https://flask-restful.readthedocs.io/en/latest/)
   - [Flask-Security](https://flask-security.readthedocs.io/en/latest/)
   - [Flask-SqlAlchemy](https://flask-sqlalchemy.readthedocs.io/en/latest/)
   - [Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/)
   
## How to Run The Website

1. Download The Project
2. Check The settings.py for mail configurations
3. Run server.py and your website is running in http://localhost:3000/
4. Create an Admin For Admin Panel Login 
5. Go to http://localhost:3000/admin/
6. Login to admin page and build your Agency 

**IMPORTANT**: *Note that you can find the following documentation in this reposit under [DevOps](DevOps/) directory*.

## Development Cycle In Agile Methodology

1. MEETING
   - Define The Requirements
   
2. DEFINE THE PROJECT
   - [Create The Project Charter](DevOps/projectCharter.pdf)
   
3. USER STORIES
   - [Define User Types](DevOps/chart.jpeg)
   - Define Epics
   - Define Non-functional Issues: Security, Performance ...
   - User stories must match with component size and they must be mapped to epics.
   - [A use case for each epic](DevOps/useCase.png)

4. EARLY SYSTEM MODELS
   - [Conceptual model](DevOps/dataFlow.png)
   - [Flow diagrams - One diagram for each use case , you can use a flowchart or business process model](DevOps/secondFlowChart.PNG)

5. FIRST SPRINT
   - [Mockups Unit Test related to User Stories](DevOps/mockups.bmpr)
   
6. MEETING
   - Make a customer meeting to show to development process and check requirements again.
   - Make some commits.
  
7. DATA MODEL
   - [Create ER diagrams for DB](DevOps/erDiagram.png)
   
8. SOFTWARE MODEL
   - [System Architecture](https://github.com/uysalemre/CastAgencyWebApp/blob/master/DevOps/System%20Architecture.png)
   - [Component Diagram](DevOps/componentDiagram.jpeg)
   - [Sequence Diagram](DevOps/communicationDiagram.PNG)
   
9. SECOND and THIRD SPRINT
   - Change Logs for First Sprint
   - [Mockups for Unit Tests](DevOps/unit%20test%20mockups/)
   
  
  
## Task List 
   - [x] Make a meeting and define the requirements
   - [x] Define the Project and Create Project Charter
   - [x] Create User Stories
   - [x] Create Conceptual Model
   - [x] First Sprint 
   - [x] Make a customer meeting and commit files for first version.
   - [x] Create Data Model and ER diagrams
   - [x] Create System Architecture
   - [x] Create Component Diagram
   - [x] Create Sequence Diagram
   - [x] Complete Second and Third Sprint
   - [x] Test Codes Completed 
   

## How to Deploy This Project ? (For example : Pythonanywhere)
   - Create an account from [HERE](https://pythonanywhere.com/)
   - Create a Flask application from WEB.
   - After that upload your files under FILES.
   - Now you need to configure your virtualenv for used packages.[Here is an explanation](https://help.pythonanywhere.com/pages/Virtualenvs/)
   - You can use your website now. 
   





 
