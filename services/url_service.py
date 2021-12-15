from codecs import encode

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import String
from models.user import User
from models.url import Url
from schemas.url import ListUrl, UrlShort

class UrlService():
    async def get_link(self, db_session: Session, url_id: String):
        url = db_session.query(Url).filter(Url.id == url_id).first()
        return url  
    
    async def get_links(self, db_session: Session, user: User) -> list[ListUrl]:
        listUrls = db_session.query(Url).filter(Url.user_id == user.id)
        return  listUrls

    async def create_redirect_link(self, db_session: Session, user: User, payload: UrlShort) -> ListUrl:
        linkUrl = Url(original_url=payload.url, user_id=user.id)
        db_session.add(linkUrl)
        db_session.commit()
        db_session.refresh(linkUrl)

        return linkUrl


        
urlService = UrlService()