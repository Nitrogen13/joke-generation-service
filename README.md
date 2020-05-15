[![Build Status](https://travis-ci.com/Nitrogen13/joke-generation-service.svg?branch=master)](https://travis-ci.com/Nitrogen13/joke-generation-service)

# Anecdote Generation Service
*Anecdote (also known as joke) Generation Service, part of Practical Machine Learning and Deep Learning (PMLDL)
and Modern Application Production (MAP) course.*
*by Ilshat Gibadullin, Timur Valiev, Ilgizar Murzakov, Aidar Valeev*

## Run
Make sure that you have [`nvidia-container-toolkit`](https://github.com/NVIDIA/nvidia-docker)  installed.

Run production version:
```bash
docker build -t jokes_generator . 
docker run --gpu all jokes_generator 
```

In order to successfully run `Joke Generation` bot, you should have 14GB free disc space and 3GB video memory.

If you want to use the anecdote generation model directly see the [model documentation](ruGPT2/README.md).


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
1. **Task / Feature cards** - Major tasks related to the project (User Stories). US that directly 
provide value to the end user are marked as Feature. US that do not provide value to the user directly are marked 
as Task (e.g. research tasks). Each US has following structure:
    * Task/Feature tag
    * US description
    * Tag name for related issues and pull requests
    * Priority (MoSCoW method)
    * Acceptance Criteria (AC)
1. **Issues** - issues are small tasks assigned to a developer. Each issues is marked with the tag of the US that it 
belongs to, one issue can belong to more than one US. Additionally, each issue is marked with the Milestone of the
sprint during which the work on this issue has started. New Issues automatically added to column *To do*.
1. **Pull requests** - pull requests are created when work on an issue is done. Pull requests are linked to the related 
issue, tagged with the tag of the related US, and marked with the Milestone of the sprint. New pull requests are 
automatically added to column US.

#### Columns 
* **Backlog** - List of US to be implemented.
* **To do** - List of Issues to be implemented. New Issues are automatically added to this column 
* **Sprint backlog** - List of Issues and Tasks to be implemented during this sprint.
* **In progress** - List of Issues in work. Issues are assigned to a developer when moved to this column.
* **Test** - List of Pull requests and completed Issues that have to be reviewed.
* **Done** - List of completed and reviewed US, Issues and Pull requests.

## Development process
Development process is organised into 2 week sprint cycle. At the beginning of each sprint, issues from *To do* column
are selected for development and moved to *Sprint backlog* column. At the end of each sprint the board is reviewed, 
US and Issues can be added, changed or removed.

When developer takes an Issue, the developer is assigned to the Issue and the card is moved to the *In progress* column.
The developer works on the Issue in a feature branch created from current `master` branch. The branch is named as 
`feature/*`, where `*` is the name of the issue. 
Once the work is completed, the developer creates a pull request to the `master` branch. Tests are automatically run 
by Travis CI. Before the pull request is merged into master, the code is reviewed by the person assigned to do code 
reviews.

Here is an example of how our gif-flow branching looks like:

![Git-flow example](https://sun9-54.userapi.com/c855424/v855424377/239981/L71RgGtdccY.jpg)


## CI details
Cl runs integration tests for the telegram bot. Tests are located at `tests`
folder. Testing performed to expose defects in the interfaces and in the
interactions between Joke Generation bot and Telegram.

We used `pook` library for mocking requests to Telegram and `pytest` for
test case writing. 

### Burndown charts  
Burndown charts for each sprint were generated by an external service and are available 
[here](http://radekstepan.com/burnchart/#!/Nitrogen13/joke-generation-service).

Burndown chart for the whole project:
![Project burndown chart](https://sun9-42.userapi.com/c855424/v855424447/22f1d7/XCMd3UnLb8U.jpg)


## PMLaDL reports (Added value)
* [D1.2-3 report](https://docs.google.com/document/d/1glTFTSRTlGs8IzuBljlIg9i5bvsGj1IOCFR_f2FSK1I/edit?usp=sharing)
* [D1.4 report](https://docs.google.com/document/d/1gU_4gnmQ1Fy-h28csdIIT_OutgjfCzKi_W-iu5qKVKs/edit?usp=sharing)
* [D1.5 report](https://docs.google.com/document/d/1KE6sYw9aejK9bPQYOA9aoucadcvU0rqfimxdLf6Zts0/edit?usp=sharing)

![Evaluation chart](https://docs.google.com/spreadsheets/d/e/2PACX-1vSHDLY6gFINy8nBgLJb81mLj9IkczivmAyML4zdw_dxAN6vNRxIOuSpkBkKgUA4ixQG_P8MFCwEXwbY/pubchart?oid=1788999918&amp;format=image)
