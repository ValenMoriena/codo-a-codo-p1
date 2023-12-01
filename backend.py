from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import datetime


app = Flask(__name__)
CORS(app) 


class Formulario:
    
    # def __init__(self, host, user, password, database):
    #     self.conn = mysql.connector.connect(
    #         host=host,
    #         user=user,
    #         password=password
    #     )
        
    #     self.cursor = self.conn.cursor()
        
    #     try:
    #         self.cursor.execute(f"USE{database}")
    #     except mysql.connector.Error as err:
    #         if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERRROR:
    #             self.cursor.execute(f"CREATE DATABASE {database}")
    #             self.conn.database = database
    #         else:
    #             raise err
            
 
    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS formulario (
    #         id int(11) NOT NULL AUTO_INCREMENT,
    #         nombre varchar (30) NOT NULL,
    #         apellido varchar(30) NOT NULL,
    #         telefono varchar (15) NOT NULL,
    #         email varchar (60) NOT NULL,
    #         mensaje varchar (500) NOT NULL,
    #         fecha_envio datetime NOT NULL,
    #         leido tinyint(1) NOT NULL,
    #         gestion varchar (500) DEFAULT NULL,
    #         fecha_gestion datetime DEFAULT NULL,
    #         PRIMARY KEY ('id')
    #         )ENGINE=InnoDB DEFAULT CHARSET=uft8 COLLATE=uft8_spanish_ci;
    #         ''')
        
    #     self.conn.commit()
        
    #     self.cursor.close()
    #     self.cursor = self.conn.cursor(dictionary=True)
 
    # def enviar_mensaje(self, nombre, apellido, telefono, email):
    #     sql = "INSERT INTO  mensajes(nombre, apellido, telefono, email, mensaje, fecha_envio)"
    #     fecha_envio = datetime.datetime.now()
    #     valores = (nombre, apellido, telefono, email, fecha_envio)
        
    #     self.cursor.execute(sql, valores)
    #     self.conn.commit()
    #     return True
    
    # def listar_mensajes(self):
    #     self.cursor.execute("SELECT * FROM formulario")
    #     formulario = self.cursor.fetchall()
    #     return formulario
    
    
    # def responder_mensaje(self, id, gestion):
    #     fecha_gestion = datetime.datetime.now()
    #     sql = "UPDATE mensajes SET leido =1, gestion = %s, fecha_gestion = %s, WHERE id = %s"
    #     valores = (gestion,fecha_gestion , id)
    #     self.cursor.execute(sql, valores)
    #     self.conn.commit()
    #     return self.cursor.rowcount > 0
    
    # def eliminar_mensaje(self, id):
    #     self.cursor.execute(f"DELETE FROM mensajes WHERE id = {id}")
    #     self.conn.commit()
    #     return self.cursor.rowcount > 0
    
    # def mostrar_mensaje(self,id):
    #     sql = f"SELECT id, nombre, apellido, telefono, email, mensaje, fecha_envio, leido, gestion, fecha_gestion, FROM mensajes WHERE id = {id}"
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchone()
       
            
    def enviar_mensaje(self, nombre, apellido, telefono, email):
        print(nombre, apellido, telefono, email)
        return True
    
# formulario = Formulario("localhost", "root", "", "formulario")
formulario = Formulario()

@app.route('/enviar_mensaje', methods=['POST'])
def recibir_mensaje():
    data = request.get_json()
    print(data)
    # formulario.enviar_mensaje(data['nombre'], data['apellido'], data['telefono'], data['email'])
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
