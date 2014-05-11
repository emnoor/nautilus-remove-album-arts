This nautilus extension provides an context menu for removing album arts from
audio files (bassically mp3 with ID3 tags). Simply select the file(s) you want
to remove album arts from, right click and select "Remove Album Arts". Album
arts will be gone.

Installation:
-------------
nautilus-remove-album-arts only depends on `python-nautilus` and `eyed3`.
On ubuntu run:

    sudo apt-get install python-nautilus python-eyed3

    mkdir -p ~/.local/share/nautilus-python/extensions

    wget -O - "https://raw.githubusercontent.com/emnoor/nautilus-remove-album-arts/master/nautilus-remove-album-arts.py" > ~/.local/share/nautilus-python/extensions/nautilus-remove-album-arts.py

Then kill the running nautilus process to load the extension:

    killall nautilus

Start nautilus from Dash.
