from storage import *

class SiteVisit:
	'''
	网站访问
	'''
	__tablename__ = "sitevisit"
	id = Column(Integer, primary_key = True, doc = "ID")
	pv = Column(Integer)
	uv = Column(Integer)
	time = Column(String(20), doc = "日期" )
	__table_args__ = (
		UniqueConstrait(time)
	)