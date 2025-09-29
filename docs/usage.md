# 📘 Usage Guide

## 🖥️ CLI

Run the full pipeline:

```bash
make run

make docker-build
make docker-run

python api.py

curl -X POST http://localhost:5000/detect \
     -H "Content-Type: application/json" \
     -d '[{"timestamp":"2025-09-28T12:00:00","source_ip":"192.168.1.1","message":"unauthorized access"}]'

python dashboard.py


from snowflake_ingest import connect_to_snowflake, insert_logs
conn = connect_to_snowflake(...)
insert_logs(conn, "logs_table", df)

make test

