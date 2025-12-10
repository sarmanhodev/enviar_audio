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
        let inputEnviar = `<div class="mt-3" id="divInputEnviarZap">
            <div class="input-group">
                <input type="tel" 
                class="form-control" 
                placeholder="Ex.: 21999999999" 
                id="numeroWhatsapp" 
                aria-label="Telefone"
                inputmode="numeric" 
                pattern="[0-9]*"
                maxlength="11">
        
            <button class="btn btn-outline-primary" disabled type="button" id="btnEnviarZap"><i class="fa-solid fa-paper-plane"></i></button>        
            </div>
            <small class="text-muted">Somente números: <b>21999999999</b></small>
        </div>`;

        let btnCancelarEnvio = `<button type="button" class="btn btn-warning btnGrupos ms-3" title="Cancelar envio" id="cancelarEnvio"><i class="fa-solid fa-ban"></i></button>`;

        $("#btnCompartilhar").remove();
        $(".btn-group").html(btnCancelarEnvio);

        $("#divDFlex").after(inputEnviar);


    });


    $("body").on("keyup", "#numeroWhatsapp", function () {
        let numeroWhatsapp = $(this).val();

        if (numeroWhatsapp.length == 11) {
            $("#btnEnviarZap").prop('disabled', false);
        } else {
            $("#btnEnviarZap").prop('disabled', true);
        }
    });

    $("body").on("click", "#btnEnviarZap", function () {
        let numeroWhatsapp = $("#numeroWhatsapp").val();

        if (numeroWhatsapp) {
            enviarWhatsApp(numeroWhatsapp);
        }
    });


    $("body").on("click", "#cancelarEnvio", function () {
        let audioURL = $("audio source").attr("src");
        let filename = $("audio source").attr("data-filename");
        
        let btnCompartilhar = `<button type="button" data-url="${audioURL}" class="btn btn-success btnGrupos" id="btnCompartilhar"><i class="fa-brands fa-whatsapp"></i></button>
        <button type="button" class="btn btn-danger ms-3 btnGrupos" data-filename="${filename}" title="Excluir áudio" id="btnExcluirAudio"><i class="fa-solid fa-trash-can"></i></button>`;

        $("#cancelarEnvio").remove();
        $(".btn-group").html(btnCompartilhar);
        $("#divInputEnviarZap").remove();
    });

    $("body").on("click", "#btnExcluirAudio", function () {
        excluirAudio();
    });
});
