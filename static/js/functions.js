function getText(texto, voice) {
    var dados = [{
        'texto': texto,
        'voice': voice
    }];

    $.ajax({
        type: 'POST',
        url: '/getText',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(dados),
        success: function (result) {

            if (result.status === 200) {

                // Mensagens / UI
                $("#divAlert").prop('hidden', false)
                              .removeClass('alert-danger alert-warning')
                              .addClass('alert-success');

                $("#textMessage").text("Texto convertido com sucesso");

                $("#divAlert").prop('hidden', true);
                $("textarea[name='text']").val("").prop('disabled', false);
                $("#btnConverter").prop('disabled', true)
                                  .html('<i class="fa-solid fa-retweet"></i> Converter');

                // Remove player anterior
                $("#divDFlex").remove();

                // NOVA URL única
                let audioUrl = result.audio_url;
                let filename = result.filename;

                let htmlAudio = `
                    <div class="d-flex flex-row justify-content-center mt-3" id="divDFlex">

                        <audio controls>
                            <source src="${audioUrl}"  data-filename="${filename}" type="audio/mp3">
                            Seu navegador não suporta áudio.
                        </audio>

                        <div class="btn-group mt-2 ms-3" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-success btnGrupos" 
                                id="btnCompartilhar" 
                                data-url="${audioUrl}">
                                <i class="fa-brands fa-whatsapp"></i>
                            </button>

                            <button type="button" class="btn btn-danger btnGrupos ms-3" 
                                title="Excluir áudio" 
                                id="btnExcluirAudio"
                                data-filename="${filename}">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </div>

                    </div>`;

                $("#divAlert").after(htmlAudio);
            }
        },
        error: function (xhr, status, error) {
            $("#divAlert").prop('hidden', false);
            $("#divAlert").removeClass('alert-success alert-warning')
                          .addClass('alert-danger');
            $("#textMessage").text('Erro ao converter texto');
            console.error("Erro ao converter texto:", status, error);
        }
    });
}



function excluirAudio() {

    // Recupera o nome do arquivo armazenado no botão
    let filename = $("#btnExcluirAudio").attr("data-filename");

    if (!filename) {
        console.error("Nenhum filename encontrado para exclusão.");
        return;
    }

    var dados = [{ 'filename': filename }];

    $.ajax({
        type: 'POST',
        url: '/excluir_audio',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(dados),
        success: function (result) {
            if (result.status === 200) {
                let message = result.message;

                $("#divAlert")
                    .removeClass('alert-danger alert-warning')
                    .addClass('alert-success')
                    .prop('hidden', false);

                $("#textMessage").text(message);

                // Remove o player e os botões
                $("#divDFlex").remove();

                setTimeout(() => {
                    $("#divAlert").prop('hidden', true);
                }, 2000);
            }
        },
        error: function (xhr, status, error) {
            $("#divAlert")
                .removeClass('alert-success alert-warning')
                .addClass('alert-danger')
                .prop('hidden', false);

            $("#textMessage").text('Erro ao excluir o áudio!');
            console.error("Erro ao excluir o áudio:", status, error);
        }
    });
}



function enviarWhatsApp(numero) {
    // pega exatamente o nome salvo no botão
    let audio = $("audio source").attr("src");

    if (!audio) {
        console.error("Arquivo de áudio não encontrado!");
        return;
    }

    // garante que tem / no caminho
    let audioUrl = `${window.location.origin}${audio.startsWith("/") ? "" : "/"}${audio}`;

    let texto = `Olá! Aqui está seu áudio: ${audioUrl}`;
    let url = `https://api.whatsapp.com/send?phone=55${numero}&text=${encodeURIComponent(texto)}`;

    
    window.open(url, "_blank");

    $("#divDFlex").remove();
    $("#divInputEnviarZap").remove();
}


