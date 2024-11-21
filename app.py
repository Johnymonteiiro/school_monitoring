from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import mysql.connector

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua-chave-secreta'  # Troque por uma chave segura
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="master",
        database="school"
    )

# Rota para obter todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # Retorna resultados como dicionários
        cursor.execute("SELECT * FROM Aluno")
        resultados = cursor.fetchall()
        return jsonify(resultados), 200  # Retorna os dados como JSON
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para adicionar um novo aluno
@app.route('/alunos', methods=['POST'])
def add_aluno():
    try:
        data = request.json  # Obtém dados do corpo da requisição
        nome = data.get('nome')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        endereco = data.get('endereco')
        condicoes_saude = data.get('condicoes_saude')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Aluno (nome, data_nascimento, cpf, endereco, condicoes_saude) VALUES (%s, %s, %s, %s, %s)", (nome, data_nascimento, cpf, endereco, condicoes_saude))
        conn.commit()  # Confirma a transação
        return jsonify({"message": "Aluno adicionado com sucesso!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para buscar um aluno pelo ID
@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno_by_id(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Aluno WHERE id_aluno = %s", (id,))
        resultado = cursor.fetchone()
        if resultado:
            return jsonify(resultado), 200
        else:
            return jsonify({"message": "Aluno não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para atualizar um aluno
@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    try:
        data = request.json
        nome = data.get('nome')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        endereco = data.get('endereco')
        condicoes_saude = data.get('condicoes_saude')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Aluno SET nome = %s, data_nascimento = %s, cpf = %s, endereco = %s, condicoes_saude = %s WHERE id_aluno = %s", (nome, data_nascimento, cpf, endereco, condicoes_saude, id))
        conn.commit()
        if cursor.rowcount > 0:
            return jsonify({"message": "Aluno atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Aluno não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para deletar um aluno
@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aluno WHERE id_aluno = %s", (id,))
        conn.commit()
        if cursor.rowcount > 0:
            return jsonify({"message": "Aluno deletado com sucesso!"}), 200
        else:
            return jsonify({"message": "Aluno não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para adicionar um professor (CREATE)
@app.route('/professores', methods=['POST'])
def add_professor():
    try:
        data = request.json
        nome = data.get('nome')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        especialidade = data.get('especialidade')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Professor (nome, cpf, email, telefone, especialidade) VALUES (%s, %s, %s, %s, %s)",
            (nome, cpf, email, telefone, especialidade)
        )
        conn.commit()
        return jsonify({"message": "Professor adicionado com sucesso!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# 2. Rota para listar todos os professores (READ)
@app.route('/professores', methods=['GET'])
def get_professores():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Professor")
        professores = cursor.fetchall()
        return jsonify(professores), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para buscar um professor por ID (READ)
@app.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Professor WHERE id_professor = %s", (id_professor,))
        professor = cursor.fetchone()
        if professor:
            return jsonify(professor), 200
        else:
            return jsonify({"message": "Professor não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para atualizar informações de um professor (UPDATE)
@app.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    try:
        data = request.json
        nome = data.get('nome')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        especialidade = data.get('especialidade')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE Professor 
            SET nome = %s, cpf = %s, email = %s, telefone = %s, especialidade = %s
            WHERE id_professor = %s
            """,
            (nome, cpf, email, telefone, especialidade, id_professor)
        )
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "Professor atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Professor não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# 5. Rota para remover um professor (DELETE)
@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Professor WHERE id_professor = %s", (id_professor,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "Professor removido com sucesso!"}), 200
        else:
            return jsonify({"message": "Professor não encontrado"}), 404
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rota para registrar novos usuários
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        tipo_usuario = data['user']

        # Hash da senha
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (nome_usuario, senha, tipo_usuario, status) VALUES (%s, %s, %s, %s)", (username, password_hash, tipo_usuario, "Ativo")
        )
        conn.commit()
        return jsonify({"message": "Usuário registrado com sucesso!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Para para login
@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        username = data['username']
        password = data['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Usuario WHERE nome_usuario = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user['senha'], password):
            # Criação do token JWT
            access_token = create_access_token(identity={"id": user['id_usuarios'], "username": user['nome_usuario']})
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Usuário ou senha inválidos"}), 401
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Rpta de proteção (exemplo)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "Acesso permitido! Você está autenticado."}), 200

if __name__ == '__main__':
    app.run(debug=True)
