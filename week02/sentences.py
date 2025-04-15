"""
This program generates sentences by randomly choosing a determiner, noun, verb, adjective, and prepostional phrases.
CREATIVITY REQUIREMENT:
The base requirements have been met, to exceed the requirements, I have added a function to get an adjective and include two prepostitional phrases instead of one.
"""

from random import choice

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = choice(words)
  return word
 
def get_noun(quantity):
    """
    Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
    Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else: 
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "men", "rabbits", "women"]
    # Choose a random noun
    noun = choice(nouns)
    return noun

def get_adjective():
    """
    Return a randomly chosen adjective.
    """
    adjectives = ["big", "small", "tall", "short", "fat", "skinny", "happy", "sad", "angry", "calm"]
    return choice(adjectives)

def get_verb(quantity, tense):
    if tense == "past":
        verbs = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    # Choose a random verb
    verb = choice(verbs)
    return verb

def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
  
  return choice(preposition)


def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or pluaral.
  Return: a prepositional phrase.
  """
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  phrase = f"{preposition} {determiner} {noun}"
  return phrase

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    preposition1 = get_prepositional_phrase(quantity)
    preposition2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {adjective} {noun} {preposition1} {verb} {preposition2}."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

main()


