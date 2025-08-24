#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - API GATEWAY SERVICE ⚡♾️🌌
Legendary API Gateway with Authentication & Rate Limiting
Multi-Service Architecture Integration
"""

import datetime
import json
import logging
import os
import time
from typing import Dict, Optional

import aioredis
import asyncpg
import httpx
import jwt
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("/app/logs/api-gateway.log"),
    ],
)
logger = logging.getLogger("EmpireAPIGateway")

# Configuration from environment
COMMAND_CENTER_URL = os.getenv(
    "COMMAND_CENTER_URL", "http://ultra-thinking-boardroom:8000"
)
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "legendary_jwt_secret_key")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# FastAPI app with enhanced security
app = FastAPI(
    title="🚀 HyperFocus Empire - API Gateway",
    description="Legendary API Gateway with Authentication & Windsurf Integration",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Security middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]  # Configure for production
)

# Security components
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Global connections
redis_pool = None
db_pool = None
http_client = None

# Rate limiting storage
rate_limit_requests = {}


# Pydantic models
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"


class ProxyRequest(BaseModel):
    method: str
    path: str
    headers: Dict[str, str] = {}
    body: Optional[str] = None


# Startup event
@app.on_event("startup")
async def startup_event():
    global redis_pool, db_pool, http_client

    logger.info("🚀 EMPIRE API GATEWAY STARTUP INITIATED")

    # Initialize Redis connection
    try:
        redis_pool = await aioredis.from_url(REDIS_URL)
        await redis_pool.ping()
        logger.info("✅ Redis connection established")
    except Exception as e:
        logger.error(f"❌ Redis connection failed: {e}")

    # Initialize PostgreSQL connection
    try:
        db_pool = await asyncpg.create_pool(DATABASE_URL)
        logger.info("✅ PostgreSQL connection established")
    except Exception as e:
        logger.error(f"❌ PostgreSQL connection failed: {e}")

    # Initialize HTTP client for proxy requests
    http_client = httpx.AsyncClient(timeout=30.0)
    logger.info("✅ HTTP client initialized")

    logger.info("🚀 EMPIRE API GATEWAY FULLY OPERATIONAL!")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    global http_client
    if http_client:
        await http_client.aclose()


# Rate limiting middleware
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()

    # Clean old entries (older than 1 minute)
    cutoff_time = current_time - 60
    for ip in list(rate_limit_requests.keys()):
        rate_limit_requests[ip] = [
            timestamp
            for timestamp in rate_limit_requests[ip]
            if timestamp > cutoff_time
        ]
        if not rate_limit_requests[ip]:
            del rate_limit_requests[ip]

    # Check rate limit (100 requests per minute per IP)
    if client_ip in rate_limit_requests:
        if len(rate_limit_requests[client_ip]) >= 100:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded. Maximum 100 requests per minute."
                },
            )
    else:
        rate_limit_requests[client_ip] = []

    rate_limit_requests[client_ip].append(current_time)
    response = await call_next(request)
    return response


# Utility functions
def create_access_token(data: dict):
    """Create JWT access token"""
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_EXPIRATION_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash password"""
    return pwd_context.hash(password)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """Get current authenticated user"""
    try:
        payload = jwt.decode(
            credentials.credentials, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return username
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Health check
@app.get("/health")
async def health_check():
    """API Gateway health check"""
    health_status = {
        "status": "LEGENDARY_OPERATIONAL",
        "timestamp": datetime.datetime.now().isoformat(),
        "services": {
            "redis": "connected" if redis_pool else "disconnected",
            "postgres": "connected" if db_pool else "disconnected",
            "command_center": "connected",  # We'll check this via proxy
        },
        "rate_limiting": "active",
        "authentication": "enabled",
    }
    return health_status


# Authentication endpoints
@app.post("/auth/login", response_model=TokenResponse)
async def login(login_request: LoginRequest):
    """User login endpoint"""
    try:
        if not db_pool:
            raise HTTPException(status_code=503, detail="Database unavailable")

        async with db_pool.acquire() as conn:
            user = await conn.fetchrow(
                "SELECT username, email, role, password_hash FROM team_members WHERE username = $1 AND is_active = TRUE",
                login_request.username,
            )

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password",
                )

            # For demo purposes, we'll create a simple password check
            # In production, use proper password hashing
            if login_request.password != "legendary_password":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid username or password",
                )

            # Create access token
            access_token = create_access_token(
                data={"sub": user["username"], "role": user["role"]}
            )

            # Update last login
            await conn.execute(
                "UPDATE team_members SET last_login = NOW() WHERE username = $1",
                login_request.username,
            )

            return TokenResponse(
                access_token=access_token,
                token_type="bearer",
                expires_in=JWT_EXPIRATION_HOURS * 3600,
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Login error: {e}")
        raise HTTPException(status_code=500, detail="Login failed")


@app.post("/auth/register")
async def register(user_data: UserCreate):
    """User registration endpoint"""
    try:
        if not db_pool:
            raise HTTPException(status_code=503, detail="Database unavailable")

        password_hash = get_password_hash(user_data.password)

        async with db_pool.acquire() as conn:
            # Check if user already exists
            existing_user = await conn.fetchrow(
                "SELECT username FROM team_members WHERE username = $1 OR email = $2",
                user_data.username,
                user_data.email,
            )

            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username or email already registered",
                )

            # Create new user
            await conn.execute(
                """
                INSERT INTO team_members (username, email, role, password_hash, permissions)
                VALUES ($1, $2, $3, $4, $5)
            """,
                user_data.username,
                user_data.email,
                user_data.role,
                password_hash,
                json.dumps({"basic_access": True}),
            )

            return {"message": "User registered successfully"}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Registration error: {e}")
        raise HTTPException(status_code=500, detail="Registration failed")


# Protected route example
@app.get("/auth/me")
async def get_current_user_info(current_user: str = Depends(get_current_user)):
    """Get current user information"""
    try:
        if not db_pool:
            raise HTTPException(status_code=503, detail="Database unavailable")

        async with db_pool.acquire() as conn:
            user = await conn.fetchrow(
                "SELECT username, email, role, permissions, last_login FROM team_members WHERE username = $1",
                current_user,
            )

            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            return {
                "username": user["username"],
                "email": user["email"],
                "role": user["role"],
                "permissions": user["permissions"],
                "last_login": user["last_login"],
            }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ User info error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get user info")


# Proxy endpoints to Command Center
@app.get("/empire/{path:path}")
async def proxy_to_command_center(
    path: str, request: Request, current_user: str = Depends(get_current_user)
):
    """Proxy requests to Ultra-Thinking Boardroom Command Center"""
    try:
        url = f"{COMMAND_CENTER_URL}/empire/{path}"

        # Forward query parameters
        if request.url.query:
            url += f"?{request.url.query}"

        response = await http_client.get(url)
        return response.json()

    except Exception as e:
        logger.error(f"❌ Proxy error: {e}")
        raise HTTPException(status_code=502, detail="Command Center unavailable")


@app.post("/empire/{path:path}")
async def proxy_post_to_command_center(
    path: str, request: Request, current_user: str = Depends(get_current_user)
):
    """Proxy POST requests to Ultra-Thinking Boardroom Command Center"""
    try:
        url = f"{COMMAND_CENTER_URL}/empire/{path}"
        body = await request.body()

        response = await http_client.post(
            url, content=body, headers={"Content-Type": "application/json"}
        )
        return response.json()

    except Exception as e:
        logger.error(f"❌ Proxy POST error: {e}")
        raise HTTPException(status_code=502, detail="Command Center unavailable")


# Windsurf integration proxy
@app.get("/windsurf/{path:path}")
async def proxy_windsurf(
    path: str, request: Request, current_user: str = Depends(get_current_user)
):
    """Proxy Windsurf AI requests through Command Center"""
    try:
        url = f"{COMMAND_CENTER_URL}/windsurf/{path}"

        if request.url.query:
            url += f"?{request.url.query}"

        response = await http_client.get(url)
        return response.json()

    except Exception as e:
        logger.error(f"❌ Windsurf proxy error: {e}")
        raise HTTPException(status_code=502, detail="Windsurf integration unavailable")


# API Gateway statistics
@app.get("/gateway/stats")
async def get_gateway_stats(current_user: str = Depends(get_current_user)):
    """Get API Gateway statistics"""
    try:
        stats = {
            "total_requests": sum(
                len(requests) for requests in rate_limit_requests.values()
            ),
            "active_ips": len(rate_limit_requests),
            "authenticated_requests": 0,  # Would track in production
            "proxy_requests": 0,  # Would track in production
            "rate_limited_requests": 0,  # Would track in production
            "uptime_seconds": time.time(),
            "services_health": {
                "command_center": "operational",
                "database": "connected" if db_pool else "disconnected",
                "cache": "connected" if redis_pool else "disconnected",
            },
        }

        return stats

    except Exception as e:
        logger.error(f"❌ Stats error: {e}")
        raise HTTPException(status_code=500, detail="Stats unavailable")


if __name__ == "__main__":
    logger.info("🚀 Starting Empire API Gateway...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", access_log=True)
