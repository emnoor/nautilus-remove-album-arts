# The MIT License (MIT)
#
# Copyright (c) 2014 Enam Mijbah Noor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from gi.repository import Nautilus, GObject
import eyed3
import eyed3.id3
from urllib2 import unquote

class RemoveAlbumArtsExtention(GObject.GObject, Nautilus.MenuProvider):

    def menu_active_cb(self, menu, files):
        for file in files:
            song = eyed3.load(unquote(file.get_uri().replace('file://', '', 1)))
            if song and song.tag and song.tag.frame_set[eyed3.id3.frames.IMAGE_FID]:
                del song.tag.frame_set[eyed3.id3.frames.IMAGE_FID]
                song.tag.save()

    def get_file_items(self, window, files):
        if len(files) < 1:
            return

        for file in files:
            if (file.is_directory()
                    or file.get_uri_scheme() != 'file'
                    or 'audio' not in file.get_mime_type()):
                return

        item = Nautilus.MenuItem(
                name='NautilusPython::removealbumarts',
                label='Remove Album Arts',
        )
        item.connect('activate', self.menu_active_cb, files)
        return item,
