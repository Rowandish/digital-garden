---
tags:
  - Coding
  - SqlServer
  - PublishedPosts
---
In SQL Server esistono due tipi di jobs principalmente: *Maintenance Jobs* e *Batch Jobs*.

I primi sono i più comuni e vengono utilizzati per eseguire backups, trovare errori di consistenza, eliminare record di history e così via.

Possiamo definire i *Batch Jobs* invece come sono una serie di istruzioni SQL che vengono lanciate periodicamente per eseguire delle esigenze funzionali di prodotto.

Esistono due modalità per creare dei JOBS, la modalità ad interfaccia grafica con *SQL Server Management Studio* e la modalità utilizzando T-SQL, approfondiamo la seconda.
Prendendo direttamente [dalla documentazione ufficiale](https://msdn.microsoft.com/en-us/library/ms190268.aspx) approfondiamo la seguente query:
```sql
EXEC dbo.sp_add_job
@job_name = N'Weekly Sales Data Backup' ;
GO
EXEC sp_add_jobstep
@job_name = N'Weekly Sales Data Backup',
@step_name = N'Set database to read only',
@command = N'ALTER DATABASE SALES SET READ_ONLY', 
@retry_attempts = 5,
@retry_interval = 5 ;
GO
EXEC dbo.sp_add_schedule
@schedule_name = N'RunOnce',
@freq_type = 1,
@active_start_time = 233000 ;
USE msdb ;
GO
EXEC sp_attach_schedule
@job_name = N'Weekly Sales Data Backup',
@schedule_name = N'RunOnce';
GO
EXEC dbo.sp_add_jobserver
@job_name = N'Weekly Sales Data Backup';
```
### sp_add_job
Aggiunge un nuovo Job eseguito dal servizio *SQLServerAgent*.
La chiamata con un solo parametro in ingresso crea il job con un determinato nome senza ulteriori opzioni
```sql
EXEC dbo.sp_add_job @job_name = N'Weekly Sales Data Backup' ;
```
E' possibile definire ulteriori opzioni, per esempio la *@delete_level* che indica quando eliminare il job. il valore di default è 0, che significa mai, ma posso indicare valori fino a 3. Il valore 1, per esempio, indica che il job viene eliminato dopo essere stato eseguito una volta correttamente.

### sp_add_jobstep
Aggiunge uno step ad un job esistente (identificato dal parametro *@job_name*).
Presenta numerose opzioni, per esempio il numero di retry in caso di fallimento (5), il numero di minuti di attesa prima di un retry successivo (10).
```sql
EXEC sp_add_jobstep
@job_name = N'Weekly Sales Data Backup',
@step_name = N'Set database to read only',
@command = N'ALTER DATABASE SALES SET READ_ONLY', 
@retry_attempts = 5,
@retry_interval = 10 ;
```

### sp_add_schedule
Crea un "oggetto" schedule che può essere usato da un quasiasi numero di job (tramite la *sp_attach_schedule*).
Anche in questo caso esistono un grande numero di opzioni, le principali sono la *@freq_type* per la frequenza con la quale il job deve essere chiamato, e *@active_start_time* che indica **quando** il job deve partire.
##### Job eseguito solo una volta

```sql
EXEC dbo.sp_add_schedule
@schedule_name = N'RunOnce',
@freq_type = 1,
@active_start_time = 233000 ;
```

##### Job eseguito ogni giorno alle 01:00

```sql
EXEC sp_add_schedule
@schedule_name = N'NightlyJobs' ,
@freq_type = 4,
@freq_interval = 1,
@active_start_time = 010000 ;
```

#### sp_attach_schedule
Lega un job con un schedule.

```sql
EXEC sp_attach_schedule
@job_name = N'BackupDatabase',
@schedule_name = N'NightlyJobs';
```

### sp_add_jobserver
Lega un determinato job con un determinato server

##### Assegna il Job al server locale
```sql
EXEC dbo.sp_add_jobserver
@job_name = N'NightlyBackups';
```

##### Assegna il Job ad un server differente
```sql
EXEC dbo.sp_add_jobserver
@job_name = N'Weekly Sales Backups',
@server_name = N'SEATTLE2';
```

