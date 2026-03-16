CREATE OR REPLACE VIEW v_fullTable AS
SELECT
    c.customerid      AS "customerID",
    c.gender          AS "gender",
    c.seniorcitizen   AS "SeniorCitizen",
    c.partner         AS "Partner",
    c.dependents      AS "Dependents",
    c.tenure          AS "tenure",
    s.phoneservice    AS "PhoneService",
    s.multiplelines   AS "MultipleLines",
    s.internetservice AS "InternetService",
    s.onlinesecurity  AS "OnlineSecurity",
    s.onlinebackup    AS "OnlineBackup",
    s.deviceprotection AS "DeviceProtection",
    s.techsupport     AS "TechSupport",
    s.streamingtv     AS "StreamingTV",
    s.streamingmovies AS "StreamingMovies",
    b.contract        AS "Contract",
    b.paperlessbilling AS "PaperlessBilling",
    b.paymentmethod   AS "PaymentMethod",
    b.monthlycharges  AS "MonthlyCharges",
    b.totalcharges    AS "TotalCharges",
    o.churn           AS "Churn"
FROM customers c
JOIN services s  USING (customerid)
JOIN billing  b  USING (customerid)
JOIN outcomes o  USING (customerid);