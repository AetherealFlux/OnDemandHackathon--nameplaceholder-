# Habit building ToDo

## Outlines
- Project Description
- Installation and Setup Instructions
- Usage Guidelines
- OnDemand APIs Utilization
- Team Members and Roles

## Project Description

The project is a Todo app, with Habit cultivation.

### Todo:
#### Basic Functionality
  - Subtasks
  - Estimated Time
#### AI Power
  - Breakdown
    - Given a thing todo, the AI will break it into subtasks if needed.
  - Scheduling
    - The AI can give a schedule of these tasks based on estimated time and other requirements.
  - Rearrange
    - The AI will suggest a rearrangement due to unexpected events such as bad weather.
  - Assessment
    - A summary/feedback can be generated daily or after a task has been completed.

### Habits:
#### Basic Functionality
  - Set a habit
  - Make plan of habit
#### AI Power
  - Planning
    - Generete a plan for this habit, and convert it into daily todos

## Installation and Setup Instructions
  - Clone this repo
  - Set up backend
    - cd backend
      - Change Directory to backend
    - python manage.py makemigrations
      - Setup database
    - python manage.py migrate
      - Apply database
  - Set up frontend
    - cd frontend
      - Change Directory to frontend
    - npm run install
      - Install frontend dependencies

## Usage Guidelines
  - Start Backend
    - cd backend
    - python manage.py runserver
  - Start Frontend
    - cd frontend
    - npm run dev
  - Browser the page through browser

## OnDemand APIs Utilization
  - Chat-GPT API
  - 4 customised knowledge-based agents to give different instructions for generation of answers
  - Internet agent to give weather data help scheduling outdoor activities.
  - Different functionalities use different plugins to provide specified answers.



## Team Members and Roles
  - Sheng Dong
    - Bachend engineer
  - Ethan Li
    - Frontend engineer
  - Stephen Zhang
    - Prompt engineer
