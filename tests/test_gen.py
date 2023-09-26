from gen import *

def test_default_adjectives():
  assert len(DEFAULT_ADJECTIVES) == len(set(DEFAULT_ADJECTIVES))
  assert DEFAULT_ADJECTIVES == sorted(DEFAULT_ADJECTIVES)
  assert all([' ' not in adjective for adjective in DEFAULT_ADJECTIVES])

def test_default_verbs():
  assert len(DEFAULT_VERBS) == len(set(DEFAULT_VERBS))
  assert DEFAULT_VERBS == sorted(DEFAULT_VERBS)
  assert all([' ' not in verb for verb in DEFAULT_VERBS])

def test_default_objects():
  assert len(DEFAULT_OBJECTS) == len(set(DEFAULT_OBJECTS))
  assert DEFAULT_OBJECTS == sorted(DEFAULT_OBJECTS)
  assert all([' ' not in obj for obj in DEFAULT_OBJECTS])

def test_default_animals():
  assert len(DEFAULT_ANIMALS) == len(set(DEFAULT_ANIMALS))
  assert DEFAULT_ANIMALS == sorted(DEFAULT_ANIMALS)
  assert all([' ' not in animal for animal in DEFAULT_ANIMALS])

def test_default_places():
  assert len(DEFAULT_PLACES) == len(set(DEFAULT_PLACES))
  assert DEFAULT_PLACES == sorted(DEFAULT_PLACES)
  assert all([' ' not in place for place in DEFAULT_PLACES])

def test_generate():
  g = NameGenerator()

  # On génère un nom
  name = g.generate()
  
  assert isinstance(name, str)
  assert len(name) > 0
  assert len(name.split('-')) == 2

def test_generate_complex():
  g = NameGenerator()

  # On génère un nom complexe
  name = g.generate_complex()
  
  assert isinstance(name, str)
  assert len(name) > 0
  assert len(name.split('-')) == 4

def test_generate_many():
  g = NameGenerator()

  # On génère plusieurs noms
  names = g.generate_many(10)
  
  assert isinstance(names, set)
  assert len(names) == 10
  assert all([isinstance(name, str) for name in names])
  assert all([len(name) > 0 for name in names])
  assert all([len(name.split('-')) == 2 for name in names])

def test_generate_many_complex():
  g = NameGenerator()

  # On génère plusieurs noms complexes
  names = g.generate_many_complex(10)
  
  assert isinstance(names, set)
  assert len(names) == 10
  assert all([isinstance(name, str) for name in names])
  assert all([len(name) > 0 for name in names])
  assert all([len(name.split('-')) == 4 for name in names])
