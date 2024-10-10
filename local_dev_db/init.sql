CREATE TABLE IF NOT EXISTS lista_negra_emails (
    email_lista_negra VARCHAR(500) PRIMARY KEY,
    motivo_lista_negra VARCHAR(100),
    id_app_cliente_uuid VARCHAR(36),
    ip_origen_solicitud VARCHAR(30),
    fecha_solicitud TIMESTAMP
);

INSERT INTO lista_negra_emails (email_lista_negra, motivo_lista_negra, id_app_cliente_uuid, ip_origen_solicitud, fecha_solicitud) VALUES
('test@test.com', 'spam', '123e4567-e89b-12d3-a456-426614174000','127.0.0.1', '2024-02-20 12:00:00'),
('test2@test.com', 'phishing', '123e4567-e89b-12d3-a456-426614174000','127.0.0.1', '2024-02-20 12:00:00');

