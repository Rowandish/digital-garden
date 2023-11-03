---
tags:
  - Coding
  - CSharp
  - Multithreading
  - PublishedPosts
---


Questo post è un seguito al mio precedente post sul [[blocking e spinning]] e vuole essere un piccolo approfondimento sulle nuove struct SpinLock e `SpinWait` di NET 4.

Come ho scritto nel post, in caso di attese molto brevi lo _spinning_ può essere preferibile al _blocking_ in quanto evita overhead di _context switch_.

Gli oggetti `SpinLock` e `SpinWait` sono state pensate esattamente per questo caso.

E' importante sottolineare che tali oggetti non sono classi ma sono `struct`. Questa scelta è stata presa per fare in modo che siano sullo [[stack]] senza mai passare per lo [[heap]] e conseguentemente eliminare il costo di allocazione e garbage collection.

## [[SpinLock]]

## [[SpinWait]]
