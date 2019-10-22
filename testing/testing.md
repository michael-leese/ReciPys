## Testing ##

This document outlines the test that were carried out in order to prove the functionality of the website.

1. Home Page(not logged in):
    * The website says Welcome and the Links are Home, Login, Register and ReciPys.
    * You can search using the search bar and on pressing search are directed to the        results page.
    * On pressing the Logo you are directed to same page.
    * You cannot view the full recipe on pressing the View Btn. You are directed to the     My ReciPys and asked to Regsiter or Login.
2. Home Page(logged in):
    * The webiste says welcome to (USERNAME) and the navbar is populated with Links to      Home, Logout, ReciPys, My ReciPys and Add ReciPy. 
    * You can search using the search bar and on pressing search are directed to the        results page.
    * On pressing the Logo you are directed to same page.
    * You can view the full recipe on pressing the View Btn.
    * On pressing Logout you are logged out and the page reverts to Home Page(not logged    in).
    * On pressing any of the links you are taken where expected.
3. Register:
    * If you do not enter information in the fields you are instructed to do so.
    * If you enter a username that already exists you are directed to the error page.
    * If you enter a password that does not meet the regex you are instructed to do so      and provided the criteria.
    * If you enter a password that does not match the confirm password you are instructed   to correct this.
    * When you click on register with valid information in the fields you are registered    and taken to the first time log in page.
4. Login:
    * If you do not fill out the fields you are instructed to do so.
    * If you enter a password that does not meet the criteria you are instructed.
    * If you enter a valid user name and password you are taken back to Home Page(logged    in).
    * If you enter an incorrect username/password you are directed to the error page.
5. Error:
    * The error page displays information relating to the page you were redirected from.
    * The Retry btn takes you back to the appropriate page last visited.
6. ReciPys:
    * Display a full list of all recipes added to the site.
7. My ReciPys(logged in):
    * This page shows only the recipes added by the user currently logged in.
8. My ReciPys(not logged in):
    * No recipes are displayed and you are asked to Regsiter or Login.
9. Add ReciPy:
    * If you do not fill out the fields you are instructed to do so.
    * If you populate the form with valid information you can add and are redirected to    My ReciPys to view your recipes.
10. ReciPy(logged in):
    * On pressing view you are taken to the full recipe page for the recipe selected.
    * If you are the creator of the recipe you have the option to Edit or Delete recipe.
11. ReciPy(not logged in):
    * You are directed to the My ReciPys and asked to Regsiter or Login.
12. Edit ReciPy:
    * You can make changes to the recipe that you have selected.
    * The form must be populated with valid information.
13. Delete ReciPy:
    * On pressing Delete you are directed to Delete Confirmation Page and asked to Delete   or Cancel.
14. Delete Confirmation:
    * On pressing Cancel you are redirected back to the recipe you were on.
    * On pressing Delete the recipe is Deleted and you are taken back to My ReciPys.
