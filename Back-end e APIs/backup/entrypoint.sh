#!/bin/bash
wait_time=15s
password=@dv202305

# tempo para o sql iniciar
echo importing data will start in $wait_time...
sleep $wait_time
echo executing script...

# importação do script, NUL para não poluir o console
/opt/mssql-tools/bin/sqlcmd -S 0.0.0.0 -U sa -P $password -i ./restore.sql