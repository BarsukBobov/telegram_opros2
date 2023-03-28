from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def inline(buttons):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for button in buttons:
        btn = InlineKeyboardButton(text=button, callback_data=button)
        keyboard.insert(btn)
    return keyboard


def inline_pro(buttons):
    if len(buttons) > 26:
        l = buttons.copy()
        l1 = []
        l2 = []
        i = 0
        while len(l) > 0:
            l1.append(l[0])
            l.pop(0)
            if len(l) == 0:
                l1.append('⏮')
                l2.append(l1)
                l1 = []
            elif i == 25:
                if not l2:
                    l1.append('⏭')
                else:
                    l1.append('⏮')
                    l1.append('⏭')
                l2.append(l1)
                l1 = []
                i = -1
            i += 1
        return l2


text1 = '''
📍Админ панель.
В любой момент можете начать заново командой - /cancel.
Выберите манипуляцию с записью:
'''
buttons1 = ['Добавить', 'Удалить']

# Добавить
NIF = '''
Введите NIF/NO.
Пример: Y3910569P
'''
Nombre = '''
Введите Nombre.
Пример: PAVLO
'''
Provincia = '''
Выберите Provincia residencia.

'''
Provincias = ['Albacete', 'Alicante/Alacant', 'Almería', 'Araba/Álava', 'Asturias', 'Ávila', 'Badajoz',
              'Balears (Illes)', 'Barcelona', 'Bizkaia', 'Burgos', 'Cáceres', 'Cádiz', 'Cantabria',
              'Castellón/Castellò', 'Ceuta', 'Ciudad ', 'Real', 'Córdoba', 'Coruña (A)', 'Cuenca', 'Gipuzkoa', 'Girona',
              'Granada', 'Guadalajara', 'Huelva', 'Huesca',
              'Jaén', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga', 'Melilla', 'Murcia', 'Navarra', 'Ourense',
              'Palencia', 'Palmas (Las)', 'Pontevedra', 'Rioja (La)', 'Salamanca', 'Santa Cruz de Tenerife', 'Segovia',
              'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia/València', 'Valladolid', 'Zamora',
              'Zaragoza']
Provincias = inline_pro(Provincias)

Fecha = '''
Введите Fecha de nacimiento.
Пример: 05/05/1987
'''
conductor = '''
Введите Certificado del conductor.
Пример: BXP728492
'''
email = '''
Введите Email aviso.
Пример: Ggs.solutions@hotmail.com
'''
apellido = '''
Введите Primer apellido.
Пример: Shevchenko
'''
phone = '''
Введите Teléfono.
Пример: 602694823
'''
city = '''
Выберите город для поиска.(Провинция на главной странице)
'''

cities = ['Albacete', 'Alicante/Alacant', 'Alicante/Alacant-Elche', 'Almería', 'Araba/Álava', 'Asturias-Gijón',
          'Asturias-Oviedo', 'Ávila', 'Badajoz', 'Barcelona', 'Barcelona-Sabadell', 'Bizkaia', 'Burgos', 'Cáceres',
          'Cádiz', 'Cádiz-La Línea', 'Cantabria', 'Castellón/Castellò', 'Ceuta', 'Ciudad Real', 'Córdoba', 'Coruña (A)',
          'Coruña (A)-Santiago', 'Cuenca', 'Gipuzkoa', 'Girona', 'Granada', 'Guadalajara', 'Huelva', 'Huesca',
          'Illes Balears-Ibiza', 'Illes Balears-Mallorca', 'Illes Balears-Menorca', 'Jaén', 'Las Palmas-Fuerteventura',
          'Las Palmas-Gran Canaria', 'Las Palmas-Lanzarote', 'León', 'Lleida', 'Lugo', 'Madrid',
          'Madrid-Alcalá de Henares', 'Madrid-Alcorcón', 'Málaga', 'Melilla', 'Murcia', 'Murcia-Cartagena', 'Navarra',
          'Ourense', 'Palencia', 'Pontevedra', 'Pontevedra-Vigo', 'Rioja (La)', 'S.C. de Tenerife',
          'S.C. de Tenerife-La Palma', 'Salamanca', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo',
          'Toledo-Talavera', 'Valencia/València', 'Valencia/València-Alzira', 'Valladolid', 'Zamora', 'Zaragoza']

cities = inline_pro(cities)

Segundo_apellido = '''
Введите Segundo apellido, если оно есть.
Пример:-
'''

Pais = '''
Выберите страну, права которой меняете:
'''
paises = ['Alemania', 'Argelia', 'Argentina', 'Austria', 'Bélgica', 'Bolivia', 'Brasil', 'Bulgaria',
          'Chile', 'Chipre', 'Colombia', 'Costa Rica', 'Croacia', 'Dinamarca', 'Ecuador', 'El Salvador', 'Eslovaquia',
          'Eslovenia', 'Estonia', 'Filipinas', 'Finlandia', 'Francia', 'Grecia', 'Guatemala', 'Hungría', 'Irlanda',
          'Islandia', 'Italia', 'Letonia', 'Lietchtenstein', 'Lituania', 'Luxemburgo', 'Macedonia', 'Malta',
          'Marruecos',
          'Nicaragua', 'Noruega', 'Países Bajos', 'Panamá', 'Paraguay', 'Perú', 'Polonia', 'Portugal',
          'República Checa',
          'República Dominicana', 'Rumanía', 'Serbia', 'Suecia', 'Túnez', 'Turquía', 'Ucrania', 'Uruguay']

paises = inline_pro(paises)

accept = ["Да", "Нет"]
