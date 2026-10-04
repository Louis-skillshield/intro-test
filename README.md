# EFREI — Introduction aux tests avec pytest

Petit projet de démonstration utilisé en journée 2 pour découvrir pytest :
`assert`, organisation des tests et fixtures.

## Prérequis

* `uv` installé (il télécharge lui-même la bonne version de Python)

## Installation

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DOSSIER>
uv sync
```

## Lancer les tests

```bash
uv run pytest
```

Avec le détail de chaque test :

```bash
uv run pytest -v
```

## Contenu

```text
├── main.py                  # fonctions à tester
└── tests/
    ├── test_intro.py        # premiers tests avec assert
    ├── fixture_users.py     # une fixture : des données réutilisables
    └── test_users.py        # tests qui utilisent la fixture
```
