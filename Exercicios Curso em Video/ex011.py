w = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(w, h, w*h))
print('Para pintar essa parede você precisará de {:.1f}l de tinta.'.format((w*h)/2))
