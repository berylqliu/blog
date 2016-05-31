from storage import *

class User(Base):
	'''
	用户信息
	'''
	__tablename__ = "user"
	id = Column(Integer, primary_key = True, doc = "ID")
	username = Column(String(40), doc = "用户名")
	nickname = Column(String(40), doc = "用户昵称")
	source = Column(String(20), doc = "用户来源")
	role = Column(String(20), doc = "用户角色")
	__table_args__ = (
		UniqueConstraint("username"),
		UniqueConstraint("nickname"),
		Index("name", "username")
	)
