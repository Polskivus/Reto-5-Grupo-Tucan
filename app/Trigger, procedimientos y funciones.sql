use Gastro_basque;
/*ESTA funcion devuelve el total de calorias en una receta,
 teniendo en cuenta las calorias de los ingrediente de la receta*/
DELIMITER $$
drop function if exists calculo_calorias_receta$$
create function calculo_calorias_receta(f_id_receta int)
returns decimal (10,2)
deterministic
reads sql data
begin
	declare total_calorias decimal(10,2);
    
    select SUM(i.calorias_por_100g * ri.cantidad_gramos / 100)
    into total_calorias
    from receta_ingrediente ri
    join ingrediente i on i.id = ri.ingrediente_id
    where ri.receta_id = f_id_receta;
    
    return coalesce(total_calorias, 0);    
END $$
DELIMITER ;
/*Este trigger comprueba que el trabajador este activo y
 que no se pueda poner un salario menor al SMI*/
DELIMITER $$
drop trigger if exists Check_salario_no_negativo$$
create trigger Check_salario_no_negativo
before update on contrato
for each row
BEGIN
	if new.salario_base < 1000 then
		signal sqlstate '45000'
        set message_text = 'El salario no puede ser menor al salario minimo';
    end if;
    if old.activo = 0 then
		signal sqlstate '45000'
        set message_text = 'No se puede editar el salario de una persona no activa';
	end if;
END $$
DELIMITER ;

/*Automatizamos el calculo de porcentaje de deducciones de IRPF (SIMULACION)*/
DELIMITER $$
drop function if exists calcular_deduccion$$
create function calcular_deduccion(salario float)
returns float
deterministic
BEGIN
	declare porcentaje float;
    /*Tramos de deduccion*/
    if salario < 1500 then
		set porcentaje = 0.10;
	elseif salario < 2000 then
		set porcentaje = 0.20;
	else
		set porcentaje = 0.30;
	end if;
	return salario * porcentaje;
END $$
DELIMITER ;
/*Comprueba si ya existe una nomina asociada al contrato en el periodo
actual para que no se duplique el registro*/
DELIMITER $$
drop trigger if exists check_nomina_duplicada$$
create trigger check_nomina_duplicada
before insert on nomina
for each row
BEGIN
	declare existe int;
    
    select count(*) into existe
    from nomina
    where contrato_id = new.contrato_id
    and periodo = new.periodo;
    
    if existe > 0 then
		signal sqlstate '45000'
        set message_text = 'Ya existe una nomina para este contrato en ese periodo';
    end if;
END$$
DELIMITER ;
/*Combina el trigger y la funcion anteriores para generar
una nomina con las deducciones ya aplicadas y que no las duplique*/
DELIMITER $$
drop procedure if exists generar_nomina$$
create procedure generar_nomina(
	in p_contrato_id int,
    in p_periodo date
)
BEGIN
	declare v_salario_base float;
    declare v_deducciones float;
    declare v_salario_neto float;
    declare v_activo boolean;
    declare v_error boolean default FALSE;
    
    -- Hacemos el capturador de errores
    declare continue handler for SQLEXCEPTION
    BEGIN
		set v_error = TRUE;
	END;
    
    START TRANSACTION;
    
    -- Miramos si el contrato existe y esta activo (es decir trabajador activo)
    select salario_base, activo
    into v_salario_base, v_activo
    from contrato
    where id = p_contrato_id;
    
    if v_error = FALSE then
		signal sqlstate '45000'
        set message_text = 'No se puede generar nomina de un contrato inactivo';
	end if;
    
    -- Aqui usamos la funcion calcular_deduccion
    set v_deducciones = calcular_deduccion(v_salario_base);
    set v_salario_neto = v_salario_base - v_deducciones;
    
    -- En este insert si hay un registro duplicado hace saltar el trigger check_nomina_duplicada
	insert into nomina (contrato_id, periodo, salario_bruto, deducciones, salario_neto)
    values (p_contrato_id, p_periodo, v_salario_base, v_deducciones, v_salario_neto);
    
    -- Ahora el "capturador de errores" si da error hara rollback si no lo confirmara
    if v_error then
		rollback;
        select 'ERROR: Transaccion revertida' AS resultado;
	else
		commit;
        select
			p_contrato_id as Id_contrato,
            p_periodo as periodo,
            v_salario_base as salario_bruto,
            v_deducciones as deducciones,
            v_salario_neto as salario_neto,
            'OK' as resultado;
		end if;
END $$
DELIMITER ;

CALL generar_nomina(1, '2025-05-01');