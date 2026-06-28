## pgvector Installation (Windows + PostgreSQL 18)

### 1. Open Developer Command Prompt (Run as Administrator)
x64 Native Tools Command Prompt

---

### 2. Clone pgvector
git clone https://github.com/pgvector/pgvector.git
cd pgvector

---

### 3. Set PostgreSQL path
set PGROOT=C:\Program Files\PostgreSQL\18

---

### 4. Build pgvector
nmake /F Makefile.win

---

### 5. Install pgvector
nmake /F Makefile.win install

---

### 6. Restart PostgreSQL
net stop postgresql-x64-18
net start postgresql-x64-18

---

### 7. Enable extension in PostgreSQL
psql -U postgres

CREATE DATABASE vectordb;
\c vectordb
CREATE EXTENSION vector;

---

### 8. Verify
\dx