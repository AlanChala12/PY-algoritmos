print('¿Cuál es la factura total de hoy, por favor?')

try:
   cuenta_de_usuario = float(input('Cuenta: '))
   propina_de_usuario = int( input('Propina: ') )

   def calcular_propina( cuenta, propina ):
      
      porcentaje = 1 + ( propina / 100 )
      cuenta_total = cuenta * porcentaje
      
      return f'La propina aplicando el { propina }% es ${ porcentaje }, que contabiliza un total de ${ cuenta_total }'

   print( calcular_propina( cuenta_de_usuario, propina_de_usuario ) )
   
except:
   print('Por favor, ingresa valores numéricos')