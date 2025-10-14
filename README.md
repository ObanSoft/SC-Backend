# Powershell
Dentro de la terminal ejecutamos

# Clonacion de git
git clone https://github.com/ObanSoft/MU-Backend.git
# Activacion Entorno Virtual
./venv/Scripts/Activate
# Ingresar a servidor 
cd .\MU-Backend\
# Instalar dependendecias necesarias
pip install -r .\requirements.txt

# Definir variable de migracion
"$"env:FLASK_APP = "manage.py" (Eliminar comillas del $)
# Inicializar directorio de migracion
flask db init
# Crear commit con la migracion de Modelos
flask db migrate -m "Comentario del commit"
# Actualizacion en la base de datos segun migracion
flask db upgrade

# Migracion a MYSQL
Antes de hacer el init recuerda en mysql crear la base de datos:
CREATE DATABASE makeup_lj;