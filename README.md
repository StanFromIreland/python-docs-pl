Polskie tłumaczenie dokumentacji Pythona
========================================
![build](https://github.com/python/python-docs-pl/workflows/.github/workflows/update-and-build.yml/badge.svg)
![22.13% przełącznika języków](https://img.shields.io/badge/przełącznik_języków-22.13%25-0.svg)
![postęp tłumaczenia całości dokumentacji](https://img.shields.io/badge/dynamic/json.svg?label=całość&query=$.pl&url=http://gce.zhsj.me/python/newest)
![4 tłumaczy](https://img.shields.io/badge/tłumaczy-4-0.svg)

[Pomóż tłumaczyć](https://www.transifex.com/python-doc/python-newest/)
dokumentację Pythona na język polski.

**Znalazłeś błąd lub masz sugestię?**
* [Dodaj zgłoszenie](https://github.com/python/python-docs-pl/issues) w tym projekcie
* lub sam(a) nanieś poprawkę w projekcie
  [*Python document translation*](https://www.transifex.com/python-doc/python-newest/)
  na platformie Transifex.

**Jak obejrzeć build dokumentacji?**

Wejdź na [https://docs.python.org/pl/](https://docs.python.org/pl/)
lub pobierz zbudowaną dokumentację z listy artefaktów w ostatniej GitHub Action. 

**Dlaczego ta dokumentacja nie jest dostępna w przełączniku języków?**

Pojawi się w tam
[kiedy w pełni przetłumaczone będą zasoby](https://www.python.org/dev/peps/pep-0545/#add-translation-to-the-language-switcher):
* `bugs`,
* wszystkie z katalogu `tutorial`,
* `library/functions`.

**Kanały komunikacji**

* [Doc-SIG](https://www.python.org/community/sigs/current/doc-sig/),
* [Transifex Forum](https://www.transifex.com/python-doc/teams/5390/discussions/),
* Freenode #python.pl-doc.

**Aktualizacja tłumaczeń**
* `./manage_translation.py recreate_tx_config`
* `./manage_translation.py fetch`
* `./manage_translation.py recreate_readme`

**Potencjalnie przydatne materiały**
* [polskie tłumaczenie dokumentacji Pythona 2.3](https://pl.python.org/docs/).
