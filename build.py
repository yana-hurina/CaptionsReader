import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',  # Main script file.
    '--onefile',  # Package the application into a single executable.
    '--windowed',  # Prevent the console from appearing.
    '--name=CaptionsReader',  # Name of the .exe file.
    '--icon=C:\\Users\\yanap\\PycharmProjects\\CaptRead\\myicon1.png',  # Path to the application's icon.
])
