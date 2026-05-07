-- ── 1. usuario ──────────────────────────────────────────────────────────────
INSERT INTO usuario (nombre, email, password_hash, rol) VALUES
('Ana García',      'ana.garcia@email.com',  'hash_ana123',    'cliente'),
('Carlos Martínez', 'carlos.m@email.com',    'hash_carlos456', 'trabajador'),
('Laura Pérez',     'laura.perez@email.com', 'hash_laura789',  'trabajador'),
('Miguel Torres',   'miguel.t@email.com',    'hash_miguel321', 'admin'),
('Sofía Ruiz',      'sofia.ruiz@email.com',  'hash_sofia654',  'cliente');

-- ── 2. trabajador ────────────────────────────────────────────────────────────
INSERT INTO trabajador (usuario_id, cargo, departamento, fecha_alta) VALUES
(2, 'Nutricionista',     'Salud y Dietas', '2022-03-15'),
(3, 'Chef Especialista', 'Cocina',         '2021-07-01'),
(4, 'Administrador',     'Dirección',      '2020-01-10');

-- ── 3. contrato ──────────────────────────────────────────────────────────────
INSERT INTO contrato (trabajador_id, tipo, salario_base, fecha_inicio, fecha_fin, activo) VALUES
(1, 'Indefinido', 2200.00, '2022-03-15', NULL,         TRUE),
(2, 'Indefinido', 2500.00, '2021-07-01', NULL,         TRUE),
(3, 'Indefinido', 3500.00, '2020-01-10', NULL,         TRUE),
(1, 'Temporal',   1800.00, '2021-01-01', '2022-03-14', FALSE);

-- ── 4. nomina ────────────────────────────────────────────────────────────────
INSERT INTO nomina (contrato_id, periodo, salario_bruto, deducciones, salario_neto) VALUES
(1, '2024-03-01', 2200.00, 418.00, 1782.00),
(1, '2024-04-01', 2200.00, 418.00, 1782.00),
(2, '2024-03-01', 2500.00, 475.00, 2025.00),
(3, '2024-03-01', 3500.00, 700.00, 2800.00),
(2, '2024-04-01', 2500.00, 475.00, 2025.00);

-- ── 5. receta ────────────────────────────────────────────────────────────────
INSERT INTO receta (nombre, descripcion, tiempo_min, dificultad, categoria) VALUES
('Ensalada César',      'Clásica ensalada con pollo y aderezo César', 15, 'facil',   'Ensaladas'),
('Salmón a la plancha', 'Filete de salmón con limón y eneldo',        20, 'facil',   'Pescados'),
('Pasta Primavera',     'Pasta con verduras de temporada',             25, 'medio',   'Pastas'),
('Pollo al curry',      'Pechuga en salsa de curry y coco',            40, 'medio',   'Carnes'),
('Tarta de manzana',    'Postre clásico con canela y masa quebrada',   60, 'dificil', 'Postres');

-- ── 6. ingrediente ───────────────────────────────────────────────────────────
INSERT INTO ingrediente (nombre, unidad, calorias_por_100g) VALUES
('Lechuga romana',   'g', 15.0),
('Pechuga de pollo', 'g', 165.0),
('Salmón',           'g', 208.0),
('Pasta',            'g', 370.0),
('Manzana',          'g', 52.0);

-- ── 7. receta_ingrediente ────────────────────────────────────────────────────
INSERT INTO receta_ingrediente (receta_id, ingrediente_id, cantidad) VALUES
(1, 1, 200.0),
(1, 2, 150.0),
(2, 3, 300.0),
(3, 4, 250.0),
(5, 5, 400.0);

-- ── 8. dieta ─────────────────────────────────────────────────────────────────
INSERT INTO dieta (nombre, descripcion, tipo, precio_mes, duracion_dias) VALUES
('Dieta Mediterránea', 'Rica en aceite de oliva, pescado y verduras', 'Equilibrada',  49.99, 30),
('Dieta Keto',         'Alta en grasas, baja en carbohidratos',       'Cetogénica',   59.99, 60),
('Dieta Vegana',       'Sin productos de origen animal',              'Plant-based',  44.99, 30),
('Dieta Hipocalórica', 'Déficit calórico controlado para adelgazar',  'Pérdida peso', 39.99, 90);

-- ── 9. suscripcion ───────────────────────────────────────────────────────────
INSERT INTO suscripcion (usuario_id, dieta_id, inicio, fin, activa) VALUES
(1, 1, '2024-01-01', NULL,         TRUE),
(1, 2, '2023-06-01', '2023-07-31', FALSE),
(5, 3, '2024-02-15', NULL,         TRUE),
(5, 4, '2024-04-01', NULL,         TRUE);


