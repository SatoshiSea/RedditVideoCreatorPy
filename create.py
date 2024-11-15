import os

def create_project_folders():
    
    folders = ["BackgroundVideos", "Screenshots", "Voiceovers", "OutputVideos"]
    

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' created.")
        else:
            print(f"Folder '{folder}' already exists.")


create_project_folders()
