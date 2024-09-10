# Sistema de permisos basado en roles usando lógica booleana
admin = False
editor = True
viewer = True

# Condiciones para determinar el acceso basado en permisos
puede_editar = editor or admin
puede_ver = viewer or editor or admin
puede_borrar = admin

print("¿Puede editar?", puede_editar)
print("¿Puede ver?", puede_ver)
print("¿Puede borrar?", puede_borrar)
