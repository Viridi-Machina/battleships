# BATTLESHIPS
![image](https://github.com/Viridi-Machina/battleships/assets/146846939/b05960af-ba25-475e-a6e6-46e95b1d656d)

![image](https://github.com/Viridi-Machina/battleships/assets/146846939/098f8c7a-847c-494e-be9b-0d7110c2c262)

## Author
Jacen Green

## Visit the repository [here](https://github.com/Viridi-Machina/battleships) or view on a live terminal [here](https://battleships-v-a3fa1471e145.herokuapp.com/)

## Summary
*BATTLESHIPS* is a based on the original pen-and-paper classic and inspired by the interactive board game still played and loved to this day.

The player is simultaneously shown two grids; one displaying their ship locations and another for the computer opponent.<br>
Both boards update with hits, misses and fully-sunken ships as the game progresses. 

The computer shouldn't be fooled for an easy opponent however, as it's aiming algorithm simulates realistic and tactical firing like a human would. 
The player and computer take turns firing until all ships on a grid have been sunk.

The player's ships are displayed on the grid with a :large_blue_circle:, whilst enemy ships once fully destroyed display as a :red_circle:.
*Visual and colourful* feedback is also given as fiery explosions for hits, with misses displaying as a white 'X' as to not overstimulate the grid with too much colour.

Below is a demonstration of the game in action through to completion. Note that as battleships can be a long game this process has been sped up:

https://github.com/Viridi-Machina/battleships/assets/146846939/c557dd08-c389-4faf-b16f-7a5896c3f6c5

<hr>

## How to play
- Go to the deployed terminal [here](https://battleships-v-a3fa1471e145.herokuapp.com/) via Heroku.
- Click 'Run Program' and the terminal will open in a virtual environment using the Code Institute template.
- Enter a username.
- Select your first target using the grid letters and numbers, e.g. 'B5'.<br>
  A function will convert the guess into a usable integer.
- Playing against the computer, take turns guessing grid locations until all ships on either board have been sunk.
- Complete the game and you will be asked if you want to play again.

<hr>

## Technologies used
- Python3
- Markdown
- Github
- Heroku
- Python packages:
  - math
  - time
  - art (large print-fonts)
  - colorama (colour-print)
  - random (randrange)

<hr>

## :green_circle: Features
### Game welcome screen
<details>
 <summary>Details :green_circle:</summary>
 
![image](https://github.com/Viridi-Machina/battleships/assets/146846939/56703510-b6a6-4669-be39-60c75f3b1060)

Using a combination of the 'colorama' and 'art' packages, as well as block strings, a colourful and bold welcome screen was produced.<br>
It was designed to be as engaging as possible given the limitations of the terminal environment.
</details>

### Instructions
<details>
 <summary>Details :green_circle:</summary>
 
![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d1cf4c30-b5f1-4a7b-a6b5-819bb44a2012)

Using 'colorama', a simple instructions screen teaches the player how to play within the terminal.
</details>

### The game board
<details>
 <summary>Details :green_circle:</summary>
 
![image](https://github.com/Viridi-Machina/battleships/assets/146846939/b2d12a77-f295-486e-9647-bd29c3da5062)

The heart of the game. Perhaps the most time-consuming aspect of the game to complete.<br>
- The `display_grid()` function simultaneously creates two grids adjacent to one another.

- On every line that is printed, each grid element is assigned a grid value 11-110.<br>
  11-110 because each axis starts at 1, including the letter A.

- Each grid element is then checked against variables defined in and imported from another<br>
  Python file called `stats.py`. This effectively acts as a class for the player and<br>
  computer's respective ship co-ordinates, hits, misses etc.

- Every grid element is then assigned a unicode symbol depending on whether it is recorded<br>
  as a hit, miss or if a ship has been completely destroyed.

- The decorative elements - border and axes - are construced around the grid using another<br>
  imported file called `grid.py`, which acts as the library for all grid elements and<br>
  colour-changing variables.

 <details>
  <summary>display_grid() :mag:</summary>

  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/33cfc449-46b1-4918-a284-701c2cf15cda)
 </details>

 <details>
  <summary>stats.py :mag:</summary>

  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/e8e668f2-bf9f-43ae-93a9-18d50437cdf3)
 </details>

 <details>
  <summary>grid.py :mag:</summary>

  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/5a0070fe-63b0-4fa8-b813-bb26751e25fa)
 </details>
</details>

### Smart computer logic
<details>
  <summary>Details :green_circle:</summary>

https://github.com/Viridi-Machina/battleships/assets/146846939/1f6d3838-cd70-4ec8-848c-135564750004

In the video clip above, take note of how the computer makes decisions. 
- Upon landing a hit, it will think of surrounding spaces that could result in a hit.
- At random, one of those guesses will be chosen. If it misses, it tries again.
- Upon another hit, the computer will work out the direction the ship is facing.
- It will keep firing until the ship is destroyed, then guess again at random.

*Special case*
- In the event that two player-ships are adjacent to one another, a ship may be<br>
  destroyed, the computer's aiming logic is reset and there may still be multiple<br>
  hits on the board.
- The computer will use the hit information to continue making educated guesses.

</details>

### End-Game
<details>
  <summary>Details :green_circle:</summary>

  
</details>

<hr>

## :purple_circle: Deployment

When deploying to Heroku, there are some essential steps that must be taken to ensure functionality of the deployed site:

### Add dependancies to `requirements.txt`:
<details>
 <summary>Method :purple_circle:</summary>

- If any packages have been installed and used within a given project, then these need to be catalogued in a requirements.txt file.<br>
This can be done by entering the following command in the workspace terminal:

      pip3 freeze > requirements.txt
  If you are using VS Code you can the following command instead:

      py -m pip freeze > requirements.txt 
  Please note however that this method will pull all current dependancies in your project, *as well* as their respective dependancies as well.<br>
  It may be more ideal to manually populate your requirements.txt file as you have greater control such as version control.

  Commit these changes and push them to your Github repository.
</details>

### Create Heroku account:
<details>
 <summary>Method :purple_circle:</summary>

- First, you will need to visit the Heroku site and log in. If you do not have an account yet then click `Sign Up` and follow their instructions.

      https://id.heroku.com/login
    <details>
     <summary>Login Screen :mag:</summary>
 
  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/c9a0efb3-f071-411e-9eea-144d391bea06)
    </details>
    
- When logging in, as an added security measure you will need to use an authenticator app in tandem with the site so that you can proceed<br>
  to the dashboard. You will need to make sure you download the `Salesforce Authenticator` app from you respective mobile marketplace.

    <details>
     <summary>Authentication Screen :mag:</summary>
 
  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/5b99b35a-9bd6-434c-9caf-43a2620f7c70)
    </details>

- Finally you will arrive at the `Heroku Dashboard` where you will be able to deploy your app.
</details>

### Create new app:
<details>
 <summary>Method :purple_circle:</summary>

- From the dashboard you will be able to see your deployed projects. Click on `New`, then `Create new app`:
  <details>
    <summary>Dashboard :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d4468782-45f9-4c26-8369-1ddffee2b408)
  </details>

- Enter a unique `App name` and `Choose a region`, then click `Create app`.<br>
  Once created you navigate to the `Settings` menu.
  <details>
    <summary>App Dashboard :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/fde9249a-f073-46af-aeff-ddf4b7d6aacf)
  </details>
  
- Within the `Settings` menu, navigate to `Config Vars` (Also known as *Environment Variables*).<br>
  This is where private and sensitive data, such as credentials and keys, will be stored for the project.
  <details>
    <summary>App Settings :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/078e131f-0ec6-483f-9031-7049385cdad8)
  </details>

- If the project is dependant on a creds.json file, then this is where the data will be stored.
- Click `Reveal Config Vars`. Type in the first `KEY`: 'CREDS'.<br>
  For the `VALUE` paste in the contents of your creds.json file from the IDE that you are using.
- It is also important to set another KEY, VALUE pair as `PORT`, `8000` respectively<br>
  or the project may not properly deploy.
  <details>
    <summary>Config Vars :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/0721287b-f32f-4b37-be16-ddcf1cfeb1c2)
  </details>

- Next, some `Buildpacks` will need to be added which will add further dependancies outisde of the project<br>
  which will allow the deployment to run in a virtual environment.
- First, click `Add buildpack` and select `python`. Then add `nodejs`. It is important that you do it in this order.<br>
  The ordering however can be changed afterwords by dragging their burger icons within the buildpacks list.
  <details>
    <summary>Buildpacks :mag:</summary>
 
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d7a30ca4-e36a-44eb-8e87-5626e84e7e25)
  </details>
</details>

### Connect to GitHub and deploy:
<details>
  <summary>Method :purple_circle:</summary>

  - Navigate to the `Deploy` menu. For `Deployment method` select GitHub. Finally, you can manually deploy the project.
    <details>
      <summary>Deploy Menu :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/9081df0b-d551-40f2-b9c1-f770b9d4a5fb)
    </details>
</details>
