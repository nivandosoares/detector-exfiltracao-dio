"""Correlaciona eventos sintéticos de telemetria de processos."""

import csv
import sys
from datetime import datetime, timedelta

JANELA = timedelta(minutes=5)


def detectar(eventos):
    leituras = {}
    for evento in sorted(eventos, key=lambda item: item["horario"]):
        horario = datetime.fromisoformat(evento["horario"])
        processo = evento["host"], evento["processo_id"]
        tipo = evento["tipo"]
        if tipo == "inicio_processo":
            leituras.pop(processo, None)
        elif tipo == "leitura_sensivel":
            leituras[processo] = horario
        elif tipo == "conexao_externa" and processo in leituras:
            if horario - leituras[processo] <= JANELA:
                yield f"{evento['horario']} | {' / '.join(processo)} | {evento['destino']} | revisar possível exposição"
            leituras.pop(processo)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python3 detectar.py eventos.csv")
    with open(sys.argv[1], encoding="utf-8", newline="") as arquivo:
        for alerta in detectar(csv.DictReader(arquivo)):
            print(alerta)
