CREATE TABLE actor (
  actor_id TEXT PRIMARY KEY,
  output_type TEXT NOT NULL,
  name TEXT NOT NULL
);

CREATE TABLE actor_parameter (
  actor_id TEXT,
  name TEXT,
  value TEXT,

  PRIMARY KEY (actor_id, name),

  FOREIGN KEY (actor_id)
    REFERENCES actor (actor_id)
);