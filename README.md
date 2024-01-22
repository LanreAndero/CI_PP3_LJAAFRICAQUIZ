# LJA Africa Quiz ! <img src="docs/africa.png" style="width: 40px;height:40px;">

**Developer: [Lanre James Andero]**

💻 [Visit live website](https://lja-africa-quiz-94254bc80955.herokuapp.com/)

![Mockup image](docs/home-screen.png)

![Responsive image](docs/amiresponsive.png)

[amiresponsive](https://ui.dev/amiresponsive?url=https://lja-africa-quiz-94254bc80955.herokuapp.com/)

## About

Welcome to the LJA Africa Quiz! Test your knowledge about Africa with this engaging and educational quiz game. Answer questions about geography, history, culture, and more to prove your expertise on the diverse continent.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Learn and have fun while testing knowledge about Africa.
- Engage in an interactive quiz game.
- Complete the quiz as many times as you which to achieve highest scores.

### Site Owner Goals

- Develop an educational and entertaining quiz platform.
- Provide a seamless and enjoyable user experience.
- Encourage users to explore and learn more about Africa.

## User Experience

### Target Audience

The quiz is suitable for anyone interested in testing and expanding their knowledge of Africa. Recommended for players aged 10 and above.

### User Requirements and Expectations

- Access to an easy-to-navigate quiz platform.
- Clear instructions on how to play the quiz.
- Immediate feedback on quiz performance.
- Engaging questions covering various aspects of Africa.

### User Manual

<details><summary>Click here to view instructions</summary>

#### Main Menu
Upon entering the quiz, users will encounter the main menu featuring the LJA Africa Quiz ASCII Art. The menu offers options:

1. ASCII-Generator
2. Start Quiz
3. Quit Quiz

<details><summary>Main Menu Options</summary>
<img src="docs/text-ascii-art.png">
<img src="docs/home-screen.png">
</details>

Players can type either yes or no option to navigate through the quiz.

#### Start Quiz
Upon selecting this option, players will be presented with quiz questions. They can input their numerical answers, and the quiz will provide instant feedback.

<details><summary>Star Quiz Option - Yes</summary>
<img src="docs/features/user-story-yes.png">
</details>

#### Completion Scores
Players can see their highest scores achieved at completion of the quiz.

<details><summary>Scores, Time and Message</summary>
<img src="docs/features/user-story-scores-time.png">
</details>

#### About the Quiz
Users can learn more about the purpose and features of the LJA Africa Quiz.

#### Quit game
With the quit quiz option, the user exits the program with Okay, maybe next time! message.

<details><summary>Quit Quiz Option - No</summary>
<img src="docs/features/user-story-no.png">
</details>

## User Stories

### Users

1. **As a quiz enthusiast, I want to challenge my knowledge about Africa.**
   - The quiz offers a diverse set of questions to test the player's understanding of the continent.

2. **As a learner, I want clear instructions on how to participate in the quiz.**
   - The user manual provides step-by-step guidance on navigating through the quiz.

3. **As a competitor, displaying the scores achieved at completion helps to know where I stand.**
   - The "Completion Scores and time spent" option allows players to see the scores achieved by them.

### Site Owner

1. **As the site owner, I want to create an engaging and educational quiz experience.**
   - The quiz is designed to be both entertaining and informative.

2. **As the site owner, I want to encourage repeat visits to the quiz platform.**
   - Providing a "Completion Scores" feature encourages users to return and improve their scores.

3. **As the site owner, I want to showcase the rich diversity of Africa through quiz questions.**
   - The quiz covers a range of topics to highlight the various aspects of the continent.

## Technologies Used

### Languages

- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Font Awesome](https://fontawesome.com/) - icons from Font Awesome were used in the footer below the program terminal
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [PEP8](https://extendsclass.com/python-tester.html/) was used to check my code against Python conventions
- [Heroku Platform](https://https://heroku.com/) was used to deploy the project into live environment

### Libraries

#### Python Libraries
- os - used to clear terminal
- random - used to alternate questions at start of the quiz
- time - used to displayed delayed messages in the terminal

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: I used this library to add color to the terminal and enhance user experience. I marked warning/error information with red color and other user feedback with blue, green and yellow.

[Back to Table Of Contents](#table-of-contents)

## Features

- Interactive quiz questions with multiple choice answers
- Completion scores and time display
- About the Quiz section for additional information

## Validation

User inputs are validated to ensure that they are appropriate for quiz participation. For example:
- Answers are checked for correctness.
- Inputs for menu options are validated.

<details><summary>Scores, Time and Message</summary>
<img src="docs/features/user-story-correct-answer.png">
<img src="docs/features/user-story-wrong-answer.png">
</details>

## Testing

### Manual Testing

Manual testing was conducted on various aspects of the quiz, including:

- **Quiz Navigation:**
  - Users can smoothly navigate through the main menu.
  - Selecting options leads to the intended sections (Start Quiz, Quit Quiz, Restart the Quiz with Run Program).

- **Quiz Gameplay:**
  - Players can input their numeric answers during the quiz.
  - Immediate feedback is provided for each question attempted.

- **Scores:**
  - The "Completion Scores" correctly displays the scores achieved by players.

- **About the Quiz:**
  - Users can access additional information about the quiz.

<details><summary>Scores, Time and Message</summary>
<img src="docs/testing/lighthouse-desktop.png">
<img src="docs/testing/lighthouse-mobile.png">
<img src="docs/testing/pep8-python-code-valdation.png">
</details>  

### Automated Testing

Automated testing was not implemented for this quiz.

## Bugs

- **User Input Validation:**
  - Validation checks for answers are effective, but additional testing may reveal edge cases that need attention.

- **Quiz Logic:**
  - While the core quiz logic is functional, further testing may be needed to identify and address potential issues.

## Deployment

The quiz is currently deployed on [Heroku]. Users can access it by visiting [https://lja-africa-quiz-94254bc80955.herokuapp.com/].

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

- Quiz content and design created by [Lanre James Andero].

### Code
- [ASCII Art Generator](https://ascii-generator.site/r/tTgmee/) was used to create quiz title - logo
- Code Institute - for git template IDE and "Love Sandwiches - Essentials Project" which helped me with my project.

## Acknowledgements

I would like to thank everyone who supported me in the development of this project:
- My mentor Mo for professional guidance, helpful feedback and words of encouragement whilst creating the project. Also, for encouraging me to learn about the unit test and including it within this project.
- My friends for their support and playing/testing the quiz with me
- Code Institute community on Slack for resources and support.

Happy quizzing! 🌍🇦🇷🤓

[Back to Table Of Contents](#table-of-contents)