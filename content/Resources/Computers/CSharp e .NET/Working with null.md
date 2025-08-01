---
tags:
  - Dometrain
---
Questa nota prende a piene mani dal corso [# From Zero to Hero: Working with Null in C#](https://dometrain.com/course/from-zero-to-hero-working-with-null-in-csharp/)

**Prima di C# 2.0**, non era possibile assegnare `null` a tipi **valore** (es. `int`, `short`, `long`, ecc.), in quanto ciò generava un errore di compilazione.
**Con C# 2.0+**, è stata introdotta la struct **`Nullable<T>`**, che permette di **wrappare un tipo valore** affinché possa rappresentare anche l’assenza di valore (`null`), ad esempio:
```csharp
Nullable<int> count = null;
```
È stato inoltre introdotto uno **zucchero sintattico** per semplificare la scrittura:
```csharp
int? count = null;
```
`int?` è quindi un alias compatto per `Nullable<int>`.
### Comportamenti importanti:
- Il tipo `int` ha come **valore di default** `0` mentre il tipo `int?` ha come **valore di default** `null`.
- È possibile inizializzare un nullable in modo implicito:
```csharp
int? x = new(); // x sarà null
```
- La struct `Nullable<T>` espone alcune proprietà/metodi utili:
    - `HasValue`: restituisce `true` se è presente un valore, `false` se è `null`.
    - `Value`: restituisce il valore sottostante (attenzione: solleva eccezione se `HasValue` è `false`).
    - `GetValueOrDefault()`: restituisce il valore sottostante se presente, altrimenti il **valore di default del tipo T** (es. `0` per `int`).
## Nullable Aware Context
**I reference type (es. `string`) possono già essere `null` da sempre**, ma **il compilatore non dava alcun avviso o aiuto** se si dimenticava di gestire il `null`, con il rischio di `NullReferenceException` a runtime.
In **C# 8** è stato introdotto il **Nullable Aware Context**, abilita un contesto in cui il compilatore **analizza il codice** per aiutare a **evitare errori da `null` non gestiti**.
Si può attivare per progetto:
```xml
<Nullable>enable</Nullable>  // nel file .csproj
```
Oppure nel singolo file C#:
```csharp
#nullable enable
```
In particolare ora se un reference type non è dichiarato con il `?` il compilatore fornirà warning se non è gestito il fatto che questa variabile possa essere null.
Il `?` su un reference type serve quindi solo per i developer e per il compilatore e indica che una variabile ci si aspetti che possa diventare null (`string?`) oppure che non dovrebbe mai essere null (`string`).
L'obiettivo è fare in modo che il compilatore ti **aiuta a prevenire i NullReferenceException** segnalando dove potresti avere `null` non gestiti.
Questa è una **verifica a livello di compilatore**, **non cambia il comportamento a runtime**: `string` può ancora essere `null` a runtime, sia che sia definito `string` che `string?`.

## Nullable value type vs nullable reference type
La differenza tra un **nullable value type** e un **nullable reference type** in C# è sostanziale sia concettualmente che dal punto di vista dell’implementazione. Quando si parla di `int?`, cioè un tipo valore nullable, ci si riferisce in realtà a una struttura `Nullable<T>`, che internamente contiene due elementi: una proprietà `HasValue`, che indica se è presente un valore, e una proprietà `Value`, che rappresenta il valore effettivo. Anche quando il tipo è `null`, non si tratta di un riferimento assente, ma di una struct che contiene un flag per indicare l’assenza del valore.
Al contrario, `Person?`, che rappresenta un **nullable reference type**, è semplicemente un riferimento che può essere null. Non c’è alcun wrapper o struttura a supporto: ==il tipo è lo stesso `Person`, ma il punto interrogativo viene usato esclusivamente per abilitare i controlli del compilatore introdotti con il nullable aware context==.
A livello di runtime, `Person?` è del tutto identico a `Person`, con la differenza che il compilatore tiene traccia delle possibili assegnazioni null e genera warning se si tenta di usare un valore senza verificarne la presenza.
Tecnicamente, i **nullable value types** vivono nello stack e solo in caso di boxing vengono allocati su heap. I **nullable reference types**, invece, sono normali riferimenti che possono semplicemente contenere `null`, senza alcuna struttura aggiuntiva. La gestione della nullabilità in questo caso è tutta a carico del compilatore, che segnala potenziali dereferenziazioni pericolose, ma non aggiunge alcuna protezione automatica a runtime.
```csharp
int value = 42;
int? nullableValue = default;
Console.WriteLine(nullableValue.HasValue);

Person person = new() { Name = "Alice", Age = 25 };
Person? nullablePerson = default;
Console.WriteLine(nullablePerson?.Name);
```

| Variabile          | Stack     | Heap                                             |
|--------------------|-----------|--------------------------------------------------|
| `value`            | `42`      | -                                                |
| `nullableValue?`   | `0x0001`  | `Nullable<int> { HasValue = false, Value = 0 }`  |
| `person`           | `0x0002`  | `Person { Name = "Alice", Age = 25 }`            |
| `nullablePerson?`  | `null`    | - (riferimento nullo, non c'è struct wrapper)     |
## Attributi

### `[AllowNull]`
In alcuni casi posso evitare il warning sull fatto che un non nullable type può avere valori null dicendo al compilatore che è ammesso che la variabile possa contenere `null` in alcuni momenti del ciclo di vita dell’applicazione (es. durante l’inizializzazione).
Prendiamo questo esempio:
```csharp
public class VehicleService
{
    [AllowNull]
    private static VehicleService instance;

    private VehicleService() { }

    public static VehicleService Create() => instance ??= new VehicleService();
}
```
- Il campo `instance` è dichiarato come **non nullable**, ma inizialmente vale `null`. Per evitare warning del compilatore, si usa **`[AllowNull]`** per dire esplicitamente che **il campo può contenere `null` temporaneamente**, anche se è non-nullable.
- Il metodo `Create()` restituisce un’istanza singleton: se `instance` è `null`, viene creato un nuovo oggetto `VehicleService` usando l’operatore `??=` (assegna solo se è `null`).
- Sono sicuro che all'esterno questa variabile non sarà mai null in quanto l'unico metodo `public` per crearla è `Create()` che la inizializza.

In questo caso avere che `VehicleService` è `null` all'inizio è una **scelta progettuale consapevole**: il campo è inizialmente `null` e verrà inizializzato **lazy** (al primo accesso tramite `??=`). Quindi, **non c'è errore logico**, ma il compilatore lo segnala comunque perché il contratto del tipo dice "non può mai essere null".
L'attributo `[AllowNull]` permette di dire **"questo campo può temporaneamente essere null anche se è dichiarato come non nullable, ed è voluto"**, senza cambiare la sua firma (cioè senza doverlo dichiarare `VehicleService?`).

### `[DisallowNull]`
Fa l’opposto di `[AllowNull]`: **impedisce che venga assegnato `null`** anche se la proprietà o campo è dichiarato come nullable (`string?`).
```csharp
[DisallowNull]
public string? Description { get; set; }
```
Qui `Description` è nullable, ma **non può ricevere `null` in fase di assegnazione**. Può però **essere `null` in lettura**.

### `[MemberNotNull(nameof(attribute))]`
L'attributo `[MemberNotNull(nameof(PropertyName))]` assicura al compilatore che, dopo l'esecuzione del metodo su cui è associato, la proprietà `PropertyName` sarà sicuramente non nulla.
Serve per migliorare l'analisi statica della nullabilità e prevenire warning.
```csharp
public class VehicleService
{
    private static VehicleService? instance;
    public static DateTime? CreatedOn { get; private set; }

    [MemberNotNull(nameof(CreatedOn))]
    public static VehicleService Create()
    {
        CreatedOn = DateTime.UtcNow;
        return instance ??= new VehicleService();
    }
}
```

### `[return: NotNullIfNotNull("param")]`
L'attributo `[return: NotNullIfNotNull("param")]` dice al compilatore che il metodo su cui è associato restituirà un valore non nullo **solo se** anche il parametro `param` non è nullo. Aiuta l’analisi di nullabilità a propagare correttamente le informazioni.
### Codice completo:

```csharp
public class VehicleService
{
    [return: NotNullIfNotNull("vehicle")]
    public Vehicle? UpgradeVehicle(Vehicle? vehicle)
    {
        if (vehicle == null) return null;
        return new Vehicle(vehicle.Id, vehicle.Make, vehicle.Model, vehicle.Color);
    }
}
```

## Warning comuni

### Converting null literal or possible null value to non-nullable type
Il compilatore sta segnalando che stai assegnando un valore potenzialmente `null` (o un `null literal` che corrisponde alla stringa `null` o un `possible null value` che corrisponde ad una funzione che può ritornare null) a un tipo dichiarato come non nullable, cosa che potrebbe portare a un **NullReferenceException a runtime**.
Esempio:
```csharp
// 
Vehicle v = null;             // Null literal
Vehicle v = GetVehicle();     // Possible null value
string color = v.Color;
Vehicle? GetVehicle() => null;
```
### Dereference of a possibly null reference
Significa che il compilatore rileva che **`v` è di tipo `Vehicle?` (nullable)**, quindi **potrebbe essere `null`**, eppure stai cercando di accedere direttamente alla sua proprietà `.Color` senza controllare prima.
Se `v` fosse effettivamente `null` a runtime, otterresti una **`NullReferenceException`**.
La soluzione è controllare che `v != null` prima dell'accesso.
```csharp
string color = v?.Color ?? defaultVehicle.Color;
```
