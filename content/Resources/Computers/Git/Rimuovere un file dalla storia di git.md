---
tags:
  - Git
---
Può capitare di dover eliminare un file dalla storia di una repository git, i motivi possono essere:

* il file è grande e appesantisce la repo;
* il file doveva essere in `.gitignore`;
* il file ha un path non compatibile con Windows (per esempio contiene delle barre / insieme a barre `\`);
* il file contiene delle credenziali riservate;
* ...

Per risolvere è necessario utilizzare questo comando:

```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch PATH-OF-THE-FILE' --prune-empty --tag-name-filter cat -- --all
```

Una volta che lo stato della repository è ok è necessario il push forzato, dato che con questo comando ho riscritto la storia e conseguentemente il locale e il remote non sono più compatibili.

```bash
git push origin --force --all
```