DROP TABLE IF EXISTS leaderboard;

CREATE TABLE leaderboard (
    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username TEXT NOT NULL,
    score INTEGER NOT NULL
);