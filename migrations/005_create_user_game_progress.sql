-- Migration: Create user game progress table
-- Syncs gamification progress (searches, views, completions, badges) across devices

CREATE TABLE IF NOT EXISTS user_game_progress (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL UNIQUE,
  data TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_game_progress_user_id ON user_game_progress(user_id);
