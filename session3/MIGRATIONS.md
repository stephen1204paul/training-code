# Database Migrations Guide

Complete guide to using Flask-Migrate for database migrations in the Contact Form application.

## Table of Contents

1. [What are Migrations?](#what-are-migrations)
2. [Why Use Migrations?](#why-use-migrations)
3. [Prerequisites](#prerequisites)
4. [Database Setup Options](#database-setup-options)
5. [Initialize Migrations](#initialize-migrations)
6. [Creating Migrations](#creating-migrations)
7. [Applying Migrations](#applying-migrations)
8. [Common Migration Commands](#common-migration-commands)
9. [Supabase PostgreSQL Setup](#supabase-postgresql-setup)
10. [Local PostgreSQL Setup](#local-postgresql-setup)
11. [SQLite Setup](#sqlite-setup)
12. [Troubleshooting](#troubleshooting)

## What are Migrations?

**Database migrations** are version-controlled changes to your database schema. They allow you to:
- Track database schema changes over time
- Share database structure with your team
- Roll back problematic changes
- Deploy schema updates to production safely

## Why Use Migrations?

✅ **Version Control** - Database schema is tracked in git
✅ **Team Collaboration** - Everyone has the same database structure
✅ **Rollback Support** - Undo schema changes if needed
✅ **Deployment Safety** - Apply changes incrementally in production
✅ **Documentation** - Migration files document schema evolution

## Prerequisites

1. **Dependencies installed**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database configured** in `.env` file

3. **Environment activated**:
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

## Database Setup Options

### Option 1: Supabase PostgreSQL (Recommended)

**Best for**: Cloud deployment, learning production workflows

1. Create a Supabase account at [supabase.com](https://supabase.com)
2. Create a new project
3. Get your database connection string:
   - Dashboard → Project Settings → Database
   - Connection String → URI
   - Copy the connection string

4. Configure `.env`:
   ```bash
   USE_DATABASE=true
   DATABASE_URL=postgresql://postgres.xxxxx:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
   ```

### Option 2: Local PostgreSQL

**Best for**: Development without internet, full control

1. Install PostgreSQL locally
2. Create a database:
   ```bash
   createdb contact_form_db
   ```

3. Configure `.env`:
   ```bash
   USE_DATABASE=true
   DATABASE_URL=postgresql://username:password@localhost:5432/contact_form_db
   ```

### Option 3: SQLite

**Best for**: Quick testing, simplest setup

1. Configure `.env`:
   ```bash
   USE_DATABASE=true
   DATABASE_URL=sqlite:///messages.db
   ```

No installation needed - SQLite is built into Python!

## Initialize Migrations

**Run this ONCE** when setting up the project:

```bash
flask db init
```

This creates a `migrations/` folder with migration scripts.

**Output:**
```
Creating directory /path/to/session3/migrations ... done
Creating directory /path/to/session3/migrations/versions ... done
Generating /path/to/session3/migrations/script.py.mako ... done
Generating /path/to/session3/migrations/env.py ... done
Generating /path/to/session3/migrations/README ... done
Generating /path/to/session3/migrations/alembic.ini ... done
Please edit configuration/connection/logging settings in '/path/to/session3/migrations/alembic.ini' before proceeding.
```

## Creating Migrations

After changing your models in `app/models.py`, create a migration:

```bash
flask db migrate -m "Initial migration - create messages table"
```

**Explanation:**
- `flask db migrate` - Generates a migration script
- `-m "message"` - Migration description (use clear, descriptive messages)

**Output:**
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'messages'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_messages_created_at' on '['created_at']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_messages_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_messages_name' on '['name']'
  Generating /path/to/migrations/versions/abc123_initial_migration.py ... done
```

This creates a new file in `migrations/versions/` with the schema changes.

## Applying Migrations

Apply migrations to your database:

```bash
flask db upgrade
```

**Output:**
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> abc123, Initial migration - create messages table
```

Your database now has the `messages` table!

## Common Migration Commands

### Check Migration Status

See which migrations have been applied:

```bash
flask db current
```

### View Migration History

See all migrations:

```bash
flask db history
```

### Rollback Last Migration

Undo the most recent migration:

```bash
flask db downgrade
```

### Rollback to Specific Version

```bash
flask db downgrade <revision_id>
```

### Upgrade to Specific Version

```bash
flask db upgrade <revision_id>
```

### Generate Empty Migration

Create a blank migration file for custom SQL:

```bash
flask db revision -m "Custom SQL changes"
```

## Supabase PostgreSQL Setup

### Complete Supabase Workflow

1. **Create Supabase Project**
   - Go to [supabase.com](https://supabase.com)
   - Click "New Project"
   - Choose organization, name, password, region
   - Wait for provisioning (~2 minutes)

2. **Get Database Connection String**
   - Dashboard → Settings (gear icon) → Database
   - Scroll to "Connection String" section
   - Select "URI" tab
   - Copy the connection string
   - Replace `[YOUR-PASSWORD]` with your actual database password

3. **Configure Environment**
   ```bash
   cp .env.example .env
   ```

   Edit `.env`:
   ```bash
   FLASK_ENV=development
   USE_DATABASE=true
   DATABASE_URL=postgresql://postgres.xxxxx:YOUR_PASSWORD@aws-0-us-east-1.pooler.supabase.com:6543/postgres
   ```

4. **Initialize and Run Migrations**
   ```bash
   # Initialize migrations (first time only)
   flask db init

   # Create initial migration
   flask db migrate -m "Initial migration - create messages table"

   # Apply migration
   flask db upgrade
   ```

5. **Verify in Supabase**
   - Dashboard → Table Editor
   - You should see the `messages` table with all columns

6. **Run the App**
   ```bash
   python app.py
   ```

   Expected output:
   ```
   ✅ Connected to Supabase PostgreSQL database
   ✅ Database tables verified/created
   ```

## Local PostgreSQL Setup

### macOS (using Homebrew)

```bash
# Install PostgreSQL
brew install postgresql@15

# Start PostgreSQL
brew services start postgresql@15

# Create database
createdb contact_form_db

# Configure .env
USE_DATABASE=true
DATABASE_URL=postgresql://$(whoami)@localhost:5432/contact_form_db
```

### Linux (Ubuntu/Debian)

```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL
sudo systemctl start postgresql

# Create user and database
sudo -u postgres createuser -s $USER
createdb contact_form_db

# Configure .env
USE_DATABASE=true
DATABASE_URL=postgresql://$(whoami)@localhost:5432/contact_form_db
```

### Windows

1. Download PostgreSQL from [postgresql.org/download/windows](https://www.postgresql.org/download/windows/)
2. Install and remember the password
3. Open pgAdmin or command line
4. Create database `contact_form_db`
5. Configure `.env`:
   ```
   USE_DATABASE=true
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/contact_form_db
   ```

Then run migrations as usual.

## SQLite Setup

**Simplest option - no installation required!**

1. **Configure `.env`**:
   ```bash
   USE_DATABASE=true
   DATABASE_URL=sqlite:///messages.db
   ```

2. **Run migrations**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

3. **Done!** A `messages.db` file will be created

**Note**: SQLite is great for development but not recommended for production.

## Troubleshooting

### Issue: `flask: command not found`

**Solution**:
```bash
# Set FLASK_APP environment variable
export FLASK_APP=app.py  # macOS/Linux
set FLASK_APP=app.py     # Windows CMD
$env:FLASK_APP="app.py"  # Windows PowerShell

# Or use Python module syntax
python -m flask db init
```

### Issue: "Target database is not up to date"

**Solution**:
```bash
flask db upgrade
```

### Issue: "Can't locate revision identified by 'abc123'"

**Solution**: Migration file is missing. Check `migrations/versions/` folder.

### Issue: Connection refused (PostgreSQL)

**Solution**:
```bash
# Check if PostgreSQL is running
brew services list  # macOS
sudo systemctl status postgresql  # Linux
```

### Issue: "password authentication failed"

**Solution**: Check your DATABASE_URL password is correct.

For Supabase:
- Go to Dashboard → Settings → Database
- Click "Reset Database Password"
- Update DATABASE_URL in `.env`

### Issue: Migration creates wrong changes

**Solution**:
1. Delete the migration file from `migrations/versions/`
2. Fix your model in `app/models.py`
3. Run `flask db migrate` again

### Issue: Need to add custom SQL

**Solution**:
```bash
# Create empty migration
flask db revision -m "Custom changes"

# Edit the generated file in migrations/versions/
# Add your SQL in upgrade() and downgrade()
```

Example:
```python
def upgrade():
    op.execute("CREATE INDEX CONCURRENTLY idx_custom ON messages(email);")

def downgrade():
    op.execute("DROP INDEX idx_custom;")
```

## Best Practices

1. **Always commit migrations** to version control
2. **Test migrations** before deploying to production
3. **Use descriptive messages** for migration names
4. **Review generated migrations** - Flask-Migrate isn't perfect
5. **Never edit applied migrations** - create a new one instead
6. **Backup production database** before running migrations
7. **Use transactions** for safety (enabled by default)

## Migration Workflow Example

```bash
# 1. Pull latest code
git pull origin main

# 2. Activate virtualenv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run pending migrations
flask db upgrade

# 5. Make model changes in app/models.py
# (e.g., add a new field)

# 6. Generate migration
flask db migrate -m "Add phone field to Message model"

# 7. Review the generated migration file
cat migrations/versions/xxx_add_phone_field.py

# 8. Apply migration
flask db upgrade

# 9. Test the changes
python app.py

# 10. Commit migration file
git add migrations/versions/xxx_add_phone_field.py
git commit -m "Add phone field to messages"
git push origin main
```

## Additional Resources

- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Supabase Database Guide](https://supabase.com/docs/guides/database)

---

**Questions?** Check the [troubleshooting section](#troubleshooting) or create an issue!
