---
tags:
  - CSharp
  - Coding
  - Memory
---

DotMemory offre la potenzialità di verificare di non avere leak tramite test, di seguito alcuni esempi.
Per degli esempi in formato script vedi [questo link](https://github.com/JetBrains/dotmemory-demos/tree/main/Tests).

* Verifica di non aver alcun oggetto in memoria con un determinato namespace
```csharp
dotMemory.Check(memory =>
	{
		Assert.That(memory.GetObjects(@where => @where.Namespace.Like("GameOfLife.*")).ObjectsCount, Is.EqualTo(0));
	});
```

* Verifica di non aver alcun oggetto di un determinato tipo

```csharp
dotMemory.Check(memory =>
                    Assert.That(memory.GetObjects(where => where.
                                Type.Is<PetriDish>())
                            .ObjectsCount,
                        Is.EqualTo(0)));
```
* Verificare che la memoria complessiva allocata di un determinato codice non superi X byte.

```csharp
const int Mb = 1024 * 1024;

[Test]
[AssertTraffic(AllocatedSizeInBytes = 2 * Mb)] // --assert
public void WholeRunTraffic()
{
	// --act
	// ...
}
```

* Verifico che un determinato codice non crei dei nuovi oggetti di un determinato tipo
```csharp
[Test]
public void DontRecreateArrays()
{
	// --arrange
	var target = new PetriDish(160, 100, timer);

	// Prendo uno snapshot della memoria
	var memoryPoint1 = dotMemory.Check();

	// --act
	target.PerformOneStep();

	// --assert
	// Confronto la meoria attuale (memory) con quella presa prima (memoryPoint1) e verifico di non aver alcun nuovo oggetto di tipo Cell.
	dotMemory.Check(memory =>
		Assert.That(memory.GetDifference(memoryPoint1)
				.GetNewObjects(where => where.Type.Is<Cell[,]>())
				.ObjectsCount,
			Is.EqualTo(0)));
}
```
* Contare il numero di oggetti in una determinata [[Garbage Collector#^cef812|Generation]] 
```csharp
dotMemory.Check(memory =>
{
	var objectSet = memory
		.GetObjects(where => where.Namespace.Like("Production"))
		.GetObjects(where => where.Generation.Is(Generation.Gen2));

	Assert.That(objectSet.ObjectsCount, Is.EqualTo(0));
}
                );
```

* Verificare che metodo non crei alcun nuovo oggetto (del mio namespace) tranne oggetti di un determinato tipo.

```csharp
[Test]
public void NoNewObjectsExceptShapesTest()
{
	using (new ShapeGenerator(_ => { }, TimeSpan.FromMilliseconds(100)))
	{
		var memoryCheckPoint = dotMemory.Check();
		Thread.Sleep(1000); // generate ~10 shapes

		dotMemory.Check(memory =>
		{
		    // Conto tutti i miei oggetti nuovi (namespace "Production")
			var newTotalCount =
				memory
					.GetDifference(memoryCheckPoint)
					.GetNewObjects(where => where.Namespace.Like("Production"))
					.ObjectsCount;

			// Conto gli oggetti nuovi di tipo IShape
			var newShapesCount =
				memory
					.GetDifference(memoryCheckPoint)
					.GetNewObjects(where => where.Interface.Is<IShape>())
					.ObjectsCount;

			// Verifico che i due valori siano uguali
			Assert.That(newTotalCount - newShapesCount, Is.EqualTo(0));
		});
	}
}
```
## Attributi
E' possibile configurare il comportamento dei test usando l'attributo `DotMemoryUnit` con determinate opzioni.
Per approfondire vedi [questo link](https://www.jetbrains.com/help/dotmemory-unit/Configuring_dotMemory_Unit.html#6343021a).

* `FailIfRunWithoutSupport`: se impostato a false non fa fallire il test se questo viene lanciato senza il supporto a `dotMemory`. Utile nel caso in cui i test vengano lanciati con Jenkins o quando si vogliono lanciare spesso e si vogliono evitare i test di leak che sono molto lenti. `[DotMemoryUnit(FailIfRunWithoutSupport = false)]`

## Esempio completo
```csharp
[Test]  
[DotMemoryUnit(FailIfRunWithoutSupport = false)]  
public void SaveFormatSync_AfterSomeModifications_DoNotLeak()  
{  
    // Arrange  
    var thermalView = Substitute.For<IView>();  
    thermalView.Head.Returns(_thermalHead);  
    var tridimensionalView = Substitute.For<IView>();  
    tridimensionalView.Head.Returns(_tridimensionalHead);  
    var views = new List<IView> { tridimensionalView, thermalView };  
    // Creo un formato con una posa con due viste, una 3d e una termo  
    SetupFormat(views);  
    var sut = new ManagePosesViewModel(_headsManager, _formatManager);  
  
    // Prendo uno snapshot della memoria  
    var memoryPoint1 = dotMemory.Check();  
  
    // Aggiungo un nuova posa  
    sut.AddAfterCommand.Execute(null);  
    // La prima posa solo 3d (quindi tolgo la view termo)  
    sut.Poses[0].Views[0].Enabled = true;  
    sut.Poses[0].Views[1].Enabled = false;  
    // La seconda posa solo termo (quindi tolgo la view 3d)  
    sut.Poses[1].Views[0].Enabled = true;  
    sut.Poses[1].Views[1].Enabled = true;  
  
    // Act  
    sut.SaveFormatSync();  
  
    // Verifico di avere lo stesso numero di IFormato di prima, di avere solo una posa in più e una vista in più rispetto a prima  
    dotMemory.Check(memory =>  
    {  
        var snapshotDifference = memory.GetDifference(memoryPoint1);  
        // Non posso usare IPose ma _formatManager.CurrentFormat.Poses[0].GetType(); in quanto non è una vera IPose ma un mock di NSubstitute.  
        var formatType = _formatManager.CurrentFormat.GetType();  
        var poseType = _formatManager.CurrentFormat.Poses[0].GetType();  
        var viewType = _formatManager.CurrentFormat.Poses[0].Views[0].GetType();  
        // Rispetto a prima non devo avere nuovi formati  
        snapshotDifference.GetNewObjects(where => where.Type == formatType).ObjectsCount.Should()  
            .Be(0);  
        // Rispetto a prima devo avere una sola posa in più  
        snapshotDifference.GetNewObjects(where => where.Type == poseType).ObjectsCount.Should()  
            .Be(1);  
        // Rispetto a prima devo avere una sola vista in più (dato che ho tolto una vista vecchia e la nuova posa ha solo una vista)  
        snapshotDifference.GetNewObjects(where => where.Type == viewType).ObjectsCount.Should()  
            .Be(1);  
    });}
```