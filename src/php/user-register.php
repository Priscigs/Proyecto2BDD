<?php
include_once 'config.php';
include_once 'conexion.php';
include_once 'users.php'; //repositorio 
include_once 'user.php'; //validador registro
include_once 'account.php'; //usuaario 

Conexion::abrirConexion();

$validador = new ValidadorRegistro($_POST['usuario'], $_POST['email'], htmlspecialchars($_POST['password']),
    htmlspecialchars($_POST['passwordConfirm']), Conexion::obtenerConexion());

if ($validador->RegistroValido()) {
    # CONTRASEÑA CON HASH DE UNA VEZ ...

    $usuario = new Usuario($validador->obtenerUsuario(), password_hash($validador->obtenerPassword(), PASSWORD_DEFAULT), '', '', $validador->obtenerEmai1()); 

    $insertar_usuario = users::insertarUsuario(Conexion::obtenerConexion(), $usuario); 

    if ($insertar_usuario) {
        echo "insertado";
    } 
    else{
        echo 'no insertado';
    }
}
else {
    $error = array(
        'errorUsuario' => $validador->obtenerErrorUsuario(),
        'errorEmail' => $validador->obtenerErrorEmail(),
        'errorP1' => $validador->obtenerErrorPassword1(),
        'errorP2' => $validador->obtenerErrorPassword2()
    );
    // Mostrar mensajes
    echo json_encode($error);
}

Conexion::cerrarConexion();

?> 