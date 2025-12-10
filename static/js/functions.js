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
                $("#divAlert").prop('hidden', false);
                $("#divAlert").removeClass('alert-danger alert-success alert-warning').addClass('alert-success');
                $("#textMessage").text("Texto convertido com sucesso");

                $("#divAlert").prop('hidden', true); // Esconde o alerta
                $("textarea[name='text']").val(""); // Limpa o textarea
                $("textarea[name='text']").prop('disabled', false); // Habilita o textarea

                // Após a função, habilitar novamente o botão e restaurar o texto
                $("#btnConverter").prop('disabled', true).html('<i class="fa-solid fa-retweet"></i> Converter');

                let htmlAudio = `<div class="d-flex flex-row justify-content-center mt-3" id="divDFlex">
                        <audio controls>
                            <source src="/audio/audio.mp3" type="audio/mp3">
                            Seu navegador não suporta áudio.
                        </audio>
                        <div class="btn-group ms-3" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-success btnGrupos" id="btnCompartilhar"><i class="fa-brands fa-whatsapp"></i></button>
                            
                            <button type="button" class="btn btn-danger btnGrupos ms-3" title="Excluir áudio" id="btnExcluirAudio"><i class="fa-solid fa-trash-can"></i></button>
                        </div>
                    </div>`;

                $("#divAlert").after(htmlAudio);

                // setTimeout(function () {
                //     // Adiciona um timestamp para evitar cache
                //     var audioUrl = result.audio_url + "?t=" + new Date().getTime();
                //     var audio = new Audio(audioUrl);
                //     audio.play();

                //     // Quando o áudio terminar, execute as ações necessárias
                //     audio.addEventListener("ended", function () {
                //         $("#divAlert").prop('hidden', true); // Esconde o alerta
                //         $("textarea[name='text']").val(""); // Limpa o textarea
                //         $("textarea[name='text']").prop('disabled', false); // Habilita o textarea

                //         // Após a função, habilitar novamente o botão e restaurar o texto
                //         $("#btnConverter").prop('disabled', false).html('<i class="fa-solid fa-retweet"></i> Converter');
                //     });
                // }, 10);

            }
        },
        error: function (xhr, status, error) {
            $("#divAlert").prop('hidden', false);
            $("#divAlert").removeClass('alert-danger alert-success alert-warning').addClass('alert-danger');
            $("#textMessage").text('Erro ao converter texto');
            console.error("Erro ao converter texto:", status, error);
        }
    });
}


function excluirAudio() {
    var dados = [{ 'excluir': 'excluir' }];

    $.ajax({
        type: 'POST',
        url: '/excluir_audio',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(dados),
        success: function (result) {
            if (result.status === 200) {
                let message = result.message;

                $("#divAlert").prop('hidden', false);
                $("#divAlert").removeClass('alert-danger alert-success alert-warning').addClass('alert-success');
                $("#textMessage").text(message);

                $("#divDFlex").remove();

                setTimeout(function () {
                    $("#divAlert").prop('hidden', true); // Esconde o alerta
                }, 2000);

            }
        },
        error: function (xhr, status, error) {
            $("#divAlert").prop('hidden', false);
            $("#divAlert").removeClass('alert-danger alert-success alert-warning').addClass('alert-danger');
            $("#textMessage").text('Erro ao excluir o áudio!');
            console.error("Erro ao excluir o áudio:", status, error);
        }
    })
}


function enviarWhatsApp(numero) {
    let audio = "/audio/audio.mp3";  // ou retornado pela API
    let texto = `Olá! Aqui está seu áudio: ${window.location.origin}${audio}`;
    let url = `https://api.whatsapp.com/send?phone=55${numero}&text=${encodeURIComponent(texto)}`;
    window.open(url, "_blank");

    $("#divDFlex").remove();
    $("#divInputEnviarZap").remove();
}



