from storage import *

class Post(Base):
	'''
	文章信息
	'''
	__tablename__ = "post"
	id = Column(Integer, primary_key = True, doc = "ID")
	title = Column(String(40), doc = "标题")
	content = Column(Text, doc = "文章内容")
	create_time = Column(DateTime, doc = "创建时间")
	summary = Column(String(255), doc = "摘要")
	author = Column(String(20), doc = "作者")
	category_id = Column(Integer, "文章分类")
	visited = Column(Integer, "阅读量")



 class Comment(Base):
 	'''
 	文章评论
 	'''
 	__tablename__ = "comment"
 	id = Column(Integer, primary_key = True, doc = "ID")
 	create_time = Column(DateTime, doc = "创建时间")
 	create_user = Column(String(20), "创建人")
 	content = Column(Text, "评论内容")


 class Tag(Base):
 	'''
 	文章标签
 	'''
 	__tablename__ = "tag"
 	id = Column(Integer, primary_key = True, doc = "ID")
 	name = Column(String(20), doc = "标签名字")

class Category:
	'''
	文章类别
	'''
	__tablename__ = "category"
 	id = Column(Integer, primary_key = True, doc = "ID")
 	name = Column(String(20), doc = "文章类别")

 class PostTag:
 	'''
 	文章标签表
 	'''
 	__tablename__ = "posttag"
 	id = Column(Integer, primary_key = True, doc = "ID")
 	post_id = Column(Integer, doc = "文章id")
 	tag_id = Column(Integer, doc = "标签id")

 class PostComment:
 	'''
 	文章评论表
 	'''
 	__tablename__ = "postcomment"
 	id = Column(Integer, primary_key = True, doc = "ID")
 	post_id = Column(Integer, doc = "文章id")
 	comment_id = Column(Integer, doc = "评论id")






