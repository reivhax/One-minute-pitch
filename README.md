# One Minute Pitch
> A website that helps you speak to the world about your ideas

One to two paragraph statement about your product and what it does.
(Live Link)[http://minutepitch.herokuapp.com/]

![One minute pitch preview](http://i.imgur.com/Rcs0jJx.png)

[Live Link](http://minutepitch.herokuapp.com/)

## As users you can

* submit a pitch in any category.
* see the pitches other people have posted.
* favourite other people's posts
* vote on the pitch they liked by giving it a downvote or upvote.
* comment on the different pitches.
* view the different categories.

## Usage example

To create an account access the live link.

Click on register and fill in your details
on the form shown.

Now you can login with the new credentials.

On login, you can view posts from other users
You can like, comment and favourite them.

When, you favourite them, They are saved to your
favourites tab and you can access them quickly on login.

After posting a pitch or a comment, you can review them,
on then my account section. Here, you can delete your comments
or posts if your not satisfied by them.


## Development setup

To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/reivhax/One-minute-pitch
  ```
2. Move to the folder and install requirements
  ```bash
  cd One-minute-pitch
  pip install -r requirements.txt
  ```
3. Export Configurations to environment
  ```bash
  export SECRET_KEY='{Your Secret Key}'
  export DATABASE_URL='postgresql+psycopg2://{Your username}:{password}@localhost/{Your database name}'
  ```
4. Run the application
  ```bash
  python3.6 manage.py server
  ```
## Licensing
This Project is under the MIT License 2017
See more about this in the [License.md](https://github.com/reivhax/One-minute-pitch/blob/master/License.md) File
