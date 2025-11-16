-- ============================================
-- Supabase Database Setup for Contact Form App
-- ============================================
-- Run this SQL in your Supabase SQL Editor
-- Dashboard > SQL Editor > New Query
-- ============================================

-- Create the messages table
CREATE TABLE IF NOT EXISTS messages (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON messages(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_messages_email ON messages(email);

-- Add a trigger to automatically update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_messages_updated_at
    BEFORE UPDATE ON messages
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Enable Row Level Security (RLS)
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Create a policy to allow all operations for authenticated users
-- You can modify these policies based on your security requirements

-- Policy: Allow anyone to insert messages (for public contact form)
CREATE POLICY "Allow public insert" ON messages
    FOR INSERT
    TO public
    WITH CHECK (true);

-- Policy: Allow anyone to read messages
-- Change this if you want to restrict who can view messages
CREATE POLICY "Allow public read" ON messages
    FOR SELECT
    TO public
    USING (true);

-- Policy: Allow authenticated users to update their own messages
-- Uncomment if you want to allow updates
-- CREATE POLICY "Allow authenticated update" ON messages
--     FOR UPDATE
--     TO authenticated
--     USING (true)
--     WITH CHECK (true);

-- Policy: Allow authenticated users to delete messages
-- Uncomment if you want to allow deletes
-- CREATE POLICY "Allow authenticated delete" ON messages
--     FOR DELETE
--     TO authenticated
--     USING (true);

-- ============================================
-- Optional: Insert sample data for testing
-- ============================================
-- Uncomment the following lines to insert sample messages

-- INSERT INTO messages (name, email, message) VALUES
--     ('John Doe', 'john@example.com', 'This is a test message from the setup script.'),
--     ('Jane Smith', 'jane@example.com', 'Another test message to verify the database is working correctly.'),
--     ('Bob Johnson', 'bob@example.com', 'Hello! This is my first message.');

-- ============================================
-- Verification Queries
-- ============================================
-- Run these to verify your setup

-- Check table structure
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'messages';

-- Count messages
-- SELECT COUNT(*) as total_messages FROM messages;

-- View all messages
-- SELECT * FROM messages ORDER BY created_at DESC;
