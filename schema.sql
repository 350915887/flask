DROP TABLE IF EXISTS db_user;
DROP TABLE IF EXISTS db_data;
DROP TABLE IF EXISTS db_metric;
DROP TABLE IF EXISTS db_fault;

CREATE TABLE db_user (
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(10),
    email VARCHAR(100),
    createtime DATETIME,
    lastlogin DATETIME
);

CREATE TABLE db_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_id INTEGER,
    sensor_id INTEGER,
    value DOUBLE,
    time DATETIME,
    unit VARCHAR(50)
);

CREATE TABLE db_metric (
    machine_id INT PRIMARY KEY,
    precision DOUBLE NOT NULL,
    recall DOUBLE NOT NULL,
    f1 DOUBLE NOT NULL,
    TP INT NOT NULL,
    FP INT NOT NULL,
    TR INT NOT NULL,
    FR INT NOT NULL,
    updatetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE db_fault (
    id INT PRIMARY KEY,
    machine_id INT,
    solve INT,
    fault_class VARCHAR(255),
    time VARCHAR(255)
);


