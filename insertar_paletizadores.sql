
CREATE TABLE IF NOT EXISTS palletizer_info (
    machine_id VARCHAR(10) PRIMARY KEY,
    model VARCHAR(50),
    location VARCHAR(50),
    install_date DATE,
    last_maintenance DATE,
    certified_operator VARCHAR(10)
);

INSERT INTO palletizer_info (machine_id, model, location, install_date, last_maintenance, certified_operator)
VALUES
('001', 'KukaX', 'Línea A', '2022-10-03', '2023-07-14', 'Sí'),
('002', 'ABB420', 'Línea B', '2022-02-28', '2023-05-04', 'No'),
('003', 'FanucLite', 'Línea C', '2022-07-07', '2023-02-14', 'No'),
('004', 'OmronDelta', 'Línea D', '2022-10-20', '2023-08-16', 'No'),
('005', 'YaskawaPro', 'Línea E', '2022-04-20', '2023-07-16', 'Sí');
