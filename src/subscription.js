const sub = document.createElement('story');
sub.innerHTML = `
<div class="container">
    <div class="center">
        <div class="d-grid gap-2 col-6 mx-auto">
            <div id="account">
                <h1 class="text-white">Nombre del app</h1>
            </div>
            <div id="register">
                <h2 class="text-white">Tipo de subscripción</h2>         
        
                <div id="infoAccount" class="text-white">Elije tu tipo de subscripción: <span id="resultvalue"></span>
                <form action="#" class="border p-3 form">
                    <div class="form-group">
                        <label for="nombre">Gratuita</label>
                        <p>Disfruta de todo nuestro contenido con anuncios.</p>
                        <input type="checkbox" id="sub1" name="sub1" value="gratis">  <label for="free">Gratis</label>
                    </div>
                    <div class="form-group mt-3">
                        <label for="email">Plus</label>
                        <p>Disfruta de todo nuestro contenido sin publicidad y con hasta 4 perfiles distintos</p>
                        <input type="checkbox" id="sub2" name="sub2" value="plus"> <label for="plus">$6.99</label>
                    </div>
                    <div class="form-group mt-3">
                        <label for="password">Premium</label>
                        <p>Disfruta de todo nuestro contenido sin publicidad y con hasta 8 perfiles distintos</p>
                        <input type="checkbox" id="sub3" name="sub3" value="premium"> <label for="premium">$11.99</label>
                    </div>
                    <div class="row">
                        <div class="d-grid gap-2 col-2 mx-auto mt-3" >
                            <button type="submit" class="btn btn-warning" >Continuar</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>`

document.body.appendChild(sub);