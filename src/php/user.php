<?php
include_once 'users.php';

class ValidadorRegistro{
    private $user;
    private $correos;
    private $pass;

    private $errorUsuario;
    private $errorEmail;
    private $errorPassword1; 
    private $errorPassword2;

    public function __construct($user, $correos, $password1, $password2, $conexion){
        $this->user="";
        $this->email="";
        $this->pass;
        
        $this->errorUsuario = $this->validarNombre($user, $conexion); 
        $this->errorEmail = $this->validarEmail($correos, $conexion);
        $this->errorPassword1 = $this->validarPassword1($password1);
        $this->errorPassword2 = $this->validarPassword2($password1, $password2);

        if ($this->errorPassword1==="" && $this->errorPassword2==="") {
            $this->pass = $password1; 
        }                   
    }

    private function variableIniciada($variable){
        if (isset($variable) && !empty($variable)){
            return true;
        }else{
            return false;
        }
     }

    private function validarNombre($usuario, $conexion){

        if(!$this->variableIniciada($usuario)){
            return "Ingrese un nombre de usuario por favor";
        }
        else{
            $this->user=$usuario;
        }
        if(strlen($usuario)<6){
            return "El nombre de usuario debe contener al menos 6 caracteres";
        }
        if(strlen($usuario)>50){
            return "El nombre de usuario no debe superar los 50 caracteres";
        } 

        if(users::usuarioExiste($conexion, $usuario)){
            return "El usuario ya está en uso, por favor ingrese otro nombre de usuario";
        }
        return ""; 
    }

    private function validarEmail($correos, $conexion){

        if (!$this->variableIniciada($correos)) {
            return "Ingrese su correo por favor";
        }
        else{
            $this->correos=$correos;
        }
        if (users::correoExiste($conexion, $correos)) {
            return "El correo ya se encuentra en uso";
        }
        return "";
    }

    private function validarPassword1($password){

        if (!$this->variableIniciada($password)) {
            return "Ingrese su contraseña antes de continuar";
        }
        if (strlen($password) < 6) {
            return "Por tu seguridad la contraseña debe contener al menos 6 caracteres";
        }
        if ($this->user===$password) {
            return "Por tu seguridad el nombre de usuario no debe ser igual a tu contraseña";
        }
        return "";
    }

    private function validarPassword2($password1, $password2){

        if (!$this->variableIniciada($password1)) {
            return "Ingrese primero su contraseña";
        }
        if (!$this->variableIniciada($password2)) {
            return "Repita su contraseña";
        }
        if ($password1!==$password2) {
            return "Las contraseñas no son iguales";
        }
        return "";
    }

    public function obtenerUsuario(){
        return $this->user;
    }
    public function obtenerEmai1(){
        return $this->correos;
    }
    public function obtenerPassword(){
        return $this->pass;
    }
    public function obtenerErrorUsuario(){
        return $this->errorUsuario;
    }
    public function obtenerErrorEmail(){
        return $this->errorEmail;
    }
    public function obtenerErrorPassword1(){
       return $this->errorPassword1;
    }
    public function obtenerErrorPassword2(){
        return $this->errorPassword2;
    }
    public function registroValido(){
        if ($this->errorUsuario==="" && $this->errorEmail==="" && $this->errorPassword1==="" && $this->errorPassword2==="") {
            return true;
        }
        else {
            return false;
        }
    }
}
 
?>