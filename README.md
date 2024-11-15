# Reddit Video Generator Py

# Windows   
---
This program generates a .mp4 video automatically by querying the top post on the
r/askreddit subreddit, and grabbing several comments. The workflow of this program is:

:: Create a virtual environment in the specified path

```bash
python -m venv path\to\venv
```

:: Activate the virtual environment (on macOS/Linux)

```bash
path\to\venv\Scripts\activate
```

:: Install the library, which is used for audio manipulation and more

```bash
pip install -r requirements.txt
```

:: Run this script to create the necessary folders with

```bash
python create.py
```

:: Run the script with

```bash
python create.py
```

- Make a copy of config.example.ini and rename to config.ini
- Register with Reddit to create an application [here](https://www.reddit.com/prefs/apps/) and copy the credentials
- Use the credentials from the previous step to update config.ini (lines 22 -> 24)

Now, you can run `python main.py` to be prompted for which post to choose. Alternatively,
you can run `python main.py <reddit-post-id>` to create a video for a specific post.
