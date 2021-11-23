text  = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry men    ea la cabeza como disgustado… -agrega el comentarista"

text = text.replace("&", "\n")
text = text.replace("g", "G", 1)
text = text.replace("strawberry", "Strawberry")
text = text.replace("curva", "curva...")

print(text)
