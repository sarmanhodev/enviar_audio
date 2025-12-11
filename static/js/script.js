$(document).ready(function () {

    // Habilita/desabilita o botão Converter conforme texto digitado
    $("body").on("keyup", "textarea[name='text']", function () {
        var texto = $(this).val();
        $("#btnConverter").prop('disabled', texto.length === 0);
    });

    // Ao clicar em Converter
    $("body").on("click", "#btnConverter", function () {
        var texto = $("textarea[name='text']").val();
        var voice = $("select[name='voice']").val();

        $(".divDFlex").remove(); // Remove player antigo

        // Desabilitar textarea e botão
        $("textarea[name='text']").prop('disabled', true);
        var button = $(this);
        button.prop('disabled', true);
        button.html('<div class="spinner-border spinner-border-sm" role="status"></div> <span>Convertendo texto</span>');

        // Chama a função getText
        setTimeout(function () {
            getText(texto, voice);
        }, 2500);
    });

    // Compartilhar via WhatsApp: mostra input para número
    $("body").on("click", "#btnCompartilhar", function () {
        let inputEnviar = `
            <div class="mt-3" id="divInputEnviarZap">
                <div class="input-group">
                    <input type="tel" 
                        class="form-control" 
                        placeholder="Ex.: 21999999999" 
                        id="numeroWhatsapp" 
                        inputmode="numeric" 
                        pattern="[0-9]*"
                        maxlength="11">
                    <button class="btn btn-outline-primary" disabled type="button" id="btnEnviarZap">
                        <i class="fa-solid fa-paper-plane"></i>
                    </button>        
                </div>
                <small class="text-muted">Somente números: <b>21999999999</b></small>
            </div>`;

        let btnCancelarEnvio = `
            <button type="button" class="btn btn-warning btnGrupos ms-3" title="Cancelar envio" id="cancelarEnvio">
                <i class="fa-solid fa-ban"></i>
            </button>`;

        $("#btnCompartilhar").remove();
        $(".btn-group").html(btnCancelarEnvio);
        $("#divAudioTag").after(inputEnviar);
    });

    // Habilita o botão Enviar WhatsApp apenas se 11 dígitos
    $("body").on("keyup", "#numeroWhatsapp", function () {
        let numeroWhatsapp = $(this).val();
        $("#btnEnviarZap").prop('disabled', numeroWhatsapp.length !== 11);
    });

    // Enviar WhatsApp
    $("body").on("click", "#btnEnviarZap", function () {
        let audioUrl = $("audio source").attr("src");
        let filename = audioUrl.split('/').pop();

        let numeroWhatsapp = $("#numeroWhatsapp").val();
        if (numeroWhatsapp) {
            enviarWhatsApp(numeroWhatsapp, filename);
        }
    });

    // Cancelar envio
    $("body").on("click", "#cancelarEnvio", function () {
        let audioURL = $("audio source").attr("src");
        let filename = $("audio source").attr("data-filename");

        let btnCompartilhar = `
            <button type="button" data-url="${audioURL}" class="btn btn-success btnGrupos" id="btnCompartilhar">
                <i class="fa-brands fa-whatsapp"></i>
            </button>
            <button type="button" class="btn btn-danger ms-3 btnGrupos" data-filename="${filename}" title="Excluir áudio" id="btnExcluirAudio">
                <i class="fa-solid fa-trash-can"></i>
            </button>`;

        $("#cancelarEnvio").remove();
        $(".btn-group").html(btnCompartilhar);
        $("#divInputEnviarZap").remove();
    });

    // Excluir áudio
    $("body").on("click", "#btnExcluirAudio", function () {
        excluirAudio();
    });

});
