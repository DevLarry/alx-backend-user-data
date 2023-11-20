#!/usr/bin/env python3
"""
Definition of class SessionAuth
"""


from api.v1.auth.auth import Auth
from uuid import uuid4

from models.user import User


class SessionAuth(Auth):
    """Session authentication implementation"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def current_user(self, request=None):
        """Gets the currently logged in user"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """get the userId or the session Id passed"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
