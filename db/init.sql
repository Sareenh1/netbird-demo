docker run -d \
  --name postgres \
  -e POSTGRES_DB=appdb \
  -e POSTGRES_USER=appuser \
  -e POSTGRES_PASSWORD=StrongPassword123 \
  -p 5432:5432 \
  postgres:16
