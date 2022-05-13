# Reto #19
# CONVERSOR TIEMPO
# Fecha publicación enunciado: 09/05/22
# Fecha publicación resolución: 16/05/22
# Dificultad: FACIL
#
# Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y
# retorne su resultado en milisegundos.
#
# Información adicional: - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para
# preguntas, dudas o prestar ayuda a la comunidad. - Puedes hacer un Fork del repo y una Pull Request al repo
# original para que veamos tu solución aportada. - Revisaré el ejercicio en directo desde Twitch el lunes siguiente
# al de su publicación. - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.


def convert_to_ms(dias=0, horas=0, minutos=0, segundos=0):
    """
    Función que recibe dias, horas, minutos y segundos y convierte en milisegundos
    :param dias:
    :param horas:
    :param minutos:
    :param segundos:
    :return: el resultado en milisegundos o -1 si alguno de los datos introducidos no era correcto
    """
    if type(dias) != int or type(horas) != int or type(minutos) != int or type(segundos) != int:
        return -1
    return segundos * 1000 + minutos * 60 * 1000 + horas * 60 * 60 * 1000 + dias * 24 * 60 * 60 * 1000


# Probando la función. 1 día, 2 horas, 6 minutos y 24 segundos
milisegundos = convert_to_ms(1, 2, 6, 24)
if milisegundos == -1:
    print(
        "Alguno de los datos introducidos no es correcto. Recuerda, tienen que ser números enteros (ni float, "
        "ni string...)")
else:
    print(f"Resultado: {milisegundos}")
