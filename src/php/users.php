<?php
class users {
    public static function insertarUsuario($conexion, $usuarios){
    
    $usuarioInsertado = false;

    if (isset($conexion)){
            try{
                $sql = "INSERT INTO usuarios (usuario, password, tipo_subscripcion, activo_desde, correo) 
                values (:user,
                        :pass, 
                        :tipo, 
                        :activo, 
                        :correos)";
                $sentencia = $conexion->prepare($sql);

                $user = $usuarios->obtenerUsuario();
                $pass = $usuarios->obtenerPassword();
                $tipo = $usuarios->obtenerTS();
                $activo = $usuarios->obtenerA();
                $correos  = $usuarios->obtenerCorreo();
                
                $sentencia->bindParm(':user', $user, PDO::PARAM_STR);
                $sentencia->bindParm(':pass', $pass, PDO::PARAM_STR);
                $sentencia->bindParm(':tipo', $tipo, PDO::PARAM_STR);
                $sentencia->bindParm(':activo', $activo, PDO::PARAM_STR);
                $sentencia->bindParm(':correos', $correos , PDO::PARAM_STR);

                // Devolver si es falso o verdadero dependiendo su ejecución
                $usuarioInsertado = $sentencia->execute(); 
                $usuarioInsertado = true;
            }
            catch(PDOException $e){
                print "ERROR". $e->getMessage();
            }
        }
        return $usuarioInsertado; // True or false
    }

    public static function obtenerUsuarioPorEmail($email, $conexion){
        $usuario = null;
        if (isset($conexion)) {
                
                try {
                    include_once 'account.php';
                    $sql = "SELECT * FROM usuarios WHERE correo = :email";
                    $sentencia = $conexion->prepare($sql);
                    $sentencia->bindParam(':email', $email, PDO::PARAM_STR);
                    $sentencia->execute();
                    $resultado = $sentencia -> fetch();

                    if (!empty($resultado)) {
                            $usuario = new Usuario($resultado['usuario'], $resultado['password'], $resultado['
                                tipo_suscripcion'], $resultado['activo_desde'], $resultado['correo']);
                    }
                } catch (PDOException $e) {
                    print "ERROR". $e -> getMessage();
                    die();
                }
            }
            return $usuario;
        }

    public static function usuarioExiste($conexion, $usuario){
        $usuarioExiste = true; 
        if(isset($conexion)){
            try {
                $sql = "SELECT * FROM usuarios where usuario = :usuario";
                $sentencia = $conexion->prepare($sql);
                $sentencia->bindParam(':usuario', $usuario, PDO::PARAM_STR);
                $sentencia->execute();
                $resultado = $sentencia->fetchAll();

                if(count($resultado)){
                    $usuarioExiste = true;
                }
                else{
                    $usuarioExiste = false;
                }
                 
            } catch(PDOException $e){
                print "ERROR ".$e->getMessage();  
            }
        }
        return $usuarioExiste;
    }

    public static function correoExiste($conexion, $email){
        $correoExiste = true;
        if(isset($conexion)){
            try {
                $sql = "SELECT * FROM usuarios where correo = :email";
                $sentencia = $conexion->prepare($sql);
                $sentencia->bindParam(':email', $email, PDO::PARAM_STR);
                $sentencia->execute();
                $resultado = $sentencia->fetchAll();

                if(count($resultado)){
                    $correoExiste = true;
                }
                else{
                    $correoExiste = false;
                }
                 
            } catch(PDOException $e){
                print "ERROR ".$e->getMessage();  
            }
        }
        return $correoExiste;
    }
}

?>
