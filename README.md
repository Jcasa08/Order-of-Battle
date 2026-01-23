# Order of Battle

The purpose of this project is to develop an 'army builder' webapp for the brand Order of Battle, it is designed to allow users to create army lists for their chosen faction as well as learn about the setting of the game.

A site user should be able to view lore and information about the world, factions and units of the game. If registered, users will also be able to create and manage army lists for their chosen faction(s).

In terms of design, I wanted to create a gritty feel to match the tone of the setting, without affecting readability of the site. The layout was designed to be intuitive and easy to navigate, with various call to actions to help the site user. 


## Desktop

### Homepage

![screenshot](readme-images/desktop-homepage.jpeg)

### Worldpage

![screenshot](readme-images/desktop-worldpage.jpeg)

### Listpage

![screenshot](readme-images/desktop-listpage.jpeg)

![screenshot](readme-images/desktop-newlist.jpeg)


### List Detail page

![screenshot](readme-images/desktop-listdetail.jpeg)

## Tablet

### Homepage

![screenshot](readme-images/ipad-homepage.jpeg)

### Worldpage

![screenshot](readme-images/ipad-worldpage.jpeg)


### Listpage

![screenshot](readme-images/ipad-listpage.jpeg)

![screenshot](readme-images/ipad-newlistpage.jpeg)

### List Detail page

![screenshot](readme-images/ipad-listdetail.jpeg)


## Mobile

### Homepage

![screenshot](readme-images/iphone-homepage.jpeg)

### Worldpage

![screenshot](readme-images/iphone-worldpage.jpeg)

### Listpage

![screenshot](readme-images/iphone-listpage.jpeg)

![screenshot](readme-images/iphone-newlist.jpeg)

### List Detail page

![screenshot](readme-images/iphone-listdetail.jpeg)

## UX 

### Typography

[**Font Awesome**](https://fontawesome.com/) icons were used across the site, namely for the social media icons

[**Cinzel**](https://fonts.google.com/specimen/Cinzel) was used for headers and primary text.

[**Roboto**](https://fonts.google.com/specimen/Roboto) was used for all other secondary text.

### Colour Scheme

![screenshot](readme-images/swatch.png)

A colour palette was picked to reflect the 'grim-dark' nature of the world. A charcoal background with a red navbar and footer, as well as using a gold for accents and ivory for text helped maintain reabability and keep elements visually separate.

## Wireframes

### Initial Design
My original wireframes for this project are listed below. They followed a similar style to other 'army builder' apps. However, early in development, I decided that I wanted to take a different approach. I went back to my wireframes and completely redid them but still kept some features.

![screenshot](readme-images/og-wireframe1.png)

![screenshot](readme-images/og-wireframe2.png)

![screenshot](readme-images/og-wireframe3.png)

![screenshot](readme-images/og-wireframe4.png)

As you can see the home, world and faction pages remained fairly similar, the list page was completely overhauled. My reasoning for this is due to the fact this project is still in early development, there is not yet all the information that other army builder app has. The change in layout helps keep the page clean and readable, with there being no blank or 'development' spaces that are waiting for content.

In the future, once the rules have been further fleshed out, the design of the website may change again to reflect the additional content.
  
### Home Page Wireframe

![screenshot](readme-images/homepage-wf.png)

### World Page Wireframe

![screenshot](readme-images/worldpage-wf.png)

### Factions Page Wireframe

![screenshot](readme-images/factions-wf.png)

### Factions Detail Wireframe

![screenshot](readme-images/factiondetail-wf.png)

### Army List Wireframe

![screenshot](readme-images/lists-wf.png)

### Army List Detailed View Wireframe

![screenshot](readme-images/lists-detail-wf.png)

## User Stories

>#### As a player, I want to create a new army list with a name and faction so that I can start building an army
>Acceptance Criteria:
> - Create button is prominently displayed on army lists page
> - Form includes required fields: list name and faction selection
> - Faction must be selected from available options
> - Form validates all inputs before submission
> - Point limit field is optional
> - Success message displays after creation
> - User is redirected to the new army list detail page
> - New list appears in user's army lists immediately

> #### As a player, I want to delete an army list I no longer need so that I can keep my account tidy
>Acceptance Criteria:
> - Delete button is available on list detail page and all lists page
> - Delete button is visually distinct (red/warning color)
> - Confirmation modal/dialog appears before deletion
> - Confirmation clearly states which list will be deleted
> - User can cancel deletion from confirmation dialog
> - Success message displays after deletion


> #### As a player, I want to view all my saved army lists so that I can choose which one to work on and have details regarding that army list
>Acceptance Criteria:
> - Page displays all army lists belonging to current user
> - Each list shows: name, faction, total points, validation status, last modified date
> - Lists are ordered by most recently modified first
> - Empty state message displays if user has no lists
> - Each list has buttons/links to: view details, edit, delete
> - Page is responsive and displays well on mobile devices
> - Lists display in card or table format with clear visual hierarchy
> - Page displays list name, faction, and total points prominently
> - All units in the list are displayed with: unit name, quantity, points per unit, subtotal
> - Overall point total is clearly displayed
> - Validation status is displayed (valid/invalid with reasons)
> - Empty state message displays if no units added yet
> - "Add Unit" button is prominently displayed
> - Each unit has edit and delete options
> - User can navigate back to all lists easily
> - Point breakdown is clear and easy to understand

> #### As a site user I want to be able to manage my army list so that I can add/delete units and alter my list at any time
>Acceptance Criteria:
> - "Add Unit" button prominently displayed on list detail page
> - Form displays only units from the list's selected faction
> - Quantity field is required
> - Quantity must be a positive integer
> - Success message displays after unit added
> - New unit appears in list immediately
> - Delete/remove button displayed next to each unit
> - Button is visually distinct (icon or red text/button)
> - Confirmation dialog appears before deletion
> - Confirmation shows unit name and quantity being removed
> - User can cancel removal
> - Success message displays after removal
> - Unit removed from list immediately
> - Cannot remove unit that doesn't exist (handled gracefully)
> - Current quantity is pre-populated
> - Success message displays after update
> - Change persists to database
> - Last modified timestamp updates

> #### As an admin, I want to add/edit/delete unit types to the system so that players have more options
>Acceptance Criteria:
> - Admin can access unit type creation form
> - Form includes: name, faction, base points, type/category, description
> - All required fields validated
> - Base points must be positive integer
> - Unit type must belong to a faction
> - Success message displays after creation
> - New unit immediately available for players
> - Duplicate names prevented within same faction
> - Admin can access unit type edit form from admin panel
> - All current values pre-populated
> - Same validation as creation
> - Changes save to database on submit
> - Success message confirms update
> - Updated values immediately reflected in player views
> - Edit history/audit log maintained
> - Existing army lists using this unit update automatically
> - Admin can delete unit types from admin panel
> - Confirmation required before deletion
> - Warning if unit type is used in existing army lists
> - Cannot delete if used in lists (or cascade delete with warning)
> - Success message after deletion
> - Deleted units removed from database

> #### As an admin, I want to add new factions so that players have more army choices
>Acceptance Criteria:
> - Admin can create new factions via admin panel
> - Faction requires: name, description (optional), image (optional)
> - Faction name must be unique
> - Success message displays after creation
> - New faction immediately available in army list creation
> - Validation prevents empty name
> - Faction can have no units initially (empty faction)

> #### As a site user I want to know the point cost for a unit so that I know if I have enough points to add it to my list
> Acceptance Criteria:
> - Base point cost displayed next to each unit in selection interface
> - Point cost clearly labeled (e.g., "150 pts")
> - Point cost displayed in army list view
> - Point cost is read-only (cannot be edited by users)
> - Format is consistent across application
> - Subtotal displayed for each unit entry in army list
> - Calculation formula is: base_points × quantity
> - Subtotal updates automatically when quantity changes
> - Subtotal clearly labeled (e.g., "450 pts total")
> - Format is consistent with other point displays
> - Calculation is accurate to avoid errors
> - Remaining points calculated as: limit - current total
> - Displayed prominently on list detail page
> - Updates automatically when units added/removed/changed
> - Set a point limit for list

> #### As a site user I want to know that my list is valid so that my list is legal for play
>Acceptance Criteria:
> - Validate point limit
> - Validate army rules
> - Validation status indicator
> - Messages indicating what is invalid
> - Clear validation error messages

> #### As a site user I want to be able to create an account so that I can create army lists on the site
>Acceptance Criteria:
> - Registration form includes username, email, password, and password confirmation fields
> - All fields are required and validated
> - Password must meet minimum security requirements (e.g., 8+ characters)
> - Password and password confirmation must match
> - Username must be unique (error displayed if taken)
> - Email must be valid format
> - Success message displays after successful registration
> - User is automatically logged in after registration
> - User is redirected to their army lists page after registration
> - Form displays clear error messages for invalid inputs
> - Guest users should be redirected to a login/signup page when trying to create list

> #### As a logged-in user, I want to see my username displayed so that I know I'm logged in and how to log out
>Acceptance Criteria:
> - Username is displayed in navigation bar when logged in
> - Login/Register links are hidden when user is logged in
> - Logout link is visible when user is logged in
> - Login/Register links are visible when user is logged out
> - Username display is visible on all pages
> - Logout option is visible when user is logged in
> - Clicking logout ends the user session
> - User is redirected to home/login page after logout
> - Success message displays confirming logout
> - User cannot access protected pages after logout without logging in again
> - Session data is cleared on logout

> #### As a user, I want my army lists to be private so that only I can view and edit them
>Acceptance Criteria:
> - Users can only view their own army lists
> - Users cannot access other users' army lists via URL manipulation
> - Attempting to access another user's list returns 403 Forbidden error
> - Army list queries are filtered by current user automatically

> #### As a site user I want know the stats of the units so that I can make decisions on which units I want in my army
>Acceptance Criteria:
> - All units have indiviual stats for: movement, attack, save etc
> - Admin can update/change the value for each stat

> #### As a site user I want know the rules of the game so that I know how to play
>Acceptance Criteria:
> - Rules for the game easily accessible on the site
> - All rules are clear and concise
> - Rules for units and factions are clearly defined

> #### As a site user I want information about the settting so that I can learn more about the game
>Acceptance Criteria:
> - detailed world page
> - detailed faction page


> #### As a site user I want the site to be fully responsive to different devices so that I have the same user experience across all device types.
>Acceptance Criteria:
> - site is fully responsive to different screen sizes


The MoSCoW approach was used to organise the 15 user stories into: 10 'Must Haves', 2 'Should Haves' and 3 'Could Haves'. The 3 'Could Haves' are still remaining in the backlog and would be prioritised in the next development cycle.

![screenshot](readme-images/agile.png)

## Features

- ### Homepage
   The homepage provides users with information about the site itself, as well as providing a call to action button to go straight to the list builder
![screenshot](readme-images/homepage-feature.png)

- ### World page
  The worldpage gives users an overview of the setting. Information is split up into paragraphs and an accordion to keep the page from being cluttered.
  ![screenshot](readme-images/world-feature1.png)
  ![screenshot](readme-images/world-feature2.png)

- ### Faction page
 The faction page provides users with 3 buttons that lead to the faction detail page
![screenshot](readme-images/factions.png)

- ### Faction Detail page
  The faction detail page provides the user with more information about each faction and their units. The information is pulled from the database and so dynamically updates when the admin adds additional units/factions. There is also a call to action at the bottom of the page that returns the user to the factions page.

  ![screenshot](readme-images/factions-detail1.png)
  ![screenshot](readme-images/factions-detail2.png)

- ### List Builder
  The list builder consists of multiple html pages working together, the user is first brought to a page where all their lists are displayed.
  ![screenshot](readme-images/listview-feature.png)

  They can then click the create list button to start a new list.
  ![screenshot](readme-images/create-list.png)

  Once filled in, the user will be redirected to a detailed list view where they can then add units to the list.
  ![screenshot](readme-images/listdetail.png)

  If a user wants to delete a list, the will have a confirmation screen.
  ![screenshot](readme-images/delete-confirm.png)

- ### Navigation
  The navbar was made using bootstrap
  ![screenshot](readme-images/navbar.png)
  and so is fully responsive
  ![screenshot](readme-images/navbar-mobile.png)

  - ### Accounts
  Users are able to register, login and logout of the site
  ![screenshot](readme-images/register-feature.png)
  ![screenshot](readme-images/login-feature.png)
  ![screeanshot](readme-images/logout-feature.png)

- ### Admin
The page has a functioning admin panel, courtesy of Django's built in panel. Here the admin can: add/edit/delete units and factions, review users and groups and review user army lists.

![screenshot](readme-images/admin-panel.png)

- ### Entity Relationship Diagram
The data structure for the project is as follows:
![screenshot](readme-images/erd.png)


## Testing

### Manual Testing

Manual Testing was carried out on the below browsers for compatibility:

#### Chrome

| Test | Expected Result | Actual Result |
| :---: | :---: |:---: |
|Click Home Link | Success | |
|Click World Link | Success | |
|Click Faction Link | Success | |
|Click Lists Link | Success | |
|Click Login Link | Success | |
|Click Logout Link | Success | |
|Click Register Link | Success | |
|Click Build a List button | Success | |
|Click Faction buttons | Success | |
|Click Back to Faction button | Success | |
|Open and close accordion | Success | |
|Redirect if not logged in and go to lists | Success | |
|Click individual list | Success | |
|Create, edit, delete list | Success | |
|Add, edit, delete unit from list | Success | |
|Click email link | Success | |
|Click GitHub link | Success | |
|Click LinkedIn link | Success | |
|Register new account | Success | |
|Access Admin interface | Success | |
|Open new page from social link | Success | |
|Responsivity | Success | |

#### Avast

| Test | Expected Result | Actual Result |
| :---: | :---: |:---: |
|Click Home Link | Success | |
|Click World Link | Success | |
|Click Faction Link | Success | |
|Click Lists Link | Success | |
|Click Login Link | Success | |
|Click Logout Link | Success | |
|Click Register Link | Success | |
|Click Build a List button | Success | |
|Click Faction buttons | Success | |
|Click Back to Faction button | Success | |
|Open and close accordion | Success | |
|Redirect if not logged in and go to lists | Success | |
|Click individual list | Success | |
|Create, edit, delete list | Success | |
|Add, edit, delete unit from list | Success | |
|Click email link | Success | |
|Click GitHub link | Success | |
|Click LinkedIn link | Success | |
|Register new account | Success | |
|Access Admin interface | Success | |
|Open new page from social link | Success | |
|Responsivity | Success | |

#### Edge

| Test | Expected Result | Actual Result |
| :---: | :---: |:---: |
|Click Home Link | Success | |
|Click World Link | Success | |
|Click Faction Link | Success | |
|Click Lists Link | Success | |
|Click Login Link | Success | |
|Click Logout Link | Success | |
|Click Register Link | Success | |
|Click Build a List button | Success | |
|Click Faction buttons | Success | |
|Click Back to Faction button | Success | |
|Open and close accordion | Success | |
|Redirect if not logged in and go to lists | Success | |
|Click individual list | Success | |
|Create, edit, delete list | Success | |
|Add, edit, delete unit from list | Success | |
|Click email link | Success | |
|Click GitHub link | Success | |
|Click LinkedIn link | Success | |
|Register new account | Success | |
|Access Admin interface | Success | |
|Open new page from social link | Success | |
|Responsivity | Success | |

#### Firefox

| Test | Expected Result | Actual Result |
| :---: | :---: |:---: |
|Click Home Link | Success | |
|Click World Link | Success | |
|Click Faction Link | Success | |
|Click Lists Link | Success | |
|Click Login Link | Success | |
|Click Logout Link | Success | |
|Click Register Link | Success | |
|Click Build a List button | Success | |
|Click Faction buttons | Success | |
|Click Back to Faction button | Success | |
|Open and close accordion | Success | |
|Redirect if not logged in and go to lists | Success | |
|Click individual list | Success | |
|Create, edit, delete list | Success | |
|Add, edit, delete unit from list | Success | |
|Click email link | Success | |
|Click GitHub link | Success | |
|Click LinkedIn link | Success | |
|Register new account | Success | |
|Access Admin interface | Success | |
|Open new page from social link | Success | |
|Responsivity | Success | |


### Lighthouse Test
All main pages was tested with Lighthouse and provided the following:

#### Homepage
The homepage initially received a score of:
![screenshot](readme-images/lh-home1.png)

After following the advice given by Lighthouse it scored:
![screenshot](readme-images/lh-home2.png)

#### World page
The homepage initially received a score of:
![screenshot](readme-images/lh-world1.png)

After following the advice given by Lighthouse it scored:
![screenshot](readme-images/lh-world2.png)

#### Factions page
![screenshot](readme-images/lh-faction.png)

#### Faction detail page
![screenshot](readme-images/lh-factions-detail.png)
The best practices score is due to using 3rd party cookies belonging to Cloudinary, which is unaviodable due to using Cloudinary to host images.

#### Lists Page
![screenshot](readme-images/lh-lists.png)

#### List Detail Page
![screenshot](readme-images/lh-lists-detail.png)

### Responsivity Tests
Chrome Developer Tools and Responsively used throught the development of this project to insure that the site remained consistent on a range of devices.

![screenshot](readme-images/responsively.png)

### Validators

#### HTML
The HTML validator was used to check all pages of the site, any errors that were present were fixed before final deployment:


#### CSS
No errors were found on the CSS validator:
![screenshot](readme-images/css-validator.png)

#### JavaScript

#### Python


## Deployment

## AI Usage

## Credits