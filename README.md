# Générateur de noms aléatoires

Ce projet contient un générateur de noms aléatoires. Au format : `prefix-suffix` ou `adjectif-verbe-sujet-lieu`.

## Utilisation

```python
from gen import NameGenerator

generator = NameGenerator()

# Génère un nom aléatoire
print(generator.generate())

# Génère un nom aléatoire complexe
print(generator.generate_complex())

# Génère une liste de noms aléatoires
print(generator.generate_many(10))

# Génère une liste de noms aléatoires complexes
print(generator.generate_many_complex(10))
```

# Développement

## Installation

```bash
task install
```

## Tests

```bash
task test
```

## Lint

```bash
task lint
```
