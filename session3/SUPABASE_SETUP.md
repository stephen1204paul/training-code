# Supabase Setup Guide

Complete guide to setting up Supabase for the Flask Contact Form Application.

## Table of Contents

1. [What is Supabase?](#what-is-supabase)
2. [Prerequisites](#prerequisites)
3. [Create a Supabase Project](#create-a-supabase-project)
4. [Database Setup](#database-setup)
5. [Get API Credentials](#get-api-credentials)
6. [Configure the Application](#configure-the-application)
7. [Testing the Integration](#testing-the-integration)
8. [Troubleshooting](#troubleshooting)

## What is Supabase?

Supabase is an open-source Firebase alternative that provides:
- **PostgreSQL Database** - Powerful relational database
- **Auto-generated APIs** - RESTful API created automatically
- **Authentication** - User authentication and authorization
- **Real-time subscriptions** - Live data updates
- **Storage** - File storage capabilities

For this project, we're using Supabase's PostgreSQL database to store contact form messages instead of a text file.

## Prerequisites

- A free Supabase account ([sign up here](https://supabase.com))
- Python 3.8+ installed
- The Flask app dependencies installed

## Create a Supabase Project

### Step 1: Sign Up / Log In

1. Go to [supabase.com](https://supabase.com)
2. Click **"Start your project"** or **"Sign In"**
3. Sign up using GitHub, Google, or email

### Step 2: Create a New Project

1. Click **"New Project"** from your dashboard
2. Fill in the project details:
   - **Name**: `contact-form` (or any name you prefer)
   - **Database Password**: Create a strong password (save this!)
   - **Region**: Choose the closest to your location
   - **Pricing Plan**: Select **Free** tier

3. Click **"Create new project"**
4. Wait 1-2 minutes for the project to be provisioned

## Database Setup

### Step 1: Open SQL Editor

1. In your Supabase project dashboard, click **"SQL Editor"** from the left sidebar
2. Click **"New Query"**

### Step 2: Run the Setup SQL

1. Copy the contents of `database_setup.sql` from this project
2. Paste it into the SQL Editor
3. Click **"Run"** or press `Ctrl+Enter` (Windows/Linux) / `Cmd+Enter` (Mac)

You should see: `Success. No rows returned`

### Step 3: Verify Table Creation

1. Click **"Table Editor"** from the left sidebar
2. You should see a table named **"messages"** with the following columns:
   - `id` (bigint, primary key)
   - `name` (varchar)
   - `email` (varchar)
   - `message` (text)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

## Get API Credentials

### Step 1: Find Your API Keys

1. Click **"Settings"** (gear icon) in the left sidebar
2. Click **"API"** under Project Settings
3. You'll see two important values:

#### Project URL
```
https://xxxxxxxxxxxxx.supabase.co
```

#### API Keys
- **anon public** - Safe to use in client-side code
- **service_role** - Secret key for server-side (keep private!)

### Step 2: Copy Your Credentials

Copy these values - you'll need them in the next step:
- Project URL
- anon public key (or service_role if you need admin access)

## Configure the Application

### Step 1: Create Environment File

1. In your project directory (`training-code/session3/`), copy the example file:

```bash
cp .env.example .env
```

### Step 2: Edit the .env File

Open `.env` and update with your Supabase credentials:

```bash
# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your-random-secret-key-here

# Enable Supabase
USE_SUPABASE=true

# Your Supabase credentials (from previous step)
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
SUPABASE_KEY=your-anon-public-key-here
```

**Important Notes:**
- Replace `xxxxxxxxxxxxx` with your actual project ID
- Replace `your-anon-public-key-here` with your actual anon key
- Set `USE_SUPABASE=true` to enable Supabase
- Set `USE_SUPABASE=false` to use file-based storage

### Step 3: Install Dependencies

Make sure you have all required packages:

```bash
pip install -r requirements.txt
```

This installs:
- `supabase==2.3.4` - Supabase Python client
- `python-dotenv==1.0.0` - Environment variable loader
- `postgrest==0.13.2` - PostgreSQL REST client

## Testing the Integration

### Step 1: Run the Application

```bash
python app.py
```

You should see:
```
✅ Supabase initialized: https://xxxxxxxxxxxxx.supabase.co
```

If you see this warning instead:
```
⚠️  Warning: USE_SUPABASE is True but credentials are missing
```
Check your `.env` file configuration.

### Step 2: Test the Contact Form

1. Open your browser to `http://localhost:8000/`
2. Fill out the contact form:
   - Name: Test User
   - Email: test@example.com
   - Message: Testing Supabase integration!
3. Click **"Send Message"**
4. You should see a success page

### Step 3: Verify in Supabase

1. Go to your Supabase dashboard
2. Click **"Table Editor"**
3. Click on the **"messages"** table
4. You should see your test message!

### Step 4: View Messages in the App

1. Navigate to `http://localhost:8000/messages`
2. You should see all submitted messages
3. Try the health check: `http://localhost:8000/health`

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-11-15T10:30:00.123456",
  "total_messages": 1,
  "storage_type": "supabase"
}
```

## Troubleshooting

### Issue: "Module 'supabase' not found"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Connection refused" or API errors

**Solution:**
1. Check your `SUPABASE_URL` is correct
2. Verify your `SUPABASE_KEY` is valid
3. Ensure your Supabase project is active (not paused)
4. Check your internet connection

### Issue: "Row Level Security" errors

**Solution:**
The `database_setup.sql` includes RLS policies. If you're getting permission errors:

1. Go to Supabase Dashboard > **Authentication** > **Policies**
2. Check the policies on the `messages` table
3. Ensure "Allow public insert" and "Allow public read" are enabled

Or disable RLS temporarily (not recommended for production):
```sql
ALTER TABLE messages DISABLE ROW LEVEL SECURITY;
```

### Issue: Messages not appearing

**Solution:**
1. Check the Supabase Table Editor to see if data is being saved
2. Verify `USE_SUPABASE=true` in your `.env` file
3. Check the console output when starting the app
4. Look for error messages in the terminal

### Issue: "Warning: USE_SUPABASE is True but credentials are missing"

**Solution:**
1. Make sure `.env` file exists in the project root
2. Verify the environment variables are set correctly:
   ```bash
   SUPABASE_URL=https://xxxxx.supabase.co
   SUPABASE_KEY=your-key-here
   ```
3. Restart the application after updating `.env`

## Switching Between Storage Methods

### Use Supabase (Database)
```bash
# In .env file
USE_SUPABASE=true
```

### Use File-based Storage
```bash
# In .env file
USE_SUPABASE=false
```

The app will automatically use the configured storage method!

## Security Best Practices

1. **Never commit `.env` file** - It's already in `.gitignore`
2. **Use `anon` key** for public operations
3. **Keep `service_role` key secret** - Only use server-side
4. **Enable RLS (Row Level Security)** - Included in setup SQL
5. **Use environment variables** - Never hardcode credentials

## Additional Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Python Client](https://github.com/supabase-community/supabase-py)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Row Level Security Guide](https://supabase.com/docs/guides/auth/row-level-security)

## Next Steps

- Set up Supabase Authentication for user login
- Add real-time subscriptions to see messages update live
- Implement message deletion and editing
- Add file uploads with Supabase Storage
- Deploy to production with proper security

---

**Need Help?** Check the [Supabase Discord](https://discord.supabase.com/) community!
