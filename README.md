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
