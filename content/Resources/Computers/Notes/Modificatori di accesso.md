---
tags:
  - Coding
  - CSharp
  - Basics
  - PublishedPosts
---


Questo articolo è una parziale traduzione di quanto riportato nel libro _Thinking in C#_ di Larry O’Brien e Bruce Eckel con l'aggiunta di immagini reperite sull'internet.

## 1. Introduzione
La regola fondamentale che deve essere sempre tenuta a mente nella programmazione ad oggetti è **separare le cose che cambiano dalle cose che rimangono sempre le stesse**.
Inoltre un codice ben scritto permette l'uso dall'esterno solo del **minor numero possibile di metodi**. Per poter garantire entrambe queste condizioni e permettere la scrittura di un buon codice, i linguaggi OO utilizzano i **modificatori di accesso**, che sono delle parole chiave anteposte ai nomi dei metodi o classi che permettono di indicare i gradi di visibilità del metodo/classe stesso.
I livelli di accesso vanno dal meno restrittivo al più, e sono i seguenti: **public**, **protected**, **internal** e **private**

## 2. Modificatori

### 2.1 Public
Definire un metodo come **public** significa che il metodo è disponibile a tutti, in particolare al client che utilizza la libreria

![image](/uploads/7b6580671932d7e13a32c31d95f460d8/image.png)

### 2.2 Internal
Un metodo **internal** viene reso disponibile a tutte le classi che sono all'interno dello stesso assembly compilato (**DLL** o **exe**), ma appare invece come privato all'esterno.
**Internal** permette quindi a classi che sono legate tra di loro logicamente di poter comunicare, conseguente il suo uso ha significato in un codice ben scritto, in cui le responsabilità sono divise per assembly.

![image](/uploads/4b298eb5003c62d1fe108f69d4db53ab/image.png)

### 2.3 Protected e protected internal
La visibilità di questo metodo è per se stessa e per le **classi figlie** ma non per il mondo esterno.
E' possibile combinare il **protected** con il **internal**, ottenendo così **protected internal**, questo significa che l'oggetto può essere acceduto ai metodi dello stesso assembly e i metodi delle classi figlie.

**Protected**:
![image](/uploads/74d7ae1824f935c702021554e455abf0/image.png)

**Protected internal**
![image](/uploads/cfde4b3b91c5734269ed077585115140/image.png)

### 2.4 Private
Un metodo **private** non può essere acceduto da nessuno trannte i metodi della classe.

![image](/uploads/37ffed1e719ccca9e7e726383533f81c/image.png)

## 3. Modificatori di default
In C#, l'accesso a ogni oggetto in cui non è stato definito un modificatore diverso è "**il più restrittivo modificatore di accesso che puoi dichiare per quell'elemento**".
Quindi, per esempio, assumiamo di avere la seguente classe:
```csharp
namespace MyCompany
{
class Outer
{
void Foo() {}
class Inner {}
}
}
```
questa è equivalente a
```csharp
namespace MyCompany
{
internal class Outer
{
private void Foo() {}
private class Inner {}
}
}
```
Di seguito riportiamo una tabella esplicativa


|Oggetto| Default | Accessibilità permesse|
|----------------------|-----------|--------------------------------|
|`namespace` | public | Nessuna |
|`enum` | public | Nessuna |
|`interface` | public | Nessuna |
|`class` | private | Tutte |
|`struct` | private | public, internal, private |
|`delegate` | private | Tutte |
|`constructor` | private | Tutte |
|`interface member` | public | Nessuna |
|`method` | private | Tutte |
|`field` | private | Tutte |
|`user-defined operator`| none | public |

