# macsound.py  16/02/2016  D.J.Whale
#
# Adaptor to make it possible to play wav files on mac

import os

def play(filename):
  os.system("afplay %s" % filename)


class mixer():
  class Sound():
    def __init__(self, filename):
      self.filename = filename

    def play(self):
      play(self.filename)

    def get_length(self):
      return 0 # TODO assumes play is blocking

  @staticmethod
  def init():
    pass



