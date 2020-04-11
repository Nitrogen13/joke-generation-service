[![Build Status](https://travis-ci.com/Nitrogen13/joke-generation-service.svg?branch=master)](https://travis-ci.com/Nitrogen13/joke-generation-service)

# Anecdote Generation Service
*Anecdote (also known as joke) Generation Service, part of Practical Machine Learning and Deep Learning (PMLDL)
and Modern Application Production (MAP) course.*
*by Ilshat Gibadullin, Timur Valiev, Ilgizar Murzakov, Aidar Valeev*

## Roles:
Timur Valiev - Scram master, PM, Code Review

Ilshat Gibadullin - Python developer

Ilgizar Murzakov - Python developer

Aidar Valeev - Python developer

The goal of the project is to develop a anecdote generation model and frontend to use it 
(web interface or Telegram bot). The finished system will generate random anecdotes on request, 
or take beginning of an anecdote and complete it.

The project can potentially bring a lot of fun and joy into people's lives. 
Our motivation for this project is to improve our language modeling and text generation skills 
(and have fun while doing it).   


## Tech stack
* Python 
* TensorFlow/Keras for model development
* PyTest for testing
* Telegram API for bot deployment
* Travis CI for CI/CD (tests running and Telegram bot deployment)

## Tools
* GitHub for VC
* Github project boards for task management
* Tensorboard
* git-flow

## Datasets
* [anekdot.ru](https://www.anekdot.ru/)
* vk.com public pages ([example](https://vk.com/jumoreski))

## Task board organization
All tasks are managed using the [GitHub project board](https://github.com/Nitrogen13/joke-generation-service/projects/2).

#### Card types
There are 3 types of cards on the board:
1. **Task / Feature cards** - Major tasks related to the project. Tasks, that directly 
provide value to the end user are marked as Feature. Each *Task* has following structure:
    * Task/Feature tag
    * Task description
    * Tag name for related issues and pull requests
    * Priority (MoSCoW method)
    * Acceptance Criteria (AC)
1. **Issues** - issues are small tasks assigned to a developer. Each issues is marked with the tag of the *Task* that it 
belongs to, one issue can belong to more than one *Task*. Additionally, each issue is marked with the Milestone of the
sprint during which the work on this issue has started. New Issues automatically added to column *To do*.
1. **Pull requests** - pull requests are created when work on an issue is done. Pull requests are linked to the related 
issue, tagged with the tag of the related *Task*, and marked with the Milestone of the sprint. New pull requests are 
automatically added to column *Test*.

#### Columns 
* **Backlog** - List of *Tasks* to be implemented.
* **To do** - List of Issues to be implemented. New Issues are automatically added to this column 
* **Sprint backlog** - List of Issues and Tasks to be implemented during this sprint.
* **In progress** - List of Issues in work. Issues are assigned to a developer when moved to this column.
* **Test** - List of Pull requests and completed Issues that have to be reviewed.
* **Done** - List of completed and reviewed *Tasks*, Issues and Pull requests.

## Development process
Development process is organised into 2 week sprint cycle. At the beginning of each sprint, issues from *To do* column
are selected for development and moved to *Sprint backlog* column.

When developer takes an Issue, the developer is assigned to the Issue and the card is moved to the *In progress* column.
The developer works on the Issue in a feature branch (with `feature/*` naming) created from current `master` branch. 
Once the work is completed, the developer creates a pull request to the `master` branch. Tests are automatically run 
by Travis CI. Before the pull request is merged into master, the code is reviewed by the person assigned to do code 
reviews.
 
At the end of each sprint the board is reviewed, *Tasks* and Issues can be added, changed or removed.

## PMLaDL reports
* [D1.2-3 report](https://docs.google.com/document/d/1glTFTSRTlGs8IzuBljlIg9i5bvsGj1IOCFR_f2FSK1I/edit?usp=sharing)
* [D1.4 report](https://docs.google.com/document/d/1gU_4gnmQ1Fy-h28csdIIT_OutgjfCzKi_W-iu5qKVKs/edit?usp=sharing)