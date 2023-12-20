---
tags:
  - CSharp
  - Basics
---
## Come compilare in x64 e x86 con Visual Studio

Visual studio permette tre possibili tipologie di compilazione: **x86**, **x64** e **any CPU**.

Il loro comportamento cambia se si sta compilando su una macchina a 32 bit o su una a 64.

## Macchina a 32 bit

-   **Any CPU**: il tuo software girerà a 32 bit (in accordo col tuo sistema operativo) e potrà quindi caricare assembly compilati sia con l'opzione “any CPU” che con l'opzione x86. Se carico invece un assembly x64 ottengo un'eccezione `BadImageFormatException`;
-   **x86**: identico a “any CPU”;
-   **x64**: ottengo sempre un'eccezione `BadImageFormatException`.

## Macchina a 64 bit

-   **Any CPU**: il tuo software girerà a 64 bit (in accordo col tuo sistema operativo) e potrà quindi caricare assembly compilati sia con l'opzione “any CPU” che con l'opzione x64. Se carico invece un assembly x86 ottengo un'eccezione `BadImageFormatException`;
-   **x86**: il tuo software girerà a 32 bit e potrà quindi caricare assembly compilati sia con l'opzione “any CPU” che con l'opzione x86. Se carico invece un assembly x64 ottengo un'eccezione `BadImageFormatException`;
-   **x64**: identico a “any CPU”.