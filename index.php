<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creación de Cuenta</title>
    <link href="src/css/account.css" type="text/css" rel="stylesheet"></link>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <!--<script src="src/js/account.js"></script>-->
    <div class="container">
        <div class="center">
            <div class="d-grid gap-2 col-6 mx-auto">
                <div id="account">
                    <h1 class="text-white">Nombre del app</h1>
                </div>
                <div id="register">
                    <h2 class="text-white">Registro</h2>         
            
                    <div id="infoAccount" class="text-white">Ingresa los siguientes datos para continuar: <span id="resultvalue"></span>
                    <form class="border p-3 form" method="POST" action="src/php/user-register.php">
                        <div class="form-group">
                            <label for="usuario">Nombre</label>
                            <input type="usuario" name="usuario" id="usuario" class="form-control" placeholder="nombre">
                        </div>
                        <div class="form-group mt-3">
                            <label for="email">Email</label>
                            <input type="email" name="email" id="email" class="form-control" placeholder="correo">
                        </div>
                        
                        <div class="form-group mt-3">
                            <label for="password">Contraseña</label>
                            <input type="password" name="password" id="password" class="form-control" placeholder="contraseña">
                        </div>
                        <div class="form-group mt-3">
                            <label for="passwordConfirm">Confirmar Contraseña</label>
                            <input type="password" name="passwordConfirm" id="passwordConfirm" class="form-control" placeholder="contraseña">
                        </div>
                        <div class="row">
                            <div class="d-grid gap-2 col-2 mx-auto mt-3" >
                                <button type="submit" class="btn btn-warning" >Sign In</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
</div>
</body>
</html>