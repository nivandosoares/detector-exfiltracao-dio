# Detecção de possível exposição de dados

Alternativa defensiva ao laboratório de malware. O programa lê exclusivamente um CSV de eventos fictícios. Ele não captura conteúdo, não acessa arquivos monitorados e não abre conexões. Os destinos do exemplo pertencem a uma faixa reservada para documentação.

O detector correlaciona uma leitura classificada como sensível seguida de uma conexão externa pelo mesmo processo, no mesmo host, dentro de cinco minutos. Um evento de início limpa a associação anterior para evitar correlação com um processo encerrado que usava o mesmo identificador. O CSV usa timestamps UTC normalizados em ISO 8601.

Execute com Python 3:

```sh
python3 detectar.py eventos.csv
```

A amostra testa três casos: sequência correlacionada, conexão por outro processo e conexão fora da janela. A saída deve coincidir com `esperado.txt`.

## Triagem

Confirme se a leitura e o destino são esperados para o aplicativo. Verifique a identidade do executável, a finalidade da conexão e os registros disponíveis. Preserve a evidência e encaminhe ao responsável por resposta a incidentes se a atividade persistir ou houver sinais adicionais. A sequência sozinha não demonstra que o arquivo foi transmitido. A regra depende de telemetria completa e pode sinalizar transferências legítimas.
