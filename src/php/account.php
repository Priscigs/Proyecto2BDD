<?php
class Usuario {
    private $user;
    private $pass;
    private $tipo;
    private $activo;
    private $correos;
    public function __constructor ($user, $pass, $tipo, $activo, $correos){
        $this->user = $user;
        $this->pass = $pass;
        $this->tipo = $tipo;
        $this->activo = $activo;
        $this->correos = $correos;
    }
    public function obtenerUsuario(){
        return $this->user;
    }

    public function obtenerPassword(){
        return $this->pass;
    }

    public function obtenerTS(){
        return $this->tipo;
    }
    
    public function obtenerA(){
        return $this->activo;
    }

    public function obtenerCorreo(){
        return $this->correos;
    }
}