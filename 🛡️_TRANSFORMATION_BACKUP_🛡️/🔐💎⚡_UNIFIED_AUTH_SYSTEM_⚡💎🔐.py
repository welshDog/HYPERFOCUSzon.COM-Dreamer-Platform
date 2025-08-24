import hashlib
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class UnifiedAuthSystem:
    """🔐 Unified authentication for Flask & FastAPI apps"""

    def __init__(self, secret_key: str = "hyperfocus-zone-legendary-secret"):
        self.secret_key = secret_key
        self.security = HTTPBearer()

    def hash_password(self, password: str) -> str:
        """Hash password with SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash"""
        return self.hash_password(password) == hashed

    def create_access_token(
        self, user_data: dict, expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create access token"""
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=24)

        return f"token_{user_data.get('user_id', 'unknown')}_{expire.timestamp()}"

    def verify_token(self, token: str) -> dict:
        """Verify and decode token"""
        if token.startswith("token_"):
            parts = token.split("_")
            if len(parts) >= 3:
                try:
                    exp_time = float(parts[2])
                    if datetime.utcnow().timestamp() < exp_time:
                        return {"user_id": parts[1], "exp": exp_time}
                except:
                    pass

        raise HTTPException(status_code=401, detail="Invalid or expired token")

    # FastAPI middleware
    async def get_current_user(
        self, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())
    ):
        """FastAPI dependency for authentication"""
        return self.verify_token(credentials.credentials)


# Global auth instance
auth_system = UnifiedAuthSystem()

if __name__ == "__main__":
    print("🔐 Unified Auth System initialized")
    print("✅ Ready for Flask & FastAPI integration")

    # Test functionality
    test_user = {"user_id": "test_user", "username": "hyperfocus"}
    token = auth_system.create_access_token(test_user)
    print(f"🎯 Test token: {token[:50]}...")

    try:
        verified = auth_system.verify_token(token)
        print(f"✅ Token verification: {verified}")
    except Exception as e:
        print(f"❌ Token error: {e}")
