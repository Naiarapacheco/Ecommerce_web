from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from empresa.models import User

    
class CadastroForm(FlaskForm):
    def validate_usuario(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de Usuário.")
        
    def validade_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro Email.")
        
    def validade_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe! Cadastre outra Senha.")
        
    usuario = StringField(label= "Username:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label= "E-mail:", validators=[Email(),  DataRequired()])
    senha1 = PasswordField(label = "Senha:", validators=[Length(min=6),  DataRequired()])
    senha2 = PasswordField(label = "Confirmação de Senha:", validators=[EqualTo("senha1"),  DataRequired()])
    submit = SubmitField(label = "Cadastrar")


class LoginForm(FlaskForm):
    usuario = StringField(label= "Usuário", validators=[DataRequired()])   #dado requerido
    senha = PasswordField(label= "Senha:", validators=[DataRequired()])   #dado requerido
    submit = SubmitField(label= "Log In")


class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label= "Comprar produto")

class VendaProdutoForm(FlaskForm):
    submit = SubmitField(label="Vender Produto")