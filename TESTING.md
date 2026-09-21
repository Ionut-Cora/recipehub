# Testing

## Manual Testing

| Feature | Test | Expected Result | Result | Screenshot |
|---|---|---|---|---|
| Homepage | Open homepage | Homepage loads and latest recipes are visible | pass | ![screenshot](documentation/images/testing-screenshots/chrome-desktop-home.png) |
| Navigation | Click each navigation link | Correct page opens | pass | ![screenshot](documentation/images/testing-screenshots/navigation.png) |
| Mobile Navigation | Open navbar on mobile | Collapsed menu opens correctly | pass | ![screenshot](documentation/images/testing-screenshots/mobile-navigation.png) |
| Recipe List | Open Recipes page | Published recipes are displayed | pass | ![screenshot](documentation/images/testing-screenshots/edge-desktop-browse-recipes.png) |
| Recipe Details | Open recipe | Full recipe information is displayed | pass | ![screenshot](documentation/images/testing-screenshots/recipe-details.png) |
| Search | Search valid recipe title | Matching recipe is displayed | pass | ![screenshot](documentation/images/testing-screenshots/search-valid-recipe.png) |
| Search | Search unknown term | No-results feedback is displayed | pass | ![screenshot](documentation/images/testing-screenshots/search-unknown.png) |
| Category Filter | Select category | Only matching recipes appear | pass | ![screenshot](documentation/images/testing-screenshots/category-filter.png) |
| Register | Submit valid registration | Account is created | pass | ![screenshot](documentation/images/testing-screenshots/valid-registration.png) |
| Register | Submit invalid registration | Validation feedback appears | pass | ![screenshot](documentation/images/testing-screenshots/invalid-registration.png) |
| Login | Enter valid credentials | User is authenticated | pass | ![screenshot](documentation/images/testing-screenshots/valid-registration.png) |
| Login | Enter invalid credentials | Error message appears | pass | ![screenshot](documentation/images/testing-screenshots/login-invalid-credentials.png) |
| Logout | Log out | Protected functionality becomes unavailable | pass | ![screenshot](documentation/images/testing-screenshots/logout.png) |
| Create Recipe | Submit valid recipe | Recipe is stored | pass | ![screenshot](documentation/images/testing-screenshots/submit-valid-recipe.png) |
| Create Recipe | Visit while logged out | Access is prevented/redirected | pass | ![screenshot](documentation/images/testing-screenshots/create-recipe-logout.png) |
| Edit Recipe | Author edits recipe | Changes are saved | pass | ![screenshot](documentation/images/testing-screenshots/edit-recipe.png) |
| Delete Recipe | Author confirms deletion | Recipe is deleted | pass | ![screenshot](documentation/images/testing-screenshots/recipe-delete-confirm.png) |
| Comment | Logged-in user comments | Comment is displayed | pass | ![screenshot](documentation/images/testing-screenshots/add-comment.png) |
| Comment | Logged-out visitor attempts comment | Action is unavailable | pass | ![screenshot](documentation/images/testing-screenshots/comment-logout.png) |
| Delete Comment | Comment author deletes comment | Comment is removed | pass | ![screenshot](documentation/images/testing-screenshots/comment-delete.png) |
| Rating | Submit rating | Rating is stored | pass | ![screenshot](documentation/images/testing-screenshots/rating-submit.png) |
| Average Rating | View rated recipe | Average rating is displayed | pass | ![screenshot](documentation/images/testing-screenshots/rating-average.png) |
| Dashboard | Logged-in user opens dashboard | Their recipes are displayed | pass | ![screenshot](documentation/images/testing-screenshots/dashboard.png) |
| Dashboard | Logged-out visitor opens dashboard | Access is prevented/redirected | pass | ![screenshot](documentation/images/testing-screenshots/create-recipe-logout.png) |
| Responsive Layout | Test mobile | No horizontal overflow | pass | ![screenshot](documentation/images/testing-screenshots/mobile-dashboard.png) |
| Responsive Layout | Test tablet | Layout adapts correctly | pass | ![screenshot](documentation/images/testing-screenshots/tablet-portrait-about.png) |
| Responsive Layout | Test desktop | Full layout displays correctly | pass | ![screenshot](documentation/images/testing-screenshots/mozzila-desktop-about.png) |

---

## User Story Testing

| User Story | Acceptance Criteria Met | Result | Screenshot |
|---|---|---|---|
| View RecipeHub homepage | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/chrome-desktop-home.png) |
| Browse published recipes | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/edge-desktop-browse-recipes.png) |
| View recipe details | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/recipe-details.png) |
| Register account | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/valid-registration.png) |
| Log in | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/valid-registration.png) |
| Log out | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/logout.png) |
| Create recipe | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/submit-valid-recipe.png) |
| Add ingredients and quantities | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/ingredients.png) |
| Edit recipe | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/edit-recipe.png) |
| Delete recipe | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/recipe-delete-confirm.png) |
| Upload recipe image | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/upload-image.png) |
| Search and filter | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/search-valid-recipe.png) |
| Comment on recipes | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/add-comment.png) |
| View dashboard | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/dashboard.png) |
| Rate recipe | Test all criteria | pass | ![screenshot](documentation/images/testing-screenshots/rating-submit.png) |

---

## Responsive Testing

| Device / Size | Area Tested | Expected Result | Result | Screenshot |
|---|---|---|---|---|
| Mobile phone | Dashboard | Responsive, no horizontal scrolling | pass | ![screenshot](documentation/images/testing-screenshots/mobile-dashboard.png) |
| Tablet portrait | About | Layout adapts correctly | pass | ![screenshot](documentation/images/testing-screenshots/tablet-portrait-about.png) |
| Tablet landscape | About | Layout adapts correctly | pass | ![screenshot](documentation/images/testing-screenshots/tablet-landscape-about.png) |
| Laptop | Browse Recipes | Correct desktop layout | pass | ![screenshot](documentation/images/testing-screenshots/laptop-browse-recipes-page2.png) |
| Large desktop | Home | Content remains readable and contained | pass | ![screenshot](documentation/images/testing-screenshots/large-desktop-monitor-home.png) |

---

## Cross-Browser Testing

| Browser | Device | Page | Result | Screenshot |
|---|---|---|---|---|
| Google Chrome | Desktop | Home | pass | ![screenshot](documentation/images/testing-screenshots/chrome-desktop-home.png) |
| Microsoft Edge | Desktop | Browse Recipes | pass | ![screenshot](documentation/images/testing-screenshots/edge-desktop-browse-recipes.png) |
| Mozilla Firefox | Desktop | About | pass | ![screenshot](documentation/images/testing-screenshots/mozzila-desktop-about.png) |
| Safari | iPhone | Home | pass | ![screenshot](documentation/images/testing-screenshots/safari-iphone-home.png) |
| Chrome | Android | Browse Recipes | pass | ![screenshot](documentation/images/testing-screenshots/chrome-android-browse-recipes.png) |

---

## Authentication and Authorisation Testing

| User Story | Result |
|---|---|
| Attempt to open the recipe creation page while logged out | pass |
| Attempt to open the dashboard while logged out | pass |
| Attempt to comment while logged out | pass |
| Attempt to rate a recipe while logged out | pass |
| Log in as User A and create a recipe | pass |
| Log out | pass |
| Log in as User B | pass |
| Manually enter User A's edit URL | pass |
| Confirm User B cannot edit the recipe | pass |
| Manually enter User A's delete URL | pass |
| Confirm User B cannot delete the recipe | pass |
| Confirm User A can still edit/delete their own recipe | pass |

---

# Checks and Validation

## Lighthouse

### Home

<img src="./documentation/images/lighthouse_screenshots/lighthouse-homepage.png" alt="Lighthouse homepage screenshot.">

### Browse Recipes

<img src="./documentation/images/lighthouse_screenshots/lighthouse-browse-recipes.png" alt="Lighthouse browse recipes page screenshot.">

### About

<img src="./documentation/images/lighthouse_screenshots/lighthouse-about.png" alt="Lighthouse about page screenshot.">

### Login

<img src="./documentation/images/lighthouse_screenshots/lighthouse-login.png" alt="Lighthouse login page screenshot.">

### Register/Signup

<img src="./documentation/images/lighthouse_screenshots/lighthouse-register.png" alt="Lighthouse register page screenshot.">

### Dashboard

<img src="./documentation/images/lighthouse_screenshots/lighthouse-dashboard.png" alt="Lighthouse dashboard page screenshot.">

### Create Recipe

<img src="./documentation/images/lighthouse_screenshots/lighthouse-create-recipe.png" alt="Lighthouse create recipe page screenshot.">

### Logout

<img src="./documentation/images/lighthouse_screenshots/lighthouse-logout.png" alt="Lighthouse logout page screenshot.">

---

## W3C Markup Validator

### Home

<img src="./documentation/images/w3c_markup_validator/html_home.png" alt="W3C Markup Validator homepage.">

### Browse Recipes

<img src="./documentation/images/w3c_markup_validator/html-browse-recipe.png" alt="W3C Markup Validator browse recipes page.">

### About

<img src="./documentation/images/w3c_markup_validator/html-about.png" alt="W3C Markup Validator about page.">

### Login

<img src="./documentation/images/w3c_markup_validator/html-login.png" alt="W3C Markup Validator login page.">

### Register/Signup

<img src="./documentation/images/w3c_markup_validator/html-signup.png" alt="W3C Markup Validator register/signup page.">

### Dashboard

<img src="./documentation/images/w3c_markup_validator/html-dashboard.png" alt="W3C Markup Validator dashboard page.">

### Create Recipe

<img src="./documentation/images/w3c_markup_validator/html-create-recipe.png" alt="W3C Markup Validator create recipe page.">

### Logout

<img src="./documentation/images/w3c_markup_validator/html-logout.png" alt="W3C Markup Validator logout page.">

---

## W3C CSS Validator

<img src="./documentation/images/w3c_css_validator/css-validator.png" alt="W3C CSS Validator screenshot.">

---

## WAVE web accessibility evaluation

### Home

<img src="./documentation/images/wave_screenshots/wave-homepage.png" alt="WAVE web accessibility evaluation homepage.">

### Browse Recipes

<img src="./documentation/images/wave_screenshots/wave-browse-recipes.png" alt="WAVE web accessibility evaluation browse recipes page.">

### About

<img src="./documentation/images/wave_screenshots/wave-about.png" alt="WAVE web accessibility evaluation about page.">

### Login

<img src="./documentation/images/wave_screenshots/wave-login.png" alt="WAVE web accessibility evaluation login page.">

---

## CI Python Linter PEP8

### recipehub/urls.py

<img src="./documentation/images/python-linter-screenshots/recipehub-urls.png" alt="recipehub/urls.py file validated using PEP8 CI Python Linter.">

### recipes/admin.py

<img src="./documentation/images/python-linter-screenshots/recipes-admin.png" alt="recipes/admin.py file validated using PEP8 CI Python Linter.">

### recipes/apps.py

<img src="./documentation/images/python-linter-screenshots/recipes-apps.png" alt="recipes/apps.py file validated using PEP8 CI Python Linter.">

### recipes/forms.py

<img src="./documentation/images/python-linter-screenshots/recipes-forms.png" alt="recipes/forms.py file validated using PEP8 CI Python Linter.">

### recipes/models.py

<img src="./documentation/images/python-linter-screenshots/recipes-models.png" alt="recipes/models.py file validated using PEP8 CI Python Linter.">

### recipes/urls.py

<img src="./documentation/images/python-linter-screenshots/recipes-urls.png" alt="recipes/urls.py file validated using PEP8 CI Python Linter.">

### recipes/views.py

<img src="./documentation/images/python-linter-screenshots/recipes-views.png" alt="recipes/views.py file validated using PEP8 CI Python Linter.">

---

## JSHint JavaScript Code Validation

<img src="./documentation/images/jshint/jshint-code-validation.png" alt="JSHint JavaScript Code Validation screenshot.">

---

# Bugs

| Bug | Cause | Fix | Status |
|---|---|---|---|
| Static CSS not updating | Old collected static file was being served | Rebuilt static files and confirmed correct source file | Fixed |
| Recipe image not displaying | Media/Cloudinary configuration required correction | Corrected image/media configuration | Fixed |

## Static Files During Deployment
A problem occurred during development where the published project was loading an older version of the project CSS file. The application loaded correctly, but any updated styling would not be visible.
Research was then done into the static-file configuration, and a rebuild of the static files was performed using WhiteNoise to load the current source CSS. This allowed a clear distinction to be made between source static files and the production-collected static files.

## Recipe Image Display
Recipe images were not loading correctly in development. The Cloudinary setup was fixed, and image and media settings were reviewed and updated to properly load and show recipe images.
