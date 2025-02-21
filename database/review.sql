SELECT datname FROM pg_database;
SELECT tablename FROM pg_tables WHERE schemaname = 'public';

CREATE EXTENSION IF NOT EXISTS pg_trgm;
SELECT * FROM pg_extension;

SELECT * from review_review;