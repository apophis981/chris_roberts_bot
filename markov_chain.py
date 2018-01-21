#!/usr/bin/env python

import markovify

class markov:
  # Read text file, replace new lines with spaces, and save to variable
  with open ("chris_roberts.txt", "r") as myfile:
  	chris_text = myfile.read().replace('\n', ' ')

  # Build the model.
  text_model = markovify.Text(chris_text)
  # Make a message
  message =  text_model.make_sentence()


