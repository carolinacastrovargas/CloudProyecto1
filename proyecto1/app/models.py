from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from app import db
from sqlalchemy import asc, desc


from sqlalchemy.exc import IntegrityError
class Concurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    nombre = db.Column( db.String(250) )
    imagen = db.Column( db.String(250) )
    url = db.Column( db.String(250) )
    fechaInicio = db.Column( db.DateTime )
    fechaFin = db.Column( db.DateTime )
    valor = db.Column( db.String(250) )
    guion = db.Column( db.String(250) )
    recomendaciones = db.Column( db.String(250) )
    fechaCreacion = db.Column( db.DateTime )
    def __repr__(self):
        return f'<Concurso {self.url}>'
    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.url:
            self.url = slugify(self.url)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def public_url(self):
        return url_for('public.show_concurso', url=self.url)
    def concurso_delete(self):
        return url_for('admin.concurso_delete',concurso_id=self.id)
    def concurso_update(self):
         return url_for('admin.concurso_update',concurso_id=self.id)
    @staticmethod
    def get_by_id(concurso_id):
        return Concurso.query.filter_by(id=concurso_id).first()
    @staticmethod
    def get_by_url(url):
        return Concurso.query.filter_by(url=url).first()
    @staticmethod
    def get_all():
        return Concurso.query.all()
    def get_by_user(user_id):
        concurso = Concurso.query.filter_by(user_id=user_id).order_by(desc(Concurso.fechaCreacion)).all()
        return concurso
