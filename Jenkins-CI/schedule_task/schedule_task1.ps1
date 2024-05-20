# Define el intervalo de tiempo de 8:00 a 15:00
$horaInicio = "08:00"
$horaFin = "15:00"

# Bucle infinito para verificar la hora actual
while ($true) {
    # Obtiene la hora actual
    $horaActual = Get-Date -Format "HH:mm"

    # Comprueba si la hora actual está dentro del intervalo
    if ($horaActual -ge $horaInicio -and $horaActual -le $horaFin) {
        # Abre el Bloc de notas
        Start-Process notepad.exe
    }

    # Espera 1 minuto antes de verificar nuevamente
    Start-Sleep -Seconds 60
}
