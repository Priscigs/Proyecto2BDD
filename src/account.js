const story = document.createElement('story');
story.innerHTML = `
<div class="container">
    <div class="center">
        <div class="d-grid gap-2 col-6 mx-auto">
            <div id="account">
                <h1 class="text-white">Nombre del app</h1>
            </div>
            <div id="register">
                <h2 class="text-white">Registro</h2>         
        
                <div id="infoAccount" class="text-white">Ingresa los siguientes datos para continuar: <span id="resultvalue"></span>
                <form action="#" class="border p-3 form">
                    <div class="form-group">
                        <label for="nombre">Nombre</label>
                        <input type="nombre" name="nombre" id="nombre" class="form-control">
                    </div>
                    <div class="form-group mt-3">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" class="form-control">
                    </div>
                    <div class="form-group mt-3">
                        <label for="password">Contraseña</label>
                        <input type="password" name="password" id="password" class="form-control">
                    </div>
                    <div class="form-group mt-3">
                        <label for="passwordConfirm">Confirmar Contraseña</label>
                        <input type="passwordConfirm" name="passwordConfirm" id="passwordConfirm" class="form-control">
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
</div>`

document.body.appendChild(story);

