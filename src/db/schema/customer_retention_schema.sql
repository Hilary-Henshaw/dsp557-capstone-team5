-- Raw Data Relational Schema Conversion
-- This splits the original flat CSV into a small relational model:
-- - customers: demographics + tenure
-- - services: subscribed services
-- - billing: contract + payment + charges
-- - outcomes: churn label

CREATE TABLE IF NOT EXISTS customers (
    customerid      TEXT PRIMARY KEY,
    gender          TEXT,
    seniorcitizen   INTEGER,
    partner         TEXT,
    dependents      TEXT,
    tenure          INTEGER
);

CREATE TABLE IF NOT EXISTS services (
    customerid          TEXT PRIMARY KEY REFERENCES customers(customerid) ON DELETE CASCADE,
    phoneservice        TEXT,
    multiplelines       TEXT,
    internetservice     TEXT,
    onlinesecurity      TEXT,
    onlinebackup        TEXT,
    deviceprotection    TEXT,
    techsupport         TEXT,
    streamingtv         TEXT,
    streamingmovies     TEXT
);

CREATE TABLE IF NOT EXISTS billing (
    customerid          TEXT PRIMARY KEY REFERENCES customers(customerid) ON DELETE CASCADE,
    contract            TEXT,
    paperlessbilling    TEXT,
    paymentmethod       TEXT,
    monthlycharges      NUMERIC,
    totalcharges        NUMERIC
);

CREATE TABLE IF NOT EXISTS outcomes (
    customerid  TEXT PRIMARY KEY REFERENCES customers(customerid) ON DELETE CASCADE,
    churn       TEXT
);
