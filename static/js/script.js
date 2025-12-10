$(document).ready(function () {


    $("body").on("keyup", "textarea[name='text']", function () {
        var texto = $(this).val();

        if (texto.length > 0) {
            $("#btnConverter").prop('disabled', false);
        } else {
            $("#btnConverter").prop('disabled', true);
        }
    });


    $("body").on("click", "#btnConverter", function () {
        var texto = $("textarea[name='text']").val();
        var voice = $("select[name='voice']").val();

        $("#divDFlex").remove();

        // Desabilitar o textarea e o botão
        $("textarea[name='text']").prop('disabled', true);
        var button = $(this);
        button.prop('disabled', true); // Desativa o botão

        // Alterar o texto do botão para o spinner
        button.html('<div class="spinner-border spinner-border-sm" role="status"></div> <span>Convertendo texto</span>');

        // Simular o tempo para chamar a função (remova o setTimeout se não precisar dele)
        setTimeout(function () {
            getText(texto, voice);
        }, 2500);
    });



    $("body").on("click", "#btnCompartilhar", function () {
        let inputEnviar = `<div class="input-group mt-3" id="divInputEnviarZap">
        <input type="text" class="form-control" placeholder="Ex.: 21999999999" id="numeroWhatsapp" aria-label="Ex.: 21999999999" aria-describedby="btnEnviarZap">
        <button class="btn btn-outline-primary" type="button" id="btnEnviarZap"><i class="fa-solid fa-paper-plane"></i></button>
        </div>`;

        let btnCancelarEnvio = `<button type="button" class="btn btn-warning btnGrupos ms-3" title="Cancelar envio" id="cancelarEnvio"><i class="fa-solid fa-ban"></i></button>`;

        $("#btnCompartilhar").remove();
        $(".btn-group").html(btnCancelarEnvio);

        $("#divDFlex").after(inputEnviar);


    });

    $("body").on("click", "#btnEnviarZap", function () {
        let numeroWhatsapp = $("#numeroWhatsapp").val();

        if (numeroWhatsapp) {
            enviarWhatsApp(numeroWhatsapp);
        }
    });


    $("body").on("click", "#cancelarEnvio", function () {
        let btnCompartilhar = `<button type="button" class="btn btn-success btnGrupos" id="btnCompartilhar"><i class="fa-brands fa-whatsapp"></i></button>`;

        $("#cancelarEnvio").remove();
        $(".btn-group").html(btnCompartilhar);
        $("#divInputEnviarZap").remove();
    });

    $("body").on("click", "#btnExcluirAudio", function(){
        excluirAudio();
    });
});
