-- crear roles
create role 'admin_role';
create role 'trabajador_role';

-- -----------------------------------------------
-- permisos admin: todo sobre todas las tablas
-- -----------------------------------------------
grant all privileges on gastro_basque.* to 'admin_role';

-- -----------------------------------------------
-- permisos trabajador: solo ver ciertas tablas
-- -----------------------------------------------
grant select on gastro_basque.dieta to 'trabajador_role';
grant select on gastro_basque.ingrediente to 'trabajador_role';
grant select on gastro_basque.receta to 'trabajador_role';
grant select on gastro_basque.suscripcion to 'trabajador_role';

-- editar dieta e ingrediente
grant update on gastro_basque.dieta to 'trabajador_role';
grant update on gastro_basque.ingrediente to 'trabajador_role';

-- -----------------------------------------------
-- crear usuarios y asignar roles
-- -----------------------------------------------
create user 'usuario_admin'@'localhost' identified by 'Admin123';
create user 'usuario_trabajador'@'localhost' identified by 'Trabajador123';

grant 'admin_role' to 'usuario_admin'@'localhost';
grant 'trabajador_role' to 'usuario_trabajador'@'localhost';

-- activar los roles por defecto al conectarse
set default role 'admin_role' to 'usuario_admin'@'localhost';
set default role 'trabajador_role' to 'usuario_trabajador'@'localhost';

flush privileges;