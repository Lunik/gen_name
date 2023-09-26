# Description: Générateur de noms aléatoires
# Version: 1.0.0
# Copyrigth: Lunik © 2023
# Authors: Lunik
# License: GPL-3.0

# Imports
import random

# Liste des adjectifs
DEFAULT_ADJECTIVES = [
  'amusing', 'ancient', 'angry', 'astute', 'attractive', 'beautiful', 'big', 'black',
  'blue', 'bright', 'brilliant', 'brisk', 'charming', 'cheerful', 'clever', 'comical',
  'contemporary', 'current', 'deformed', 'delicate', 'delighted', 'elegant', 'enraged',
  'exquisite', 'fast', 'fat', 'fleet', 'forceful', 'fresh', 'frightful', 'fuming', 'funny',
  'furious', 'glad', 'gorgeous', 'green', 'grey', 'grotesque', 'gruesome', 'handsome',
  'happy', 'hasty', 'hideous', 'hilarious', 'horrid', 'humorous', 'incensed', 'infuriated',
  'intelligent', 'irate', 'jocular', 'joking', 'jolly', 'jovial', 'joyful', 'keen', 'large',
  'livid', 'long', 'lovely', 'mad', 'merry', 'mighty', 'modern', 'monstrous', 'new',
  'nimble', 'old', 'orange', 'pink', 'pleased', 'potent', 'powerful', 'present', 'pretty',
  'purple', 'quick', 'rapid', 'recent', 'red', 'repulsive', 'robust', 'sad', 'sharp',
  'short', 'shrewd', 'skinny', 'slow', 'small', 'smart', 'solid', 'speedy', 'strong',
  'sturdy', 'swift', 'tall', 'thin', 'thrilled', 'tiny', 'ugly', 'unsightly', 'vigorous',
  'weak', 'white', 'wise', 'witty', 'wrathful', 'yellow', 'young'
]

# Liste des verbes
DEFAULT_VERBS = [
  'abhorring', 'abominating', 'aching', 'attending', 'believing', 'biting', 'caressing',
  'champing', 'chewing', 'climbing', 'clutching', 'comprehending', 'concentrating','coveting',
  'craving', 'crawling', 'deciphering', 'desiring', 'despising', 'detesting', 'devouring',
  'disliking', 'doubting', 'eavesdropping', 'feeling', 'flying', 'focusing', 'forgetting',
  'gaping', 'gazing', 'glancing', 'glaring', 'glimpsing', 'gnawing', 'gobbling', 'grabbing',
  'grasping', 'gripping', 'hating', 'having', 'hearing', 'holding', 'hoping', 'hungering',
  'imagining', 'inhaling', 'jumping', 'keeping', 'knowing', 'leaping', 'learning', 'licking',
  'liking', 'listening', 'longing', 'looking', 'loving', 'mumbling', 'muttering', 'needing',
  'nibbling', 'nipping', 'overhearing', 'owning', 'peering', 'possessing', 'realizing',
  'recognizing', 'remembering', 'rolling', 'rubbing', 'running', 'saying', 'scenting',
  'scorning', 'screaming', 'seeing', 'shouting', 'sliding', 'smelling', 'sniffing', 'snorting',
  'solving', 'speaking', 'staring', 'stroking', 'suspecting', 'swimming', 'talking', 'tasting',
  'telling', 'thinking', 'thirsting', 'touching', 'understanding', 'walking', 'wanting',
  'watching', 'whispering', 'wishing', 'wondering', 'yearning', 'yelling'
]

# Liste des objets
# Un objet est un nom commun (pas de verbe, pas d'adjectif)
# On veut seulement ne nom de l'objet, pas d'article
DEFAULT_OBJECTS = [
  'amulet', 'armchair', 'arrow', 'axe', 'bed', 'bench', 'bike', 'boat', 'book', 'bottle',
  'bowl', 'brush', 'bus', 'bush', 'cabinet', 'camera', 'car', 'ceiling', 'chair', 'comb',
  'computer', 'corridor', 'couch', 'cup', 'dagger', 'desk', 'document', 'door', 'elevator',
  'envelope', 'escalator', 'file', 'floor', 'flower', 'folder', 'fork', 'glass', 'grass',
  'jug', 'keyboard', 'knife', 'lance', 'letter', 'mirror', 'motorcycle', 'mouse', 'mug',
  'notebook', 'paper', 'pen', 'pencil', 'phone', 'plane', 'plate', 'potion', 'printer',
  'razor', 'ring', 'roof', 'scanner', 'screen', 'shampoo', 'shield', 'ship', 'soap', 'sofa',
  'spell', 'spoon', 'stair', 'stool', 'sword', 'table', 'tablet', 'television', 'toothbrush',
  'toothpaste', 'towel', 'train', 'tree', 'truck', 'van', 'wall', 'window'
]

# Liste des animaux
# Un animal est un nom commun (pas de verbe, pas d'adjectif)
# On veut seulement ne nom de l'animal, pas d'article
DEFAULT_ANIMALS = [
  'alligator', 'ant', 'baboon', 'bear', 'beaver', 'bee', 'beetle', 'bird', 'bobcat', 'cat',
  'cheetah', 'chicken', 'chimpanzee', 'chinchilla', 'chipmunk', 'cougar', 'cow', 'crocodile',
  'dog', 'dolphin', 'dragon', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'frog', 'gerbil',
  'giraffe', 'goat', 'goose', 'gorilla', 'hamster', 'hedgehog', 'hippopotamus',
  'hornet', 'horse', 'insect', 'jaguar', 'ladybug', 'leopard', 'lion', 'lizard', 'lynx', 'manatee',
  'monkey', 'mosquito', 'mouse', 'newt', 'orangutan', 'otter', 'panther', 'pig', 'porpoise',
  'puma', 'rabbit', 'rat', 'rhinoceros', 'salamander', 'scorpion', 'seal', 'shark', 'sheep',
  'snake', 'spider', 'squirrel', 'tiger', 'toad', 'tortoise', 'turkey', 'turtle', 'walrus',
  'wasp', 'whale', 'wolf', 'zebra'
]

# Liste des lieux
# Un lieu est un nom commun (pas de verbe, pas d'adjectif)
# On veut seulement ne nom du lieu, pas d'article
DEFAULT_PLACES = [
  'abbey', 'academy', 'airport', 'apartment', 'arena', 'avenue', 'bar', 'basilica', 'beach',
  'boulevard', 'bridge', 'cabin', 'cafe', 'castle', 'cathedral', 'cave', 'cemetery', 'chapel',
  'church', 'cinema', 'city', 'clinic', 'club', 'college', 'concert', 'continent', 'country',
  'county', 'desert', 'district', 'dungeon', 'earth', 'flat', 'forest', 'galaxy', 'garden',
  'hamlet', 'home', 'hospital', 'hostel', 'hotel', 'house', 'inn', 'island', 'jungle', 'lake',
  'land', 'library', 'mansion', 'monastery', 'mosque', 'mountain', 'museum', 'neighborhood',
  'ocean', 'palace', 'park', 'parking', 'pharmacy', 'plain', 'planet', 'province', 'pub',
  'restaurant', 'river', 'road', 'school', 'sea', 'shrine', 'square', 'stadium', 'state',
  'station', 'store', 'street', 'synagogue', 'temple', 'theater', 'town', 'tunnel', 'universe',
  'university', 'village', 'world'
]

class NameGenerator:
  '''
  Générateur de noms
  '''
  def __init__(
      self,
      verbs=DEFAULT_VERBS,
      adjectives=DEFAULT_ADJECTIVES,
      objects=DEFAULT_OBJECTS,
      animals=DEFAULT_ANIMALS,
      places=DEFAULT_PLACES
    ):
    '''
    Constructeur
    '''
    self.verbs = verbs
    self.adjectives = adjectives
    self.objects = objects
    self.animals = animals
    self.places = places

    self.prefixes = self.adjectives + self.verbs
    self.suffixes = self.objects + self.animals + self.places

  def generate(self):
    '''
    Génère un nom
    '''
    prefix = random.choice(self.prefixes)
    suffix = random.choice(self.suffixes)
    return f'{prefix}-{suffix}'

  def generate_many(self, count):
    '''
    Génère plusieurs noms
    Format : [prefix]-[suffix]
    '''

    prefixes = random.choices(self.prefixes, k=count)
    suffixes = random.choices(self.suffixes, k=count)

    names = {
      "-".join(args)
      for args in zip(prefixes, suffixes)
    }
    if len(names) < count:
      names = names.union(self.generate_many(count - len(names)))

    return names

  def generate_complex(self):
    '''
    Génère un nom complexe
    Format : [adjective]-[verb]-[object]-[place]
    '''
    adjective = random.choice(self.adjectives)
    verb = random.choice(self.verbs)
    subjet = random.choice(self.objects + self.animals)
    place = random.choice(self.places)

    return f'{adjective}-{verb}-{subjet}-{place}'

  def generate_many_complex(self, count):
    '''
    Génère plusieurs noms complexes
    Format : [adjective]-[verb]-[object]-[place]
    '''
    names = []

    adjectives = random.choices(self.adjectives, k=count)
    verbs = random.choices(self.verbs, k=count)
    subjects = random.choices(self.objects + self.animals, k=count)
    places = random.choices(self.places, k=count)

    names = {
      "-".join(args)
      for args in zip(adjectives, verbs, subjects, places)
    }
    if len(names) < count:
      names = names.union(self.generate_many_complex(count - len(names)))

    return names

def main_demo():
  '''
  Fonction utilisée pour la démonstration
  '''
  # On crée un générateur de noms
  generator = NameGenerator()

  # On génère 10 noms
  names = generator.generate_many(10)

  # On affiche les noms
  print('\nNoms générés :\n')
  for name in names:
    print('\t', name)


  # On génère 10 noms complexes
  names = generator.generate_many_complex(10)

  # On affiche les noms
  print('\nNoms complexes générés :\n')
  for name in names:
    print('\t', name)


def main_perf(count):
  '''
  Fonction utilisée pour le test de performance
  '''
  # On crée un générateur de noms
  generator = NameGenerator()

  # On génère plusieurs noms
  _ = generator.generate_many(count)
  _ = generator.generate_many_complex(count)

# Code
if __name__ == '__main__':
  import os

  if 'DEBUG' in os.environ:
    import cProfile
    import pstats
    import sys

    with cProfile.Profile() as pr:
      main_perf(count=int(sys.argv[1]))

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

  else:
    main_demo()
